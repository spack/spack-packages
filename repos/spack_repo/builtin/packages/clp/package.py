# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Clp(AutotoolsPackage):
    """Clp (Coin-or linear programming) is an open-source
    linear programming solver written in C++."""

    homepage = "https://projects.coin-or.org/Clp"
    url = "https://github.com/coin-or/Clp/archive/releases/1.17.11.tar.gz"

    license("EPL-2.0")

    version("1.17.11", sha256="2c078e174dc1a7a308e091b6256fb34b4017897fc140ea707ba207b2913ea46d")
    version("1.17.9", sha256="b02109be54e2c9c6babc9480c242b2c3c7499368cfca8c0430f74782a694a49f")
    version("1.17.7", sha256="c4c2c0e014220ce8b6294f3be0f3a595a37bef58a14bf9bac406016e9e73b0f5")
    version("1.17.6", sha256="afff465b1620cfcbb7b7c17b5d331d412039650ff471c4160c7eb24ae01284c9")
    version("1.17.4", sha256="ef412cde00cb1313d9041115a700d8d59d4b8b8b5e4dde43e9deb5108fcfbea8")
    version("1.16.12", sha256="3ea36ea3d1500bec9d5c9a105dbc5dc282851272b6bb1412cd6edf2a4b5ea559")
    version("1.16.11", sha256="ac42c00ba95e1e034ae75ba0e3a5ff03b452191e0c9b2f5e2d5e65bf652fb0a1")
    version("1.16.8", sha256="22042aaf5857272b83039be8d1f84baff8f349a76f2527c62de7ad36717c7d04")
    version("1.15.12", sha256="652c45aabbe06859ba2e7f702962447cf7af71f7c6835e847074dc44c327faf0")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # Passing -DNDEBUG to CXXFLAGS allows building with %gcc@11: but with side-effects.
    conflicts("gcc@11:", when="@:1.16.10")

    depends_on("pkgconfig", type="build")

    depends_on("coinutils@2.11.2:", when="@1.17.2:")
    depends_on("coinutils@2.11.0:", when="@1.17.0:1.17.1")
    depends_on("coinutils@2.10.6:", when="@1.16.6:1.16")
    depends_on("coinutils")

    depends_on("osi")

    build_directory = "spack-build"
