# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPillowBase(PythonPackage):
    """Base class for Pillow and its fork Pillow-SIMD."""

    maintainers("adamjstewart")
    provides("pil")

    # These defaults correspond to Pillow defaults
    # https://pillow.readthedocs.io/en/stable/installation/building-from-source.html
    VARIANTS = (
        "zlib",
        "jpeg",
        "tiff",
        "freetype",
        "raqm",
        "lcms",
        "webp",
        "webpmux",
        "jpeg2000",
        "imagequant",
        "xcb",
        "avif",
    )
    variant("zlib", default=True, description="Compressed PNG functionality")
    variant("jpeg", default=True, description="JPEG functionality")
    variant("tiff", default=False, description="Compressed TIFF functionality")
    variant("freetype", default=False, description="Type related services")
    variant("raqm", when="@8.2:+freetype", default=False, description="RAQM support")
    variant("lcms", default=False, description="Color management")
    variant("webp", default=False, description="WebP format")
    variant("webpmux", when="@:10+webp", default=False, description="WebP metadata")
    variant("jpeg2000", default=False, description="JPEG 2000 functionality")
    variant("imagequant", default=False, description="Improved color quantization")
    variant("xcb", default=False, description="X11 screengrab support")
    variant("avif", when="@11.2:", default=False, description="Support for the AVIF format")

    # Required dependencies
    # https://pillow.readthedocs.io/en/stable/installation/python-support.html
    with default_args(type=("build", "link", "run")):
        depends_on("python@3.10:3.14", when="@12:")
        depends_on("python@3.9:3.14", when="@11.3")
        depends_on("python@3.9:3.13", when="@11.0:11.2")
        depends_on("python@3.8:3.13", when="@10.4")
        depends_on("python@3.8:3.12", when="@10.1:10.3")
        depends_on("python@3.8:3.11", when="@10.0")
        depends_on("python@3.7:3.11", when="@9.3:9.5")
        depends_on("python@3.7:3.10", when="@9.0:9.2")
        depends_on("python@3.6:3.10", when="@8.3.2:8.4")
        depends_on("python@3.6:3.9", when="@8:8.3.1")

    # pyproject.toml
    with default_args(type="build"):
        depends_on("py-pip@22.1:", when="@10:")
        depends_on("py-pybind11", when="@12:")
        depends_on("py-setuptools@77:", when="@11.2:")
        depends_on("py-setuptools@67.8:", when="@10:")
        depends_on("py-setuptools")

    # Optional dependencies
    # https://pillow.readthedocs.io/en/stable/installation/building-from-source.html
    depends_on("zlib-api", when="+zlib")
    depends_on("jpeg", when="+jpeg")
    depends_on("libtiff", when="+tiff")
    depends_on("freetype@2.9.1:", when="@12:+freetype")
    depends_on("freetype", when="+freetype")
    depends_on("libraqm", when="+raqm")
    depends_on("lcms@2:", when="+lcms")
    depends_on("libwebp", when="+webp")
    depends_on("libwebp+libwebpmux+libwebpdemux", when="+webpmux")
    depends_on("openjpeg@2:", when="+jpeg2000")
    depends_on("libimagequant", when="+imagequant")
    depends_on("libxcb", when="+xcb")
    depends_on("libavif@1:", when="+avif")

    patch(
        "https://github.com/python-pillow/Pillow/commit/1c11d4581c5705dfa21bc5a4f3b6980c556978bf.patch?full_index=1",
        sha256="599f37e6a5a8d1adb9f4025ffc7cae5f5b61cad60a04e7c7a3015f9e350047bb",
        when="@11.0.0",
    )

    @when("@10:")
    def config_settings(self, spec, prefix):
        settings = {"parallel": make_jobs}

        for variant in self.VARIANTS:
            if spec.satisfies(f"+{variant}"):
                settings[variant] = "enable"
            elif spec.satisfies(f"~{variant}"):
                settings[variant] = "disable"

        return settings

    def patch(self):
        """Patch setup.py to provide library and include directories for dependencies."""
        library_dirs = []
        include_dirs = []
        for dep in self.spec.dependencies(deptype="link"):
            query = self.spec[dep.name]
            library_dirs.extend(query.libs.directories)
            include_dirs.extend(query.headers.directories)

        setup = FileFilter("setup.py")
        if self.version >= Version("11"):
            setup.filter(
                "library_dirs: list[str] = []",
                "library_dirs: list[str] = {0}".format(library_dirs),
                string=True,
            )
            setup.filter(
                "include_dirs: list[str] = []",
                "include_dirs: list[str] = {0}".format(include_dirs),
                string=True,
            )
        else:
            setup.filter(
                "library_dirs = []", "library_dirs = {0}".format(library_dirs), string=True
            )
            setup.filter(
                "include_dirs = []", "include_dirs = {0}".format(include_dirs), string=True
            )

        if self.spec.satisfies("@:9"):
            with open("setup.cfg", "a") as setup:
                print("[build_ext]", file=setup)

                for variant in self.VARIANTS:
                    if self.spec.satisfies(f"+{variant}"):
                        print(f"enable_{variant}=1", file=setup)
                    elif self.spec.satisfies(f"~{variant}"):
                        print(f"disable_{variant}=1", file=setup)

                print("rpath={0}".format(":".join(self.rpath)), file=setup)
                print("[install]", file=setup)

    @when("@:9")
    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("MAX_CONCURRENCY", str(make_jobs))


