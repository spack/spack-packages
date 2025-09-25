# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import json
import os
import platform
import re
import subprocess
import sys
from pathlib import Path
from shutil import copy
from typing import Dict, List

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


def make_pyvenv_cfg(python_pkg: Package, venv_prefix: str) -> str:
    """Make a pyvenv_cfg file for a given (real) python command and venv prefix."""
    python_cmd = python_pkg.command.path
    lines = [
        # directory containing python command
        f"home = {os.path.dirname(python_cmd)}",
        # venv should not allow site packages from the real python to be loaded
        "include-system-site-packages = false",
        # version of the python command
        f"version = {python_pkg.spec.version}",
        # the path to the python command
        f"executable = {python_cmd}",
        # command "used" to create the pyvenv.cfg
        f"command = {python_cmd} -m venv --without-pip {venv_prefix}",
    ]

    return "\n".join(lines) + "\n"


class Python(Package):
    """The Python programming language."""

    homepage = "https://www.python.org/"
    url = "https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz"
    list_url = "https://www.python.org/ftp/python/"
    list_depth = 1
    tags = ["windows", "build-tools"]

    maintainers("adamjstewart", "skosukhin", "scheibelp")

    phases = ["configure", "build", "install"]

    #: phase
    install_targets = ["install"]
    build_targets: List[str] = []

    license("0BSD")

    version("3.13.7", sha256="6c9d80839cfa20024f34d9a6dd31ae2a9cd97ff5e980e969209746037a5153b2")
    version("3.12.11", sha256="7b8d59af8216044d2313de8120bfc2cc00a9bd2e542f15795e1d616c51faf3d6")
    version("3.11.13", sha256="0f1a22f4dfd34595a29cf69ee7ea73b9eff8b1cc89d7ab29b3ab0ec04179dad8")
    version("3.10.18", sha256="1b19ab802518eb36a851f5ddef571862c7a31ece533109a99df6d5af0a1ceb99")
    version("3.9.23", sha256="9a69aad184dc1d06f6819930741da3a328d34875a41f8ba33875774dbfc51b51")

    # Deprecated because newer bug fix patch releases exist
    with default_args(deprecated=True):
        version(
            "3.13.5", sha256="e6190f52699b534ee203d9f417bdbca05a92f23e35c19c691a50ed2942835385"
        )
        version(
            "3.13.4", sha256="2666038f1521b7a8ec34bf2997b363778118d6f3979282c93723e872bcd464e0"
        )
        version(
            "3.13.3", sha256="988d735a6d33568cbaff1384a65cb22a1fb18a9ecb73d43ef868000193ce23ed"
        )
        version(
            "3.13.2", sha256="b8d79530e3b7c96a5cb2d40d431ddb512af4a563e863728d8713039aa50203f9"
        )
        version(
            "3.13.1", sha256="1513925a9f255ef0793dbf2f78bb4533c9f184bdd0ad19763fd7f47a400a7c55"
        )
        version(
            "3.13.0", sha256="12445c7b3db3126c41190bfdc1c8239c39c719404e844babbd015a1bc3fafcd4"
        )
        version(
            "3.12.9", sha256="45313e4c5f0e8acdec9580161d565cf5fea578e3eabf25df7cc6355bf4afa1ee"
        )
        version(
            "3.12.8", sha256="5978435c479a376648cb02854df3b892ace9ed7d32b1fead652712bee9d03a45"
        )
        version(
            "3.12.7", sha256="73ac8fe780227bf371add8373c3079f42a0dc62deff8d612cd15a618082ab623"
        )
        version(
            "3.11.11", sha256="883bddee3c92fcb91cf9c09c5343196953cbb9ced826213545849693970868ed"
        )
        version(
            "3.10.16", sha256="f2e22ed965a93cfeb642378ed6e6cdbc127682664b24123679f3d013fafe9cd0"
        )
        version(
            "3.9.21", sha256="667c3ba2ca98d39ead1162f6548c3475768582e2ff89e0821d25eb956ac09944"
        )

    # EOL versions we still want to be able to install
    with default_args(deprecated=True):
        version(
            "3.8.20", sha256="9f2d5962c2583e67ef75924cd56d0c1af78bf45ec57035cf8a2cc09f74f4bf78"
        )
        version(
            "3.7.17", sha256="fd50161bc2a04f4c22a0971ff0f3856d98b4bf294f89740a9f06b520aae63b49"
        )
        version(
            "3.6.15", sha256="54570b7e339e2cfd72b29c7e2fdb47c0b7b18b7412e61de5b463fc087c13b043"
        )

    extendable = True

    # Variants to avoid cyclical dependencies for concretizer
    variant("libxml2", default=True, description="Use a gettext library build with libxml2")

    variant(
        "debug", default=False, description="debug build with extra checks (this is high overhead)"
    )

    variant("shared", default=True, description="Enable shared libraries")
    variant("pic", default=True, description="Produce position-independent code (for shared libs)")
    variant(
        "optimizations",
        default=False,
        description="Enable expensive build-time optimizations, if available",
    )
    # See https://legacy.python.org/dev/peps/pep-0394/
    variant(
        "pythoncmd",
        default=sys.platform != "win32",
        description="Symlink 'python3' executable to 'python' (not PEP 394 compliant)",
    )

    # Optional Python modules
    variant("readline", default=sys.platform != "win32", description="Build readline module")
    variant("ssl", default=True, description="Build ssl module")
    variant("sqlite3", default=True, description="Build sqlite3 module")
    variant("dbm", default=True, description="Build dbm module")
    variant("zlib", default=True, description="Build zlib module")
    variant("bz2", default=True, description="Build bz2 module")
    variant("lzma", default=True, description="Build lzma module")
    variant("pyexpat", default=True, description="Build pyexpat module")
    variant("ctypes", default=True, description="Build ctypes module")
    variant("tkinter", default=False, description="Build tkinter module")
    variant("uuid", default=True, description="Build uuid module")
    variant("tix", default=False, description="Build Tix module", when="+tkinter")
    variant("crypt", default=True, description="Build crypt module", when="@:3.12 platform=linux")
    variant("crypt", default=True, description="Build crypt module", when="@:3.12 platform=darwin")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    if sys.platform != "win32":
        depends_on("gmake", type="build")
        depends_on("pkgconfig", type="build")
        depends_on("gettext +libxml2", when="+libxml2")
        depends_on("gettext ~libxml2", when="~libxml2")

        # Optional dependencies
        # See detect_modules() in setup.py for details
        depends_on("readline", when="+readline")
        depends_on("ncurses", when="+readline")
        depends_on("openssl", when="+ssl")
        # https://docs.python.org/3/whatsnew/3.7.html#build-changes
        depends_on("openssl@1.0.2:", when="+ssl")
        # https://docs.python.org/3.10/whatsnew/3.10.html#build-changes
        depends_on("openssl@1.1.1:", when="@3.10:+ssl")
        depends_on("sqlite@3.0.8:", when="@:3.9+sqlite3")
        # https://docs.python.org/3.10/whatsnew/3.10.html#build-changes
        depends_on("sqlite@3.7.15:", when="@3.10:+sqlite3")
        depends_on("gdbm", when="+dbm")  # alternatively ndbm or berkeley-db
        depends_on("zlib-api", when="+zlib")
        depends_on("bzip2", when="+bz2")
        depends_on("xz libs=shared", when="+lzma")
        depends_on("expat", when="+pyexpat")
        depends_on("libffi", when="+ctypes")
        # https://docs.python.org/3/whatsnew/3.11.html#build-changes
        depends_on("tk@8.5.12:", when="@3.11: +tkinter")
        depends_on("tk", when="+tkinter")
        depends_on("tcl@8.5.12:", when="@3.11: +tkinter")
        depends_on("tcl", when="+tkinter")
        depends_on("uuid", when="+uuid")
        depends_on("tix", when="+tix")
        depends_on("libxcrypt", when="+crypt")

    patch(
        "https://bugs.python.org/file44413/alignment.patch",
        when="@3.6",
        sha256="d39bacde16128f380933992ea7f237ac8f70f9cdffb40c051aca3be46dc29bdf",
    )
    # Python needs to be patched to build extensions w/ mixed C/C++ code:
    # https://github.com/NixOS/nixpkgs/pull/19585/files
    # https://bugs.python.org/issue1222585
    #
    # NOTE: This patch puts Spack's default Python installation out of
    # sync with standard Python installs. If you're using such an
    # installation as an external and encountering build issues with mixed
    # C/C++ modules, consider installing a Spack-managed Python with
    # this patch instead. For more information, see:
    # https://github.com/spack/spack/pull/16856
    patch("python-3.7.4+-distutils-C++.patch", when="@3.7.4:3.10")
    patch("python-3.7.4+-distutils-C++-testsuite.patch", when="@3.7.4:3.11")
    patch("python-3.11-distutils-C++.patch", when="@3.11.0:3.11")
    patch("cpython-windows-externals.patch", when="@:3.9.6 platform=windows")
    patch("tkinter-3.7.patch", when="@3.7 platform=darwin")
    # Patch the setup script to deny that tcl/x11 exists rather than allowing
    # autodetection of (possibly broken) system components
    patch("tkinter-3.8.patch", when="@3.8:3.9 ~tkinter")
    patch("tkinter-3.10.patch", when="@3.10.0:3.10 ~tkinter")
    patch("tkinter-3.11.patch", when="@3.11.0:3.11 ~tkinter")

    # Ensure that distutils chooses correct compiler option for RPATH:
    patch("rpath-non-gcc.patch", when="@:3.11")

    # Ensure that distutils chooses correct compiler option for RPATH on fj:
    patch("fj-rpath-3.1.patch", when="@:3.9.7,3.10.0 %fj")
    patch("fj-rpath-3.9.patch", when="@3.9.8:3.9,3.10.1:3.11 %fj")

    # CPython tries to build an Objective-C file with GCC's C frontend
    # https://github.com/spack/spack/pull/16222
    # https://github.com/python/cpython/pull/13306
    conflicts(
        "platform=darwin %gcc",
        msg="CPython does not compile with GCC on macOS yet, use clang. "
        "See: https://github.com/python/cpython/pull/13306",
    )
    conflicts("%nvhpc")

    # https://bugs.python.org/issue45405
    conflicts("@:3.7.12,3.8.0:3.8.12,3.9.0:3.9.7,3.10.0", when="%apple-clang@13:")

    # See https://github.com/python/cpython/issues/106424
    # datetime.now(timezone.utc) segfaults
    conflicts("@3.9:", when="%oneapi@2022.2.1:2023")

    # Used to cache various attributes that are expensive to compute
    _config_vars: Dict[str, Dict[str, str]] = {}

    # An in-source build with --enable-optimizations fails for python@3.X
    build_directory = "spack-build"

    executables = [r"^python\d?$"]

    @classmethod
    def determine_version(cls, exe):
        # Newer versions of Python support `--version`,
        # but older versions only support `-V`
        # Output looks like:
        #   Python 3.7.7
        # On pre-production Ubuntu, this is also possible:
        #   Python 3.10.2+
        output = Executable(exe)("-V", output=str, error=str)
        match = re.search(r"Python\s+([A-Za-z0-9_.-]+)", output)
        return match.group(1) if match else None

    @classmethod
    def determine_variants(cls, exes, version_str):
        python = Executable(exes[0])

        variants = ""
        for exe in exes:
            if os.path.basename(exe) == "python":
                variants += "+pythoncmd"
                break
        else:
            variants += "~pythoncmd"

        for module in [
            "readline",
            "sqlite3",
            "dbm",
            "zlib",
            "bz2",
            "lzma",
            "ctypes",
            "tkinter",
            "uuid",
        ]:
            try:
                python("-c", "import " + module, error=os.devnull)
                variants += "+" + module
            except ProcessError:
                variants += "~" + module

        # Some variants enable multiple modules
        try:
            python("-c", "import ssl", error=os.devnull)
            python("-c", "import hashlib", error=os.devnull)
            variants += "+ssl"
        except ProcessError:
            variants += "~ssl"

        try:
            python("-c", "import xml.parsers.expat", error=os.devnull)
            python("-c", "import xml.etree.ElementTree", error=os.devnull)
            variants += "+pyexpat"
        except ProcessError:
            variants += "~pyexpat"

        # Some variant names do not match module names
        if "+tkinter" in variants:
            try:
                python("-c", "import tkinter.tix", error=os.devnull)
                variants += "+tix"
            except ProcessError:
                variants += "~tix"

        # Some modules are platform-dependent
        if sys.platform != "win32" and Version(version_str) < Version("3.13"):
            try:
                python("-c", "import crypt", error=os.devnull)
                variants += "+crypt"
            except ProcessError:
                variants += "~crypt"

        return variants

    def url_for_version(self, version):
        url = "https://www.python.org/ftp/python/{0}/Python-{1}.tgz"
        return url.format(re.split("[a-z]", str(version))[0], version)

    def patch(self):
        # NOTE: Python's default installation procedure makes it possible for a
        # user's local configurations to change the Spack installation.  In
        # order to prevent this behavior for a full installation, we must
        # modify the installation script so that it ignores user files.
        ff = FileFilter("Makefile.pre.in")
        ff.filter(
            r"^(.*)setup\.py(.*)((build)|(install))(.*)$", r"\1setup.py\2 --no-user-cfg \3\6"
        )

        # limit the number of processes to use for compileall in older Python versions
        # https://github.com/python/cpython/commit/9a7e9f9921804f3f90151ca42703e612697dd430
        if self.spec.satisfies("@:3.11"):
            ff.filter("-j0 ", f"-j{make_jobs} ")

        # disable building the nis module (there is no flag to disable it).
        if self.spec.satisfies("@3.8:3.10"):
            filter_file(
                "if MS_WINDOWS or CYGWIN or HOST_PLATFORM == 'qnx6':",
                "if True:",
                "setup.py",
                string=True,
            )
        elif self.spec.satisfies("@3.7"):
            filter_file(
                "if host_platform in {'win32', 'cygwin', 'qnx6'}:",
                "if True:",
                "setup.py",
                string=True,
            )
        elif self.spec.satisfies("@3.6"):
            filter_file(
                "if (host_platform not in ['cygwin', 'qnx6'] and",
                "if False and",
                "setup.py",
                string=True,
            )

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        spec = self.spec

        # TODO: Python has incomplete support for Python modules with mixed
        # C/C++ source, and patches are required to enable building for these
        # modules. All Python versions without a viable patch are installed
        # with a warning message about this potentially erroneous behavior.
        if not spec.satisfies("@3.7.2:"):
            tty.warn(
                (
                    'Python v{0} does not have the C++ "distutils" patch; '
                    "errors may occur when installing Python modules w/ "
                    "mixed C/C++ source files."
                ).format(self.version)
            )

        env.unset("PYTHONPATH")
        env.unset("PYTHONHOME")

        # avoid build error on fugaku
        if spec.satisfies("@3.10.0 arch=linux-rhel8-a64fx"):
            if spec.satisfies("%gcc") or spec.satisfies("%fj"):
                env.unset("LC_ALL")

        # https://github.com/python/cpython/issues/87275
        if spec.satisfies("@:3.9.5 +optimizations %apple-clang"):
            xcrun = Executable("/usr/bin/xcrun")
            env.set("LLVM_AR", xcrun("-find", "ar", output=str).strip())

    def flag_handler(self, name, flags):
        # python 3.8 requires -fwrapv when compiled with intel
        if self.spec.satisfies("@3.8: %intel"):
            if name == "cflags":
                flags.append("-fwrapv")

        # Fix for following issues for python with aocc%3.2.0:
        # https://github.com/spack/spack/issues/29115
        # https://github.com/spack/spack/pull/28708
        if self.spec.satisfies("%aocc@3.2.0"):
            if name == "cflags":
                flags.extend(["-mllvm", "-disable-indvar-simplify=true"])

        # allow flags to be passed through compiler wrapper
        return (flags, None, None)

    @property
    def plat_arch(self):
        """
        String referencing platform architecture
        filtered through Python's Windows build file
        architecture support map

        Note: This function really only makes
        sense to use on Windows, could be overridden to
        cross compile however.
        """

        arch_map = {"AMD64": "x64", "x86": "Win32", "IA64": "Win32", "EM64T": "Win32"}
        arch = platform.machine()
        if arch in arch_map:
            arch = arch_map[arch]
        return arch

    @property
    def win_build_params(self):
        """
        Arguments must be passed to the Python build batch script
        in order to configure it to spec and system.
        A number of these toggle optional MSBuild Projects
        directly corresponding to the python support of the same
        name.
        """
        args = []
        args.append("-p %s" % self.plat_arch)
        if self.spec.satisfies("+debug"):
            args.append("-d")
        if self.spec.satisfies("~ctypes"):
            args.append("--no-ctypes")
        if self.spec.satisfies("~ssl"):
            args.append("--no-ssl")
        if self.spec.satisfies("~tkinter"):
            args.append("--no-tkinter")
        return args

    def win_installer(self, prefix):
        """
        Python on Windows does not export an install target
        so we must handcraft one here. This structure
        directly mimics the install tree of the Python
        Installer on Windows.

        Parameters:
            prefix (str): Install prefix for package
        """
        proj_root = Path(self.stage.source_path)
        pcbuild_root = proj_root / "PCbuild"
        build_root = pcbuild_root / platform.machine().lower()
        # install headers
        include_dir = proj_root / "Include"
        copy_tree(str(include_dir), prefix.include)
        if self.spec.satisfies("@3.13:"):
            pyconfig = pcbuild_root / platform.machine().lower() / "pyconfig.h"
        else:
            pyconfig = proj_root / "PC" / "pyconfig.h"
        copy(str(pyconfig), prefix.include)
        # install docs
        doc_dir = proj_root / "Doc"
        copy_tree(str(doc_dir), prefix.Doc)
        # install tools
        tools_dir = proj_root / "Tools"
        copy_tree(str(tools_dir), prefix.Tools)
        # install stdlib python modules
        lib_dir = proj_root / "Lib"
        copy_tree(str(lib_dir), prefix.Lib)

        # locate and track all pdb files
        pdbs = glob.glob(f"{str(build_root)}\\*.pdb")
        pdb_assoc = {}
        for pdb in pdbs:
            filename = os.path.splitext(os.path.basename(pdb))[0]
            pdb_assoc[filename] = pdb

        def install_pdb(binary: str, loc: str):
            file_name = os.path.splitext(os.path.basename(binary))[0]
            if file_name in pdb_assoc:
                copy(pdb_assoc[file_name], loc)

        # handle executables
        executables = glob.glob(f"{str(build_root)}\\*.exe")
        for exe in executables:
            copy(exe, prefix)
            install_pdb(exe, prefix)

        # setup venv module correctly
        venv_binaries = ("python.exe", "pythonw.exe")
        if self.spec.satisfies("@3.13:"):
            # 3.13 installs two new executables rather than copying
            # python.exe into the venv module
            # there are essentially just python.exe with a different name
            # and are renamed to python.exe by the venv module when venvs
            # are created
            venv_binaries = ("venvlauncher.exe", "venvwlauncher.exe")
        for binary in venv_binaries:
            copy(str(build_root / binary), prefix.Lib.venv.scripts.nt)

        # handle shared libraries
        shared_libraries = glob.glob(f"{str(build_root)}\\*.dll")
        shared_libraries.extend(glob.glob(f"{str(build_root)}\\*.pyd"))
        os.makedirs(prefix.DLLs)
        for lib in shared_libraries:
            libname = os.path.basename(lib)
            dest = prefix.DLLs
            if "python" in libname or "vcruntime" in libname:
                dest = prefix

            copy(lib, dest)
            install_pdb(lib, dest)

        # handle static libraries
        static_libraries = glob.glob(f"{str(build_root)}\\*.lib")
        os.makedirs(prefix.libs, exist_ok=True)
        for lib in static_libraries:
            copy(lib, prefix.libs)
            install_pdb(lib, prefix.libs)

    def configure_args(self):
        spec = self.spec
        config_args = []
        cflags = []

        # setup.py needs to be able to read the CPPFLAGS and LDFLAGS
        # as it scans for the library and headers to build
        link_deps = spec.dependencies(deptype="link")

        if link_deps:
            # Header files are often included assuming they reside in a
            # subdirectory of prefix.include, e.g. #include <openssl/ssl.h>,
            # which is why we don't use HeaderList here. The header files of
            # libffi reside in prefix.lib but the configure script of Python
            # finds them using pkg-config.
            cppflags = " ".join("-I" + spec[dep.name].prefix.include for dep in link_deps)

            # Currently, the only way to get SpecBuildInterface wrappers of the
            # dependencies (which we need to get their 'libs') is to get them
            # using spec.__getitem__.
            ldflags = " ".join(spec[dep.name].libs.search_flags for dep in link_deps)

            config_args.extend(["CPPFLAGS=" + cppflags, "LDFLAGS=" + ldflags])

        if "+optimizations" in spec:
            config_args.append("--enable-optimizations")
            # Prefer thin LTO for faster compilation times.
            if "@3.11.0: %clang@3.9:" in spec or "@3.11.0: %apple-clang@8:" in spec:
                config_args.append("--with-lto=thin")
            else:
                config_args.append("--with-lto")
            config_args.append("--with-computed-gotos")

        if spec.satisfies("@3.7 %intel"):
            config_args.append("--with-icc={0}".format(spack_cc))

        if "+debug" in spec:
            config_args.append("--with-pydebug")
        else:
            config_args.append("--without-pydebug")

        if "+shared" in spec:
            config_args.append("--enable-shared")
        else:
            config_args.append("--disable-shared")

        config_args.append("--without-ensurepip")

        if "+pic" in spec:
            cflags.append(self["c"].pic_flag)

        if "+ssl" in spec:
            config_args.append("--with-openssl={0}".format(spec["openssl"].prefix))

        if "+dbm" in spec:
            # Default order is ndbm:gdbm:bdb
            config_args.append("--with-dbmliborder=gdbm")
        else:
            config_args.append("--with-dbmliborder=")

        if "+pyexpat" in spec:
            config_args.append("--with-system-expat")
        else:
            config_args.append("--without-system-expat")

        if self.version < Version("3.12.0"):
            if "+ctypes" in spec:
                config_args.append("--with-system-ffi")
            else:
                config_args.append("--without-system-ffi")

        if "+tkinter" in spec:
            config_args.extend(
                [
                    "--with-tcltk-includes=-I{0} -I{1}".format(
                        spec["tcl"].prefix.include, spec["tk"].prefix.include
                    ),
                    "--with-tcltk-libs={0} {1}".format(
                        spec["tcl"].libs.ld_flags, spec["tk"].libs.ld_flags
                    ),
                ]
            )

        # Disable the nis module in the configure script for Python 3.11 and 3.12. It is deleted
        # in Python 3.13. See ``def patch`` for disabling the nis module in Python 3.10 and older.
        if spec.satisfies("@3.11:3.12"):
            config_args.append("py_cv_module_nis=n/a")

        # https://docs.python.org/3.8/library/sqlite3.html#f1
        if spec.satisfies("+sqlite3 ^sqlite+dynamic_extensions"):
            config_args.append("--enable-loadable-sqlite-extensions")

        if spec.satisfies("%oneapi"):
            cflags.append("-fp-model=strict")

        if cflags:
            config_args.append("CFLAGS={0}".format(" ".join(cflags)))

        if self.version >= Version("3.12.0") and sys.platform == "darwin":
            config_args.append("CURSES_LIBS={0}".format(spec["ncurses"].libs.link_flags))

        return config_args

    def configure(self, spec, prefix):
        """Runs configure with the arguments specified in
        :meth:`~spack_repo.builtin.build_systems.autotools.AutotoolsPackage.configure_args`
        and an appropriately set prefix.
        """
        with working_dir(self.stage.source_path, create=True):
            if sys.platform == "win32":
                pass
            else:
                options = getattr(self, "configure_flag_args", [])
                options += ["--prefix={0}".format(prefix)]
                options += self.configure_args()
                configure(*options)

    def build(self, spec, prefix):
        """Makes the build targets specified by
        :py:attr:``~.AutotoolsPackage.build_targets``
        """
        # Windows builds use a batch script to drive
        # configure and build in one step
        with working_dir(self.stage.source_path):
            if sys.platform == "win32":
                pcbuild_root = os.path.join(self.stage.source_path, "PCbuild")
                builder_cmd = os.path.join(pcbuild_root, "build.bat")
                try:
                    subprocess.check_output(  # novermin
                        " ".join([builder_cmd] + self.win_build_params), stderr=subprocess.STDOUT
                    )
                except subprocess.CalledProcessError as e:
                    raise ProcessError(
                        "Process exited with status %d" % e.returncode,
                        long_message=e.output.decode("utf-8"),
                    )
            else:
                # See https://autotools.io/automake/silent.html
                params = ["V=1"]
                params += self.build_targets
                make(*params)

    def install(self, spec, prefix):
        """Makes the install targets specified by
        :py:attr:``~.AutotoolsPackage.install_targets``
        """
        with working_dir(self.stage.source_path):
            if sys.platform == "win32":
                self.win_installer(prefix)
            else:
                # See https://github.com/python/cpython/issues/102007
                make(*self.install_targets, f"COMPILEALL_OPTS=-j{make_jobs}", parallel=False)

    @run_after("install")
    def filter_compilers(self):
        """Run after install to tell the configuration files and Makefiles
        to use the compilers that Spack built the package with.

        If this isn't done, they'll have CC and CXX set to Spack's generic
        cc and c++. We want them to be bound to whatever compiler
        they were built with."""
        if sys.platform == "win32":
            return
        kwargs = {"ignore_absent": True, "backup": False, "string": True}

        filenames = [self.get_sysconfigdata_name(), self.config_vars["makefile_filename"]]

        filter_file(spack_cc, self["c"].cc, *filenames, **kwargs)
        if spack_cxx:
            filter_file(spack_cxx, self["cxx"].cxx, *filenames, **kwargs)

    @run_after("install")
    def symlink(self):
        if sys.platform == "win32":
            return
        spec = self.spec
        prefix = self.prefix

        if spec.satisfies("+pythoncmd"):
            os.symlink(os.path.join(prefix.bin, "python3"), os.path.join(prefix.bin, "python"))
            os.symlink(
                os.path.join(prefix.bin, "python3-config"),
                os.path.join(prefix.bin, "python-config"),
            )

    @run_after("install")
    def install_python_gdb(self):
        # https://devguide.python.org/gdb/
        src = os.path.join("Tools", "gdb", "libpython.py")
        if os.path.exists(src):
            install(src, self.command.path + "-gdb.py")

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def import_tests(self):
        """Test that basic Python functionality works."""

        spec = self.spec

        with working_dir("spack-test", create=True):
            # Ensure that readline module works
            if "+readline" in spec:
                self.command("-c", "import readline")

            # Ensure that ssl module works
            if "+ssl" in spec:
                self.command("-c", "import ssl")
                self.command("-c", "import hashlib")

            # Ensure that sqlite3 module works
            if "+sqlite3" in spec:
                self.command("-c", "import sqlite3")

            # Ensure that dbm module works
            if "+dbm" in spec:
                self.command("-c", "import dbm")

            # Ensure that zlib module works
            if "+zlib" in spec:
                self.command("-c", "import zlib")

            # Ensure that bz2 module works
            if "+bz2" in spec:
                self.command("-c", "import bz2")

            # Ensure that lzma module works
            if "+lzma" in spec:
                self.command("-c", "import lzma")

            # Ensure that pyexpat module works
            if "+pyexpat" in spec:
                self.command("-c", "import xml.parsers.expat")
                self.command("-c", "import xml.etree.ElementTree")

            # Ensure that ctypes module works
            if "+ctypes" in spec:
                self.command("-c", "import ctypes")

            # Ensure that tkinter module works
            # https://wiki.python.org/moin/TkInter
            if "+tkinter" in spec:
                # Only works if ForwardX11Trusted is enabled, i.e. `ssh -Y`
                if "DISPLAY" in env:
                    self.command("-c", "import tkinter; tkinter._test()")
                else:
                    self.command("-c", "import tkinter")

            # Ensure that uuid module works
            if "+uuid" in spec:
                self.command("-c", "import uuid")

            # Ensure that tix module works
            if "+tix" in spec:
                self.command("-c", "import tkinter.tix")

            # Ensure that crypt module works
            if "+crypt" in spec:
                self.command("-c", "import crypt")

    # ========================================================================
    # Set up environment to make install easy for python extensions.
    # ========================================================================

    @property
    def command(self):
        """Returns the Python command, which may vary depending
        on the version of Python and how it was installed.

        In general, Python 3 only comes with a ``python3`` command. However, some
        package managers will symlink ``python`` to ``python3``, while others
        may contain ``python3.11``, ``python3.10``, and ``python3.9`` in the
        same directory.

        Returns:
            Executable: the Python command
        """
        # We need to be careful here. If the user is using an externally
        # installed python, several different commands could be located
        # in the same directory. Be as specific as possible. Search for:
        #
        # * python3.11
        # * python3
        # * python
        #
        # in that order if using python@3.11.0, for example.
        suffixes = [self.spec.version.up_to(2), self.spec.version.up_to(1), ""]
        ext = "" if sys.platform != "win32" else ".exe"
        filenames = [f"python{ver}{ext}" for ver in suffixes]
        root = self.prefix.bin if sys.platform != "win32" else self.prefix

        for filename in filenames:
            path = os.path.join(root, filename)
            if is_exe(path):
                return Executable(path)

        # Give a last try at rhel8 platform python
        platform_python = os.path.join(self.prefix, "libexec", "platform-python")
        if self.spec.external and self.prefix == "/usr" and is_exe(platform_python):
            return Executable(platform_python)

        raise RuntimeError(
            f"cannot locate the '{self.name}' command in {root} or its subdirectories"
        )

    @property
    def config_vars(self):
        """Return a set of variable definitions associated with a Python installation.

        Wrapper around various ``sysconfig`` functions. To see these variables on the
        command line, run:

        .. code-block:: console

           $ python -m sysconfig

        Returns:
            dict: variable definitions
        """
        cmd = """
import json
from sysconfig import (
    get_config_vars,
    get_config_h_filename,
    get_makefile_filename,
    get_paths,
)

config = get_config_vars()
config['config_h_filename'] = get_config_h_filename()
config['makefile_filename'] = get_makefile_filename()
config.update(get_paths())

print(json.dumps(config))
"""

        dag_hash = self.spec.dag_hash()
        lib_prefix = "lib" if sys.platform != "win32" else ""
        if dag_hash not in self._config_vars:
            # Default config vars
            version = self.version.up_to(2)
            if sys.platform == "win32":
                version = str(version).split(".")[0]
            config = {
                # get_config_vars
                "BINDIR": self.prefix.bin,
                "CC": "cc",
                "CONFINCLUDEPY": self.prefix.include.join("python{}").format(version),
                "CXX": "c++",
                "INCLUDEPY": self.prefix.include.join("python{}").format(version),
                "LIBDEST": self.prefix.lib.join("python{}").format(version),
                "LIBDIR": self.prefix.lib,
                "LIBPL": self.prefix.lib.join("python{0}")
                .join("config-{0}-{1}")
                .format(version, sys.platform),
                "LDLIBRARY": "{}python{}.{}".format(
                    lib_prefix, version, shared_library_suffix(self.spec)
                ),
                "LIBRARY": "{}python{}.{}".format(
                    lib_prefix, version, static_library_suffix(self.spec)
                ),
                "LDSHARED": "cc",
                "LDCXXSHARED": "c++",
                "PYTHONFRAMEWORKPREFIX": "/System/Library/Frameworks",
                "base": self.prefix,
                "installed_base": self.prefix,
                "installed_platbase": self.prefix,
                "platbase": self.prefix,
                "prefix": self.prefix,
                # get_config_h_filename
                "config_h_filename": self.prefix.include.join("python{}")
                .join("pyconfig.h")
                .format(version),
                # get_makefile_filename
                "makefile_filename": self.prefix.lib.join("python{0}")
                .join("config-{0}-{1}")
                .Makefile.format(version, sys.platform),
                # get_paths
                "data": self.prefix,
                "include": self.prefix.include.join("python{}".format(version)),
                "platinclude": self.prefix.include64.join("python{}".format(version)),
                "platlib": self.prefix.lib64.join("python{}".format(version)).join(
                    "site-packages"
                ),
                "platstdlib": self.prefix.lib64.join("python{}".format(version)),
                "purelib": self.prefix.lib.join("python{}".format(version)).join("site-packages"),
                "scripts": self.prefix.bin,
                "stdlib": self.prefix.lib.join("python{}".format(version)),
            }

            try:
                config.update(json.loads(self.command("-c", cmd, output=str)))
            except (ProcessError, RuntimeError):
                pass
            self._config_vars[dag_hash] = config
        return self._config_vars[dag_hash]

    def get_sysconfigdata_name(self):
        """Return the full path name of the sysconfigdata file."""

        libdest = self.config_vars["LIBDEST"]

        cmd = "from sysconfig import _get_sysconfigdata_name; "
        cmd += "print(_get_sysconfigdata_name())"
        filename = self.command("-c", cmd, output=str).strip()
        filename += ".py"

        return join_path(libdest, filename)

    @property
    def home(self):
        """Most of the time, ``PYTHONHOME`` is simply
        ``spec['python'].prefix``. However, if the user is using an
        externally installed python, it may be symlinked. For example,
        Homebrew installs python in ``/usr/local/Cellar/python/2.7.12_2``
        and symlinks it to ``/usr/local``. Users may not know the actual
        installation directory and add ``/usr/local`` to their
        ``packages.yaml`` unknowingly. Query the python executable to
        determine exactly where it is installed.
        """
        return Prefix(self.config_vars["base"])

    def find_library(self, library):
        # Spack installs libraries into lib, except on openSUSE where it installs them
        # into lib64. If the user is using an externally installed package, it may be
        # in either lib or lib64, so we need to ask Python where its LIBDIR is.
        libdir = self.config_vars["LIBDIR"]

        # Debian and derivatives use a triplet subdir under /usr/lib, LIBPL can be used
        # to get the Python library directory
        libpldir = self.config_vars["LIBPL"]

        # The system Python installation on macOS and Homebrew installations
        # install libraries into a Frameworks directory
        frameworkprefix = self.config_vars["PYTHONFRAMEWORKPREFIX"]

        # Get the active Xcode environment's Framework location.
        macos_developerdir = os.environ.get("DEVELOPER_DIR")
        if macos_developerdir and os.path.exists(macos_developerdir):
            macos_developerdir = os.path.join(macos_developerdir, "Library", "Frameworks")
        else:
            macos_developerdir = ""

        # Windows libraries are installed directly to BINDIR
        win_bin_dir = self.config_vars["BINDIR"]
        win_root_dir = self.config_vars["prefix"]

        directories = [
            libdir,
            libpldir,
            frameworkprefix,
            macos_developerdir,
            win_bin_dir,
            win_root_dir,
        ]

        if self.spec.satisfies("platform=windows"):
            lib_dirs = ["libs"]
        else:
            # The Python shipped with Xcode command line tools isn't in any of these locations
            lib_dirs = ["lib", "lib64"]

        for subdir in lib_dirs:
            directories.append(os.path.join(self.config_vars["base"], subdir))

        directories = dedupe(directories)
        for directory in directories:
            path = os.path.join(directory, library)
            if os.path.exists(path):
                return LibraryList(path)

    @property
    def libs(self):
        py_version = self.version.up_to(2)
        if sys.platform == "win32":
            py_version = str(py_version).replace(".", "")
        lib_prefix = "lib" if sys.platform != "win32" else ""
        # The values of LDLIBRARY and LIBRARY aren't reliable. Intel Python uses a
        # static binary but installs shared libraries, so sysconfig reports
        # libpythonX.Y.a but only libpythonX.Y.so exists. So we add our own paths, too.

        # With framework python on macOS, self.config_vars["LDLIBRARY"] can point
        # to a library that is not linkable because it does not have the required
        # suffix of a shared library (it is called "Python" without extention).
        # The linker then falls back to libPython.tbd in the default macOS
        # software tree, which security settings prohibit to link against
        # (your binary is not an allowed client of /path/to/libPython.tbd).
        # To avoid this, we replace the entry in config_vars with a default value.
        file_extension_shared = os.path.splitext(self.config_vars["LDLIBRARY"])[-1]
        if file_extension_shared == "":
            shared_libs = []
        else:
            shared_libs = [self.config_vars["LDLIBRARY"]]
        shared_libs += [
            "{}python{}.{}".format(lib_prefix, py_version, shared_library_suffix(self.spec))
        ]
        # Like LDLIBRARY for Python on Mac OS, LIBRARY may refer to an un-linkable object
        file_extension_static = os.path.splitext(self.config_vars["LIBRARY"])[-1]
        if file_extension_static == "":
            static_libs = []
        else:
            static_libs = [self.config_vars["LIBRARY"]]
        static_libs += [
            "{}python{}.{}".format(lib_prefix, py_version, static_library_suffix(self.spec))
        ]

        # The +shared variant isn't reliable, as `spack external find` currently can't
        # detect it. If +shared, prefer the shared libraries, but check for static if
        # those aren't found. Vice versa for ~shared.
        if self.spec.satisfies("platform=windows"):
            # Since we are searching for link libraries, on Windows search only for
            # ".Lib" extensions by default as those represent import libraries for implict links.
            candidates = static_libs
        elif self.spec.satisfies("+shared"):
            candidates = shared_libs + static_libs
        else:
            candidates = static_libs + shared_libs

        for candidate in dedupe(candidates):
            lib = self.find_library(candidate)
            if lib:
                return lib

        raise NoLibrariesError(
            "Unable to find {} libraries with the following names:\n\n* ".format(self.name)
            + "\n* ".join(candidates)
        )

    @property
    def headers(self):
        # Locations where pyconfig.h could be
        # This varies by system, especially on macOS where the command line tools are
        # installed in a very different directory from the system python interpreter.
        py_version = str(self.version.up_to(2))
        candidates = [
            os.path.dirname(self.config_vars["config_h_filename"]),
            self.config_vars["INCLUDEPY"],
            self.config_vars["CONFINCLUDEPY"],
            os.path.join(self.config_vars["base"], "include", py_version),
            os.path.join(self.config_vars["base"], "Headers"),
        ]
        candidates = list(dedupe(candidates))

        for directory in candidates:
            headers = find_headers("pyconfig", directory)
            if headers:
                config_h = headers[0]
                break
        else:
            raise NoHeadersError(
                "Unable to locate {} headers in any of these locations:\n\n* ".format(self.name)
                + "\n* ".join(candidates)
            )

        headers.directories = [os.path.dirname(config_h)]
        return headers

    # https://docs.python.org/3/library/sysconfig.html#installation-paths
    # https://discuss.python.org/t/understanding-site-packages-directories/12959
    # https://github.com/pypa/pip/blob/22.1/src/pip/_internal/locations/__init__.py
    # https://github.com/pypa/installer/pull/103

    # NOTE: XCode Python's sysconfing module was incorrectly patched, and hard-codes
    # everything to be installed in /Library/Python. Therefore, we need to use a
    # fallback in the following methods. For more information, see:
    # https://github.com/pypa/pip/blob/22.1/src/pip/_internal/locations/__init__.py#L486

    @property
    def platlib(self):
        """Directory for site-specific, platform-specific files.

        Exact directory depends on platform/OS/Python version. Examples include:

        * ``lib/pythonX.Y/site-packages`` on most POSIX systems
        * ``lib64/pythonX.Y/site-packages`` on RHEL/CentOS/Fedora with system Python
        * ``lib/pythonX/dist-packages`` on Debian/Ubuntu with system Python
        * ``lib/python/site-packages`` on macOS with framework Python
        * ``Lib/site-packages`` on Windows

        Returns:
            str: platform-specific site-packages directory
        """
        prefix = self.config_vars["platbase"] + os.sep
        path = self.config_vars["platlib"]
        if path.startswith(prefix):
            return path.replace(prefix, "")
        return os.path.join("lib64", f"python{self.version.up_to(2)}", "site-packages")

    @property
    def purelib(self):
        """Directory for site-specific, non-platform-specific files.

        Exact directory depends on platform/OS/Python version. Examples include:

        * ``lib/pythonX.Y/site-packages`` on most POSIX systems
        * ``lib/pythonX/dist-packages`` on Debian/Ubuntu with system Python
        * ``lib/python/site-packages`` on macOS with framework Python
        * ``Lib/site-packages`` on Windows

        Returns:
            str: platform-independent site-packages directory
        """
        prefix = self.config_vars["base"] + os.sep
        path = self.config_vars["purelib"]
        if path.startswith(prefix):
            return path.replace(prefix, "")
        return os.path.join("lib", f"python{self.version.up_to(2)}", "site-packages")

    @property
    def include(self):
        """Directory for non-platform-specific header files.

        Exact directory depends on platform/Python version/ABI flags. Examples include:

        * ``include/pythonX.Y`` on most POSIX systems
        * ``include/pythonX.Yd`` for debug builds
        * ``include/pythonX.Ym`` for malloc builds
        * ``include/pythonX.Yu`` for wide unicode builds
        * ``include`` on macOS with framework Python
        * ``Include`` on Windows

        Returns:
            str: platform-independent header file directory
        """
        prefix = self.config_vars["installed_base"] + os.sep
        path = self.config_vars["include"]
        if path.startswith(prefix):
            return path.replace(prefix, "")
        return os.path.join("include", "python{}".format(self.version.up_to(2)))

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        """Set PYTHONPATH to include the site-packages directory for the
        extension and any other python extensions it depends on.
        """
        # The logic below is linux specific, and used to inject the compiler wrapper to
        # compile Python extensions. Thus, it is not needed on Windows.
        if sys.platform == "win32":
            env.prepend_path("PATH", self.prefix)
            return

        # We need to make sure that the extensions are compiled and linked with
        # the Spack wrapper. Paths to the executables that are used for these
        # operations are normally taken from the sysconfigdata file, which we
        # modify after the installation (see method filter compilers). The
        # modified file contains paths to the real compilers, not the wrappers.
        # The values in the file, however, can be overridden with environment
        # variables. The first variable, CC (CXX), which is used for
        # compilation, is set by Spack for the dependent package by default.
        # That is not 100% correct because the value for CC (CXX) in the
        # sysconfigdata file often contains additional compiler flags (e.g.
        # -pthread), which we lose by simply setting CC (CXX) to the path to the
        # Spack wrapper. Moreover, the user might try to build an extension with
        # a compiler that is different from the one that was used to build
        # Python itself, which might have unexpected side effects. However, the
        # experience shows that none of the above is a real issue and we will
        # not try to change the default behaviour. Given that, we will simply
        # try to modify LDSHARED (LDCXXSHARED), the second variable, which is
        # used for linking, in a consistent manner.

        for language, compile_var, link_var in [
            ("c", "CC", "LDSHARED"),
            ("cxx", "CXX", "LDCXXSHARED"),
        ]:
            if not dependent_spec.has_virtual_dependency(language):
                continue

            compiler_wrapper_pkg = dependent_spec["compiler-wrapper"].package
            compiler_pkg = dependent_spec[language].package

            # First, we get the values from the sysconfigdata:
            config_compile = self.config_vars[compile_var]
            config_link = self.config_vars[link_var]

            # The dependent environment will have the compilation command set to
            # the following:
            new_compile = str(
                compiler_wrapper_pkg.bin_dir() / compiler_pkg.compiler_wrapper_link_paths[language]
            )

            # Normally, the link command starts with the compilation command:
            if config_link.startswith(config_compile):
                new_link = new_compile + config_link[len(config_compile) :]
            else:
                # Otherwise, we try to replace the compiler command if it
                # appears "in the middle" of the link command; to avoid
                # mistaking some substring of a path for the compiler (e.g. to
                # avoid replacing "gcc" in "-L/path/to/gcc/"), we require that
                # the compiler command be surrounded by spaces. Note this may
                # leave "config_link" unchanged if the compilation command does
                # not appear in the link command at all, for example if "ld" is
                # invoked directly (no change would be required in that case
                # because Spack arranges for the Spack ld wrapper to be the
                # first instance of "ld" in PATH).
                new_link = config_link.replace(f" {config_compile} ", f" {new_compile} ")

            # There is logic in the sysconfig module that is sensitive to the
            # fact that LDSHARED is set in the environment, therefore we export
            # the variable only if the new value is different from what we got
            # from the sysconfigdata file:
            if config_link != new_link and sys.platform != "win32":
                env.set(link_var, new_link)

    def setup_dependent_run_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        """Set PYTHONPATH to include the site-packages directory for the
        extension and any other python extensions it depends on.
        """
        if sys.platform == "win32":
            env.prepend_path("PATH", self.prefix)
        if not dependent_spec.package.extends(self.spec) or dependent_spec.dependencies(
            "python-venv"
        ):
            return

        # Packages may be installed in platform-specific or platform-independent site-packages
        # directories
        for directory in {self.platlib, self.purelib}:
            env.prepend_path("PYTHONPATH", os.path.join(dependent_spec.prefix, directory))

    def setup_dependent_package(self, module, dependent_spec):
        """Called before python modules' install() methods."""
        module.python = self.command
        module.python_include = join_path(dependent_spec.prefix, self.include)
        module.python_platlib = join_path(dependent_spec.prefix, self.platlib)
        module.python_purelib = join_path(dependent_spec.prefix, self.purelib)

    def add_files_to_view(self, view, merge_map, skip_if_exists=True):
        """Make the view a virtual environment if it isn't one already.

        If `python-venv` is linked into the view, it will already be a virtual
        environment. If not, then this is an older python that doesn't use the
        python-venv support, or we may be using python packages that
        use ``depends_on("python")`` but not ``extends("python")``.

        We used to copy the python interpreter in, but we can get the same effect in a
        simpler way by adding a ``pyvenv.cfg`` to the environment.

        """
        super().add_files_to_view(view, merge_map, skip_if_exists=skip_if_exists)

        # location of python inside the view, where we will put the venv config
        projection = view.get_projection_for_spec(self.spec)
        pyvenv_cfg = os.path.join(projection, "pyvenv.cfg")
        if os.path.lexists(pyvenv_cfg):
            return

        # don't put a pyvenv.cfg in a copy view
        if view.link_type == "copy":
            return

        with open(pyvenv_cfg, "w") as cfg_file:
            cfg_file.write(make_pyvenv_cfg(self, projection))

    def test_hello_world(self):
        """run simple hello world program"""
        out = self.command("-c", 'print("hello world!")', output=str.split, error=str.split)
        assert "hello world!" in out

    def test_import_executable(self):
        """ensure import of installed executable works"""
        python = self.command
        out = python("-c", "import sys; print(sys.executable)", output=str.split, error=str.split)
        assert self.spec.prefix in out
