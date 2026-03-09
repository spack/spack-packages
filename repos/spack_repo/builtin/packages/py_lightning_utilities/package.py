# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLightningUtilities(PythonPackage):
    """Common Python utilities and GitHub Actions in Lightning Ecosystem"""

    homepage = "https://github.com/Lightning-AI/utilities"
    pypi = "lightning-utilities/lightning_utilities-0.4.1.tar.gz"

    maintainers("adamjstewart")

    license("Apache-2.0")

    version("0.15.3", sha256="792ae0204c79f6859721ac7f386c237a33b0ed06ba775009cb894e010a842033")
    version("0.11.2", sha256="adf4cf9c5d912fe505db4729e51d1369c6927f3a8ac55a9dff895ce5c0da08d9")
    version("0.8.0", sha256="8e5d95c7c57f026cdfed7c154303e88c93a7a5e868c9944cb02cf71f1db29720")
    version(
        "0.6.0.post0", sha256="6f02cfe59e6576487e709a0e66e07671563bde9e21b40e1c567918e4d753278c"
    )
    version("0.5.0", sha256="01ef5b7fd50a8b54b849d8621720a65c36c91b374933a8384fb2be3d86cfa8f1")
    version("0.4.2", sha256="dc6696ab180117f7e97b5488dac1d77765ab891022f7521a97a39e10d362bdb8")
    version("0.4.1", sha256="969697b0debffd808d4cf3b74af4952f82bf6726f4ce561119037871547690a5")
    version("0.4.0", sha256="961c29774c2c8303e0a2f6e6512a2e21e1d8acaf6df182865667af4a51bc176c")
    version("0.3.0", sha256="d769ab9b76ebdee3243d1051d509aafee57d7947734ddc22977deef8a6427f2f")

    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        # requirements/core.txt
        depends_on("py-packaging@22:", when="@0.15.3:")
        depends_on("py-packaging@17.1:", when="@0.6.0.post0:")
        depends_on("py-packaging@20:", when="@0.5:0.6.0.a")
        depends_on("py-typing-extensions", when="@0.5:")

        # Historical dependencies
        depends_on("py-fire", when="@0.3.0")
        # https://github.com/Lightning-AI/utilities/pull/473
        depends_on("py-setuptools@:81", when="@:0.15.2")

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/l/lightning-utilities/{}-{}.tar.gz"
        if version >= Version("0.11.3"):
            name = "lightning_utilities"
        else:
            name = "lightning-utilities"
        return url.format(name, version)
