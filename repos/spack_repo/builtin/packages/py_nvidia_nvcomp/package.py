# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNvidiaNvcomp(PythonPackage):
    """The nvCOMP library provides fast lossless data compression and
    decompression using a GPU. Not open-source anymore."""

    homepage = "https://docs.nvidia.com/cuda/nvcomp/index.html"
    git = "https://github.com/NVIDIA/nvcomp"

    skip_version_audit = ["platform=darwin", "platform=windows"]

    maintainers("thomas-bouvier")

    system = platform.system().lower()
    arch = platform.machine()
    if "linux" in system and arch == "x86_64":
        version(
            "5.1.0.21-cuda130",
            sha256="b8b89f14435529b750f2fab61c35655e234611807e0857d606c77c41807e5d58",
            url="https://files.pythonhosted.org/packages/08/e9/a60b0df949c65d758420109c5f2c6223caa2ee9c99f0f489641588ce6dbe/nvidia_nvcomp_cu13-5.1.0.21-py3-none-manylinux_2_28_x86_64.whl",
        )
        version(
            "5.1.0.21-cuda120",
            sha256="87b7dbd4c7e00a9f0272467b4023dfd1e57fb778c7593813c636bdfaf1007d69",
            url="https://files.pythonhosted.org/packages/ca/9e/1dffa63e4fa6a789e96dc10dde519bb76e4c009feceb1e05b893fa2197b1/nvidia_nvcomp_cu12-5.1.0.21-py3-none-manylinux_2_28_x86_64.whl",
        )
        version(
            "5.0.0.6-cuda130",
            sha256="91a4e4b1dc15b0f38e54a3353c917086c99c9f415e1ad79a57d5f28d62b68a4d",
            url="https://files.pythonhosted.org/packages/56/c9/f8a1b957f949ab4c4dc29e7f56316a2224b92c78cad9a66aeab2b36f8857/nvidia_nvcomp_cu13-5.0.0.6-py3-none-manylinux_2_28_x86_64.whl",
        )
        version(
            "5.0.0.6-cuda120",
            sha256="b5b8a9a3ed33c4a87bb9103fbe59c83b28e4559234447ad40cab11896557c031",
            url="https://files.pythonhosted.org/packages/e3/b5/1c3b2493dbcd0f436715b3faba4bef4747743dbb1828ce7823e61423863c/nvidia_nvcomp_cu12-5.0.0.6-py3-none-manylinux_2_28_x86_64.whl",
        )
        version(
            "5.0.0.6-cuda110",
            sha256="816ed4c53718cd9de2e25e4cab8b20b219ceb2e0712c4452c7225c6eec83bd6b",
            url="https://files.pythonhosted.org/packages/3c/3a/572e3881d86d227d2f274306c4996543a55f1876b03f0934e3f65f3ddd5e/nvidia_nvcomp_cu11-5.0.0.6-py3-none-manylinux_2_28_x86_64.whl",
        )
    elif "linux" in system and arch == "aarch64":
        version(
            "5.1.0.21-cuda130",
            sha256="e43bdd25ee4265ee5b0e30b2b20b2a88e5249864e1f7a69607a05fc8249152fa",
            url="https://files.pythonhosted.org/packages/44/93/cadd09eabc687450e0dccecd793d55b3bfd055529a1fb4b05e7bf5767e90/nvidia_nvcomp_cu13-5.1.0.21-py3-none-manylinux_2_28_aarch64.whl",
        )
        version(
            "5.1.0.21-cuda120",
            sha256="3ea5a6eba548daebf9dd1d86ee58acfff0fd89cb7c6ee76479cdb07d89cfa871",
            url="https://files.pythonhosted.org/packages/19/59/18b6f4aac53942e30bcd81d7ec3e052dce364dbb8e4c6ad7397c854e02c1/nvidia_nvcomp_cu12-5.1.0.21-py3-none-manylinux_2_28_aarch64.whl",
        )
        version(
            "5.0.0.6-cuda130",
            sha256="13910a5e5dbf7d4ce21c807c801a1f10c261b9a2d538896e93b736c21d7d6b1d",
            url="https://files.pythonhosted.org/packages/a3/86/e5eccb10e8be41501dfb7191a6b2cff32558d0bba3370ae67f37561caf43/nvidia_nvcomp_cu13-5.0.0.6-py3-none-manylinux_2_28_aarch64.whl",
        )
        version(
            "5.0.0.6-cuda120",
            sha256="7af1093e866ee7a468753e3df94327fd63ba253dd119a2c04cd18df1761f4754",
            url="https://files.pythonhosted.org/packages/8b/96/530b265e36e23e1e8dd88c864d5479bfd116d9c6cd78c6e3bf91cdf68c62/nvidia_nvcomp_cu12-5.0.0.6-py3-none-manylinux_2_28_aarch64.whl",
        )
        version(
            "5.0.0.6-cuda110",
            sha256="99eb163d389cf06f62978ecfcd1cea427fb3e928b23bd56cf76d8287944ef908",
            url="https://files.pythonhosted.org/packages/b7/08/07922c747e404df408d0e7637394d110607be8c11291f15be9168b833fee/nvidia_nvcomp_cu11-5.0.0.6-py3-none-manylinux_2_28_aarch64.whl",
        )

    cuda130_versions = ("@5.1.0.21-cuda130", "@5.0.0.6-cuda130")
    cuda120_versions = ("@5.1.0.21-cuda120", "@5.0.0.6-cuda120")
    cuda110_versions = ("@5.0.0.6-cuda110",)

    for v in cuda130_versions:
        depends_on("cuda@13", when=v, type=("build", "run"))
    for v in cuda120_versions:
        depends_on("cuda@12", when=v, type=("build", "run"))
    for v in cuda110_versions:
        depends_on("cuda@11", when=v, type=("build", "run"))

    depends_on("python@3.8:", type=("build", "run"))
