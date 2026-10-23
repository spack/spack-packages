# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage, PythonPipBuilder

from spack.package import *


class PyPyqir(PythonPackage):
    """
    PyQIR is a set of APIs for generating, parsing, and evaluating Quantum Intermediate
    Representation (QIR).
    """

    homepage = "https://qir-alliance.github.io/pyqir"

    url = "https://github.com/qir-alliance/pyqir/archive/refs/tags/v0.12.5.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("0.12.5", sha256="170c4b981d5f6a48d8678c5dd519d915d57ab53f864830319cfeb5a78b732d77")
    version("0.12.4", sha256="4db944bc741863054b8e2fd2a0d4b7635d235d5ad8a4edcb5cc3f1476318e2ed")
    version("0.12.3", sha256="ac762e6981348a8f2219971bcb1de9fd0c4475b8f048c2a6a3acee064be6dbbf")
    version("0.12.2", sha256="2439d7f7362a4098b7969751f8206facf7d2a68b7cb8d18595c277414b65a1b8")
    version("0.12.1", sha256="1d9c43f5aa37895555967c9ecc86be8d2ea889b023cde7bc0ae9dc26809437e1")
    version("0.12.0", sha256="5fe0b1b36409caf8240879c1e4b0ed1e95f2e0c842559d96a0570d575acd97f6")
    version("0.11.1", sha256="cd198aa7d8d5ba2f6d71945ed8468569e9877f6d9529ad4952928f28d2c8f989")
    version("0.11.0", sha256="4930ab54a4984f5aeb9d405d6f6e449dce2d9d2384a57112de6cb45531a4eec4")
    version("0.10.9", sha256="0938b8a18b97ce06272ca568dae38faf2259bf8cc862a301ee748606ca4f6dca")
    version("0.10.8", sha256="f14e4c6d202cbb9f83add8ecb2e62d56731b2fdde021b3916d1d3f3d8f07202d")

    depends_on("c")
    depends_on("cxx")
    depends_on("llvm@20.1", when="@0.12")
    depends_on("llvm@14.0", when="@0.10")
    depends_on("python@3.9:", type=("build", "run"), when="@0.11:0.12")
    depends_on("python@3.8:", type=("build", "run"), when="@0.10")

    with default_args(type="build"):
        depends_on("py-maturin@1.10.2:1.10", when="@0.12.4:")
        depends_on("py-maturin@1.8.3:1.8", when="@0.11:0.12.3")
        depends_on("py-maturin@1.7.8:1.7", when="@0.10")

    def patch(self):
        llvm_string = "llvm" + self.spec["llvm"].version.up_to_2.dashed.string
        filter_file(
            r"(\[tool\.maturin\])[ \t]*\r?\n",
            lambda m: m.group(1) + '\nfeatures = ["' + llvm_string + '"]\n',
            "pyqir/pyproject.toml",
        )

    def install(self, spec, prefix):
        with working_dir("pyqir"):
            pip(*PythonPipBuilder.std_args(self), f"--prefix={self.prefix}", ".")
