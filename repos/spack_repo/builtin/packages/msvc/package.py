# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os.path
import re

from spack_repo.builtin.build_systems import compiler
from spack_repo.builtin.build_systems.compiler import CompilerPackage
from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

FC_PATH: Dict[str, str] = dict()


def get_latest_valid_fortran_pth():
    """Assign maximum available fortran compiler version"""
    # TODO (johnwparent): validate compatibility w/ try compiler
    # functionality when added
    sort_fn = lambda fc_ver: Version(fc_ver)
    sort_fc_ver = sorted(list(FC_PATH.keys()), key=sort_fn)
    return FC_PATH[sort_fc_ver[-1]] if sort_fc_ver else None


class Msvc(Package, CompilerPackage):
    """
    Microsoft Visual C++ is a compiler for the C, C++, C++/CLI and C++/CX programming languages.
    """

    homepage = "https://visualstudio.microsoft.com/vs/features/cplusplus/"

    has_code = False

    def install(self, spec, prefix):
        raise InstallError(
            "MSVC compilers are not installable with Spack, but can be "
            "detected on a system where they are externally installed"
        )

    compiler_languages = ["c", "cxx", "fortran"]
    c_names = ["cl"]
    cxx_names = ["cl"]
    fortran_names = ["ifx", "ifort"]

    compiler_version_argument = ""
    compiler_version_regex = r"([1-9][0-9]*\.[0-9]*\.[0-9]*)"

    # Due to the challenges of supporting compiler wrappers
    # in Windows, we leave these blank, and dynamically compute
    # based on proper versions of MSVC from there
    # pending acceptance of #28117 for full support using
    # compiler wrappers
    compiler_wrapper_link_paths = {"c": "", "cxx": "", "fortran": ""}

    provides("c", "cxx", "fortran")
    requires("platform=windows", msg="MSVC is only supported on Windows")

    @classmethod
    def determine_version(cls, exe):
        # MSVC compiler does not have a proper version argument
        # Errors out and prints version info with no args
        is_ifx = "ifx.exe" in str(exe)
        match = re.search(
            cls.compiler_version_regex,
            compiler.compiler_output(exe, version_argument=None, ignore_errors=1),
        )
        if match:
            if is_ifx:
                FC_PATH[match.group(1)] = str(exe)
            return match.group(1)

    @classmethod
    def determine_variants(cls, exes, version_str):
        # MSVC uses same executable for both languages
        spec, extras = super().determine_variants(exes, version_str)
        extras["compilers"]["c"] = extras["compilers"]["cxx"]
        # This depends on oneapi being processed before msvc
        # which is guarunteed from detection behavior.
        # Processing oneAPI tracks oneAPI installations within
        # this module, which are then used to populate compatible
        # MSVC version's fortran compiler spots

        # TODO: remove this once #45189 lands
        # TODO: interrogate intel and msvc for compatibility after
        # #45189 lands
        fortran_compiler = get_latest_valid_fortran_pth()
        if fortran_compiler is not None:
            extras["compilers"]["fortran"] = fortran_compiler
        return spec, extras

    def setup_dependent_package(self, module, dependent_spec):
        """Populates dependent module with tooling available from VS"""
        # We want these to resolve to the paths set by MSVC's VCVARs
        # so no paths
        module.nmake = Executable("nmake")
        module.msbuild = Executable("msbuild")

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:

        # To use the MSVC compilers, VCVARS must be invoked
        # VCVARS is located at a fixed location, referencable
        # idiomatically by the following relative path from the
        # compiler.
        # Spack first finds the compilers via VSWHERE
        # and stores their path, but their respective VCVARS
        # file must be invoked before useage.
        compiler_root = os.path.join(os.path.dirname(self.cc), "../../../../../..")
        vcvars_script_path = os.path.join(compiler_root, "Auxiliary", "Build", "vcvars64.bat")
        # get current platform architecture and format for vcvars argument
        arch = host_platform().default.lower()
        arch = arch.replace("-", "_")
        if self.spec.satisfies("target=x86_64:"):
            arch = "amd64"

        msvc_version = Version(re.search(Msvc.compiler_version_regex, self.cc).group(1))
        vcvars_ver = f"-vcvars_ver={msvc_version}"
        vcvars_args = [arch]
        # vcvars can target specific sdk versions, force it to pick up concretized sdk
        # version, if needed by spec
        if dependent_spec.name != "win-sdk" and "win-sdk" in dependent_spec:
            vcvars_args.append(dependent_spec["win-sdk"].version.string + ".0")
        vcvars_args.append(vcvars_ver)
        if dependent_spec.satisfies("+spectre"):
            vcvars_args.append("spectre")
        local_env = os.environ.copy()
        vars_mods = EnvironmentModifications.from_sourcing_file(
            vcvars_script_path, *vcvars_args, env=local_env
        )
        vars_mods.apply_modifications(env=local_env)

        def get_oneapi_root(pth: str):
            """From within a prefix known to be a oneAPI path
            determine the oneAPI root path from arbitrary point
            under root

            Args:
                pth: path prefixed within oneAPI root
            """
            if not pth:
                return ""
            while os.path.basename(pth) and os.path.basename(pth) != "oneAPI":
                pth = os.path.dirname(pth)
            return pth

        if self.fortran:
            # If this found, it sets all the vars
            oneapi_root = get_oneapi_root(self.fortran)
            if not oneapi_root:
                raise RuntimeError(f"Non-oneAPI Fortran compiler {self.fortran} assigned to MSVC")
            oneapi_root_setvars = os.path.join(oneapi_root, "setvars.bat")
            # some oneAPI exes return a version more precise than their
            # install paths specify, so we determine path from
            # the install path rather than the fc executable itself
            numver = r"\d+\.\d+(?:\.\d+)?"
            pattern = f"((?:{numver})|(?:latest))"
            version_from_path = re.search(pattern, self.fortran).group(1)
            oneapi_version_setvars = os.path.join(
                oneapi_root, "compiler", version_from_path, "env", "vars.bat"
            )
            version_setvar_mods = EnvironmentModifications.from_sourcing_file(
                oneapi_version_setvars, env=local_env
            )
            version_setvar_mods.apply_modifications(env=local_env)
            root_setvars_mods = EnvironmentModifications.from_sourcing_file(
                oneapi_root_setvars, env=local_env
            )
            vars_mods.extend(version_setvar_mods)
            vars_mods.extend(root_setvars_mods)
        env.extend(vars_mods)

        if self.cc:
            env.set("CC", self.cc)
        if self.cxx:
            env.set("CXX", self.cxx)
        if self.fortran:
            env.set("FC", self.fortran)
            env.set("F77", self.fortran)

    def _standard_flag(self, *, language: str, standard: str) -> str:
        flags = {
            "cxx": {
                "11": "/std:c++11",
                "14": "/std:c++14",
                "17": "/std:c++17",
                "20": "/std:c++20",
            },
            "c": {"11": "/std:c11", "17": "/std:c17"},
        }
        return flags[language][standard]

    @property
    def short_msvc_version(self):
        """This is the shorthand VCToolset version of form
        MSVC<short-ver>
        """
        return "MSVC" + self.vc_toolset_ver

    @property
    def vc_toolset_ver(self):
        """
        The toolset version is the version of the combined set of cl and link
        This typically relates directly to VS version i.e. VS 2022 is v143
        VS 19 is v142, etc.
        This value is defined by the first three digits of the major + minor
        version of the VS toolset (143 for 14.3x.bbbbb). Traditionally the
        minor version has remained a static two digit number for a VS release
        series, however, as of VS22, this is no longer true, both
        14.4x.bbbbb and 14.3x.bbbbb are considered valid VS22 VC toolset
        versions due to a change in toolset minor version sentiment.

        This is *NOT* the full version, for that see
        Msvc.msvc_version or MSVC.platform_toolset_ver for the
        raw platform toolset version

        """
        ver = self.msvc_version[:2].joined.string[:3]
        return ver

    @property
    def msvc_version(self):
        """This is the VCToolset version *NOT* the actual version of the cl compiler"""
        return Version(re.search(Msvc.compiler_version_regex, self.cc).group(1))

    @property
    def vs_root(self):
        # The MSVC install root is located at a fix level above the compiler
        # and is referenceable idiomatically via the pattern below
        # this should be consistent accross versions
        return os.path.abspath(os.path.join(self.cc, "../../../../../../../.."))

    @property
    def platform_toolset_ver(self):
        """
        This is the platform toolset version of current MSVC compiler
        i.e. 142. The platform toolset is the targeted MSVC library/compiler
        versions by compilation (this is different from the VC Toolset)


        This is different from the VC toolset version as established
        by `short_msvc_version`, but typically are represented by the same
        three digit value
        """
        # Typically VS toolset version and platform toolset versions match
        # VS22 introduces the first divergence of VS toolset version
        # (144 for "recent" releases) and platform toolset version (143)
        # so it needs additional handling until MS releases v144
        # (assuming v144 is also for VS22)
        # or adds better support for detection
        # TODO: (johnwparent) Update this logic for the next platform toolset
        # or VC toolset version update
        toolset_ver = self.vc_toolset_ver
        vs22_toolset = Version(toolset_ver) > Version("142")
        return toolset_ver if not vs22_toolset else "143"


FC_PATH = {}


def get_valid_fortran_pth():
    """Assign maximum available fortran compiler version"""
    # TODO (johnwparent): validate compatibility w/ try compiler
    # functionality when added
    sort_fn = lambda fc_ver: Version(fc_ver)
    sort_fc_ver = sorted(list(FC_PATH.keys()), key=sort_fn)
    return FC_PATH[sort_fc_ver[-1]] if sort_fc_ver else None
