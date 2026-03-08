# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyaml(PythonPackage):
    """PyYAML-based python module to produce pretty and readable
    YAML-serialized data."""

    maintainers("Kerilk", "liuyangzhuan")

    homepage = "https://github.com/mk-fg/pretty-yaml"
    pypi = "pyaml/pyaml-21.8.3.tar.gz"

    license("WTFPL")

    version("25.7.0", sha256="e113a64ec16881bf2b092e2beb84b7dcf1bd98096ad17f5f14e8fb782a75d99b")
    version("25.5.0", sha256="5799560c7b1c9daf35a7a4535f53e2c30323f74cbd7cb4f2e715b16dd681a58a")
    version("25.1.0", sha256="33a93ac49218f57e020b81e280d2706cea554ac5a76445ac79add760d019c709")
    version("24.12.1", sha256="3938c2b47924ed74524f844961a011852f7968fb8cc7b3933276087c5d1e45b3")
    version("24.12.0", sha256="193c599b35fa05b9d5c96eea991acb6bd375f9f87d2dd1bdb2dc60f620c68f0d")
    version("24.9.0", sha256="e78dee8b0d4fed56bb9fa11a8a7858e6fade1ec70a9a122cee6736efac3e69b5")
    version("24.7.0", sha256="5d0fdf9e681036fb263a783d0298fc3af580a6e2a6cf1a3314ffc48dc3d91ccb")
    version("24.4.0", sha256="0e483d9289010e747a325dc43171bcc39d6562dd1dd4719e8cc7e7c96c99fce6")
    version("23.12.0", sha256="ce6f648efdfb1b3a5579f8cedb04facf0fa1e8f64846b639309b585bb322b4e5")
    version("23.9.7", sha256="581ea4e99f0e308864407e04c03c609241aefa3a15dfba8964da7644baf3b217")
    version("23.9.6", sha256="2b2c39017b718a127bef9f96bc55f89414d960876668d69880aae66f4ba98957")
    version("23.9.5", sha256="9b903a1185eefdf85499cb856b70b12245988db990bfd6af596d3521ece306a4")
    version("23.9.4", sha256="9fb8683c619736dc1437abafe4645689f3fbd16f00164056cf0467a1a860f113")
    version("23.9.3", sha256="b3f9b38335327d3214c88834930037386c0fe4457e1ae19719c56faa239222bd")
    version("23.9.2", sha256="eee6dde0c848e126e521e74ae2f21e7a431e4cc3d650b3338696907b237e759c")
    version("23.9.1", sha256="4e2030f5fc0d3b5784a3a7853ba78b1ae8de943c6dba5507876550c5bd18f387")
    version("23.9.0", sha256="c6bf6d278ea9f467ac0b1a7203f48975c07f77553b25f506600bd2f5741e6c48")
    version("23.7.0", sha256="0c510bbb8938309400e0b1e47ac16fd90e56d652805a93417128786718f33546")
    version("23.5.9", sha256="4c4b28b6fe89336000f08646f3cf1f6b68fb11e4c409626b77562e65a577273b")
    version("23.5.8", sha256="287c58ad3aca43fd6da216f42b3d89c835aa1c79301948bbd25be9a2bb71def3")
    version("23.5.7", sha256="b2737e9c7829884e2c1279271d52f217210adbfbf103eefd6c9b6aa6f9d4faf2")
    version("23.5.6", sha256="e20a38630eb5ce58191aa6bacd5c2472f14f3588f7d85ba40f731d4f0804f2cc")
    version("23.5.5", sha256="2a5575c2b5de5b3d4f3ea93d9298626b8dc5b41bdff047900c7d230cb82e93a9")
    version("21.10.1", sha256="c6519fee13bf06e3bb3f20cacdea8eba9140385a7c2546df5dbae4887f768383")
    version("21.8.3", sha256="a1636d63c476328a07213d0b7111bb63570f1ab8a3eddf60522630250c23d975")

    depends_on("python@2.7:2,3.5:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-pyyaml", type=("build", "run"))
