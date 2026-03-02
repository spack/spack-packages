# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFenicsUfl(PythonPackage):
    """The Unified Form Language (UFL) is a domain specific language for
    declaration of finite element discretizations of variational forms. More
    precisely, it defines a flexible interface for choosing finite element
    spaces and defining expressions for weak forms in a notation close to
    mathematical notation."""

    homepage = "https://fenicsproject.org/"
    url = "https://github.com/FEniCS/ufl/archive/2019.1.0.tar.gz"
    git = "https://github.com/FEniCS/ufl.git"
    maintainers("chrisrichardson", "garth-wells", "jhale")

    license("LGPL-3.0-or-later")

    version("main", branch="main", no_cache=True)
    version(
        "2025.2.0.post0", sha256="2182fed6d0fc41fd97244d73fe6aa95e50725e5ba8fe1b3b0f3f4d0215b45534"
    )
    version("2025.1.0", sha256="a3aedb6fd06bb43e954c96e7cccc190a29dc9a00287f95bc365dbfc81b43a5f9")
    version("2024.2.0", sha256="d9353d23ccbdd9887f8d6edab74c04fe06d818da972072081dbf0c25bc86f5a7")
    version(
        "2024.1.0.post1", sha256="6e38e93a2c8417271c9fb316e0d0ea5fe1101c6a37b2496fff8290e7ea7ead74"
    )

    depends_on("python@3.10:", when="@2025.2.0:", type=("build", "run"))
    depends_on("python@3.9:", when="@2025.1.0:", type=("build", "run"))
    depends_on("python@3.8:", when="@2023.2.0:", type=("build", "run"))

    depends_on("py-setuptools@77:", when="@2025.1.0:", type="build")
    depends_on("py-setuptools@62:", when="@2023.2.0:", type="build")
    depends_on("py-setuptools@58:", when="@2022.1.0:2023.1.1.post0", type="build")
    depends_on("py-setuptools@40:", when="@2016.2.0:2021.1.0", type="build")
    depends_on("py-numpy", type=("build", "run"))

    depends_on("py-pytest", type="test")

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def check_build(self):
        with working_dir(self.stage.source_path):
            python("-m", "pytest")
