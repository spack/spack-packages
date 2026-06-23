import os
import shlex
import shutil
import socket

import spack.llnl.util.filesystem as fs

try:
    import spack.build_systems.cmake as cmake_build_system
except ImportError:
    import spack_repo.builtin.build_systems.cmake as cmake_build_system

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

UNIT_TEST_TIMEOUT = os.getenv("SPACK_TEST_TIMEOUT", "1800")
SPACK_BUILD_NAME_PREFIX = os.getenv("SPACK_BUILD_NAME_PREFIX", None)
SPACK_CDASH_TRACK = os.getenv("SPACK_CDASH_TRACK", "Experimental")
SPACK_CDASH_URL = os.getenv("SPACK_CDASH_URL", None)
SPACK_REPORT_WITH_CTEST = os.getenv("SPACK_REPORT_WITH_CTEST", False)


def use_cdash_subgroups():
    if SPACK_REPORT_WITH_CTEST:
        return SPACK_REPORT_WITH_CTEST.upper() == "SUBPROJECT"
    else:
        return False


CTEST_DRIVER = """\
cmake_policy(SET CMP0012 NEW)

if(${CTEST_USE_SUBGROUPS})
    set(CTEST_LABELS_FOR_SUBPROJECTS ${CTEST_SUBGROUP_NAME})
endif()

if(${CTEST_APPEND})
    ctest_start(Nightly GROUP ${CDASH_TRACK} APPEND)
else()
    ctest_start(Nightly GROUP ${CDASH_TRACK})
endif()

if(${CTEST_CONFIGURE})
    set(CTEST_UPDATE_COMMAND git)
    set(CTEST_UPDATE_VERSION_ONLY ON)
    ctest_update()
    ctest_configure(RETURN_VALUE ESTAT)
endif()

if(${CTEST_BUILD})
    set(CTEST_BUILD_COMMAND "cmake --build ${CTEST_BINARY_DIRECTORY}")
    ctest_build(RETURN_VALUE ESTAT)
endif()

if(${CTEST_TEST})
    ctest_test(RETURN_VALUE ESTAT)
endif()

if(${CTEST_SUBMIT_RESULTS})
    ctest_submit(SUBMIT_URL ${CDASH_URL})
endif()

if(NOT ${ESTAT} EQUAL 0)
    message(FATAL_ERROR "Command failed")
endif()
"""


def get_xml(root, xml_name):
    tag_file = os.path.join(root, "Testing/TAG")
    if os.path.isfile(tag_file):
        with open(tag_file) as f:
            tag = f.readline().strip()
        xml = os.path.join(root, "Testing", tag, xml_name)
        if os.path.isfile(xml):
            return xml


def create_configure_wrapper(configure_script, config_command):
    if not os.path.isdir(os.path.dirname(configure_script)):
        os.makedirs(os.path.dirname(configure_script))
    with open(configure_script, "w") as f:
        f.writelines(
            [
                "#!/bin/bash\n",
                f"echo \"CONFIGURE COMMAND: 'cmake {config_command}'\"\n",
                f"cmake {config_command}\n",
            ]
        )
    os.chmod(configure_script, 0o700)


