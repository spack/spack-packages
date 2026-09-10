# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHatchet(PythonPackage):
    """Hatchet is a performance tool for analyzing hierarchical performance data
    using a graph-indexed Pandas dataframe."""

    homepage = "https://github.com/hatchet/hatchet"
    url = "https://github.com/hatchet/hatchet/archive/v1.0.0.tar.gz"
    tags = ["radiuss"]

    maintainers("slabasan", "bhatele", "tgamblin")

    license("MIT")

    version("1.4.0", sha256="9f934f128666703d30818e9a091493df1bf1819bf7445ffb35a0f46871501b55")

    depends_on("c", type="build")  # generated

    depends_on("py-cython", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-pydot", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-textx", type=("build", "run"))
    depends_on("py-multiprocess", type=("build", "run"))
    depends_on("py-caliper-reader", type=("build", "run"))
    depends_on("py-pycubexr", type=("build", "run"))
