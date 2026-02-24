# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyZfitPhysics(PythonPackage):
    """Tools and models to extend zfit with physics specific content."""

    homepage = "https://github.com/zfit/zfit-physics"
    pypi = "zfit-physics/zfit_physics-0.7.0.tar.gz"

    maintainers("jonas-eschle", "ikrommyd")
    license("BSD-3-Clause", checked_by="jonas-eschle")

    tags = ["likelihood", "statistics", "inference", "fitting", "hep"]

    version("0.9.0", sha256="e59b64ead1c92ca43efc4852b40ba345828ff91f47a1e5c0e519c1f27f40c3d4")
    version("0.8.1", sha256="8e2c2549665798d806c789943f3cf8a82cf2f93b178e93dbd302bb642fa0fff7")
    version("0.7.0", sha256="5d65becff7265a12d9b62a8476c5359e75ec10d6ac0fd84dfa39eb82b6693cda")

    depends_on("py-hatchling@1.17.1:", type="build", when="@0.8:")
    depends_on("py-hatch-vcs", type="build", when="@0.8:")

    depends_on("py-setuptools@42:", type="build", when="@:0.7")
    depends_on("py-setuptools-scm@3.4:+toml", type="build", when="@:0.7")
    depends_on("py-setuptools-scm-git-archive", type="build", when="@:0.7")

    # TODO: remove "build" once fixed in spack that tests need "run", not "build"
    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@0.8:")
        depends_on("python@3.9:", when="@0.7:")
        depends_on("py-zfit@0.20:", when="@0.7:")
