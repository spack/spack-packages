# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.gnu import GNUMirrorPackage

from spack.package import *


class Gzip(AutotoolsPackage, GNUMirrorPackage):
    """GNU Gzip is a popular data compression program originally written by
    Jean-loup Gailly for the GNU project."""

    homepage = "https://www.gnu.org/software/gzip/"
    gnu_mirror_path = "gzip/gzip-1.10.tar.gz"

    license("GPL-3.0-or-later")

    version("1.15", sha256="545886cf57fa88a65e967fbf705903d7fcb2567c82c7342493e82e8d7b1a210b")
    version("1.14", sha256="613d6ea44f1248d7370c7ccdeee0dd0017a09e6c39de894b3c6f03f981191c6b")
    version("1.13", sha256="20fc818aeebae87cdbf209d35141ad9d3cf312b35a5e6be61bfcfbf9eddd212a")

    depends_on("c", type="build")

    # https://lists.gnu.org/archive/html/bug-gzip/2026-09/msg00031.html
    patch(
        "https://cgit.git.savannah.gnu.org/cgit/gzip.git/rawdiff/?id=b4ed8e73401968bcad749afb0e636dd3ec205ca7",
        sha256="79dc82e4c747a7828e364d45a68a1049820e95d9a3772e585ff8a27146b44add",
        when="@1.15",
    )

    # Gzip makes a recursive symlink if built in-source
    build_directory = "spack-build"
