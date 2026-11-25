from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Libri(Package, CudaPackage):
    """Header-only resolution-of-identity library."""

    homepage = "https://github.com/deepmodeling/LibRI"
    url = "https://github.com/abacusmodeling/LibRI/archive/refs/tags/v0.3.0.0.tar.gz"
    git = "https://github.com/abacusmodeling/LibRI.git"

    maintainers("Growl1234")

    license("LGPL-3.0-only", checked_by="Growl1234")

    version("master", branch="master")
    version("0.3.0.0", sha256="c6910c2cef38dbb93df59576e332b8f28a9f624db1dc46e3d374004ecfdca193")
    # Retain the snapshot for existing environments.
    version("0.2.1.2-202609", commit="6ce3c8480ae38a085746dc81cc4dbb59b8074430")
    version("0.2.1.1", sha256="cd33fd5428400ea696b82c9132878c07bf785847b3f56b1979e25a3a5fc0b311")

    depends_on("mpi")
    depends_on("blas")
    depends_on("lapack")
    depends_on("cereal")
    depends_on("libcomm")

    depends_on("libddla@0.0.7: +cuda", when="+cuda")
    conflicts("+cuda", when="@:0.2", msg="The DDLA GPU backend requires LibRI 0.3.0.0 or newer")
    conflicts("cuda_arch=none", when="+cuda", msg="Specify the CUDA architecture for LibDDLA")
    for arch in CudaPackage.cuda_arch_values:
        depends_on(f"libddla cuda_arch={arch}", when=f"+cuda cuda_arch={arch}")

    def install(self, spec, prefix):
        install_tree("include", prefix.include)

        # Export usage requirements on an opt-in target, without changing a
        # dependent package's global compiler or linker flags.
        config_dir = join_path(prefix.lib, "cmake", "LibRI")
        mkdirp(config_dir)
        includes = [
            "${CMAKE_CURRENT_LIST_DIR}/../../../include",
            str(spec["libcomm"].prefix.include),
            str(spec["cereal"].prefix.include),
        ]
        math_libs = spec["lapack"].libs + spec["blas"].libs
        config = [
            "include(CMakeFindDependencyMacro)",
            "find_dependency(MPI COMPONENTS CXX)",
            "find_dependency(OpenMP COMPONENTS CXX)",
        ]
        if "+cuda" in spec:
            config.append(
                'find_dependency(LibDDLA 0.0.7 CONFIG PATHS "{0}" NO_DEFAULT_PATH)'.format(
                    spec["libddla"].prefix
                )
            )
        config += [
            "if(NOT TARGET LibRI::LibRI)",
            "  add_library(LibRI::LibRI INTERFACE IMPORTED)",
            "  set_target_properties(LibRI::LibRI PROPERTIES",
            '    INTERFACE_INCLUDE_DIRECTORIES "{0}"'.format(";".join(includes)),
            '    INTERFACE_COMPILE_FEATURES "cxx_std_14"',
            '    INTERFACE_LINK_LIBRARIES "MPI::MPI_CXX;OpenMP::OpenMP_CXX;{0}")'.format(
                ";".join(math_libs)
            ),
        ]
        if "+cuda" in spec:
            config += [
                "  target_compile_definitions(LibRI::LibRI INTERFACE __GPU_RI __DDLA_RI)",
                "  target_link_libraries(LibRI::LibRI INTERFACE ddla::ddla)",
            ]
        config.append("endif()")
        with open(join_path(config_dir, "LibRIConfig.cmake"), "w") as stream:
            stream.write("\n".join(config) + "\n")