class PyPillow(PyPillowBase):
    """Pillow is a fork of the Python Imaging Library (PIL). It adds image
    processing capabilities to your Python interpreter. This library supports
    many file formats, and provides powerful image processing and graphics
    capabilities."""

    homepage = "https://python-pillow.org/"
    pypi = "pillow/pillow-10.2.0.tar.gz"

    license("MIT-CMU", when="@11:")
    license("HPND", when="@:10")

    version("12.1.1", sha256="9ad8fa5937ab05218e2b6a4cff30295ad35afd2f83ac592e68c0d871bb0fdbc4")
    with default_args(deprecated=True):
        # https://www.cvedetails.com/cve/CVE-2026-25990/
        version(
            "12.1.0", sha256="5c5ae0a06e9ea030ab786b0251b32c7e4ce10e58d983c0d5c56029455180b5b9"
        )
        version(
            "12.0.0", sha256="87d4f8125c9988bfbed67af47dd7a953e2fc7b0cc1e7800ec6d2080d490bb353"
        )
        version(
            "11.3.0", sha256="3828ee7586cd0b2091b6209e5ad53e20d0649bbe87164a459d0676e035e8f523"
        )
        # https://www.cvedetails.com/cve/CVE-2025-48379/
        version(
            "11.2.1", sha256="a64dd61998416367b7ef979b73d3a85853ba9bec4c2925f74e588879a58716b6"
        )
        version(
            "11.1.0", sha256="368da70808b36d73b4b390a8ffac11069f8a5c85f29eff1f1b01bcf3ef5b2a20"
        )
        version(
            "11.0.0", sha256="72bacbaf24ac003fea9bff9837d1eedb6088758d41e100c1552930151f677739"
        )
        version(
            "10.4.0", sha256="166c1cd4d24309b30d61f79f4a9114b7b2313d7450912277855ff5dfd7cd4a06"
        )
        version(
            "10.3.0", sha256="9d2455fbf44c914840c793e89aa82d0e1763a14253a000743719ae5946814b2d"
        )
        # https://www.cvedetails.com/cve/CVE-2024-28219/
        version(
            "10.2.0", sha256="e87f0b2c78157e12d7686b27d63c070fd65d994e8ddae6f328e0dcf4a0cd007e"
        )
        version(
            "10.1.0", sha256="e6bf8de6c36ed96c86ea3b6e1d5273c53f46ef518a062464cd7ef5dd2cf92e38"
        )
        # https://www.cvedetails.com/cve/CVE-2023-50447/
        version(
            "10.0.1", sha256="d72967b06be9300fed5cfbc8b5bafceec48bf7cdc7dab66b1d2549035287191d"
        )
        version(
            "10.0.0", sha256="9c82b5b3e043c7af0d95792d0d20ccf68f61a1fec6b3530e718b688422727396"
        )
        # https://www.cvedetails.com/cve/CVE-2023-44271/
        version("9.5.0", sha256="bf548479d336726d7a0eceb6e767e179fbde37833ae42794602631a070d630f1")
        version("9.4.0", sha256="a1c2d7780448eb93fbcc3789bf3916aa5720d942e37945f4056680317f1cd23e")
        version("9.3.0", sha256="c935a22a557a560108d780f9a0fc426dd7459940dc54faa49d83249c8d3e760f")
        # https://www.cvedetails.com/cve/CVE-2022-45199/
        version("9.2.0", sha256="75e636fd3e0fb872693f23ccb8a5ff2cd578801251f3a4f6854c6a5d437d3c04")
        # https://www.cvedetails.com/cve/CVE-2022-45198/
        version("9.1.1", sha256="7502539939b53d7565f3d11d87c78e7ec900d3c72945d4ee0e2f250d598309a0")
        # https://www.cvedetails.com/cve/CVE-2022-30595/
        version("9.1.0", sha256="f401ed2bbb155e1ade150ccc63db1a4f6c1909d3d378f7d1235a44e90d75fb97")
        version("9.0.1", sha256="6c8bc8238a7dfdaf7a75f5ec5a663f4173f8c367e5a39f87e720495e1eed75fa")
        # https://www.cvedetails.com/cve/CVE-2022-24303/
        version("9.0.0", sha256="ee6e2963e92762923956fe5d3479b1fdc3b76c83f290aad131a2f98c3df0593e")
        # https://www.cvedetails.com/cve/CVE-2022-22817/
        # https://www.cvedetails.com/cve/CVE-2022-22816/
        # https://www.cvedetails.com/cve/CVE-2022-22815/
        version("8.4.0", sha256="b8e2f83c56e141920c39464b852de3719dfbfb6e3c99a2d8da0edf4fb33176ed")
        # https://www.cvedetails.com/cve/CVE-2021-34552/
        # https://www.cvedetails.com/cve/CVE-2021-28678/
        # https://www.cvedetails.com/cve/CVE-2021-28677/
        # https://www.cvedetails.com/cve/CVE-2021-28676/
        # https://www.cvedetails.com/cve/CVE-2021-28675/
        # https://www.cvedetails.com/cve/CVE-2021-27923/
        # https://www.cvedetails.com/cve/CVE-2021-27922/
        # https://www.cvedetails.com/cve/CVE-2021-27921/
        # https://www.cvedetails.com/cve/CVE-2021-25293/
        # https://www.cvedetails.com/cve/CVE-2021-25292/
        # https://www.cvedetails.com/cve/CVE-2021-25291/
        # https://www.cvedetails.com/cve/CVE-2021-25290/
        # https://www.cvedetails.com/cve/CVE-2021-25289/
        # and many, many more...
        version("8.0.0", sha256="59304c67d12394815331eda95ec892bf54ad95e0aa7bc1ccd8e0a4a5a25d4bf3")

    depends_on("c", type="build")

    for ver in [
        "12.1.1",
        "12.1.0",
        "12.0.0",
        "11.3.0",
        "11.2.1",
        "11.1.0",
        "11.0.0",
        "10.4.0",
        "10.3.0",
        "10.2.0",
        "10.1.0",
        "10.0.1",
        "10.0.0",
        "9.5.0",
        "9.4.0",
        "9.3.0",
        "9.2.0",
        "9.1.1",
        "9.1.0",
        "9.0.1",
        "9.0.0",
        "8.4.0",
        "8.0.0",
    ]:
        provides("pil@" + ver, when="@" + ver)

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/{0}/{0}illow/{0}illow-{1}.tar.gz"
        if version >= Version("10.2"):
            letter = "p"
        else:
            letter = "P"
        return url.format(letter, version)
