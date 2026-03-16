# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform
from os.path import split

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

_versions = {
    "25.5.1": {
        "Linux-x86_64": (
            "612af113b49db0368e2be41ac4d51b7088eebd5f31daeeb89f23fff8f920db58",
            "https://repo.anaconda.com/miniconda/Miniconda3-py313_25.5.1-1-Linux-x86_64.sh",
        )
    },
    "25.3.1": {
        "Linux-x86_64": (
            "53a86109463cfd70ba7acab396d416e623012914eee004729e1ecd6fe94e8c69",
            "https://repo.anaconda.com/miniconda/Miniconda3-py313_25.3.1-1-Linux-x86_64.sh",
        )
    },
    "25.1.1": {
        "Linux-x86_64": (
            "4766d85b5f7d235ce250e998ebb5a8a8210cbd4f2b0fea4d2177b3ed9ea87884",
            "https://repo.anaconda.com/miniconda/Miniconda3-py312_25.1.1-2-Linux-x86_64.sh",
        )
    },
    "24.11.1": {
        "Linux-x86_64": (
            "636b209b00b6673471f846581829d4b96b9c3378679925a59a584257c3fef5a3",
            "https://repo.anaconda.com/miniconda/Miniconda3-py312_24.11.1-0-Linux-x86_64.sh",
        )
    },
    "24.9.2": {
        "Linux-x86_64": (
            "8d936ba600300e08eca3d874dee88c61c6f39303597b2b66baee54af4f7b4122",
            "https://repo.anaconda.com/miniconda/Miniconda3-py312_24.9.2-0-Linux-x86_64.sh",
        )
    },
    "24.7.1": {
        "Linux-x86_64": (
            "33442cd3813df33dcbb4a932b938ee95398be98344dff4c30f7e757cd2110e4f",
            "https://repo.anaconda.com/miniconda/Miniconda3-py312_24.7.1-0-Linux-x86_64.sh",
        )
    },
    "24.5.0": {
        "Linux-x86_64": (
            "4b3b3b1b99215e85fd73fb2c2d7ebf318ac942a457072de62d885056556eb83e",
            "https://repo.anaconda.com/miniconda/Miniconda3-py312_24.5.0-0-Linux-x86_64.sh",
        )
    },
    "24.4.0": {
        "Linux-x86_64": (
            "b6597785e6b071f1ca69cf7be6d0161015b96340b9a9e132215d5713408c3a7c",
            "https://repo.anaconda.com/miniconda/Miniconda3-py312_24.4.0-0-Linux-x86_64.sh",
        )
    },
    "24.3.0": {
        "Linux-x86_64": (
            "96a44849ff17e960eeb8877ecd9055246381c4d4f2d031263b63fa7e2e930af1",
            "https://repo.anaconda.com/miniconda/Miniconda3-py312_24.3.0-0-Linux-x86_64.sh",
        )
    },
    "24.1.2": {
        "Linux-x86_64": (
            "b978856ec3c826eb495b60e3fffe621f670c101150ebcbdeede4f961f22dc438",
            "https://repo.anaconda.com/miniconda/Miniconda3-py312_24.1.2-0-Linux-x86_64.sh",
        )
    },
    "23.11.0": {
        "Linux-x86_64": (
            "c9ae82568e9665b1105117b4b1e499607d2a920f0aea6f94410e417a0eff1b9c",
            "https://repo.anaconda.com/miniconda/Miniconda3-py311_23.11.0-2-Linux-x86_64.sh",
        )
    },
    "23.9.0": {
        "Linux-x86_64": (
            "43651393236cb8bb4219dcd429b3803a60f318e5507d8d84ca00dafa0c69f1bb",
            "https://repo.anaconda.com/miniconda/Miniconda3-py311_23.9.0-0-Linux-x86_64.sh",
        )
    },
    "23.5.2": {
        "Linux-x86_64": (
            "634d76df5e489c44ade4085552b97bebc786d49245ed1a830022b0b406de5817",
            "https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.2-0-Linux-x86_64.sh",
        )
    },
    "23.5.1": {
        "Linux-x86_64": (
            "333779c9cae3fe14735949a8dcb9657b9e55ada69e9c60f191c5d582b2deac20",
            "https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.1-0-Linux-x86_64.sh",
        )
    },
    "23.5.0": {
        "Linux-x86_64": (
            "61a5c087893f6210176045931b89ee6e8760c17abd9c862b2cab4c1b7d00f7c8",
            "https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.0-3-Linux-x86_64.sh",
        )
    },
    "23.3.1": {
        "Linux-x86_64": (
            "aef279d6baea7f67940f16aad17ebe5f6aac97487c7c03466ff01f4819e5a651",
            "https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Linux-x86_64.sh",
        )
    },
    "23.1.0": {
        "Linux-x86_64": (
            "32d73e1bc33fda089d7cd9ef4c1be542616bd8e437d1f77afeeaf7afdb019787",
            "https://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-Linux-x86_64.sh",
        )
    },
    "22.11.1": {
        "Linux-x86_64": (
            "00938c3534750a0e4069499baf8f4e6dc1c2e471c86a59caa0dd03f4a9269db6",
            "https://repo.anaconda.com/miniconda/Miniconda3-py310_22.11.1-1-Linux-x86_64.sh",
        )
    },
    "4.10.3": {
        "Linux-x86_64": (
            "1ea2f885b4dbc3098662845560bc64271eb17085387a70c2ba3f29fff6f8d52f",
            "https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh",
        )
    },
    "4.9.2": {
        "Linux-ppc64le": (
            "2b111dab4b72a34c969188aa7a91eca927a034b14a87f725fa8d295955364e71",
            "https://repo.anaconda.com/miniconda/Miniconda3-py38_4.9.2-Linux-ppc64le.sh",
        ),
        "Linux-x86_64": (
            "1314b90489f154602fd794accfc90446111514a5a72fe1f71ab83e07de9504a7",
            "https://repo.anaconda.com/miniconda/Miniconda3-py38_4.9.2-Linux-x86_64.sh",
        ),
    },
    "4.8.2": {
        "Linux-x86_64": (
            "5bbb193fd201ebe25f4aeb3c58ba83feced6a25982ef4afa86d5506c3656c142",
            "https://repo.anaconda.com/miniconda/Miniconda3-py38_4.8.2-Linux-x86_64.sh",
        )
    },
    "4.7.12.1": {
        "Linux-x86_64": (
            "bfe34e1fa28d6d75a7ad05fd02fa5472275673d5f5621b77380898dee1be15d2",
            "https://repo.continuum.io/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh",
        )
    },
    "4.6.14": {
        "Linux-x86_64": (
            "0d6b23895a91294a4924bd685a3a1f48e35a17970a073cd2f684ffe2c31fc4be",
            "https://repo.continuum.io/miniconda/Miniconda3-4.6.14-Linux-x86_64.sh",
        )
    },
    "4.5.11": {
        "Linux-x86_64": (
            "ea4594241e13a2671c5b158b3b813f0794fe58d514795fbf72a1aad24db918cf",
            "https://repo.continuum.io/miniconda/Miniconda3-4.5.11-Linux-x86_64.sh",
        )
    },
    "4.5.4": {
        "Linux-x86_64": (
            "80ecc86f8c2f131c5170e43df489514f80e3971dd105c075935470bbf2476dea",
            "https://repo.continuum.io/miniconda/Miniconda3-4.5.4-Linux-x86_64.sh",
        )
    },
    "4.3.30": {
        "Linux-x86_64": (
            "66c822dfe76636b4cc2ae5604816e0e723aa01620f50087f06410ecf5bfdf38c",
            "https://repo.continuum.io/miniconda/Miniconda3-4.3.30-Linux-x86_64.sh",
        )
    },
    "4.3.14": {
        "Linux-x86_64": (
            "902f31a46b4a05477a9862485be5f84af761a444f8813345ff8dad8f6d3bccb2",
            "https://repo.continuum.io/miniconda/Miniconda3-4.3.14-Linux-x86_64.sh",
        )
    },
    "4.3.11": {
        "Linux-x86_64": (
            "b9fe70ce7b6fa8df05abfb56995959b897d0365299f5046063bc236843474fb8",
            "https://repo.continuum.io/miniconda/Miniconda3-4.3.11-Linux-x86_64.sh",
        )
    },
}


class Miniconda3(Package):
    """The minimalist bootstrap toolset for conda and Python3."""

    homepage = "https://docs.anaconda.com/miniconda/"

    for ver, packages in _versions.items():
        key = "{0}-{1}".format(platform.system(), platform.machine())
        pkg = packages.get(key)
        if pkg:
            version(ver, sha256=pkg[0], url=pkg[1], expand=False)

    def install(self, spec, prefix):
        # peel the name of the script out of the pathname of the
        # downloaded file
        dir, script = split(self.stage.archive_file)
        bash = which("bash", required=True)
        bash(script, "-b", "-f", "-p", self.prefix)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        filename = self.prefix.etc.join("profile.d").join("conda.sh")
        env.extend(EnvironmentModifications.from_sourcing_file(filename))
