# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAtb(PythonPackage):
    """Python ab initio tight-binding simulation package."""

    homepage = "https://pyatb.github.io/pyatb/"
    git = "https://github.com/pyatb/pyatb.git"

    maintainers("Growl1234")

    license("GPL-3.0-only", checked_by="RMeli")

    version("main", branch="main")
    version("1.1.2", commit="1b35d9f1f5ee1e6aa8b24c5ccf3c92bd19d32e36")

    depends_on("cxx", type="build")

    with default_args(type="build"):
        depends_on("py-setuptools@42:")
        depends_on("py-pybind11")
        depends_on("eigen")

    # pyATB directly uses the BLAS/LAPACK/LAPACKE interfaces provided by
    # OpenBLAS. Keep the ABI at the LP64, unsuffixed interface expected by
    # the current pyATB sources.
    depends_on(
        "openblas~ilp64 symbol_suffix=none",
        type=("build", "link"),
    )

    with default_args(type=("build", "run")):
        depends_on("py-numpy@1.17:")
        depends_on("py-scipy@1.5:")
        depends_on("py-mpi4py@3.1:")
        depends_on("py-matplotlib@2.2.2:")
        depends_on("py-ase")

    def patch(self):
        # Use Spack's Eigen instead of the bundled git submodule.
        filter_file(
            'os.path.join("eigen"),',
            '"{0}",'.format(self.spec["eigen"].prefix.include.eigen3),
            "setup.py",
            string=True,
        )

        # OpenBLAS provides BLAS, LAPACK, and LAPACKE in libopenblas, so do
        # not pull in a second, potentially ABI-incompatible LAPACK library.
        filter_file(
            "libraries = ['openblas', 'lapacke']",
            "libraries = ['openblas']",
            "setup.py",
            string=True,
        )

        # Use the OpenMP option appropriate for the selected compiler.
        openmp_flag = self.compiler.openmp_flag
        filter_file(
            "extra_compile_args = ['-fopenmp']",
            "extra_compile_args = [{0!r}]".format(openmp_flag),
            "setup.py",
            string=True,
        )
        filter_file(
            "extra_link_args = ['-lgomp']",
            "extra_link_args = [{0!r}]".format(openmp_flag),
            "setup.py",
            string=True,
        )
