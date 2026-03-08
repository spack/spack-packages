# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyjwt(PythonPackage):
    """JSON Web Token implementation in Python"""

    homepage = "https://github.com/jpadilla/pyjwt"
    pypi = "PyJWT/PyJWT-1.7.1.tar.gz"

    license("MIT")

    version("2.8.0", sha256="57e28d156e3d5c10088e0c68abb90bfac3df82b40a71bd0daa20c65ccd5c23de")  # FIXME
    version("2.7.0", sha256="bd6ca4a3c4285c1a2d4349e5a035fdf8fb94e04ccd0fcbe6ba289dae9cc3e074")  # FIXME
    version("2.6.0", sha256="69285c7e31fc44f68a1feb309e948e0df53259d579295e6cfe2b1792329f05fd")  # FIXME
    version("2.5.0", sha256="e77ab89480905d86998442ac5788f35333fa85f65047a534adc38edf3c88fc3b")  # FIXME
    version("2.4.0", sha256="d42908208c699b3b973cbeb01a969ba6a96c821eefb1c5bfe4c390c01d67abba")
    version("2.1.0", sha256="fba44e7898bbca160a2b2b501f492824fc8382485d3a6f11ba5d0c1937ce6130")
    version("1.7.1", sha256="8d59a976fb773f3e6a39c85636357c4f0e242707394cadadd9814f5cbaa20e96")

    variant(
        "crypto", default=False, description="Build with cryptography support", when="@:2.0,2.4:"
    )

    depends_on("python@2.7:2.8,3.4:", type=("build", "run"))
    depends_on("python@3.6:", when="@2.1.0:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-cryptography@3.3.1:", when="+crypto", type=("build", "run"))
    depends_on("py-cryptography@1.4:", when="+crypto", type=("build", "run"))
    depends_on("py-cryptography@3.3.1:", when="@2.4:+crypto", type=("build", "run"))
