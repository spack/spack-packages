# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Otf2(AutotoolsPackage):
    """The Open Trace Format 2 is a highly scalable, memory efficient event
    trace data format plus support library.
    """

    homepage = "https://www.vi-hps.org/projects/score-p"
    url = "https://perftools.pages.jsc.fz-juelich.de/cicd/otf2/tags/otf2-3.1/otf2-3.1.tar.gz"
    version("3.1.1", sha256="5a4e013a51ac4ed794fe35c55b700cd720346fda7f33ec84c76b86a5fb880a6e")
    version("3.1", sha256="09dff2eda692486b88ad5ee189bbc9d7ebc1f17c863108c44ccf9631badbada4")
    version("3.0.3", sha256="18a3905f7917340387e3edc8e5766f31ab1af41f4ecc5665da6c769ca21c4ee8")
    version("3.0", sha256="6fff0728761556e805b140fd464402ced394a3c622ededdb618025e6cdaa6d8c")
    version("2.3", sha256="36957428d37c40d35b6b45208f050fb5cfe23c54e874189778a24b0e9219c7e3")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    extends("python")

    # `imp` module required
    depends_on("python@3", type=("build", "run"), when="@3.1:")
    depends_on("python@:3.11", type=("build", "run"), when="@:3.0")

    # Fix missing initialization of variable resulting in issues when used by
    # APEX/HPX: https://github.com/STEllAR-GROUP/hpx/issues/5239
    patch("collective_callbacks.patch")

    def flag_handler(self, name, flags):
        if name == "cflags":
            flags.append(self.compiler.cc_pic_flag)
        elif name == "cxxflags":
            flags.append(self.compiler.cxx_pic_flag)
        return (flags, None, None)

    def configure_args(self):
        return [
            "--enable-shared",
            f"CC={spack_cc}",
            f"CXX={spack_cxx}",
            f"F77={spack_f77}",
            f"FC={spack_fc}",
            "PYTHON_FOR_GENERATOR=:",
        ]
