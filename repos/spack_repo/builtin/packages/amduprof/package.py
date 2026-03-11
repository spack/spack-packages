# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Amduprof(Package):
    """AMD uProf ("MICRO-prof") is a software profiling analysis tool for x86
    applications running on Windows, Linux and FreeBSD operating systems and
    provides event information unique to the AMD "Zen"-based processors and AMD
    Instinct(tm) MI Series accelerators. AMD uProf enables the developer to better
    understand the limiters of application performance and evaluate
    improvements."""

    homepage = "https://www.amd.com/en/developer/uprof.html"
    manual_download = True

    maintainers("amd-toolchain-support")

    version(
        "5.2.606",
        sha256="d5856a6640f6c673941dcb6e42f72b589d656ba40d2ba03ff1215611b2830f11",
        url="file://{0}/AMDuProf_Linux_x64_5.2.606.tar.bz2".format(os.getcwd()),
    )
    version(
        "5.1.701",
        sha256="8fd83170170883a6617391609545dffd557d6ca4a8f8f00a7a8a2d6cdee08189",
        url="file://{0}/AMDuProf_Linux_x64_5.1.701.tar.bz2".format(os.getcwd()),
    )
    version(
        "5.0.1479",
        sha256="065d24d9b84d2ef94ae8a360bf55c74a0f3fe9250b01cc7fb2642495028130d5",
        url="file://{0}/AMDuProf_Linux_x64_5.0.1479.tar.bz2".format(os.getcwd()),
    )
    version(
        "4.2.850",
        sha256="f2d7c4eb9ec9c32845ff8f19874c1e6bcb0fa8ab2c12e73addcbf23a6d1bd623",
        url="file://{0}/AMDuProf_Linux_x64_4.2.850.tar.bz2".format(os.getcwd()),
    )

    depends_on("binutils@2.27:", type="run")

    # Licensing
    license_required = True
    license_url = "https://www.amd.com/en/developer/uprof/uprof-eula.html"

    conflicts("platform=darwin")
    requires("target=x86_64:", msg="AMD uProf available only on x86_64")

    def install(self, spec, prefix):
        install_tree(".", prefix)
