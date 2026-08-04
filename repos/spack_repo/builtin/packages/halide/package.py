# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cmake import CMakePackage, generator
from spack_repo.builtin.build_systems.python import PythonExtension

from spack.package import *


class Halide(CMakePackage, PythonExtension):
    """Halide is a programming language designed to make it easier to write
    high-performance image and array processing code on modern machines."""

    homepage = "https://halide-lang.org/"
    url = "https://github.com/halide/Halide/archive/refs/tags/v14.0.0.tar.gz"
    git = "https://github.com/halide/Halide.git"

    license("MIT")

    maintainers("wraith1995", "alexreinking")
    version("main", branch="main")
    version("21.0.0", sha256="aa6b6f5e89709ca6bc754ce72b8b13b2abce0d6b001cb2516b1c6f518f910141")
    version("19.0.0", sha256="83bae1f0e24dc44d9d85014d5cd0474df2dd03975680894ce3fafd6e97dffee2")
    version("18.0.0", sha256="1176b42a3e2374ab38555d9316c78e39b157044b5a8e765c748bf3afd2edb351")
    version("17.0.2", sha256="5f3a43ba27b47d3dcbcee963faabf1d633d4151031e60b6ff7cc62472e5677a0")
    version("17.0.1", sha256="beb18331d9e4b6f69943bcc75fb9d923a250ae689f09f6940a01636243289727")
    version("17.0.0", sha256="7e5a526b4074887b528d25b0265ddfa92c0a6d8bfdfbbba536313ecddf352da3")
    version("16.0.0", sha256="a0cccee762681ea697124b8172dd65595856d0fa5bd4d1af7933046b4a085b04")
    version("15.0.0", sha256="6680424f80c5731a85d977c06327096afe5af31da3667e91d4d36a25fabdda15")
    version("14.0.0", sha256="f9fc9765217cbd10e3a3e3883a60fc8f2dbbeaac634b45c789577a8a87999a01")

    # Halide 20.0.0 was intentionally skipped by upstream so that the Halide
    # major version tracks the LLVM major version it is built against.

    variant(
        "build_type",
        default="Release",
        description="The build type to build",
        values=("Release", "Debug", "RelWithDebInfo"),
    )
    generator("ninja")
    variant("python", default=False, description="Install python bindings")
    variant("tutorials", default=False, description="Install the Halide Tutorials.")
    variant("utils", default=False, description="Install the Halide Utilities.")
    variant("tests", default=False, description="Build and Run Halide Tests and Apps.")
    # The non-LLVM runtime backends below are only configurable on Halide 18 and
    # earlier. Halide 19 onward always builds every runtime backend, so these
    # variants have no effect there.
    variant("opencl", default=False, description="Build Non-llvm based OpenCl-C backend.")
    variant("metal", default=False, description="Build Non-llvm based Metal backend.")
    variant(
        "d3d12", default=False, description="Build Non-llvm based Direct3D 12 Compute backend."
    )
    # Features introduced by the reworked Halide 19 CMake build system.
    variant(
        "autoschedulers", default=True, description="Build the Halide autoschedulers.", when="@19:"
    )
    variant(
        "serialization",
        default=True,
        description="Build the experimental serialization/deserialization support.",
        when="@19:",
    )
    variant(
        "docs",
        default=False,
        description="Build and install the Halide documentation.",
        when="@19:",
    )
    extends("python", when="+python")
    _values = (
        "aarch64",
        "amdgpu",
        "arm",
        "hexagon",
        "nvptx",
        "powerpc",
        "riscv",
        "webassembly",
        "x86",
    )
    variant(
        "targets",
        default="arm,x86,nvptx,aarch64,hexagon,webassembly",
        description=("What targets to build. Spack's target family is always added "),
        values=_values,
        multi=True,
    )
    variant("sharedllvm", default=False, description="Link to the shared version of LLVM.")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.22:", type="build", when="@:18")
    depends_on("cmake@3.28:", type="build", when="@19:")
    depends_on("llvm+clang+lld build_type=Release", type=("link", "run"))
    depends_on("llvm@14.0.0:14", type=("link", "run"), when="@14.0.0:14")
    depends_on("llvm@15.0.0:15", type=("link", "run"), when="@15.0.0:15")
    depends_on("llvm@16.0.0:16", type=("link", "run"), when="@16.0.0:16")
    depends_on("llvm@17.0.0:17", type=("link", "run"), when="@17.0.0:17")
    depends_on("llvm@17.0.0:18", type=("link", "run"), when="@18.0.0:18")
    depends_on("llvm@19.0.0:19", type=("link", "run"), when="@19.0.0:19")
    depends_on("llvm@21.0.0:21", type=("link", "run"), when="@21.0.0:21")

    for v in _values:
        depends_on(
            "llvm targets={0}".format(v), type=("link", "run"), when="targets={0}".format(v)
        )
    depends_on("llvm+llvm_dylib", type=("link", "run"), when="+sharedllvm")

    depends_on("libjpeg", type=("build", "link", "run"))
    depends_on("libpng", type=("build", "link", "run"))

    # Halide 19+ serialization uses FlatBuffers. Upstream bundles FlatBuffers
    # 23.5.26 via FetchContent; provide it from Spack instead (see cmake_args).
    # Halide links the static `flatbuffers::flatbuffers` target, which is only
    # produced by the ~shared build of FlatBuffers.
    depends_on("flatbuffers@23.5.26:~shared", type="build", when="@19:+serialization")

    depends_on("doxygen", type="build", when="+docs")

    depends_on("python@3.8:", type=("build", "link", "run"), when="+python")
    depends_on("python@3.9:", type=("build", "link", "run"), when="@21:+python")
    # See https://github.com/halide/Halide/blob/main/requirements.txt
    depends_on("py-pybind11@2.6.2", type="build", when="@14.0.0:17+python")
    depends_on("py-pybind11@2.10.4", type="build", when="@18.0.0:19+python")
    depends_on("py-pybind11@2.11.1:", type="build", when="@21:+python")
    depends_on("py-setuptools@43:", type="build", when="+python")
    depends_on("py-scikit-build", type="build", when="@:18+python")
    depends_on("py-wheel", type="build", when="+python")

    depends_on("py-imageio", type=("build", "run"), when="+python")
    depends_on("pil", type=("build", "run"), when="+python")
    depends_on("py-scipy", type=("build", "run"), when="+python")
    depends_on("py-numpy", type=("build", "run"), when="+python")

    @property
    def libs(self):
        return find_libraries("libHalide", root=self.prefix, recursive=True)

    def cmake_args(self):
        # See https://github.com/halide/Halide/blob/main/doc/BuildingHalideWithCMake.md
        spec = self.spec
        llvm_config = Executable(spec["llvm"].prefix.bin.join("llvm-config"))
        llvmdir = llvm_config("--cmakedir", output=str).strip()
        args = [
            self.define("LLVM_DIR", llvmdir),
            self.define_from_variant("WITH_TESTS", "tests"),
            self.define_from_variant("WITH_TUTORIALS", "tutorials"),
            self.define_from_variant("WITH_UTILS", "utils"),
            self.define_from_variant("WITH_PYTHON_BINDINGS", "python"),
        ]
        if spec.satisfies("@19:"):
            # Halide 19 reworked the CMake build: build-time dependencies are
            # pulled in through FetchContent by default and several options were
            # renamed. Spack builds offline, so disable FetchContent and supply
            # FlatBuffers/pybind11 through find_package (i.e. from Spack).
            args += [
                self.define("Halide_USE_FETCHCONTENT", False),
                # The in-process WebAssembly JIT executor (wabt) is fetched via
                # FetchContent upstream. Disable it; ahead-of-time codegen to the
                # wasm target still works through LLVM/LLD. This replaces the old
                # WITH_WABT option removed after Halide 18.
                self.define("Halide_WASM_BACKEND", "OFF"),
                self.define_from_variant("Halide_LLVM_SHARED_LIBS", "sharedllvm"),
                self.define_from_variant("WITH_AUTOSCHEDULERS", "autoschedulers"),
                self.define_from_variant("WITH_SERIALIZATION", "serialization"),
                self.define_from_variant("WITH_DOCS", "docs"),
            ]
        else:
            args += [
                self.define_from_variant("Halide_SHARED_LLVM", "sharedllvm"),
                self.define("WITH_WABT", False),
                self.define_from_variant("TARGET_OPENCL", "opencl"),
                self.define_from_variant("TARGET_METAL", "metal"),
                self.define_from_variant("TARGET_D3D12COMPUTE", "d3d12"),
            ]
            # Halide 18 and earlier selected codegen backends explicitly via
            # TARGET_<ARCH>. Halide 19+ always builds every codegen backend that
            # the linked LLVM supports, so this is only needed for old releases.
            llvm_targets = get_llvm_targets_to_build(spec)
            for target in llvm_targets:
                args += [self.define("TARGET_{0}".format(target[0]), target[1])]

        if spec.satisfies("+python"):
            args += [self.define("Halide_INSTALL_PYTHONDIR", python_platlib)]
            if spec.satisfies("@:18"):
                args += [self.define("PYBIND11_USE_FETCHCONTENT", False)]
        return args


def get_llvm_targets_to_build(spec):
    targets = spec.variants["targets"].value
    llvm_targets = set()
    # Convert targets variant values to CMake LLVM_TARGETS_TO_BUILD array.
    spack_to_cmake = {
        "aarch64": "AARCH64",
        "amdgpu": "AMDGPU",
        "arm": "ARM",
        "hexagon": "HEXAGON",
        "nvptx": "NVPTX",
        "powerpc": "POWERPC",
        "riscv": "RISCV",
        "webassembly": "WEBASSEMBLY",
        "x86": "X86",
    }
    for t in targets:
        llvm_targets.add((spack_to_cmake[t], True))

    if spec.target.family in ("x86", "x86_64"):
        llvm_targets.add(("X86", True))
    elif spec.target.family == "arm":
        llvm_targets.add(("ARM", True))
    elif spec.target.family == "aarch64":
        llvm_targets.add(("AARCH64", True))
    elif spec.target.family in ("ppc64", "ppc64le", "ppc", "ppcle"):
        llvm_targets.add(("POWERPC", True))

    # for everything not represented, we add False
    for v in spack_to_cmake.values():
        if (v, True) not in llvm_targets:
            llvm_targets.add((v, False))

    return list(llvm_targets)
