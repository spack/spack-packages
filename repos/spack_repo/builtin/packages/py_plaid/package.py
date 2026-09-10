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

    version("0.1.15", sha256="e596ee155804da31793af0ee8f0e93c5fe629e246cbdca87dcae741a1e1f1205")

    # Build deps
    with default_args(type="build"):
        depends_on("py-setuptools@60:76.1.0")
        depends_on("py-setuptools-scm@8:")

    # Build and run deps
    with default_args(type=("build", "run")):
        depends_on("python@3.11:3.13")

    # Run deps
    with default_args(type=("run")):
        depends_on("py-tqdm@4.60:4")
        depends_on("py-pyyaml@6")
        depends_on("py-pycgns@6.3:6")
        depends_on("py-zarr@3.1:3")
        depends_on("py-scikit-learn@1.4:1")
        depends_on("py-datasets@2.18:4")
        depends_on("py-numpy@1.26:2")
        depends_on("py-matplotlib@3.8:3")
        depends_on("py-pydantic@2.6:2")
