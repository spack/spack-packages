# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGpawData(PythonPackage):
    """Data package for PAW files and other data files for the GPAW DFT code."""

    homepage = "https://gpaw.readthedocs.io/"
    # Only wheels provided on pypi and no releases or release tags on gitlab
    url = (
        "https://files.pythonhosted.org/packages/py3/g/gpaw_data/gpaw_data-1.2.1-py3-none-any.whl"
    )

    maintainers("alikhamze")

    license("GPL-3.0-or-later", checked_by="alikhamze")

    version("1.2.1", sha256="5ded7ef43ca9b53332ad2fe9d7951dd36e6fba221662227fd24abf748b904c27")
    version("1.1.0", sha256="d6d2f2450cd6b22aa421738fce21c9c83b7f534cbc3bb4081ce5593fd9487173")
    version("1.0.1", sha256="f7a724a77c5974c51e6071f134e465c2aa97307ddff155f26b6a8e4d6f03edcf")

    with when("@1.2.1"):
        depends_on("python@3.11:", type=("build", "run"))
    with when("@1.1.0"):
        depends_on("python@3.10:", type=("build", "run"))
    with when("@1.0.1"):
        depends_on("python@3.9:", type=("build", "run"))

    depends_on("py-setuptools", type="build")
