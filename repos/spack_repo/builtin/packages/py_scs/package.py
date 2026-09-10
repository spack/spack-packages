# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyScs(PythonPackage, CudaPackage):
    """SCS: splitting conic solver"""

    homepage = "https://github.com/cvxgrp/scs"
    pypi = "scs/scs-2.1.1-2.tar.gz"

    maintainers("meyersbs")

    license("MIT")

    version("3.2.11", sha256="2a5455cf2093d07f84f2f848c199faed52e79cdb3a11fe250b5622b6bbac4913")
    version("3.2.2", sha256="7206a2ad27ca031d693d65cbcbcfc661498f3983838079a66579bcc784b25293")
    version("2.1.1-2", sha256="f816cfe3d4b4cff3ac2b8b96588c5960ddd2a3dc946bda6b09db04e7bc6577f2")

    variant(
        "float32",
        default=False,
        description="Use 32 bit (single precision) floats, default is 64 bit",
    )
    variant("extra_verbose", default=False, description="Extra verbose SCS (for debugging)")
    variant("int32", default=False, description="Use 32 bit ints")
    variant("blas64", default=False, description="Use 64 bit ints for the blas/lapack libs")

    depends_on("c", type="build")  # generated

    # from pyproject.toml since version 3.2.4
    depends_on("py-meson-python", type="build", when="@3.2.4:")
    # from pyproject.toml of version 3.2.3
    depends_on("py-setuptools@:65.5", type="build", when="@:3.2.3")
    # from pyproject.toml since version 3.2.5
    depends_on("py-numpy@2:", type=("build", "run"), when="@3.2.5:")
    depends_on("py-numpy@1.7:", type=("build", "run"))
    depends_on("py-scipy@0.13.2:", type=("build", "run"))

    # in newer pip versions --install-option does not exist
    # technically only the variants need this restriction
    depends_on("py-pip@:23.0", type="build")

    def install_options(self, spec, prefix):
        args = []
        if (
            "+cuda" in spec
            or "+float32" in spec
            or "+int32" in spec
            or "+extra_verbose" in spec
            or "+blas64" in spec
        ):
            args = ["--scs"]
        if "+cuda" in spec:
            args.append("--gpu")
        if "+float32" in spec:
            args.append("--float")
        if "+extra_verbose" in spec:
            args.append("--extraverbose")
        if "+int32" in spec:
            args.append("--int")
        if "+blas64" in spec:
            args.append("--blas64")
        return args
