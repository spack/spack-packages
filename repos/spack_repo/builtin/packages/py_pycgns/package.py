# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPycgns(PythonPackage):
    """PyCGNS package provides Python bindings for the CGNS library."""

    homepage = "https://github.com/pyCGNS/pyCGNS"

    pypi = "pyCGNS/pycgns-6.3.5.tar.gz"

    maintainers("williampiat3")

    license("LGPL-2.1-only")

    version(
        "6.3.5",
        sha256="0414362305e7831c5719ccedfbec2c477bd345a6ff426d2a0601de727c5d74c3",
    )

    # build dependencies
    with default_args(type="build"):
        depends_on("c")
        depends_on("py-meson-python@0.15:")
        depends_on("py-cython@3.0.6:")
        depends_on("pkgconfig")
    # run dependencies
    with default_args(type=("build", "run")):
        depends_on("python@3.10:")
        depends_on("py-numpy@2:")
        depends_on("hdf5~mpi+hl")

    def setup_build_environment(self, env):
        env.set("CC", self.compiler.cc)
