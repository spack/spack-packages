# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator

from spack.package import *


class Shamrock(CMakePackage):
    """The Shamrock exascale framework for astrophysics"""

    homepage = "https://shamrock-code.github.io/"
    url = "https://github.com/Shamrock-code/Shamrock/releases/download/v2025.10.0/shamrock-2025.10.0.tar"
    git = "https://github.com/Shamrock-code/Shamrock.git"

    maintainers("tdavidcl")

    license("CeCILL Free Software License Agreement v2.1", checked_by="tdavidcl")

    version("main", branch="main", submodules=True)

    version("2025.05.0", sha256="59d5652467fd9453a65ae7b48e0c9b7d4162edc8df92e09d08dcc5275407a897")
    version("2025.10.0", sha256="72683352d862d7b3d39568151a17ea78633bd4976a40eacb77098d3ef0ca3c55")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    variant("shared", default=True, description="Enables the build of shared libraries")
    variant("testing", default=True, description="Enables the build of tests")
    variant("pybindings", default=True, description="Install python bindings")

    generator("ninja")

    depends_on("sycl")
    requires(
        "^[virtuals=sycl] intel-oneapi",
        "^[virtuals=sycl] hipsycl",
        policy="one_of",
        msg="sycl provider must be one of intel-oneapi or hipsycl",
    )

    depends_on("mpi")
    depends_on("python")

    extends("python", when="+pybindings")

    def cmake_args(self):
        spec = self.spec

        args = [
            self.define("SHAMROCK_ENABLE_BACKEND", "SYCL"),
            self.define("PYTHON_EXECUTABLE", spec["python"].command.path),
            self.define_from_variant("BUILD_TEST", "testing"),
        ]

        # switch based on SYCL provider
        sycl_spec = self.spec["sycl"]
        if sycl_spec.satisfies("intel-oneapi"):
            args += [
                self.define("SYCL_IMPLEMENTATION", "IntelLLVM"),
                self.define("CMAKE_CXX_COMPILER", "icpx"),
                self.define("INTEL_LLVM_PATH", self.spec["intel-oneapi"].prefix),
            ]
        elif sycl_spec.satisfies("hipsycl"):
            args += [self.define("SYCL_IMPLEMENTATION", "ACPPDirect")]

            if sycl_spec.satisfies("hipsycl@:0.9.4"):
                args += [self.define("CMAKE_CXX_COMPILER", "syclcc")]
            else:
                args += [self.define("CMAKE_CXX_COMPILER", "acpp")]

            args += [self.define("ACPP_PATH", self.spec["hipsycl"].prefix)]

        if self.spec.satisfies("+pybindings"):
            py_libdir = join_path(
                self.prefix.lib, f"python{spec['python'].version.up_to(2)}", "site-packages"
            )
            args.append(self.define("CMAKE_INSTALL_PYTHONDIR", py_libdir))

        return args

    def test_install(self):
        """Test the install (executable, python bindings)"""

        shamrock = Executable(self.prefix.bin.shamrock)

        shamrock("--help")
        shamrock("--smi")
        shamrock("--smi", "--sycl-cfg", "0:0")

        python(
            "-c",
            "import shamrock;"
            "shamrock.change_loglevel(125);"
            "shamrock.sys.init('0:0');"
            "shamrock.sys.close()",
        )