class CTestBuilder(cmake_build_system.CMakeBuilder):
    reported_xml = []
    reporter = None
    ctest_script_subdir = "ctestconfig"

    phases = ("cmake", "build", "install")

    @property
    def ctest_args(self):
        args = []
        if use_cdash_subgroups():
            args = [
                self.define("CTEST_USE_SUBGROUPS", True),
                self.define("CTEST_SUBGROUP_NAME", self.pkg.name),
            ]
        return args + [
            self.define("CTEST_PROJECT_NAME", self.get_buildname()),
            self.define("CTEST_BUILD_NAME", self.get_buildname()),
            self.define("CTEST_NIGHTLY_START_TIME", "'00:00:00 MDT'"),
            self.define("CDASH_URL", SPACK_CDASH_URL),
            self.define("CDASH_TRACK", SPACK_CDASH_TRACK),
            self.define("CTEST_SOURCE_DIRECTORY", self.stage.source_path),
            self.define("CTEST_BINARY_DIRECTORY", self.build_directory),
            self.define("CTEST_TEST_TIMEOUT", UNIT_TEST_TIMEOUT),
            self.define("CTEST_SITE", socket.gethostname()),
            self.define("CTEST_APPEND", bool(self.reported_xml)),
            self.define("CTEST_SUBMIT_RESULTS", bool(SPACK_CDASH_URL)),
        ]

    def get_buildname(self):
        if use_cdash_subgroups() and SPACK_BUILD_NAME_PREFIX:
            return SPACK_BUILD_NAME_PREFIX
        elif use_cdash_subgroups():
            return "SPACK - CTEST"
        elif SPACK_BUILD_NAME_PREFIX:
            return f"{SPACK_BUILD_NAME_PREFIX} - {self.pkg.name}"
        else:
            return self.pkg.name

    def write_ctest_script(self, ctest_script):
        if not os.path.isdir(os.path.dirname(ctest_script)):
            os.makedirs(os.path.dirname(ctest_script))
        with open(ctest_script, "w") as f:
            f.write(CTEST_DRIVER)

    def get_ctest(self):
        ctest = Executable(self.spec["cmake"].prefix.bin.ctest)
        ctest.add_default_env("CMAKE_BUILD_PARALLEL_LEVEL", str(make_jobs))
        with fs.working_dir(self.build_directory):
            ctest_script = os.path.join(
                self.build_directory, self.ctest_script_subdir, "ctest_driver.cmake"
            )
            self.write_ctest_script(ctest_script)
            ctest.add_default_arg("-S", ctest_script)
            ctest.add_default_arg("-VV")
        return ctest

    def update_reported_xml(self, xml):
        xml_file = get_xml(self.build_directory, xml)
        if xml_file:
            new_xml = os.path.join(self.build_directory, "submitted", xml)
            if not os.path.isdir(os.path.dirname(new_xml)):
                os.makedirs(os.path.dirname(new_xml))
            os.replace(xml_file, new_xml)
            self.reported_xml.append(new_xml)

    def cmake(self, pkg, spec, prefix):
        """Runs ``cmake`` in the build directory"""
        if SPACK_REPORT_WITH_CTEST:
            options = self.std_cmake_args
            options += self.cmake_args()
            options.append(os.path.abspath(self.root_cmakelists_dir))
            command = " ".join([shlex.quote(opt) for opt in options])
            with fs.working_dir(self.build_directory, create=True):
                configure_script = os.path.join(
                    self.build_directory, self.ctest_script_subdir, "spack-configure.sh"
                )
                create_configure_wrapper(configure_script, command)
                ctest = self.get_ctest()
                try:
                    ctest(
                        self.define("CTEST_CONFIGURE", True),
                        self.define("CTEST_CONFIGURE_COMMAND", configure_script),
                        *self.ctest_args,
                    )
                finally:
                    self.update_reported_xml("Update.xml")
                    self.update_reported_xml("Configure.xml")
        else:
            super().cmake(pkg, spec, prefix)

    def build(self, pkg, spec, prefix):
        if SPACK_REPORT_WITH_CTEST:
            with fs.working_dir(self.build_directory):
                ctest = self.get_ctest()
                try:
                    ctest(self.define("CTEST_BUILD", True), *self.ctest_args)
                finally:
                    self.update_reported_xml("Build.xml")
        else:
            super().build(pkg, spec, prefix)

    def check(self):
        pass

    @run_after("build")
    def unit_test(self):
        if self.pkg.run_tests:
            ctest = self.get_ctest()

            with fs.working_dir(self.build_directory):
                try:
                    ctest("--no-tests=ignore", self.define("CTEST_TEST", True), *self.ctest_args)
                finally:
                    if SPACK_REPORT_WITH_CTEST:
                        self.update_reported_xml("Test.xml")


class CtestPackage(CMakePackage):
    CMakeBuilder = CTestBuilder
