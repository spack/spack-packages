# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCryptography(PythonPackage):
    """cryptography is a package which provides cryptographic recipes
    and primitives to Python developers"""

    homepage = "https://github.com/pyca/cryptography"
    pypi = "cryptography/cryptography-1.8.1.tar.gz"

    license("Apache-2.0")

    version("46.0.3", sha256="a8b17438104fed022ce745b362294d9ce35b4c2e45c1d958ad4a4b019285f4a1")
    version("45.0.5", sha256="72e76caa004ab63accdf26023fccd1d087f6d90ec6048ff33ad0445abf7f605a")
    version("43.0.3", sha256="315b9001266a492a6ff443b61238f956b214dbec9910a081ba5b6646a055a805")
    version("43.0.1", sha256="203e92a75716d8cfb491dc47c79e17d0d9207ccffcbcb35f598fbe463ae3444d")
    version("42.0.8", sha256="8d09d05439ce7baa8e9e95b07ec5b6c886f548deb7e0f69ef25f64b3bce842f2")
    version("41.0.7", sha256="13f93ce9bea8016c253b34afc6bd6a75993e5c40672ed5405a9c832f0d4a00bc")
    version("41.0.3", sha256="6d192741113ef5e30d89dcb5b956ef4e1578f304708701b8b73d38e3e1461f34")
    version("40.0.2", sha256="c33c0d32b8594fa647d2e01dbccc303478e16fdd7cf98652d5b3ed11aa5e5c99")
    version("38.0.1", sha256="1db3d807a14931fa317f96435695d9ec386be7b84b618cc61cfa5d08b0ae33d7")
    version("37.0.4", sha256="63f9c17c0e2474ccbebc9302ce2f07b55b3b3fcb211ded18a42d5764f5c10a82")
    version("36.0.1", sha256="53e5c1dc3d7a953de055d77bef2ff607ceef7a2aac0353b5d630ab67f7423638")
    version("35.0.0", sha256="9933f28f70d0517686bd7de36166dda42094eac49415459d9bdf5e7df3e0086d")

    # pyo3 <= 0.22 required in version <= 42
    depends_on("python@:3.12", when="@:42", type=("build", "run"))
    # distutils required in version <= 40
    depends_on("python@:3.11", when="@:40", type=("build", "run"))

    depends_on("py-maturin@1.9.4:1", when="@46:", type="build")
    depends_on("py-maturin@1.8.6:1", when="@45", type="build")
    depends_on("py-maturin@1", when="@43:44", type="build")
    depends_on("py-setuptools@61.0:", when="@41:", type="build")
    depends_on("py-setuptools@40.6:60.8,60.9.1:", when="@37:", type="build")
    depends_on("py-setuptools@40.6:", when="@:36", type="build")
    with when("@:42"):
        depends_on("py-setuptools-rust@1.7.0:", when="@42", type=("build", "run"))
        depends_on("py-setuptools-rust@0.11.4:", type="build")

    # from https://cryptography.io/en/latest/installation/#rust
    depends_on("rust@1.74:", when="@45:", type="build")
    depends_on("rust@1.65:", when="@43:", type="build")
    depends_on("rust@1.63:", when="@42:", type="build")
    depends_on("rust@1.56:", when="@41:", type="build")
    depends_on("rust@1.48:", when="@38:", type="build")
    depends_on("rust@1.41:", type="build")
    depends_on("pkgconfig", when="@40:", type="build")

    depends_on("py-cffi@1.14:", when="@45:", type=("build", "run"))
    depends_on("py-cffi@1.12:", type=("build", "run"))
    depends_on("py-typing-extensions@4.13.2:", when="@46: ^python@:3.10", type=("build", "run"))

    # from https://cryptography.io/en/latest/installation/
    depends_on("openssl@3:", when="@42:")
    depends_on("openssl@1.1.1:", when="@39:")
    depends_on("openssl")

    conflicts("^python@3.9.0,3.9.1", when="@45:")
    conflicts("^py-setuptools@74.0.0,74.1.0,74.1.1,74.1.2", when="@44:")
    conflicts(
        "^py-setuptools@74.0.0,74.1.0,74.1.1,74.1.2,74.1.3,75.0.0,75.1.0,75.2.0",
        msg="some setuptools version are incompatible",
        when="@43",
    )

    # To fix https://github.com/spack/spack/issues/29669
    # https://community.home-assistant.io/t/error-failed-building-wheel-for-cryptography/352020/14
    # We use CLI git instead of Cargo's internal git library
    # See reference: https://doc.rust-lang.org/cargo/reference/config.html#netgit-fetch-with-cli
    depends_on("git", type="build")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CARGO_NET_GIT_FETCH_WITH_CLI", "true")
