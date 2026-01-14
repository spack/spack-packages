# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLightpipes(PythonPackage):
    """LightPipes for Python optical toolbox."""

    homepage = "https://github.com/opticspy/lightpipes"
    pypi = "LightPipes/LightPipes-2.1.5-py3-none-any.whl"
    # Work-around URL until the CI version check can rely on the URL related to a PyPi wheel.
    url = "https://pypi.io/packages/py3/l/lightpipes/LightPipes-2.1.5-py3-none-any.whl"
    maintainers("LydDeb")

    license("BSD-3-Clause", checked_by="LydDeb")

    version("2.1.5", sha256="0943916bf5e57a2197e337098ab8941132ffc706dabe99c7c03b2552fc107810")

    variant("fftw", default=False, description="Enable fftw support")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-pyfftw", type=("build", "run"), when="+fftw")
