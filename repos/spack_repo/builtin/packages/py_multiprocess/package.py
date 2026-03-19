# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMultiprocess(PythonPackage):
    """Better multiprocessing and multithreading in Python"""

    homepage = "https://github.com/uqfoundation/multiprocess"
    pypi = "multiprocess/multiprocess-0.70.17.tar.gz"

    license("BSD-3-Clause")

    version("0.70.19", sha256="952021e0e6c55a4a9fe4cd787895b86e239a40e76802a789d6305398d3975897")
    version("0.70.18", sha256="f9597128e6b3e67b23956da07cf3d2e5cba79e2f4e0fba8d7903636663ec6d0d")
    version("0.70.17", sha256="4ae2f11a3416809ebc9a48abfc8b14ecce0652a0944731a1493a3c1ba44ff57a")
    version("0.70.16", sha256="161af703d4652a0e1410be6abccecde4a7ddffd19341be0a7011b94aeb171ac1")
    version("0.70.15", sha256="f20eed3036c0ef477b07a4177cf7c1ba520d9a2677870a4f47fe026f0cd6787e")
    version("0.70.14", sha256="3eddafc12f2260d27ae03fe6069b12570ab4764ab59a75e81624fac453fbf46a")
    version("0.70.13", sha256="2e096dd618a84d15aa369a9cf6695815e5539f853dc8fa4f4b9153b11b1d0b32")
    version("0.70.12.2", sha256="206bb9b97b73f87fec1ed15a19f8762950256aa84225450abc7150d02855a083")
    version("0.70.12.1", sha256="d73afab98823e06423f68271cce77743fd82ce587090bf5a6ce408396d9a68f3")
    version("0.70.12", sha256="853d02581a03b3bf7872f5e997d2e2b62e177c22a9d05158dc96a675854f2b60")
    version("0.70.11.1", sha256="9d5e417f3ebce4d027a3c900995840f167f316d9f73c0a7a1fbb4ac0116298d0")
    version("0.70.11", sha256="e75f02a8dc3707207d3356e0d272933a718654b54d792fc1f7b2925b5c0e120d")
    version("0.70.10", sha256="81f388527a0c8766e94fe084fd8a408da5045a9fe7b28e199f684a796f3c6bf8")
    version("0.70.9", sha256="9fd5bd990132da77e73dec6e9613408602a4612e1d73caf2e2b813d2b61508e5")
    version("0.70.8", sha256="fc6b2d8f33e7d437a82c6d1c2f1673ae20a271152a1ac6a18571d10308de027d")
    version("0.70.7", sha256="46479a327388df8e77ad268892f2e73eac06d6271189b868ce9d4f95474e58e3")
    version("0.70.6.1", sha256="985d2faa28def907e303b4222b01281d2dcd3baa0fe53a4a0178ac63be62e5c6")
    version("0.70.6", sha256="255c3d744ea682998c5f3a9f7cecefbc8c73853040d39401a218067f19e88c1b")
    version("0.70.5", sha256="c4c196f3c4561dc1d78139c3e73709906a222d2fc166ef3eef895d8623df7267")
    version("0.70.4", sha256="a692c6dc8392c25b29391abb58a9fbdc1ac38bca73c6f27d787774201e68e12c")
    version("0.70.3", sha256="071e15e7758a69710c5fad85e691d79e2efc780c41b00e69b7d10388edd3993b")
    version("0.70.1", sha256="82bce12d7c7171aaa2f8624c9be2bd9e27df2b621cfa85f3d394394fb3b38999")

    depends_on("py-setuptools@0.6:", type="build")

    # Python
    depends_on("python@3.9:", when="@0.70.19:")
    depends_on("python@3.8:", when="@0.70.16:0.70.18")
    depends_on("python@3.7:", when="@0.70.14:0.70.15")
    depends_on("python@2.7,3.7:", when="@0.70.13")
    depends_on("python@2.7,3.6:", when="@0.70.12.1:0.70.12.2")
    depends_on("python@2.7,3.5:", when="@0.70.10:0.70.11.1")
    depends_on("python@2.5:,3.1:", when="@0.70.8:0.70.9")

    # dill
    depends_on("py-dill@0.4.1:", type=("build", "run"), when="@0.70.19:")
    depends_on("py-dill@0.4.0:", type=("build", "run"), when="@0.70.18")
    depends_on("py-dill@0.3.9:", type=("build", "run"), when="@0.70.17")
    depends_on("py-dill@0.3.8:", type=("build", "run"), when="@0.70.16")
    depends_on("py-dill@0.3.7:", type=("build", "run"), when="@0.70.15")
    depends_on("py-dill@0.3.6:", type=("build", "run"), when="@0.70.14")
    depends_on("py-dill@0.3.5.1:", type=("build", "run"), when="@0.70.13")
    depends_on("py-dill@0.3.4:", type=("build", "run"), when="@0.70.12.1:0.70.12.2")
    depends_on("py-dill@0.3.3:", type=("build", "run"), when="@0.70.11:0.70.11.1")
    depends_on("py-dill@0.3.2:", type=("build", "run"), when="@0.70.10")
    depends_on("py-dill@0.3.1:", type=("build", "run"), when="@0.70.9")
    depends_on("py-dill@0.3.0:", type=("build", "run"), when="@0.70.8")
    depends_on("py-dill@0.2.9:", type=("build", "run"), when="@0.70.7")
    depends_on("py-dill@0.2.8.1:", type=("build", "run"), when="@0.70.6:0.70.6.1")
    depends_on("py-dill@0.2.6:", type=("build", "run"), when="@0.70.5")
    depends_on("py-dill@0.2.5:", type=("build", "run"), when="@0.70.4")
    depends_on("py-dill@0.2.3:", type=("build", "run"), when="@0.70.3")
    depends_on("py-dill@0.2.2:", type=("build", "run"), when="@0.70.1")

    def url_for_version(self, version):
        url = "https://pypi.io/packages/source/p/multiprocess/multiprocess-{0}.{1}"
        zip_versions = [
            Version("0.70.12.2"),
            Version("0.70.12.1"),
            Version("0.70.12"),
            Version("0.70.11.1"),
            Version("0.70.11"),
            Version("0.70.10"),
            Version("0.70.5"),
            Version("0.70.4"),
            Version("0.70.3"),
            Version("0.70.1"),
        ]
        ext = "zip" if version in zip_versions else "tar.gz"
        return url.format(version, ext)
