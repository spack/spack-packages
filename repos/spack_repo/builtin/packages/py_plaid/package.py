# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPlaid(PythonPackage):
    """A package that implements a data model tailored for AI and ML
    in the context of physics problems
    """

    homepage = "https://github.com/PLAID-lib/plaid"
    pypi = "pyplaid/pyplaid-0.1.15.tar.gz"

    maintainers("williampiat3", "casenave", "bstaber")

    license("BSD-3-Clause", checked_by="casenave")

    version("1.0.0", sha256="fb0015f08db6ac73d3fe240fb24f2c908421398ecf6251f2cce81c0f15e3714a")
    version("0.1.15", sha256="e596ee155804da31793af0ee8f0e93c5fe629e246cbdca87dcae741a1e1f1205")

    variant("viewer", default=False, description="Enable the interactive viewer (plaid[viewer])")

    # Build deps
    with default_args(type="build"):
        depends_on("py-setuptools@60:76.1.0")
        depends_on("py-setuptools-scm@8:")

    # Build and run deps
    with default_args(type=("build", "run")):
        depends_on("python@3.11:3.13")

    # Run deps
    with default_args(type="run"):
        depends_on("py-tqdm@4.60:4")
        depends_on("py-pyyaml@6")
        depends_on("py-pycgns@6.3:6")
        depends_on("py-zarr@3.1:3")
        depends_on("py-numpy@1.26:2")
        depends_on("py-pydantic@2.6:2")

        # datasets upper bound widened to <6 in 1.0.0
        depends_on("py-datasets@2.18:4", when="@0.1.15")
        depends_on("py-datasets@2.18:5", when="@1.0.0:")

        # only runtime deps in 0.1.15 (dev-only in 1.0.0)
        depends_on("py-scikit-learn@1.4:1", when="@0.1.15")
        depends_on("py-matplotlib@3.8:3", when="@0.1.15")

    # Optional viewer deps (plaid[viewer]), available since 1.0.0
    with default_args(type="run"):
        with when("+viewer @1.0.0:"):
            depends_on("py-trame@3.6:3")
            depends_on("py-trame-vtk@2.8:2")
            depends_on("py-trame-vuetify@2.7:3")
            depends_on("vtk@9.6.1:")
