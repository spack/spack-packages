# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCtypesDlpack(PythonPackage):
    """Compatibility layer for dlpack in ctypes"""

    homepage = "https://docs.metatensor.org/ctypes-dlpack/latest/index.html"
    pypi = "ctypes_dlpack/ctypes_dlpack-0.1.0.tar.gz"

    supplier = "metatensor"

    maintainers("RMeli", "Luthaf")

    license("BSD-3-Clause", checked_by="RMeli")

    version("0.1.0", sha256="a1f8811e761f05bc28aa60cab2674afe4f6c7242255987214776cfc04c605132")

    depends_on("python@3.10:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@77:")

    def config_settings(self, spec, prefix):
        settings = {}
        return settings
