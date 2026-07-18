# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class TruchasPbf(CMakePackage):
    """A spin-off of Truchas specialized for metal powder bed fusion and welding."""

    homepage = "https://gitlab.com/truchas-pbf/truchas-pbf"
    git = "ssh://git@gitlab.com/truchas-pbf/truchas-pbf.git"

    maintainers("zjibben")

    version("develop", branch="master")
    version("keyholing", branch="keyholing")

    ### Variants #################################
    # variant("unit", default=False, description="Enable Unit Tests")
    variant("doc", default=False, description="Build Sphinx documentation")
    variant("postprocessing", default=False, description="Include postprocessing tools")
    variant("config", default=True, description="Use proved Truchas-PBF config files for cmake")

    ### Dependencies #############################
    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("mpi")
    depends_on("cmake@3.21:", type="build")
    depends_on("amrex@25.02:26.04 +shared +fortran +hypre +plotfile_tools")
    depends_on("hypre@2.31:2.33 +shared")
    depends_on("petaca@23.11 +shared")
    depends_on("py-sphinx", type="build", when="+doc")
    depends_on("py-sphinx-rtd-theme", type="build", when="+doc")
    depends_on("py-yt ~astropy", when="+postprocessing")

    def cmake_args(self):
        opts = [self.define_from_variant("BUILD_HTML", "doc")]

        spec = self.spec
        if "+config" in spec:
            root = self.root_cmakelists_dir

            nag = "nag" in self.compiler.fc

            if spec.satisfies("platform=linux"):
                if nag or "%nag" in spec:
                    opts.append("-C {}/config/linux-nag.cmake".format(root))
                elif "%gcc" in spec:
                    opts.append("-C {}/config/linux-gcc.cmake".format(root))
                elif "%intel" in spec:
                    opts.append("-C {}/config/linux-intel.cmake".format(root))

            elif spec.satisfies("platform=darwin"):
                if "%apple-clang" in spec:
                    opts.append("-C {}/config/mac-gcc-clang.cmake".format(root))

        return opts
