# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems import autotools
from spack_repo.builtin.build_systems import meson

from spack.package import *


class Coinhsl(meson.MesonPackage, autotools.AutotoolsPackage):
    """
    CoinHSL is a collection of linear algebra libraries (KB22, MA27,
    MA28, MA54, MA57, MA64, MA77, MA86, MA97, MC19, MC34, MC64, MC68,
    MC69, MC78, MC80, OF01, ZB01, ZB11) bundled for use with IPOPT and
    other applications that use these HSL routines.

    Note: CoinHSL is licensed software. You will need to request a
    license from Research Councils UK and download a .tar.gz archive
    of CoinHSL yourself. Spack will search your current directory for
    the download file.

    To get a personal licence for the archive version, request the
    licence here: https://licences.stfc.ac.uk/product/coin-hsl-archive
    """

    depends_on("c", type="build")
    depends_on("fortran", type="build")

    # Since the 2024 release, coinhsl uses meson and files are
    # distributed with names such as:
    # - coinhsl-2024.05.15.tar.gz
    # - coinhsl-archive-2024.05.15.tar.gz
    # Prior to this release, coinhsl used autotools and both the reduced
    # "archive" and full libraries just had a date.
    # The version system is used here to differentiate the three:
    # - `"2023" < version` - This will always be a full meson build
    # - `version < "b"` - The version starts with "a" and is an archive.
    #                     This convention came in after the autotools
    #                     build so is a meson build
    # - `"b" < version < "2023"` - The old autotools builds
    build_system(
        conditional("autotools", when="@b:2019.05.21"),
        conditional("meson", when="@2023:,:b"),
        default="meson",
    )

    homepage = "https://www.hsl.rl.ac.uk/ipopt/"
    url = f"file://{os.getcwd()}/coinhsl-2024.05.15.tar.gz"
    manual_download = True

    maintainers("AndrewLister-STFC")

    # Meson builds
    version(
        "2024.05.15",
        sha256="2534807b4f6a4a69661c82dc0da7094f685f0fce6443a9147ee90a21caba9e63",
        preferred=True,
    )
    version(
        "archive-2024.05.15",
        sha256="1d907ce5d84331ce8f78125d5fc766184f0fce9a7b340db7f3c4821a7f4b7c4c",
    )

    # Full lib requires extra deps (archive has no deps)
    with when("build_system=meson @2023:"):
        depends_on("blas")
        depends_on("lapack")
        variant("metis", default=True, description="Build with Metis support.")
        depends_on("metis", when="+metis")

    # Autotools builds
    version(
        "2019.05.21",
        sha256="95ce1160f0b013151a3e25d40337775c760a8f3a79d801a1d190598bf4e4c0c3"
    )
    version(
        "2015.06.23",
        sha256="3e955a2072f669b8f357ae746531b37aea921552e415dc219a5dd13577575fb3"
    )
    version(
        "2014.01.17",
        sha256="ed49fea62692c5d2f928d4007988930da9ff9a2e944e4c559d028671d122437b"
    )
    version(
        "2014.01.10",
        sha256="7c2be60a3913b406904c66ee83acdbd0709f229b652c4e39ee5d0876f6b2e907"
    )

    with when("build_system=autotools"):
        parallel = False
        variant("blas", default=False,
                description="Link to external BLAS library")
        depends_on("blas", when="+blas")


class MesonBuilder(meson.MesonBuilder):
    """Builder class to hold functions specific to meson"""
    def meson_args(self) -> list[str]:
        """Add arguments for calling meson setup"""
        spec = self.spec
        args: list[str] = []

        # archive versions have no deps
        if spec.satisfies("@:b"):
            return []

        # Configure blas
        blas: str = spec["blas"].libs.names[0]
        blas_paths: list[str] = [
            sf[2:] for sf in spec["blas"].libs.search_flags.split()
        ]
        args.append(f"-Dlibblas={blas}")
        args.extend([f"-Dlibblas_path={p}" for p in blas_paths])

        # Configure lapack
        lapack: str = spec["lapack"].libs.names[0]
        lapack_paths: list[str] = [
            sf[2:] for sf in spec["lapack"].libs.search_flags.split()
        ]
        args.append(f"-Dliblapack={lapack}")
        args.extend([f"-Dliblapack_path={p}" for p in lapack_paths])

        # Configure metis
        if spec.satisfies("+metis"):
            metis = spec["metis"]
            if metis.satisfies("@5"):
                args.append("-Dlibmetis_version=5")
            else:
                args.append("-Dlibmetis_version=4")
            args.extend(
                [
                    f"-Dlibmetis_include={metis.prefix.include}",
                    f"-Dlibmetis_path={metis.prefix.lib}",
                ]
            )
        return args


class AutotoolsBuilder(autotools.AutotoolsBuilder):
    """Builder class to hold functions specific to autotools"""
    def configure_args(self) -> list[str]:
        """Add arguments for the calling configure"""
        spec = self.spec
        args: list[str] = []

        # Configure blas
        if spec.satisfies("+blas"):
            args.append(f"--with-blas={spec['blas'].libs.ld_flags}")

        return args
