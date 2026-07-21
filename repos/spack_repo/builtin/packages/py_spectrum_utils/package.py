# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySpectrumUtils(PythonPackage):
    """Efficient mass spectrometry data processing and visualization."""

    homepage = "https://github.com/bittremieuxlab/spectrum_utils"
    pypi = "spectrum_utils/spectrum_utils-0.5.0.tar.gz"

    license("Apache-2.0")

    version("0.5.0", sha256="150455c8a771499f1e5e17f98be7115c6c9263ad3404e562e962d364d2ced951")

    variant("plotting", default=False, description="Plotting helpers")
    variant("pyteomics", default=False, description="Optional to avoid circular dependency")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-fastobo")
    depends_on("py-lark@1.0:")
    depends_on("py-matplotlib@3.5:")
    depends_on("py-numba@0.57:")
    depends_on("py-numpy")
    depends_on("py-platformdirs")
    depends_on("py-pyteomics@4.6:", when="+pyteomics")

    depends_on("py-altair", when="+plotting")
    depends_on("py-pandas", when="+plotting")
