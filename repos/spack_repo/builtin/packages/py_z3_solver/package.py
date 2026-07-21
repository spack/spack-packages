# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyZ3Solver(PythonPackage):
    """Z3 is a theorem prover from Microsoft Research. It is licensed under the MIT license."""

    homepage = "https://github.com/Z3Prover/z3"
    pypi = "z3-solver/z3-solver-4.12.3.0.tar.gz"

    license("MIT")

    version("4.13.0.0", sha256="52588e92aec7cb338fd6288ce93758ae01770f62ca0c80e8f4f2b2333feaf51b")
    version("4.12.3.0", sha256="b6719daf9676711a8f1c708af0ea185578b0f22a3cb9bf9a55735e21691dc38d")

    depends_on("cxx", type="build")  # generated

    depends_on("py-setuptools@46.4:", type="build")
    # https://github.com/Z3Prover/z3/blob/z3-4.12.3/CMakeLists.txt#L2
    depends_on("cmake@3.16:", type="build")
