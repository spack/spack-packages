# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGromacswrapper(PythonPackage):
    """
    GromacsWrapper: A Python framework that wraps GROMACS
    tools into thin classes for easier scripting.
    """

    homepage = "https://github.com/Becksteinlab/GromacsWrapper"
    pypi = "gromacswrapper/gromacswrapper-0.9.2.tar.gz"

    license("GPL-3.0-or-later")
    maintainers("adamwitmer")

    version("0.9.2", sha256="73a7077258d68f92b1ee359e45af904e2f89766fc3f411bda9e2bf440f381a36")

    # Variants
    variant("pandas", default=True, description="Optional dependency on Pandas")

    # Dependencies
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numkit", type=("build", "run"))
    depends_on("py-setuptools@42:", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-pandas", when="+pandas")
