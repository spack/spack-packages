# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from typing import List, Optional, Tuple

from spack.package import (
    ClassProperty,
    InstallError,
    classproperty,
    depends_on,
    extends,
    mkdirp,
    run_before,
)

from .generic import GenericBuilder, Package


class RBuilder(GenericBuilder):
    """The R builder provides a single phase that can be overridden:

        1. :py:meth:`~.RBuilder.install`

    It has sensible defaults, and for many packages the only thing
    necessary will be to add dependencies.
    """

    #: Names associated with package methods in the old build-system format
    package_methods: Tuple[str, ...] = (
        "configure_args",
        "configure_vars",
    ) + GenericBuilder.package_methods

    def configure_args(self):
        """Arguments to pass to install via ``--configure-args``."""
        return []

    def configure_vars(self):
        """Arguments to pass to install via ``--configure-vars``."""
        return []

    def install(self, pkg, spec, prefix):
        """Installs an R package."""
        mkdirp(pkg.module.r_lib_dir)

        config_args = self.configure_args()
        config_vars = self.configure_vars()

        args = ["--vanilla", "CMD", "INSTALL"]

        if config_args:
            args.append(f"--configure-args={' '.join(config_args)}")

        if config_vars:
            args.append(f"--configure-vars={' '.join(config_vars)}")

        args.extend([f"--library={pkg.module.r_lib_dir}", self.stage.source_path])

        pkg.module.R(*args)

    @run_before("install")
    def check_compiler_matches_r(self) -> None:
        """R packages with compiled code are dyn.load()-ed into the same
        running R process as R itself, so they need to be ABI-compatible
        with it -- but ``extends("r")`` places no constraint at all on
        which compiler an RPackage is built with. A mismatch here usually
        doesn't fail at build time: it fails later, in a way that's hard to
        connect back to the real cause (an unsupported dialect flag coming
        from R's own Makeconf, e.g. ``-std=gnu23`` against a compiler that
        doesn't support it; or an undefined Fortran runtime symbol at
        ``library()`` time, because gfortran and flang runtimes aren't
        ABI-compatible). Catch the mismatch here instead, with a message
        that points at the actual fix."""
        pkg = self.pkg
        spec = pkg.spec
        r_spec = spec["r"]
        for lang in ("c", "cxx", "fortran"):
            if not spec.satisfies(f"%{lang}") or not r_spec.satisfies(f"%{lang}"):
                continue
            pkg_compiler = spec[lang]
            r_compiler = r_spec[lang]
            if pkg_compiler.dag_hash() == r_compiler.dag_hash():
                continue
            raise InstallError(
                f"{pkg.name} is being built with "
                f"{pkg_compiler.name}@{pkg_compiler.version} for {lang}, but "
                f"the R it extends was built with "
                f"{r_compiler.name}@{r_compiler.version}. R loads compiled "
                f"packages into its own process, so a compiler/runtime "
                f"mismatch here tends to surface later as a confusing "
                f"error (an unsupported dialect flag, or an undefined "
                f"runtime symbol) instead of a clear one now. Pin "
                f"{pkg.name} to the same compiler as R, e.g. in "
                f"packages.yaml:\n"
                f"  packages:\n"
                f"    {pkg.name}:\n"
                f'      require: "%{r_compiler.name}@{r_compiler.version}"'
            )


def _homepage(cls: "RPackage") -> Optional[str]:
    if cls.cran:
        return f"https://cloud.r-project.org/package={cls.cran}"
    elif cls.bioc:
        return f"https://bioconductor.org/packages/{cls.bioc}"
    return None


def _urls(cls: "RPackage") -> List[str]:
    if cls.cran:
        return [
            f"https://cran.r-project.org/src/contrib/{cls.cran}_{str(list(cls.versions)[0])}.tar.gz",
            f"https://cran.r-project.org/src/contrib/Archive/{cls.cran}/{cls.cran}_{str(list(cls.versions)[0])}.tar.gz",
        ]
    return []


def _list_url(cls: "RPackage") -> Optional[str]:
    if cls.cran:
        return f"https://cran.r-project.org/src/contrib/Archive/{cls.cran}/"
    return None


def _git(cls: "RPackage") -> Optional[str]:
    if cls.bioc:
        return f"https://git.bioconductor.org/packages/{cls.bioc}"
    return None


class RPackage(Package):
    """Specialized class for packages that are built using R.

    For more information on the R build system, see:
    https://stat.ethz.ch/R-manual/R-devel/library/utils/html/INSTALL.html
    """

    # package attributes that can be expanded to set the homepage, url,
    # list_url, and git values
    # For CRAN packages
    cran: Optional[str] = None

    # For Bioconductor packages
    bioc: Optional[str] = None

    GenericBuilder = RBuilder

    #: This attribute is used in UI queries that need to know the build
    #: system base class
    build_system_class = "RPackage"

    extends("r")

    # needed for packages that need compiling
    depends_on("gmake", type="build", when="%c")
    depends_on("gmake", type="build", when="%cxx")
    depends_on("gmake", type="build", when="%fortran")

    homepage: ClassProperty[Optional[str]] = classproperty(_homepage)
    urls: ClassProperty[List[str]] = classproperty(_urls)
    list_url: ClassProperty[Optional[str]] = classproperty(_list_url)
    git: ClassProperty[Optional[str]] = classproperty(_git)
