# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTypesPsutil(PythonPackage):
    """Typing stubs for psutil."""

    homepage = "https://github.com/python/typeshed"
    pypi = "types_psutil/types_psutil-7.0.0.20251001.tar.gz"

    version(
        "7.2.2.20260130", sha256="15b0ab69c52841cf9ce3c383e8480c620a4d13d6a8e22b16978ebddac5590950"
    )
    version(
        "7.2.1.20260116", sha256="4661be5d5d7acd5d8afb02a92d05160a6cbb2ce74723245b51f7ba7dfdb9f981"
    )
    version(
        "7.2.1.20251231", sha256="dbf9df530b1130e131e4211ed8cea62c08007bfa69faf2883d296bd241d30e4a"
    )
    version(
        "7.2.0.20251228", sha256="dde992ac5b22512724a82ed21a43b03971592dff6cd271e2bd42a8750b30929b"
    )
    version(
        "7.1.3.20251211", sha256="2c25f8fd3a1a4aebdffb861b97755c9a2d5d8019dd6ec1a2f2a77ec796652c89"
    )
    version(
        "7.1.3.20251210", sha256="0fef0f363574d76965385e5170a0c95f88ef2c67327e4337298b3a1d35e61be4"
    )
    version(
        "7.1.3.20251202", sha256="5cfecaced7c486fb3995bb290eab45043d697a261718aca01b9b340d1ab7968a"
    )
    version(
        "7.1.3.20251130", sha256="7f42e7a7845a93397e430b48a8074a35410d7a436695fd3375ec9b687d8d95f8"
    )
    version(
        "7.1.3.20251129", sha256="3d6af84712be290803ed3cf4dd4ea7eb0b2fa61ed40de7d5c3a909879c4191ee"
    )
    version(
        "7.1.3.20251128", sha256="7e5b0b6b6db0b8a714d483636718baaf6587498e57b55953264b40a4fd6786ea"
    )
    version(
        "7.1.3.20251127", sha256="21d74eaca4688ef168aa28181a465dc067cf9d4bb09df949db573f9140f66557"
    )
    version(
        "7.1.3.20251125", sha256="bee98e02e496db28967e552bfb793f43deb11060cdf2d15ecb16c942aed02e3c"
    )
    version(
        "7.1.1.20251122", sha256="cdb39c30a81ce6e433aa672922d59b78c4c6a9c64cd9936f1f6894d26c82ae0f"
    )
    version(
        "7.0.0.20251116", sha256="92b5c78962e55ce1ed7b0189901a4409ece36ab9fd50c3029cca7e681c606c8a"
    )
    version(
        "7.0.0.20251115", sha256="67db0fbe0f2ed540f9a7d419273086c7d65cbaed8ccc32c8197d12963eedde72"
    )
    version(
        "7.0.0.20251111", sha256="d109ee2da4c0a9b69b8cefc46e195db8cf0fc0200b6641480df71e7f3f51a239"
    )
    version(
        "7.0.0.20251001", sha256="60d696200ddae28677e7d88cdebd6e960294e85adefbaafe0f6e5d0e7b4c1963"
    )
    version("5.9.5.16", sha256="4e9b219efb625d3d04f6bf106934f87cab49aa41a94b0a3b3089403f47a79228")
    version("5.9.5.5", sha256="4f26fdb2cb064b274cbc6359fba4abf3b3a2993d7d4abc336ad0947568212c62")

    depends_on("python@3.9:", type=("build", "run"), when="@7.0.0.20250218:")
    depends_on("py-setuptools@77.0.3:", type="build", when="@7.0.0.20250516:")
    depends_on("py-setuptools", type="build")

    def url_for_version(self, version):
        if self.spec.satisfies("@6.1.0.20241221:"):
            name = "types_psutil"
        else:
            name = "types-psutil"
        return f"https://files.pythonhosted.org/packages/source/{name[0]}/{name}/{name}-{version}.tar.gz"
