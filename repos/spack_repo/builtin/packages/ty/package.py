# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cargo import CargoPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class Ty(CargoPackage, PythonPackage):
    """An extremely fast Python type checker, written in Rust."""

    homepage = "https://github.com/astral-sh/ty/"
    # Needs to be "source" tarball (not GH generated) to get ruff submodule
    url = "https://github.com/astral-sh/ty/releases/download/0.0.24/source.tar.gz"

    build_directory = "ruff/crates/ty"

    build_args = ["--bin", "ty"]

    license("MIT")
    maintainers("adamjstewart")

    version("0.0.29", sha256="f03fb2349e404bdb62a828fcea96d1d7b97a06722d25de4a27b83e289cf810f2")
    version("0.0.28", sha256="578792eec001dfca85a5be5df2e5acee64d5bda8dada9715472e211598ad5352")
    version("0.0.27", sha256="d83bb1a634d7cbbb3a37dc715861ad601bbcfc61c3c2211c1c2a26413df376a2")
    version("0.0.26", sha256="a7cdf959700f96784396dd673a7bcd82300a16e337995fbbc6c4842a730ad5e5")
    version("0.0.25", sha256="e22a3f371b260f482fdece3ebd44e42342241661224283e4b7be283df0dfcc3b")
    version("0.0.24", sha256="cddb2c6022e2b96faf289c9a275bf4ee05a3430e922ffe9e123fad6a9542a325")
    version("0.0.23", sha256="cc418cb981ed727777e5f97d70a85927007018488a912de8f66483a68904f692")
    version("0.0.22", sha256="fbdb6cb5bf7761648d74264736dffd247921d3692711cafa22ee4a169632d58a")
    version("0.0.21", sha256="a8c0cca4fbeecf4154e143e3346a8f2387794f56df5bede7613af616752c2d6a")
    version("0.0.20", sha256="8c58223406f4fa5e27fbb78764518a40ef1e277e6a689a22e9e3f1d2367ba9e7")
    version("0.0.19", sha256="94179a639987f29d75ff8ff8cad408a4c540ef904c9ef53a58fc023239fdc348")
    version("0.0.18", sha256="041796166dbe3ac1079a8b5b7c676a35529944036ffa2355ab91542ccdb484c9")
    version("0.0.17", sha256="0e46d435f4a3f553a04c254b74ba9f5f6579046f2d4d921833bcc87dda08dfb8")
    version("0.0.16", sha256="e078831ec7e0b6be4dd920043a7c19fd1b6e92c26b48df0635b03cd59b348a1a")
    version("0.0.15", sha256="ac07106322ed0367fa3932d1e008140dffa7d115471f8cccefa810fd3c368b6a")

    variant("python", default=False, description="Build and install ruff as a wheel")

    build_system("cargo", conditional("python_pip", when="+python"), default="cargo")

    with when("+python"):
        build_system("python_pip")
        depends_on("py-maturin@1", type="build")

    with default_args(type="build"):
        depends_on("c")
        depends_on("gmake")
        # ruff/Cargo.toml
        depends_on("rust@1.92:", when="@0.0.25:")
        depends_on("rust@1.91:", when="@0.0.15:")
