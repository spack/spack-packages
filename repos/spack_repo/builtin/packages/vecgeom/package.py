# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


def _std_when(values):
    for v in values:
        if isinstance(v, str):
            yield v, ""
            continue
        for c in v:
            yield c.value, c.when


class Vecgeom(CMakePackage, CudaPackage):
    """The vectorized geometry library for particle-detector simulation
    (toolkits)."""

    homepage = "https://gitlab.cern.ch/VecGeom/VecGeom"
    url = "https://gitlab.cern.ch/VecGeom/VecGeom/-/archive/v1.1.6/VecGeom-v1.1.6.tar.gz"
    git = "https://gitlab.cern.ch/VecGeom/VecGeom.git"

    tags = ["hep"]

    maintainers("drbenmorgan", "sethrj")

    version("master", branch="master", get_full_repo=True)
    version(
        "2.0.0",
        url="https://gitlab.cern.ch/-/project/981/uploads/d2ae816669e324d5828c16857b307372/VecGeom-v2.0.0.tar.gz",
        sha256="f5fb455b2a2a5f386e171a621d0e95908ab6269803c4b186861849e8c88e8350",
    )
    version(
        "2.0.0-rc.9",
        url="https://gitlab.cern.ch/-/project/981/uploads/4a8ba32606365d4be04455827ea32c51/VecGeom-v2.0.0-rc.9.tar.gz",
        sha256="cfc0cb86303c1dc475a5dde9022384e2034f789a0908feb007103c1e7cd9aa65",
        deprecated=True,
    )
    version(
        "2.0.0-rc.7",
        url="https://gitlab.cern.ch/-/project/981/uploads/f1017874e9d138165f221d4b854a39a4/VecGeom-v2.0.0-rc.7.tar.gz",
        sha256="f95eacd7154f7b41950161988465b5c086f80dade91dec8328085949c6f443a0",
        deprecated=True,
    )
    version(
        "1.2.11",
        url="https://gitlab.cern.ch/-/project/981/uploads/f2a483a4a073fac560714280e0e223ec/VecGeom-v1.2.11.tar.gz",
        sha256="0e251b0c6d79401e49cd2137a32b499ce3857045683d1fc8b6cd3b527247a3ef",
        preferred=True,
    )
    version(
        "1.2.10",
        url="https://gitlab.cern.ch/-/project/981/uploads/8e0a94013efdd1b2d4f44c3fbb10bcdf/VecGeom-v1.2.10.tar.gz",
        sha256="3e0934842694452e4cb4a265428cb99af1ecc45f0e2d28a32dfeaa0634c21e2a",
    )
    version("1.1.20", sha256="e1c75e480fc72bca8f8072ea00320878a9ae375eed7401628b15cddd097ed7fd")

    _cxxstd_values = (
        conditional("11", "14", when="@:1.1"),
        "17",
        conditional("20", when="@1.2:"),
        # Assuming versions not supporting C++20 do not support C++23
        conditional("23", when="@1.2:"),
    )
    variant(
        "cxxstd",
        default="17",
        values=_cxxstd_values,
        multi=False,
        description="Use the specified C++ standard when building",
    )
    variant("gdml", default=True, description="Support native GDML geometry descriptions")
    # TODO: delete geant4/root variants since they don't affect the build
    variant(
        "geant4", default=False, when="@:1", description="Support Geant4 geometry construction"
    )
    variant("root", default=False, when="@:1", description="Support ROOT geometry construction")
    variant("shared", default=True, description="Build shared libraries")
    variant(
        "surface", default=False, when="@2:", description="Support surface frame representation"
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("veccore")
    depends_on("veccore@0.8.1:", when="+cuda")
    depends_on("veccore@0.8.0:0.8", when="@1.1.18:")

    conflicts("+cuda", when="@:1.1.5")

    # Fix empty -Xcompiler= with nvcc
    patch(
        "https://gitlab.cern.ch/VecGeom/VecGeom/-/commit/0bf9b675ab70eb5cb9409ff73c1152fd1326dbf4.diff",
        sha256="f172b0a9ee1de4931b106d8500d1a60d5688c9bce324cf12ca107ec866a16c56",
        when="@1.2.7:1.2.10 +cuda ^cuda@:11",
    )
    # Fix -Wmissing-template-arg-list-after-template-kw
    patch(
        "https://gitlab.cern.ch/VecGeom/VecGeom/-/merge_requests/1251.diff",
        sha256="b9419c6666389b69ee2c9125d10f25b423fce339495413ac4762ae6f32bdea63",
        when="@:1.2.10 ^apple-clang@17:",
    )

    for _std, _when in _std_when(_cxxstd_values):
        depends_on(f"geant4 cxxstd={_std}", when=f"{_when} +geant4 cxxstd={_std}")
        depends_on(f"root cxxstd={_std}", when=f"{_when} +root cxxstd={_std}")
        depends_on(f"xerces-c cxxstd={_std}", when=f"{_when} +gdml cxxstd={_std}")

    def cmake_args(self):
        spec = self.spec
        define = self.define
        from_variant = self.define_from_variant

        target_instructions = "empty"
        if "~cuda" in spec:
            # Only add vectorization if CUDA is disabled due to nvcc flag
            # forwarding issues
            vecgeom_arch = "sse2 sse3 ssse3 sse4.1 sse4.2 avx avx2".split()
            for feature in reversed(vecgeom_arch):
                if feature.replace(".", "_") in spec.target:
                    target_instructions = feature
                    break

        prefix = "VECGEOM_" if spec.satisfies("@1.2:") else ""
        args = [
            define(prefix + "BACKEND", "Scalar"),
            define(prefix + "BUILTIN_VECCORE", False),
            define(prefix + "NO_SPECIALIZATION", True),
            define("VECGEOM_VECTOR", target_instructions),
            from_variant("BUILD_SHARED_LIBS", "shared"),
            from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            from_variant(prefix + "GDML", "gdml"),
            from_variant(prefix + "GEANT4", "geant4"),
            from_variant(prefix + "ROOT", "root"),
        ]

        if spec.satisfies("@1.1.19:"):
            args.append(from_variant("VECGEOM_ENABLE_CUDA", "cuda"))
            if "+cuda" in spec:
                # This will add an (ignored) empty string if no values are
                # selected, otherwise will add a CMake list of arch values
                args.append(define("CMAKE_CUDA_ARCHITECTURES", spec.variants["cuda_arch"].value))
        else:
            args.append(from_variant("CUDA"))
            if "+cuda" in spec:
                arch = spec.variants["cuda_arch"].value
                if len(arch) != 1:
                    raise InstallError("Exactly one cuda_arch must be specified")
                args.append(define("CUDA_ARCH", arch[0]))

        args.append(from_variant("VECGEOM_USE_SURF", "surface"))

        # Set testing flags
        build_tests = self.run_tests
        args.append(define("BUILD_TESTING", build_tests))
        if spec.satisfies("@:1.1"):
            args.extend(
                [
                    define("CTEST", build_tests),
                    define("GDMLTESTING", build_tests and "+gdml" in spec),
                ]
            )

        return args
