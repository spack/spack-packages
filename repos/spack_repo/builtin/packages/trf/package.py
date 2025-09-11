# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Trf(AutotoolsPackage):
    """Tandem Repeats Finder is a program to locate and display tandem repeats
    in DNA sequences.

    Note: A manual download is required for TRF.
    Spack will search your current directory for the download file.
    Alternatively, add this file to a mirror so that Spack can find it.
    For instructions on how to set up a mirror, see
    https://spack.readthedocs.io/en/latest/mirrors.html"""

    homepage = "https://tandem.bu.edu/trf/trf.html"
    url = "https://github.com/Benson-Genomics-Lab/TRF/archive/refs/tags/v4.09.1.tar.gz"

    license("AGPL-3.0-only")

    version("4.09.1", sha256="516015b625473350c3d1c9b83cac86baea620c8418498ab64c0a67029c3fb28a")
    version("4.09", sha256="9332155384bef82f6c7c449c038d27f1a14b984b2e93000bfcf125f4d44d6aca")

    depends_on("c", type="build")  # generated
