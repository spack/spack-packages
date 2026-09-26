# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTorchvision(PythonPackage):
    """Image and video datasets and models for torch deep learning."""

    homepage = "https://github.com/pytorch/vision"
    url = "https://github.com/pytorch/vision/archive/v0.8.2.tar.gz"
    git = "https://github.com/pytorch/vision.git"

    maintainers("adamjstewart")

    license("BSD-3-Clause")

    version("main", branch="main")
    version("0.29.0", sha256="24be57d922927d8a2ac2e8f076f07c3447ddf8f1d25ddbb7b65578f36c9ab8e3")
    version("0.28.0", sha256="ecc4451241c8eeadc0c88213bd65c7932c9622d1d0034254b938f25362283ee9")
    version("0.27.1", sha256="705d5ab7d01af9ece3bfbb1486eed3c23a2f68414fcc9c9a88910fb3c018c3db")
    version("0.27.0", sha256="04c588d80e63903e1e4444db8a1c32dc56e4080ed48782555e1d00752d6edb17")
    version("0.26.0", sha256="fb95b6b78b3801c4d4d6332f7a5a0b6c624588e1b39e0d6fa145227b0c749403")
    version("0.25.0", sha256="a7ac1b3ab489d71f6e27edfad1e27616e4b8a9b1517e60fce4a950600d3510e8")

    desc = "Enable support for native encoding/decoding of {} formats in torchvision.io"
    variant("png", default=True, description=desc.format("PNG"))
    variant("jpeg", default=True, description=desc.format("JPEG"))
    variant("webp", default=False, description=desc.format("WEBP"))
    variant("nvjpeg", default=False, description=desc.format("NVJPEG"))
    variant("video_codec", default=False, description=desc.format("video_codec"), when="@:0.25")
    variant("ffmpeg", default=False, description=desc.format("FFMPEG"), when="@:0.25")

    # torchvision does not yet support disabling giflib:
    # https://github.com/pytorch/vision/pull/8406#discussion_r1590926939
    # variant("gif", default=False, description=desc.format("GIF"))

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type=("build", "link", "run")):
        # Based on PyPI wheel availability
        depends_on("python@3.10:3.15", when="@0.28:")
        depends_on("python@3.10:3.14", when="@:0.27")

        # https://github.com/pytorch/vision#installation
        depends_on("py-torch@main", when="@main")
        depends_on("py-torch@2.14.0:", when="@0.29.0:")
        depends_on("py-torch@2.13.0", when="@0.28.0")
        depends_on("py-torch@2.12.1", when="@0.27.1")
        depends_on("py-torch@2.12.0", when="@0.27.0")
        depends_on("py-torch@2.11.0", when="@0.26.0")
        depends_on("py-torch@2.10.0", when="@0.25.0")

    depends_on("ninja", type="build")

    # setup.py
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("pil@5.3:", type=("build", "run"))

    # Extensions
    depends_on("libpng@1.6:", when="+png")
    depends_on("jpeg", when="+jpeg")
    depends_on("libwebp", when="+webp")
    depends_on("cuda", when="+nvjpeg")
    depends_on("cuda", when="+video_codec")
    depends_on("ffmpeg@3.1:", when="+ffmpeg")

    # torchvision does not yet support externally-installed giflib:
    # https://github.com/pytorch/vision/pull/8406#discussion_r1590926939
    # depends_on("giflib", when="+gif")

    # https://github.com/pytorch/vision/issues/9307
    conflicts("^python@3.14.1")
    # https://github.com/pytorch/vision/issues/4146
    # https://github.com/pytorch/vision/issues/4934
    conflicts("^pil@8.3")
    # https://github.com/pytorch/pytorch/issues/65000
    conflicts("+ffmpeg", when="platform=darwin")
    # https://github.com/pytorch/vision/pull/7378
    conflicts("^ffmpeg@6:")

    # Many of the datasets require additional dependencies to use.
    # These can be installed after the fact.

    # Fix duplicate symbol error when building with ROCm
    patch("torchvision-0.26.0-rocm-vision-duplicate-symbol.patch", when="@0.26.0 ^py-torch+rocm")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # The only documentation on building is what is found in setup.py and:
        # https://github.com/pytorch/vision/blob/main/CONTRIBUTING.md#development-installation

        # By default, version is read from `version.txt`, but this includes an `a0`
        # suffix used for alpha builds. Override the version for stable releases.
        if not self.spec.satisfies("@main"):
            env.set("BUILD_VERSION", str(self.version))

        # Used by ninja
        env.set("MAX_JOBS", str(make_jobs))

        if "^cuda" in self.spec:
            env.set("CUDA_HOME", self.spec["cuda"].prefix)

        for gpu in ["cuda", "mps"]:
            env.set(f"FORCE_{gpu.upper()}", str(f"+{gpu}" in self.spec["py-torch"]))

        extensions = ["png", "jpeg", "webp", "nvjpeg", "video_codec", "ffmpeg"]
        for extension in extensions:
            env.set(f"TORCHVISION_USE_{extension.upper()}", str(f"+{extension}" in self.spec))

        include = []
        library = []
        for dep in self.spec.dependencies(deptype="link"):
            query = self.spec[dep.name]
            include.extend(query.headers.directories)
            library.extend(query.libs.directories)

        # When building with ROCm, add all ROCm library include paths for HIP compilation
        # PyTorch headers transitively include many ROCm headers that extensions need
        if "^py-torch+rocm" in self.spec:
            rocm_deps = [
                "rocthrust",
                "rocprim",
                "hipsparse",
                "hipblas",
                "hipblas-common",
                "hipblaslt",
                "hipfft",
                "hiprand",
                "hipsolver",
                "rocblas",
                "rocsparse",
                "rocsolver",
                "rocfft",
            ]
            for dep in rocm_deps:
                if dep in self.spec:
                    include.append(self.spec[dep].prefix.include)

        # CONTRIBUTING.md says to use TORCHVISION_INCLUDE and TORCHVISION_LIBRARY, but
        # these do not work for older releases. Build uses a mix of Spack's compiler wrapper
        # and the actual compiler, so this is needed to get parts of the build working.
        # See https://github.com/pytorch/vision/issues/2591
        env.set("TORCHVISION_INCLUDE", ":".join(include))
        env.set("TORCHVISION_LIBRARY", ":".join(library))
        env.set("CPATH", ":".join(include))
        env.set("LIBRARY_PATH", ":".join(library))

        # For ROCm builds, also prepend ROCm includes to ensure hipcc can find them
        if "^py-torch+rocm" in self.spec:
            for dep in rocm_deps:
                if dep in self.spec:
                    env.prepend_path("CPATH", self.spec[dep].prefix.include)
                    env.prepend_path("CPLUS_INCLUDE_PATH", self.spec[dep].prefix.include)
