# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyClustershell(PythonPackage):
    """Scalable cluster administration Python framework - Manage node sets
    node groups and execute commands on cluster nodes in parallel.
    """

    homepage = "https://clustershell.github.io/clustershell"
    url = "https://github.com/clustershell/clustershell/archive/v1.10.tar.gz"

    license("LGPL-2.1-or-later")

    version("1.10", sha256="fda39e4fba3e6ae8f8c5b83c440d867de959a5dc24947ebf50d4cb092c1d282d")
    version("1.9.3", sha256="94c97e8de4d701ceb953772a4cfd88b60323dd5b50bfd9ad765e92fe543303f3")
    version("1.8.4", sha256="763793f729bd1c275361717c540e01ad5fe536119eca92f14077c0995739b9d7")
    version("1.8.3", sha256="86b0d524e5e50c0a15faec01d8642f0ff12ba78d50b7e7b660261be5d53fed9c")
    version("1.8.2", sha256="abf5ed23b6adfc802ee65aa0208c697f617e5fb8fd0d8cb0100ee337e2721796")
    version("1.8.1", sha256="0c3da87108de8b735f40b5905b8dcd8084a234849aee2a8b8d2e20b99b57100c")
    version("1.8", sha256="ad5a13e2d107b4095229810c35365e22ea94dfd2baf4fdcfcc68ce58ee37cee3")

    conflicts("@:1.9", when="%python@3.12:", msg="@:1.9 use distutils, removed in python 3.12")

    depends_on("py-setuptools", type="build")
    depends_on("py-pyyaml", type=("build", "run"))
