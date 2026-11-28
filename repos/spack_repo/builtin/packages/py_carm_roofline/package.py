# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCarmRoofline(PythonPackage):
    """The CARM Tool - benchmark, visualize and profile Intel, AMD, ARM, and RISC-V CPUs."""

    homepage = "https://github.com/champ-hub/carm-roofline"
    pypi = "carm-roofline/carm_roofline-1.4.0.tar.gz"

    maintainers("Alexandre425")

    license("Apache-2.0", checked_by="Alexandre425")

    version("1.4.0", sha256="54f68b175b84d0ced1fca6454346d70d7db403a046dd2bd9a3b28ed05d1e8c5b")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@64:", type="build")
    depends_on("py-wheel", type="build")

    depends_on("py-rich@14.3.2:", type=("build", "run"))
    depends_on("py-rich-argparse@1.7.0:", type=("build", "run"))
    depends_on("py-matplotlib@3.7.2:", type=("build", "run"))
    depends_on("py-pandas@2.3.3:", type=("build", "run"))
    depends_on("py-tomli@2.0.0:", type=("build", "run"))
    depends_on("py-platformdirs@4.0.0:", type=("build", "run"))
    depends_on("py-argcomplete@3.0.0:", type=("build", "run"))
    depends_on("py-dash@4.4.1:", type=("build", "run"))
    depends_on("py-dash-bootstrap-components@2.0.4:", type=("build", "run"))
    depends_on("py-plotly@6.7.0:", type=("build", "run"))
