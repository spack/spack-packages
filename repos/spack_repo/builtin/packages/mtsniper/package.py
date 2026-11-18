# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Mtsniper(CMakePackage):
    """Multithreaded event-processing extension of the SNiPER framework.

    MtSNiPER provides a task scheduler and shared event buffers for running
    SNiPER algorithms concurrently using Intel TBB.
    """

    homepage = "https://github.com/SNiPER-Framework/mt.sniper"
    git = "https://github.com/SNiPER-Framework/mt.sniper.git"

    maintainers("guangzhuangzhao")

    license("LGPL-3.0-or-later", checked_by="guangzhuangzhao")

    version("0.9.1", commit="8f6ae172ebb604a134447732263a9c4fa551b437")

    variant(
        "cxxstd",
        default="17",
        values=("17", "20"),
        multi=False,
        description="C++ language standard",
    )

    depends_on("cxx", type="build")
    depends_on("cmake@3.12:", type="build")
    depends_on("sniper@2.1:2 +python +root", type=("build", "link", "run"))
    depends_on("python@3:", type=("build", "link", "run"))
    depends_on("boost@1.67:+python")
    depends_on("root")

    # The released scheduler uses tbb::task, which is absent from oneTBB.
    depends_on("intel-tbb@=2020.3 build_system=makefile +shared")

    for std in ("17", "20"):
        depends_on(f"sniper cxxstd={std}", when=f"cxxstd={std}")
        depends_on(f"root cxxstd={std}", when=f"cxxstd={std}")

    # C++20 disallows template-ids in destructor declarators.
    patch("cxx20-template-destructors.patch", when="@0.9.1 cxxstd=20")

    def cmake_args(self):
        return [
            self.define("BUILDIN_TBB", False),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define("Python3_EXECUTABLE", self.spec["python"].command.path),
            self.define("USE_PYTHON2", False),
        ]

    @run_after("install")
    def expose_muster_library(self):
        # C++ clients and the Python extension must load the same shared object
        # to avoid registering the same SNiPER classes twice.
        source = join_path(self.prefix.python, "SniperMuster", "libSniperMuster.so")
        if not os.path.isfile(source):
            raise InstallError("Missing installed libSniperMuster.so")
        mkdirp(self.prefix.lib)
        symlink(
            os.path.relpath(source, self.prefix.lib),
            join_path(self.prefix.lib, "libSniperMuster.so"),
        )

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def test_muster(self):
        """Check both library entry points and run a bounded two-worker job."""
        run_env = EnvironmentModifications()
        self.spec["sniper"].package.setup_run_environment(run_env)
        self.setup_run_environment(run_env)

        python = Executable(self.spec["python"].command.path)
        python.add_default_envmod(run_env)
        python(
            "-c",
            f"""
import ctypes
import os
import Sniper

library = {str(self.prefix.lib)!r} + "/libSniperMuster.so"
extension = {str(self.prefix.python)!r} + "/SniperMuster/libSniperMuster.so"
if not os.path.islink(library) or not os.path.samefile(library, extension):
    raise RuntimeError("The C++ and Python library paths must resolve to the same file")
ctypes.CDLL(library)
import SniperMuster
import MtIOExample

def worker():
    return SniperMuster.createWorker("Task")

muster = SniperMuster.Muster()
muster.setEvtMax(4)
if not muster.config(worker, 2) or not muster.run():
    raise RuntimeError("The MtSNiPER scheduler smoke test failed")
print("PASS: shared-library identity, Python import, and two-worker scheduler")
""",
        )

    def setup_run_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        env.prepend_path("PYTHONPATH", self.prefix.python)
