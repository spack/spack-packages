# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFilelock(PythonPackage):
    """A platform-independent file lock for Python.

    This package contains a single module, which implements a platform
    independent file lock in Python, which provides a simple way of
    inter-process communication"""

    homepage = "https://github.com/tox-dev/py-filelock"
    pypi = "filelock/filelock-3.0.4.tar.gz"

    license("Unlicense")

    version("3.24.3", sha256="011a5644dc937c22699943ebbfc46e969cdde3e171470a6e40b9533e5a72affa")  # FIXME
    version("3.24.2", sha256="c22803117490f156e59fafce621f0550a7a853e2bbf4f87f112b11d469b6c81b")  # FIXME
    version("3.24.1", sha256="3440181dd03f8904c108c8e9f5b11d1663e9fc960f1c837586a11f1c5c041e54")  # FIXME
    version("3.24.0", sha256="aeeab479339ddf463a1cdd1f15a6e6894db976071e5883efc94d22ed5139044b")  # FIXME
    version("3.23.0", sha256="f64442f6f4707b9385049bb490be0bc48e3ab8e74ad27d4063435252917f4d4b")  # FIXME
    version("3.22.0", sha256="61eb14cc8775af91381024c7282e3f526e1fb27f42bfdde706113c7e01a5544b")  # FIXME
    version("3.21.2", sha256="cfd218cfccf8b947fce7837da312ec3359d10ef2a47c8602edd59e0bacffb708")  # FIXME
    version("3.21.1", sha256="fd13d64b92f79605f30ffaa0a2accb793f178b8aebcf56be8f1cad922fd278ad")  # FIXME
    version("3.21.0", sha256="48c739c73c6fcacd381ed532226991150947c4a76dcd674f84d6807fd55dbaf2")  # FIXME
    version("3.20.4", sha256="92b98bb6be1a4e6c1b00f8aedae011c6e2d367c195000a049daa34f554af3d94")  # FIXME
    version("3.20.3", sha256="18c57ee915c7ec61cff0ecf7f0f869936c7c30191bb0cf406f1341778d0834e1")  # FIXME
    version("3.20.2", sha256="a2241ff4ddde2a7cebddf78e39832509cb045d18ec1a09d7248d6bfc6bfbbe64")  # FIXME
    version("3.20.1", sha256="b8360948b351b80f420878d8516519a2204b07aefcdcfd24912a5d33127f188c")  # FIXME
    version("3.20.0", sha256="711e943b4ec6be42e1d4e6690b48dc175c822967466bb31c0c293f34334c13f4")  # FIXME
    version("3.19.1", sha256="66eda1888b0171c998b35be2bcc0f6d75c388a7ce20c3f3f37aa8e96c2dddf58")
    version("3.12.4", sha256="2e6f249f1f3654291606e046b09f1fd5eac39b360664c27f5aad072012f8bcbd")
    version("3.12.0", sha256="fc03ae43288c013d2ea83c8597001b1129db351aad9c57fe2409327916b8e718")
    version("3.8.0", sha256="55447caa666f2198c5b6b13a26d2084d26fa5b115c00d065664b2124680c4edc")
    version("3.5.0", sha256="137b661e657f7850eec9def2a001efadba3414be523b87cd3f9a037372d80a15")
    version("3.4.0", sha256="93d512b32a23baf4cac44ffd72ccf70732aeff7b8050fcaf6d3ec406d954baf4")
    version("3.0.12", sha256="18d82244ee114f543149c66a6e0c14e9c4f8a1044b5cdaadd0f82159d6a6ff59")
    version("3.0.4", sha256="011327d4ed939693a5b28c0fdf2fd9bda1f68614c1d6d0643a89382ce9843a71")
    version("3.0.3", sha256="7d8a86350736aa0efea0730e6a7f774195cbb1c2d61134c15f6be576399e87ff")
    version("3.0.0", sha256="b3ad481724adfb2280773edd95ce501e497e88fa4489c6e41e637ab3fd9a456c")
    version("2.0.13", sha256="d05079e7d7cae7576e192749d3461999ca6b0843d35b0f79f1fa956b0f6fc7d8")
    version("2.0.12", sha256="eb4314a9a032707a914b037433ce866d4ed363fce8605d45f0c9d2cd6ac52f98")
    version("2.0.11", sha256="e9e370efe86c30b19a2c8c36dd9fcce8e5ce294ef4ed6ac86664b666eaf852ca")
    version("2.0.10", sha256="c73bf706d8a0c5722de0b745495fed9cda0e46c0eabb44eb18ee3f00520fa85f")
    version("2.0.9", sha256="0f91dce339c9f25d6f2e0733a17e4f9a47b139dffda52619a0e61e013e5c6782")
    version("2.0.8", sha256="7e48e4906de3c9a5d64d8f235eb3ae1050dfefa63fd65eaf318cc915c935212b")

    depends_on("python@3.10:", when="@3.20:", type=("build", "run"))
    depends_on("python@3.9:", when="@3.17:3.19", type=("build", "run"))
    depends_on("python@3.8:", when="@3.12.3:", type=("build", "run"))

    depends_on("py-hatch-vcs@0.5:", when="@3.19:", type="build")
    depends_on("py-hatch-vcs@0.3:", when="@3.8:", type="build")
    depends_on("py-hatchling@1.27:", when="@3.17:", type="build")
    depends_on("py-hatchling@1.18:", when="@3.12.3:", type="build")
    depends_on("py-hatchling@1.14:", when="@3.8:", type="build")

    # Historical dependencies
    with when("@:3.8.0"):
        depends_on("py-setuptools@63.4:", when="@3.8:", type="build")
        depends_on("py-setuptools@41:", when="@3.1:", type="build")
        depends_on("py-setuptools", type="build")
        depends_on("py-setuptools-scm@7.0.5:", when="@3.8:", type="build")
        depends_on("py-setuptools-scm@2:", when="@3.1:", type="build")

    depends_on("py-wheel@0.30:", when="@3.1:3.7", type="build")
