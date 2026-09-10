# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Xterm(AutotoolsPackage):
    """The xterm program is a terminal emulator for the X Window System. It
    provides DEC VT102 and Tektronix 4014 compatible terminals for programs
    that can't use the window system directly."""

    homepage = "https://invisible-island.net/xterm/"
    url = "https://invisible-island.net/archives/xterm/xterm-327.tgz"

    license("MIT")

    version("401", sha256="3da2b5e64cb49b03aa13057d85e62e1f2e64f7c744719c00d338d11cd3e6ca1a")
    version("400", sha256="eed84ecc05efa63d589c5a2a3f5a947e14b798d03b5342cc6883710f648f1a06")
    version("399", sha256="9db34ad0f53ddb1223d70b247c8391e52f3e4b166d6ad85426a4c47813d1b1e3")
    version("398", sha256="f679bd45f97063f10a880ecf7fc1611a9a03e8c8b98f063e99e0a079e87ee968")
    version("397", sha256="2e9b742b9cba44ecec58074e513237f6cd6d5923f1737cb36a4e5625f4ae8662")
    version("396", sha256="43f94b6d0eecb4219a99f46352e746f2ab5558e40d922d411acff96cc778a6a5")
    version("395", sha256="286e3caa5938eae38e202827621567629dfeaae689e8070b413ca11398093dc8")
    version("394", sha256="a2a0cb206eb0423dedc34794f5c2d38c83390d2dd1106b66aba0960c3a976c7a")
    version("393", sha256="dc3abf533d66ae3db49e6783b0e1e29f0e4d045b4b3dac797a5e93be2735ec7b")
    version("353", sha256="e521d3ee9def61f5d5c911afc74dd5c3a56ce147c7071c74023ea24cac9bb768")
    version("350", sha256="aefb59eefd310268080d1a90a447368fb97a9a6737bfecfc3800bf6cc304104d")
    version("340", sha256="b5c7f77b7afade798461e2a2f86d5af64f9c9c9f408b1af0f545add978df722a")
    version("330", sha256="7aeef9f29f6b95e09f481173c8c3053357bf5ffe162585647f690fd1707556df")
    version("327", sha256="66fb2f6c35b342148f549c276b12a3aa3fb408e27ab6360ddec513e14376150b")

    depends_on("libxft")
    depends_on("fontconfig")
    depends_on("libxaw")
    depends_on("libxmu")
    depends_on("libxt")
    depends_on("libx11")
    depends_on("libxinerama")
    depends_on("libxpm")
    depends_on("libice")
    depends_on("freetype")
    depends_on("libxrender")
    depends_on("libxext")
    depends_on("libsm")
    depends_on("libxcb")
    depends_on("libxau")
    depends_on("bzip2")
    depends_on("ncurses")

    depends_on("c", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("termcap", type="link")
