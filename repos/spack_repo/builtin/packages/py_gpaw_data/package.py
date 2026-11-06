# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGpawData(PythonPackage):
    """Data package for PAW files and other data files for the GPAW DFT code."""

    homepage = "https://gpaw.readthedocs.io/"
    url = "https://files.pythonhosted.org/packages/2b/68/2e8639afacbead047ad2688b36b8a5b96c87b49a23e07bd0af3d1d9efb8e/gpaw_data-1.2.1-py3-none-any.whl"

    maintainers("alikhamze")

    license("GPL-3.0-or-later", checked_by="alikhamze")

    version("1.2.1", sha256="5ded7ef43ca9b53332ad2fe9d7951dd36e6fba221662227fd24abf748b904c27")
    version("1.1.0", sha256="d6d2f2450cd6b22aa421738fce21c9c83b7f534cbc3bb4081ce5593fd9487173")
    version("1.0.1", sha256="28212110aa04daae333ef1260b281d70b818ad9cf4282078624ee3fc7a8fc05c")

    with when("@1.2.1"):
        depends_on("python@3.11:", type=("build", "run"))
    with when("@1.1.0"):
        depends_on("python@3.10:", type=("build", "run"))
    with when("@1.0.1"):
        depends_on("python@3.9:", type=("build", "run"))

    depends_on("py-setuptools", type="build")
