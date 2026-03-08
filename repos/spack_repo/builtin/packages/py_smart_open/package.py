# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySmartOpen(PythonPackage):
    """smart_open is a Python 2 & Python 3 library for efficient streaming of
    very large files from/to S3, HDFS, WebHDFS, HTTP, or local storage. It
    supports transparent, on-the-fly (de-)compression for a variety of
    different formats."""

    homepage = "https://github.com/piskvorky/smart_open"
    pypi = "smart_open/smart_open-5.2.1.tar.gz"
    maintainers("marcusboden")

    license("MIT")

    version("7.5.0", sha256="f394b143851d8091011832ac8113ea4aba6b92e6c35f6e677ddaaccb169d7cb9")
    version("7.4.4", sha256="2c264f43c55c2fcdea37b1752dcd06bb152afd514490a0aee5d21db0424b0669")
    version("7.3.1", sha256="b33fee8dffd206f189d5e704106a8723afb4210d2ff47e0e1f7fbe436187a990")
    version(
        "7.3.0.post1", sha256="ce6a3d9bc1afbf6234ad13c010b77f8cd36d24636811e3c52c3b5160f5214d1e"
    )
    version("7.1.0", sha256="a4f09f84f0f6d3637c6543aca7b5487438877a21360e7368ccf1f704789752ba")
    version("7.0.5", sha256="d3672003b1dbc85e2013e4983b88eb9a5ccfd389b0d4e5015f39a9ee5620ec18")
    version("6.4.0", sha256="be3c92c246fbe80ebce8fbacb180494a481a77fcdcb7c1aadb2ea5b9c2bee8b9")
    version("6.3.0", sha256="d5238825fe9a9340645fac3d75b287c08fbb99fb2b422477de781c9f5f09e019")
    version("6.2.0", sha256="1b4df5c8365218f3852c507451920ccad606c80b0acb4e67508e50ba9b5d2632")
    version("6.1.0", sha256="c8fd9e9f90f0e285f1346481b0ae0fb57bd04b1138826c5e826ee98b2029d7f3")
    version("6.0.0", sha256="d60106b96f0bcaedf5f1cd46ff5524a1c3d02d5653425618bb0fa66e158d22b0")
    version("5.2.1", sha256="75abf758717a92a8f53aa96953f0c245c8cedf8e1e4184903db3659b419d4c17")
    version("1.10.0", sha256="bea5624c0c2e49987c227bdf3596573157eccd96fd1d53198856c8d53948fa2c")
    version("1.8.4", sha256="788e07f035defcbb62e3c1e313329a70b0976f4f65406ee767db73ad5d2d04f9")

    depends_on("py-setuptools", type="build")

    with when("@5:"):
        depends_on("python@3.6:3", type=("build", "run"))

        # google cloud support
        variant("gcs", default=False, description="Adds Google Cloud support")
        depends_on("py-google-cloud-storage", when="+gcs", type=("build", "run"))

        # aws support
        variant("s3", default=False, description="Adds AWS S3 support")
        depends_on("py-boto3", when="+s3", type=("build", "run"))

        # http support
        variant("http", default=True, description="Adds http and webhdfs support")
        depends_on("py-requests", when="+http", type=("build", "run"))

        # azure support
        variant("azure", default=False, description="Adds Microsoft Azure Support")
        with when("+azure"):
            depends_on("py-azure-storage-blob", type=("build", "run"))
            depends_on("py-azure-common", type=("build", "run"))
            depends_on("py-azure-core", type=("build", "run"))

    with when("@:2"):
        depends_on("py-requests", type=("build", "run"))
        depends_on("py-boto3", type=("build", "run"))
        depends_on("py-boto@2.3.2:", when="@1.8.4", type=("build", "run"))
        depends_on("py-google-cloud-storage", when="@1.10:", type=("build", "run"))
