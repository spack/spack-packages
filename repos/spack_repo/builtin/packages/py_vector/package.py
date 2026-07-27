# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyVector(PythonPackage):
    """Vector classes and utilities"""

    homepage = "https://github.com/scikit-hep/vector"
    pypi = "vector/vector-0.8.4.tar.gz"
    git = "https://github.com/scikit-hep/vector.git"

    maintainers("wdconinc")

    tags = ["hep"]

    license("BSD-3-Clause", checked_by="wdconinc")

    version("1.8.0", sha256="58f95e9e24463851ca34176a20df2fd2e80b41d78615e5b1f7ae4bf313424ca6")
    version("1.7.0", sha256="8b05ea2953322c74c49d2af180f7eac73ad0aa3d4c391cab896175ec4fa3d642")
    version("1.6.3", sha256="a85149a62fcaa8a4d95214ca217f3910ea6800d79d65ef1cfb1005720b4f713a")
    version("1.5.2", sha256="42a027df219011eebab8144877b6cebcddf3113a713c23fcae2a81464454009a")
    version("1.5.1", sha256="41ec731fb67ea35af2075eb3a4d6c83ef93b580dade63010821cbc00f1b98961")
    version("1.5.0", sha256="77e48bd40b7e7d30a17bf79bb6ed0f2d6985d915fcb9bf0879836276a619a0a9")
    version("1.4.2", sha256="3805848eb9e53e9c60aa24dd5be88c842a6cd3d241e22984bfe12629b08536a9")
    version("1.4.1", sha256="15aef8911560db1ea3ffa9dbd5414d0ec575a504a2c3f23ea45170a18994466e")
    version("1.3.1", sha256="1a94210c21a5d38d36d0fa36c1afb92c2857ba1d09c824b0d4b8615d51f4f2e5")
    version("1.2.0", sha256="23b7ac5bdab273b4f9306167fd86666a3777a52804d0282a556d989130cb57a4")
    version("1.1.1", sha256="6957451e59ce508f618335519c53f30ceb88b7053d65f3d166459fd708ed38b5")
    version("1.0.0", sha256="4fada4fddaa5c1bd69a5ba296ffd948cccb575ad7abe53d14960f56fe32dd4c1")
    version("0.11.0", sha256="fded30643588226f6f8b7ecd1242048ad423d29d4cd77d8000eea277479a0396")
    version("0.10.0", sha256="b785678f449de32476f427911248391ddcc7c3582a522a88cbbd50c92dcae490")
    version("0.9.0", sha256="67ba72edfecb5523b6f6e25156ddfc691f7588dd5dcd924838e6e3904d038778")
    version("0.8.5", sha256="2c7c8b228168b89da5d30d50dbd05452348920559ebe0eb94cfdafa15cdc8378")
    version("0.8.4", sha256="ef97bfec0263766edbb74c290401f89921f8d11ae9e4a0ffd904ae40674f1239")

    variant("awkward", default=True, description="Build with awkward support", when="@0.9:")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("python@3.7:", type=("build", "run"), when="@0.10:")
    depends_on("python@3.8:", type=("build", "run"), when="@1.1:")
    depends_on("python@3.9:", type=("build", "run"), when="@1.7:")
    depends_on("python@3.10:", type=("build", "run"), when="@1.8:")
    with when("@0.9:"):
        depends_on("py-hatchling", type="build")
        depends_on("py-hatch-vcs", type="build")
    with when("@:0.8"):
        depends_on("py-setuptools@42:", type="build")
        depends_on("py-setuptools-scm@3.4: +toml", type="build")
        depends_on("py-wheel", type="build")
    depends_on("py-numpy@1.13.3:", type=("build", "run"))
    depends_on("py-numpy@1.19.3:", type=("build", "run"), when="@1.7:")
    depends_on("py-packaging@19.0:", type=("build", "run"))
    depends_on("py-packaging@20:", type=("build", "run"), when="@1.7:")
    depends_on("py-importlib-metadata@0.22:", type=("build", "run"), when="@:1.0 ^python@:3.7")
    depends_on("py-typing-extensions", type=("build", "run"), when="@:1.0 ^python@:3.7")

    with when("+awkward"):
        depends_on("py-awkward@1.2:", type=("build", "run"))
        depends_on("py-awkward@2:", type=("build", "run"), when="@1.5:")

    # Historical dependencies
    depends_on("py-numpy@:2.0", type=("build", "run"), when="@:1.5.0")
