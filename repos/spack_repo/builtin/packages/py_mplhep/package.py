# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMplhep(PythonPackage):
    """Matplotlib styles for HEP"""

    homepage = "https://github.com/scikit-hep/mplhep"
    pypi = "mplhep/mplhep-0.3.15.tar.gz"
    git = "https://github.com/scikit-hep/mplhep.git"

    license("MIT", checked_by="wdconinc")

    version("1.1.0", sha256="bc79cc481b27835f7cc069e9e0d801e203e37c61af3131c717191d19838908db")
    version("1.0.0", sha256="efab1ec4545f75a47fe6d1dd5862667e8c12054f4d933c089052c345e6940b43")
    version("0.4.1", sha256="86e2d99680bdb19598e847ff5b24f3bf1c63f164b99f076be98255acd738ee48")
    version("0.4.0", sha256="485d67db2dd7a1091eee86580fe46cf32dd0b0fc34d6db6246b1ef59346a810c")
    version("0.3.59", sha256="06f4b3a799e92fe6982ed3939dd648d0f972781aca3dc814a83e5bbd970649fe")
    version("0.3.58", sha256="fed8b5d5fee92c7aa40cfe70e5b8d2b2bb8ed7aeb7a2c272d73b241279e1adba")
    version("0.3.57", sha256="3b04a91f75889e31c0d7a5e520dd092f2fd29fb6000418c26cf4e497cc977541")
    version("0.3.56", sha256="2e773a65a233d186071b81d5faeadd340b768e9bd8825b40bd20c81a419d25f2")
    version("0.3.55", sha256="0fb87cd4b025225ba8fd5d82d58324cfb094fbcdd7929e5a9ea1ea7e22108814")
    version("0.3.26", sha256="d707a95ce59b0bac2fe4fe1c57fede14e15da639f3a7c732e7513a753fd9e9ac")
    version("0.3.15", sha256="595f796ea65930094e86a805214e0d44537ead267a7487ae16eda02d1670653e")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("python@3.8:", type=("build", "run"), when="@0.3.29:")
    depends_on("python@3.9:", type=("build", "run"), when="@1:")
    with when("@0.3.53:"):
        depends_on("py-hatchling", type="build")
        depends_on("py-hatch-vcs", type="build")
    with when("@:0.3.52"):
        depends_on("py-setuptools@39.2:", type="build")
        depends_on("py-setuptools@42:", when="@0.3.26:", type="build")
        depends_on("py-setuptools-scm@3.4:+toml", when="@0.3.2:", type="build")
    depends_on("py-matplotlib@3.4:", type=("build", "run"))
    # properly handle docstring -> _docstring transition in mplhep#443 and mplhep#455
    depends_on("py-matplotlib@3.6:", type=("build", "run"), when="@0.3.29:")
    depends_on("py-matplotlib@:3.9", type=("build", "run"), when="@1: ^python@:3.9")
    depends_on("py-matplotlib@3.10.8:", type=("build", "run"), when="@1: ^python@3.10:")
    depends_on("py-matplotlib@:3.8", type=("build", "run"), when="@:0.3.28")
    depends_on("py-pyparsing@:3.2", type=("build", "run"), when="@1: ^python@:3.9")
    depends_on("py-mplhep-data", type=("build", "run"))
    depends_on("py-mplhep-data@0.0.4:", type=("build", "run"), when="@0.3.54:")
    depends_on("py-numpy@1.16.0:", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-uhi@0.2.0:", type=("build", "run"))
