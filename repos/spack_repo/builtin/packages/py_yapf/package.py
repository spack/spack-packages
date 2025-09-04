# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyYapf(PythonPackage):
    """Yet Another Python Formatter"""

    homepage = "https://github.com/google/yapf"
    # base https://pypi.python.org/pypi/cffi
    url = "https://github.com/google/yapf/archive/v0.2.1.tar.gz"

    license("Apache-2.0")

    version("0.43.0", sha256="1d8ca9d7e1fc429c496e0a046e509e437d5ae766487b0394c45fc1fdf253b5d4")
    version("0.40.2", sha256="8e0825803c488aa2cb118ed277a18d4617984608e75d10d5bffa5e24734eb022")
    version("0.40.1", sha256="ed9e606d9f74ea44196249c1e5be2a16ec7c205314e798c1e2d92cf51cdc50aa")
    version("0.40.0", sha256="c295a4e9d259c189b74cafb34d645cc9acff73a1aa33589d8e175362c3164050")
    version("0.33.0", sha256="c7bab16bab19c94a478e4f25fbcae545aa29c5f5fbe7c630f06ceafd807cc13b")
    version("0.32.0", sha256="410ed0f592c898d75d73f7792aee6569bdbc0b57bc72b417c722c17f41f66b12")
    version("0.31.0", sha256="e6330f89f024615b102f3140e50a1b864196c4d9d8e29ace4eaa234feec4c924")
    version("0.30.0", sha256="9f561af26f8d27c3a334d3d2ee8947b8826a86691087e447ce483512d834682c")
    version("0.29.1", sha256="22046ea87e672376b3a9f7898357cb8328a473f512123f14fcca8cbe22d32631")
    version("0.29.0", sha256="f4bc9924de51d30da0241503d56e9e26a1a583bc58b3a13b2c450c4d16c9920d")
    version("0.2.1", sha256="13158055acd8e3c2f3a577528051a1c5057237f699150211a86fb405c4ea3936")

    depends_on("py-setuptools", type="build")
