# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyEtils(PythonPackage):
    """etils (eclectic utils) is an open-source collection of utils
    for python."""

    homepage = "https://github.com/google/etils"
    pypi = "etils/etils-0.9.0.tar.gz"

    license("Apache-2.0")

    version("1.15.0", sha256="7a7e242b299813f454d3c2910b8428fd5758ef3c6df58af4808fd0a511f0a032")
    version("1.7.0", sha256="97b68fd25e185683215286ef3a54e38199b6245f5fe8be6bedc1189be4256350")
    version("0.9.0", sha256="489103e9e499a566765c60458ee15d185cf0065f2060a4d16a68f8f46962ed0d")

    variant("epath", default=False, description="with epath module")
    variant("epy", default=False, description="with epy module")
    variant("enp", default=False, description="with enp module", when="@1.15:")
    variant("etqdm", default=False, description="with etqdm module", when="@1.15:")
    variant("etree", default=False, description="with etree module", when="@1.15:")

    depends_on("python@3.11:", type=("build", "run"), when="@1.15:")
    depends_on("python@3.10:", type=("build", "run"), when="@1.7:")
    depends_on("py-flit-core@3.8:3", type="build", when="@1.7:")
    depends_on("py-flit-core@3.5:3", type="build")

    conflicts("~epy", when="+epath")
    conflicts("~epy", when="+enp")
    conflicts("~epy", when="+etqdm")
    conflicts("~enp", when="+etree")
    conflicts("~etqdm", when="+etree")

    with when("+epath"):
        depends_on("py-fsspec", type=("build", "run"), when="@1.7:")
        depends_on("py-importlib-resources", type=("build", "run"), when="@:1.7")
        depends_on("py-typing-extensions", type=("build", "run"))
        depends_on("py-zipp", type=("build", "run"))

    with when("+epy"):
        depends_on("py-typing-extensions", type=("build", "run"))

    with when("+enp"):
        depends_on("py-numpy", type=("build", "run"))
        depends_on("py-einops", type=("build", "run"))

    with when("+etqdm"):
        depends_on("py-absl-py", type=("build", "run"))
        depends_on("py-tqdm", type=("build", "run"))
