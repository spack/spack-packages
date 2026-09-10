# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os
import sys

from spack_repo.builtin.build_systems.compiler import CompilerPackage
from spack_repo.builtin.build_systems.generic import Package
from spack_repo.builtin.build_systems.oneapi import IntelOneApiPackage

from spack.package import *


@IntelOneApiPackage.update_description
class IntelOneapiCompilersClassic(Package, CompilerPackage):
    """Relies on intel-oneapi-compilers to install the compilers, and
    configures modules for icc/icpc/ifort.

    """

    maintainers("rscohn2")

    homepage = "https://software.intel.com/content/www/us/en/develop/tools/oneapi.html"

    has_code = False

    compiler_languages = ["c", "cxx", "fortran"]
    c_names = ["icc"]
    cxx_names = ["icpc"]
    fortran_names = ["ifort"]

    @classproperty
    def compiler_version_argument(self):
        if sys.platform == "win32":
            return "/QV"
        return "--version"

    @classproperty
    def compiler_version_regex(self):
        if sys.platform == "win32":
            return r"([1-9][0-9]*\.[0-9]*\.[0-9]*)"
        return r"\((?:IFORT|ICC)\) ([^ ]+)"

    compiler_wrapper_link_paths = {
        "c": os.path.join("intel", "icc"),
        "cxx": os.path.join("intel", "icpc"),
        "fortran": os.path.join("intel", "ifort"),
    }

    implicit_rpath_libs = ["libirc", "libifcore", "libifcoremt", "libirng"]

    stdcxx_libs = ("-cxxlib",)

    provides("c", "cxx", when="@:2021.10")
    provides("fortran")

    version_map = {
        "2021.1.2": "2021.1.2",
        "2021.2.0": "2021.2.0",
        "2021.3.0": "2021.3.0",
        "2021.4.0": "2021.4.0",
        "2021.5.0": "2022.0.1:2022.0.2",
        "2021.6.0": "2022.1.0",
        "2021.7.0": "2022.2.0",
        "2021.7.1": "2022.2.1",
        "2021.8.0": "2023.0.0",
        "2021.9.0": "2023.1.0",
        "2021.10.0": "2023.2.4",
        "2021.11.0": "2024.0.0",
        "2021.11.1": "2024.0.1:2024.0.2",
        "2021.12.0": "2024.1.0",
        "2021.13.0": "2024.2.0",
        "2021.13.1": "2024.2.1",
    }

    # Versions before 2021 are in the `intel` package
    # intel-oneapi versions before 2022 use intel@19.0.4
    for ver, oneapi_ver in version_map.items():
        # prefer 2021.10.0 because it is the last one that has a C compiler
        version(ver, preferred=(ver == "2021.10.0"))
        depends_on("intel-oneapi-compilers@" + oneapi_ver, when="@" + ver, type="build")

    # icc@2021.6.0 does not support gcc@12 headers
    conflicts("%gcc@12:", when="@:2021.6.0")

    @property
    def oneapi_compiler_prefix(self):
        return self["intel-oneapi-compilers"].component_prefix

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        """Adds environment variables to the generated module file.

        These environment variables come from running:
        .. code-block:: console
           $ source {prefix}/{component}/{version}/env/vars.sh
        and from setting CC/CXX/F77/FC
        """
        env.set("CC", self.prefix.bin.icc)
        env.set("CXX", self.prefix.bin.icpc)
        env.set("F77", self.prefix.bin.ifort)
        env.set("FC", self.prefix.bin.ifort)

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        super().setup_dependent_build_environment(env, dependent_spec)
        # Edge cases for Intel's oneAPI compilers when using the legacy classic compilers:
        # Always pass flags to disable deprecation warnings, since these warnings can
        # confuse tools that parse the output of compiler commands (e.g. version checks).
        if dependent_spec.satisfies("^[virtuals=c] intel-oneapi-compilers-classic"):
            env.append_flags("SPACK_ALWAYS_CFLAGS", "-diag-disable=10441")

        if dependent_spec.satisfies("^[virtuals=cxx] intel-oneapi-compilers-classic"):
            env.append_flags("SPACK_ALWAYS_CXXFLAGS", "-diag-disable=10441")

        if dependent_spec.satisfies("^[virtuals=fortran] intel-oneapi-compilers-classic"):
            env.append_flags("SPACK_ALWAYS_FFLAGS", "-diag-disable=10448")

    def install(self, spec, prefix):
        # List of all binaries from intel-oneapi-compilers related to ifort
        binaries = [
            "codecov",
            "fortcom",
            "fpp",
            "ifort",
            "ifort.cfg",
            "map_opts",
            "profdcg",
            "profmerge",
            "profmergesampling",
            "proforder",
            "tselect",
            "xiar",
            "xiar.cfg",
            "xild",
            "xild.cfg",
        ]

        # We do a full copy (not symlinks) to avoid a run dependency on intel-oneapi-compilers
        # which would prevent mixing versions in a DAG
        mkdirp(prefix.bin)
        for binary in binaries:
            install(self.oneapi_compiler_prefix.bin.join(binary), prefix.bin)
        install_tree(self.oneapi_compiler_prefix.lib, prefix.lib)
        install_tree(self.oneapi_compiler_prefix.opt, prefix.opt)
        install_tree(self.oneapi_compiler_prefix.etc, prefix.etc)
        install_tree(self.oneapi_compiler_prefix.share, prefix.share)

    @when("@:2021.10")
    def install(self, spec, prefix):
        # We do a full copy (not symlinks) to avoid a run dependency on intel-oneapi-compilers
        # which would prevent mixing versions in a DAG
        install_tree(self.oneapi_compiler_prefix.linux.bin.intel64, prefix.bin.intel64)
        binaries = [
            "codecov",
            "fortcom",
            "fpp",
            "icc",
            "icpc",
            "ifort",
            "mcpcom",
            "profdcg",
            "profmerge",
            "profmergesampling",
            "proforder",
            "tselect",
            "xiar",
            "xild",
        ]
        for binary in binaries:
            os.symlink(prefix.bin.intel64.join(binary), prefix.bin.join(binary))
        install_tree(self.oneapi_compiler_prefix.linux.lib, prefix.lib)
        install_tree(
            self.oneapi_compiler_prefix.linux.compiler.lib.intel64_lin,
            prefix.linux.compiler.lib.intel64_lin,
        )
        install_tree(self.oneapi_compiler_prefix.linux.include, prefix.include)
        install_tree(self.oneapi_compiler_prefix.linux.compiler, prefix.compiler)
        install_tree(self.oneapi_compiler_prefix.documentation.en.man, prefix.man)

    def _cc_path(self):
        return str(self.prefix.bin.icc)

    def _cxx_path(self):
        return str(self.prefix.bin.icpc)

    def _fortran_path(self):
        return str(self.prefix.bin.ifort)

    def archspec_name(self):
        return "intel"

    def _standard_flag(self, *, language, standard):
        flags = {
            "cxx": {
                "11": "-std=c++11",
                "14": "-std=c++14",
                "17": "-std=c++17",
                "18": "-std=c++18",
            },
            "c": {"99": "-std=c99", "11": "-std=c11", "17": "-std=c17", "18": "-std=c18"},
        }
        return flags[language][standard]
