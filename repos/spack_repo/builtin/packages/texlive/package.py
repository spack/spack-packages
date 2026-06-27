# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import platform
import re

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Texlive(AutotoolsPackage):
    """TeX Live is an easy (we hope) way to get up and running with the TeX
    document production system. It provides a comprehensive TeX system with
    binaries for most flavors of Unix, including GNU/Linux, macOS, and also
    Windows. It includes all the major TeX-related programs, macro packages,
    and fonts that are free software, including support for many languages
    around the world."""

    homepage = "https://www.tug.org/texlive"
    url = "https://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2020/texlive-20200406-source.tar.xz"
    base_url = "https://ftp.math.utah.edu/pub/tex/historic/systems/texlive/{year}/texlive-{version}-{dist}.tar.xz"
    list_url = "https://ftp.math.utah.edu/pub/tex/historic/systems/texlive"
    list_depth = 1

    license("GPL-2.0-or-later AND GPL-3.0-or-later", checked_by="tgamblin")

    # Add information for new versions below.
    releases = [
        {
            "version": "20260301",
            "year": "2026",
            "sha256_source": "cb120d314d3ceb23ac608af17ddd2c623afcf02331f400a0f25eead5b8ac1d70",
            "sha256_texmf": "349eb7c5c2c15333d77490a52934b053c6dcb88834f2224978f7a4edf67940e7",
        },
        {
            "version": "20250308",
            "year": "2025",
            "sha256_source": "fffdb1a3d143c177a4398a2229a40d6a88f18098e5f6dcfd57648c9f2417490f",
            "sha256_texmf": "08dcda7430bf0d2f6ebb326f1e197e1473d3f7cc0984a2adb7236df45316c7cf",
        },
        {
            "version": "20240312",
            "year": "2024",
            "sha256_source": "7b6d87cf01661670fac45c93126bed97b9843139ed510f975d047ea938b6fe96",
            "sha256_texmf": "c8eae2deaaf51e86d93baa6bbcc4e94c12aa06a0d92893df474cc7d2a012c7a7",
        },
        {
            "version": "20230313",
            "year": "2023",
            "sha256_source": "3878aa0e1ed0301c053b0e2ee4e9ad999c441345f4882e79bdd1c8f4ce9e79b9",
            "sha256_texmf": "4c4dc77a025acaad90fb6140db2802cdb7ca7a9a2332b5e3d66aa77c43a81253",
        },
        {
            "version": "20220321",
            "year": "2022",
            "sha256_source": "5ffa3485e51eb2c4490496450fc69b9d7bd7cb9e53357d92db4bcd4fd6179b56",
            "sha256_texmf": "372b2b07b1f7d1dd12766cfc7f6656e22c34a5a20d03c1fe80510129361a3f16",
        },
        {
            "version": "20210325",
            "year": "2021",
            "sha256_source": "7aefd96608d72061970f2d73f275be5648ea8ae815af073016d3106acc0d584b",
            "sha256_texmf": "ff12d436c23e99fb30aad55924266104356847eb0238c193e839c150d9670f1c",
        },
        {
            "version": "20200406",
            "year": "2020",
            "sha256_source": "e32f3d08cbbbcf21d8d3f96f2143b64a1f5e4cb01b06b761d6249c8785249078",
            "sha256_texmf": "0aa97e583ecfd488e1dc60ff049fec073c1e22dfe7de30a3e4e8c851bb875a95",
        },
        {
            "version": "20190410",
            "year": "2019",
            "sha256_source": "d2a29fef04e34dc3d2d2296c18995fc357aa7625e7a6bbf40fb92d83d3d0d7b5",
            "sha256_texmf": "c2ec974abc98b91995969e7871a0b56dbc80dd8508113ffcff6923e912c4c402",
        },
    ]

    for release in releases:
        version(
            release["version"],
            sha256=release["sha256_source"],
            url=base_url.format(year=release["year"], version=release["version"], dist="source"),
        )

        resource(
            name="texmf",
            url=base_url.format(year=release["year"], version=release["version"], dist="texmf"),
            sha256=release["sha256_texmf"],
            when="@{0}".format(release["version"]),
        )

    variant("doc", default=False, description="Install the documentation files")
    variant("src", default=False, description="Install the source files")
    variant("dvipng", default=False, description="Build the dvipng program")
    variant("metapost", default=False, description="Build MetaPost programs")
    variant("X", default=False, description="Build X11 programs like xdvik and xpdfopen")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("pkgconfig", type="build")

    depends_on("cairo", when="+metapost")
    depends_on("freetype")
    depends_on("gmp", when="+metapost")
    depends_on("harfbuzz+graphite2")
    depends_on("icu4c")
    depends_on("libgd", when="+dvipng")
    depends_on("libpaper")
    depends_on("libpng")
    depends_on("libxaw", when="+X")
    depends_on("libxt", when="+X")
    depends_on("lua-lpeg", when="@20240312:")
    depends_on("mpfr@4:", when="+metapost")
    depends_on("perl")
    depends_on("pixman", when="+metapost")
    depends_on("poppler", when="@:2020")
    depends_on("poppler@:0.83", when="@:2019")
    depends_on("teckit")
    depends_on("zlib-api")
    depends_on("zziplib")

    build_directory = "spack-build"

    def tex_arch(self):
        return f"{platform.machine()}-{platform.system().lower()}"

    def configure_args(self):
        args = [
            f"--bindir={join_path(self.prefix.bin, self.tex_arch())}",
            "--disable-dvisvgm",
            "--disable-missing",
            "--disable-native-texlive-build",
            "--disable-static",
            "--enable-shared",
            "--with-banner-add= - Spack",
            f"--dataroot={self.prefix}",
            "--with-system-freetype2",
            "--with-system-graphite2",
            "--with-system-harfbuzz",
            "--with-system-icu",
            "--with-system-libpaper",
            "--with-system-libpng",
            "--with-system-poppler",
            "--with-system-teckit",
            "--with-system-zlib",
            "--with-system-zziplib",
        ]

        if self.spec.satisfies("+dvipng"):
            args.append("--with-system-gd")
        else:
            args.append("--disable-dvipng")

        if self.spec.satisfies("+metapost"):
            args.extend(
                [
                    "--with-system-cairo",
                    "--with-system-gmp",
                    "--with-system-mpfr",
                    "--with-system-pixman",
                ]
            )
        else:
            args.extend(
                [
                    "--disable-mp",
                    "--disable-pmp",
                    "--disable-upmp",
                ]
            )

        if self.spec.satisfies("+X"):
            args.append("--with-xdvi-x-toolkit=xaw")
        else:
            args.append("--without-x")

        return args

    @run_after("install")
    def setup_texlive(self):
        mkdirp(self.prefix.tlpkg.TeXLive)
        install("texk/tests/TeXLive/*", self.prefix.tlpkg.TeXLive)

        with working_dir("spack-build"):
            make("texlinks")

        skip_docs = self.spec.satisfies("~doc")
        skip_sources = self.spec.satisfies("~src")

        def ignore(path):
            parts = path.split(os.sep)
            if len(parts) <= 1:
                return False

            section = parts[1]
            return (skip_docs and section == "doc") or (skip_sources and section == "source")

        copy_tree(f"texlive-{self.version.string}-texmf", self.prefix, ignore=ignore)

        # Create and run setup utilities
        fmtutil_sys = Executable(join_path(self.prefix.bin, self.tex_arch(), "fmtutil-sys"))
        mktexlsr = Executable(join_path(self.prefix.bin, self.tex_arch(), "mktexlsr"))
        mktexlsr()
        if self.spec.satisfies("@20260301"):
            filter_file(
                "hilatex hitex language.dat -etex -ltx hilatex.ini",
                "# hilatex hitex language.dat -etex -ltx hilatex.ini",
                join_path(self.prefix, "texmf-dist", "web2c", "fmtutil.cnf"),
                string=True,
            )
        fmtutil_sys("--all")
        if self.spec.satisfies("@:2023"):
            mtxrun = Executable(join_path(self.prefix.bin, self.tex_arch(), "mtxrun"))
        else:
            mtxrun_lua = join_path(
                self.prefix, "texmf-dist", "scripts", "context", "lua", "mtxrun.lua"
            )
            chmod = which("chmod", required=True)
            chmod("+x", mtxrun_lua)
            mtxrun = Executable(mtxrun_lua)
        mtxrun("--generate")

    def flag_handler(self, name, flags):
        if name == "cxxflags" and self.spec.satisfies("@20240312:"):
            flags.append(self.compiler.cxx17_flag)
        return (flags, None, None)

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("PATH", join_path(self.prefix.bin, self.tex_arch()))

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("PATH", join_path(self.prefix.bin, self.tex_arch()))

    executables = [r"^tex$"]

    @classmethod
    def determine_version(cls, exe):
        # https://askubuntu.com/questions/100406/finding-the-tex-live-version
        # Thanks to @michaelkuhn that told how to reuse the package releases
        # variable.
        releases = cls.releases
        # tex indicates the year only
        output = Executable(exe)("--version", output=str, error=str)
        match = re.search(r"TeX Live (\d+)", output)
        ver = match.group(1) if match else None
        # We search for the repo actual release
        if ver is not None:
            for release in releases:
                year = release["year"]
                if year == ver:
                    ver = release["version"]
                    break
        return ver
