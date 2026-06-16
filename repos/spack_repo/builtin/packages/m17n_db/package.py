# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class M17nDb(AutotoolsPackage):
    """Provide various information to the `m17n` library.

    The project is not explained in any way beyond the above."""
    homepage = "https://www.nongnu.org/m17n"
    url = "http://download.savannah.nongnu.org/releases/m17n/m17n-db-1.8.4.tar.gz"
    git = "https://git.savannah.nongnu.org/git/m17n/m17n-db.git"

    license("LGPL-2.1")

    resource(name="glibc-2.3.2",
             url="https://ftpmirror.gnu.org/glibc/glibc-2.3.2.tar.gz",
             sha256="dbf0deb003531cbd2493986718a1b34a113c914238a90de8b5b3218217257d82",
             destination="glibc-2.3.2")

    version("1.8.10", sha256="31024e0513533448b9b31ea3294d35a6426e6690eb44628680731aa955c0c16c")
    version("1.8.4", sha256="b72cf4daa57518bad1582d5c8008908494580d3f1c7164d429809068623b6751")
    version("master", branch="master")

    def c
