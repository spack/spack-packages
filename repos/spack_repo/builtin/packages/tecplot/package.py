# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Tecplot(Package):
    """Tecplot 360 is a Computational Fluid Dynamics (CFD) and numerical
    simulation software package used in post-processing simulation results.
    It is also used in chemistry applications to visualize molecule structure
    by post-processing charge density data."""

    homepage = "https://www.tecplot.com/"
    manual_download = True

    maintainers("LRWeber")

    license("LicenseRef-Tecplot-Proprietary", checked_by="alecbcs")

    redistribute(source=False, binary=False)

    # Semantic Versioning
    version(
        "2025.2.2",
        sha256="0359d87036ff7124865aba9f0da3ca8f2dd458277ab5689e87ed7e613dcae5d6",
        expand=False,
    )
    version(
        "2025.2.1",
        sha256="2deba2be44fed96935ec07111459b2d4d22b51bcf321de32a8d0dc7460359e3d",
        expand=False,
    )
    version(
        "2025.2.0",
        sha256="640e85cf9037c437f071265a8424291096095d823ee0a2af1245747b31dcc1e1",
        expand=False,
    )
    version(
        "2025.1.0",
        sha256="1927ebe5d5ca6445940bfaa2bd55de48c75f7a339f1e3fb2d502796855ec0432",
        expand=False,
    )
    version(
        "2024.1.1",
        sha256="46012aab7e3f18d77344448d1e1a8d43a58f5e35fb0a296c593199810df4bc8e",
        expand=False,
    )
    version(
        "2024.1.0",
        sha256="709022a5d5532d46a47cfa3bf0698a4ea8428c7a0dea2feb708a5add8091a8f0",
        expand=False,
    )
    version(
        "2023.2.0",
        sha256="6e19da9d1e6b1e70b3619f0d67707019d2c35690c068c69078edcbc7b8879498",
        expand=False,
    )
    version(
        "2023.1.0",
        sha256="58e7f4de875e65047f4edd684013d0ff538df6246f00c059458989f281be4c93",
        expand=False,
    )
    version(
        "2022.2.1",
        sha256="e30cb7bf894e7cd568a2b24beb4bf667f1781ae27b59bb73410fafe12ddfdcdf",
        expand=False,
        deprecated=True,
    )
    # Previous Versioning
    version(
        "2025r2",
        # 2025 R2 M1 / 2025.2.1
        sha256="2deba2be44fed96935ec07111459b2d4d22b51bcf321de32a8d0dc7460359e3d",
        expand=False,
        deprecated=True,
    )
    version(
        "2025r1",
        # 2025 R1 / 2025.1.0
        sha256="1927ebe5d5ca6445940bfaa2bd55de48c75f7a339f1e3fb2d502796855ec0432",
        expand=False,
        deprecated=True,
    )
    version(
        "2024r1",
        # 2024 R1 M1 / 2024.1.1
        sha256="46012aab7e3f18d77344448d1e1a8d43a58f5e35fb0a296c593199810df4bc8e",
        expand=False,
        deprecated=True,
    )
    version(
        "2023r1",
        # 2023 R1 / 2023.1.0
        sha256="58e7f4de875e65047f4edd684013d0ff538df6246f00c059458989f281be4c93",
        expand=False,
        deprecated=True,
    )
    version(
        "2022r2",
        # 2022 R2 / 2022.2.1 (M1 not specified in download list despite patch version)
        sha256="e30cb7bf894e7cd568a2b24beb4bf667f1781ae27b59bb73410fafe12ddfdcdf",
        expand=False,
        deprecated=True,
    )

    # Licensing
    license_required = True
    license_comment = "#"
    license_files = ["tecplotlm.lic"]

    def url_for_version(self, version):
        # NOTE: Official downloads only specify major+minor (year+release) versions in filenames.
        #       Patch (maintenance) versions can only be verified by the hash.
        if "r" in str(version):
            # Parse as previous versioning
            return "file://{0}/tecplot360ex{1}_linux64.sh".format(os.getcwd(), version)
        else:
            # Parse as semantic versioning
            return "file://{0}/tecplot360ex{1}r{2}_linux64.sh".format(
                os.getcwd(), version[0], version[1]
            )

    def install(self, spec, prefix):
        set_executable(self.stage.archive_file)
        installer = Executable(self.stage.archive_file)
        installer("--skip-license", "--prefix=%s" % prefix)
        # Link individual products to top level license file
        lic360 = "360ex_{0}/tecplotlm.lic".format(self.version)
        licChorus = "chorus_{0}/tecplotlm.lic".format(self.version)
        force_symlink("../tecplotlm.lic", join_path(self.prefix, lic360))
        force_symlink("../tecplotlm.lic", join_path(self.prefix, licChorus))

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        # Add Chorus bin
        binChorus = "chorus_{0}/bin".format(self.version)
        env.prepend_path("PATH", join_path(self.prefix, binChorus))
        # Add Tecplot 360 bin
        bin360 = "360ex_{0}/bin".format(self.version)
        env.prepend_path("PATH", join_path(self.prefix, bin360))
        # Add Tecplot 360 lib
        lib360 = "360ex_{0}/lib".format(self.version)
        env.prepend_path("LD_LIBRARY_PATH", join_path(self.prefix, lib360))
