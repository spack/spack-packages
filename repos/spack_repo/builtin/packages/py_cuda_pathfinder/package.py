# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCudaPathfinder(PythonPackage):
    """Pathfinder for CUDA components"""

    homepage = "https://nvidia.github.io/cuda-python/cuda-pathfinder"
    url = "https://files.pythonhosted.org/packages/py3/c/cuda-pathfinder/cuda_pathfinder-1.3.3-py3-none-any.whl"
    list_url = "https://pypi.org/project/cuda-pathfinder"

    license("Apache-2.0")

    version("1.5.4", sha256="9563d3175ce1828531acf4b94e1c1c7d67208c347ca002493e2654878b26f4b7")
    version("1.5.3", sha256="dff021123aedbb4117cc7ec81717bbfe198fb4e8b5f1ee57e0e084fec5c8577d")
    version("1.5.2", sha256="0c5f160a7756c5b072723cbbd6d861e38917ef956c68150b02f0b6e9271c71fa")
    version("1.5.1", sha256="b3718097fb57cf9e8a904dd072d806f2c9a27627e35c020b06ab9454bcec08c0")
    version("1.5.0", sha256="498f90a9e9de36044a7924742aecce11c50c49f735f1bc53e05aa46de9ea4110")
    version("1.4.4", sha256="1a9e7feccae0d969ad88545d0462f2ed2750df8e6732309798dc1e1ca603a28b")
    version("1.4.3", sha256="4345d8ead1f701c4fb8a99be6bc1843a7348b6ba0ef3b031f5a2d66fb128ae4c")
    version("1.4.2", sha256="eb354abc20278f8609dc5b666a24648655bef5613c6dfe78a238a6fd95566754")
    version("1.4.1", sha256="40793006082de88e0950753655e55558a446bed9a7d9d0bcb48b2506d50ed82a")
    version("1.4.0", sha256="437079ca59e7b61ae439ecc501d69ed87b3accc34d58153ef1e54815e2c2e118")
    version("1.3.5", sha256="6c88220f8637cb35d2a75c620d72efebf683b248b923713d8fbe235844c1a4b9")
    version("1.3.4", sha256="fb983f6e0d43af27ef486e14d5989b5f904ef45cedf40538bfdcbffa6bb01fb2")
    version("1.3.3", sha256="9984b664e404f7c134954a771be8775dfd6180ea1e1aef4a5a37d4be05d9bbb1")
    version("1.3.2", sha256="7bd2774bc6be93aea226d579f415a63803b2b2c062207ed06c1d6dfc9cfacc3c")
    version("1.3.1", sha256="0f04527f647e16ee26055447d3e4479bd608acce60f6506b14043f51d71736e7")
    version("1.3.0", sha256="2e904a408ab4ebfba5b3ee67ecd15383487ffe109fc6e1f2e2ea61577e4519be")
    version("1.2.3", sha256="e6cf54d550441e878002d9ec9d280863ef0d6bb2bd8f52ca01582a5f381eace4")
    version("1.2.2", sha256="4a97b8eb29bc4bbd52f419141dd0345da95f67e599deeed686bd925729d22228")
    version("1.2.1", sha256="d4fba3a8f6a01bbc72753d69bc7f6bcf8078a91a73adeea0f0c9adf917461d7b")
    version("1.2.0", sha256="bf83060b06e571236cd77e2f26adab218dcceb2a87effbc830fe32940277f081")
    version("1.1.0", sha256="3e66fe0af8ead20eca25e077d2e0cb2dcc027d4297d550a74f99a0211e610799")
    version("1.0.0", sha256="672cc49ce16cb10cb39a9fbcfbcac2cf4a3a22561adee9faeea48f20ce19401f")

    depends_on("py-setuptools", type="build")
