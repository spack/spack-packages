# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import os

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyStatsmodels(PythonPackage):
    """Statistical computations and models for use with SciPy"""

    homepage = "https://www.statsmodels.org"
    pypi = "statsmodels/statsmodels-0.8.0.tar.gz"
    git = "https://github.com/statsmodels/statsmodels.git"

    maintainers("climbfuji")

    license("BSD-3-Clause")

    version("0.14.5", sha256="de260e58cccfd2ceddf835b55a357233d6ca853a1aa4f90f7553a52cc71c6ddf")
    version("0.14.1", sha256="2260efdc1ef89f39c670a0bd8151b1d0843567781bcafec6cda0534eb47a94f6")

    depends_on("c", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("python@3.9:", when="@0.14.2:", type=("build", "link", "run"))
    depends_on("python@3.8:", type=("build", "link", "run"))

    depends_on("py-setuptools@69.0.2:", when="@0.14.1:", type="build")
    depends_on("py-setuptools@69.0.2:", when="@0.14.1 ^python@3.12:", type="build")
    depends_on("py-setuptools@63.4.3:", when="@0.14.1", type="build")
    depends_on("py-cython@3.0.10:3", when="@0.14.2:", type="build")
    depends_on("py-cython@0.29.33:3", when="@0.14.1", type="build")
    depends_on("py-setuptools-scm+toml@8", when="@0.14.1:", type="build")

    # patsy@0.5.1 works around a Python change
    #    https://github.com/statsmodels/statsmodels/issues/5343 and
    #    https://github.com/pydata/patsy/pull/131

    # requirements.txt
    depends_on("py-numpy@1.22.3:2", when="@0.14.3:", type=("build", "link", "run"))
    depends_on("py-numpy@1.22.3:1", when="@0.14.1", type=("build", "link", "run"))
    depends_on("py-scipy@1.8:", when="@0.14.2:", type=("build", "run"))
    depends_on("py-scipy@1.4:", when="@0.13.5:0.14.1", type=("build", "run"))
    depends_on("py-pandas@1.4:", when="@0.14:", type=("build", "run"))
    depends_on("py-pandas@1:", when="@0.14:", type=("build", "run"))
    depends_on("py-pandas@0.25:", when="@0.13:", type=("build", "run"))
    depends_on("py-patsy@0.5.6:", when="@0.14.2:", type=("build", "run"))
    depends_on("py-patsy@0.5.4:", when="@0.14.1", type=("build", "run"))
    depends_on("py-packaging@21.3:", when="@0.13.2:", type=("build", "run"))

    conflicts("^py-scipy@1.9.2")
    conflicts("^py-pandas@2.1.0")

    depends_on("py-pytest", type="test")

    @run_before("install")
    def remove_generated_sources(self):
        # Automatic recythonization doesn't work here, because cythonize is called
        # with force=False by default, so remove generated C files manually.
        for f in find(".", "*.c"):
            os.unlink(f)

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def build_test(self):
        dirs = glob.glob("build/lib*")  # There can be only one...
        with working_dir(dirs[0]):
            pytest = which("pytest", required=True)
            pytest("statsmodels")
