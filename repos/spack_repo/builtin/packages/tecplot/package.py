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

    version(
        "2025r2",
        sha256="2deba2be44fed96935ec07111459b2d4d22b51bcf321de32a8d0dc7460359e3d",
        expand=False,
    )
    version(
        "2025r1",
        sha256="1927ebe5d5ca6445940bfaa2bd55de48c75f7a339f1e3fb2d502796855ec0432",
        expand=False,
    )
    version(
        "2024r1",
        sha256="46012aab7e3f18d77344448d1e1a8d43a58f5e35fb0a296c593199810df4bc8e",
        expand=False,
    )
    version(
        "2023r1",
        sha256="58e7f4de875e65047f4edd684013d0ff538df6246f00c059458989f281be4c93",
        expand=False,
    )
    version(
        "2022r2",
        sha256="e30cb7bf894e7cd568a2b24beb4bf667f1781ae27b59bb73410fafe12ddfdcdf",
        expand=False,
    )

    # Licensing
    license_required = True
    license_comment = "#"
    license_files = ["tecplotlm.lic"]

    def url_for_version(self, version):
        return "file://{0}/tecplot360ex{1}_linux64.sh".format(os.getcwd(), version)

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
