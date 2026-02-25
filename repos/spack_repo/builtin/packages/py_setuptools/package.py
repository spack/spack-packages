# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack_repo.builtin.build_systems.python import PythonExtension, PythonPipBuilder

from spack.package import *


class PySetuptools(Package, PythonExtension):
    """A Python utility that aids in the process of downloading, building,
    upgrading, installing, and uninstalling Python packages."""

    homepage = "https://github.com/pypa/setuptools"
    url = "https://files.pythonhosted.org/packages/py3/s/setuptools/setuptools-62.3.2-py3-none-any.whl"
    list_url = "https://pypi.org/simple/setuptools/"

    license("MIT")
    maintainers("RobertMaaskant")

    tags = ["build-tools"]

    # Requires railroad
    skip_modules = ["setuptools._vendor", "pkg_resources._vendor"]

    version("82.0.0", sha256="70b18734b607bd1da571d097d236cfcfacaf01de45717d59e6e04b96877532e0")
    version("80.9.0", sha256="062d34222ad13e0cc312a4c02d73f059e86a4acbfbdea8f8f76b28c99f306922")
    version("79.0.1", sha256="e147c0549f27767ba362f9da434eab9c5dc0045d5304feb602a0af001089fc51")
    version("78.1.1", sha256="c3a9c4211ff4c309edb8b8c4f1cbfa7ae324c4ba9f91ff254e3d305b9fd54561")
    version("78.1.0", sha256="3e386e96793c8702ae83d17b853fb93d3e09ef82ec62722e61da5cd22376dcd8")
    version("78.0.2", sha256="4a612c80e1f1d71b80e4906ce730152e8dec23df439f82731d9d0b608d7b700d")
    version("78.0.1", sha256="1cc9b32ee94f93224d6c80193cbb768004667aa2f2732a473d6949b0236c1d4e")
    version("77.0.3", sha256="67122e78221da5cf550ddd04cf8742c8fe12094483749a792d56cd669d6cf58c")
    version("77.0.1", sha256="81a234dff81a82bb52e522c8aef145d0dd4de1fd6de4d3b196d0f77dc2fded26")
    version("76.1.0", sha256="34750dcb17d046929f545dec9b8349fe42bf4ba13ddffee78428aec422dbfb73")
    version("76.0.0", sha256="199466a166ff664970d0ee145839f5582cb9bca7a0a3a2e795b6a9cb2308e9c6")
    version("75.9.1", sha256="0a6f876d62f4d978ca1a11ab4daf728d1357731f978543ff18ecdbf9fd071f73")
    version("75.8.2", sha256="558e47c15f1811c1fa7adbd0096669bf76c1d3f433f58324df69f3f5ecac4e8f")
    version("75.8.1", sha256="3bc32c0b84c643299ca94e77f834730f126efd621de0cc1de64119e0e17dab1f")
    version("75.8.0", sha256="e3982f444617239225d675215d51f6ba05f845d4eec313da4418fdbb56fb27e3")
    # Last version supporting Python 3.8
    version("75.3.2", sha256="90ab613b6583fc02d5369cbca13ea26ea0e182d1df2d943ee9cbe81d4c61add9")
    version("75.3.1", sha256="ccd77cda9d3bc3d3e99036d221b91d15f86e53195139d643b5b5299d42463cd3")
    version("75.3.0", sha256="f2504966861356aa38616760c0f66568e535562374995367b4e69c7143cf6bcd")
    version("69.2.0", sha256="c21c49fb1042386df081cb5d86759792ab89efca84cf114889191cd09aacc80c")
    version("69.1.1", sha256="02fa291a0471b3a18b2b2481ed902af520c69e8ae0919c13da936542754b4c56")
    version("69.0.3", sha256="385eb4edd9c9d5c17540511303e39a147ce2fc04bc55289c322b9e5904fe2c05")
    version("68.2.2", sha256="b454a35605876da60632df1a60f736524eb73cc47bbc9f3f1ef1b644de74fd2a")
    # Last version supporting Python 3.7
    version("68.0.0", sha256="11e52c67415a381d10d6b462ced9cfb97066179f0e871399e006c4ab101fc85f")
    version("67.6.0", sha256="b78aaa36f6b90a074c1fa651168723acbf45d14cb1196b6f02c0fd07f17623b2")
    version("65.5.0", sha256="f62ea9da9ed6289bfe868cd6845968a2c854d1427f8548d52cae02a42b4f0356")
    version("65.0.0", sha256="fe9a97f68b064a6ddd4bacfb0b4b93a4c65a556d97ce906255540439d0c35cef")
    version("64.0.0", sha256="63f463b90ff5e0a1422010100268fd688e15c44ae0798659013c8412963e15e4")
    version("63.4.3", sha256="7f61f7e82647f77d4118eeaf43d64cbcd4d87e38af9611694d4866eb070cd10d")
    version("63.0.0", sha256="045aec56a3eee5c82373a70e02db8b6da9a10f7faf61ff89a14ab66c738ed370")
    version("62.6.0", sha256="c1848f654aea2e3526d17fc3ce6aeaa5e7e24e66e645b5be2171f3f6b4e5a178")
    version("62.4.0", sha256="5a844ad6e190dccc67d6d7411d119c5152ce01f7c76be4d8a1eaa314501bba77")
    version("62.3.2", sha256="68e45d17c9281ba25dc0104eadd2647172b3472d9e01f911efa57965e8d51a36")
    # Last version supporting Python 3.6
    version("59.4.0", sha256="feb5ff19b354cde9efd2344ef6d5e79880ce4be643037641b49508bbb850d060")
    version("58.2.0", sha256="2551203ae6955b9876741a26ab3e767bb3242dafe86a32a749ea0d78b6792f11")
    version("57.4.0", sha256="a49230977aa6cfb9d933614d2f7b79036e9945c4cdd7583163f4e920b83418d6")

    extends("python")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:", when="@75.4:")
        depends_on("python@3.8:", when="@68.1:")
        depends_on("python@3.7:", when="@59.7:")
        depends_on("python@3.6:", when="@51:")

        # https://github.com/pypa/setuptools/issues/3661
        depends_on("python@:3.11", when="@:67")

    depends_on("py-pip", type="build")

    conflicts(
        "^python@:3.9 ^py-pip@25:",
        when="@:75.1.0",
        msg="py-pip@25: vendors pyproject-hooks@1.2. "
        "The combination pyproject-hooks@1.2, python@:3.9, and py-setuptools@:75.1.0 is broken. "
        "See https://github.com/pypa/pyproject-hooks/issues/206 for details.",
    )

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/py3/s/setuptools/setuptools-{}-py3-none-any.whl"
        return url.format(version)

    def install(self, spec, prefix):
        # When setuptools changes its entry point we might get weird
        # incompatibilities if building from sources in a non-isolated environment.
        #
        # https://github.com/pypa/setuptools/issues/980#issuecomment-1154471423
        #
        # We work around this issue by installing setuptools from wheels
        whl = self.stage.archive_file
        python("-m", "pip", *PythonPipBuilder.std_args(self), f"--prefix={prefix}", whl)
