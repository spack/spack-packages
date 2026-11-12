from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Libcomm(Package):
    """Header-only communication library used by LibRI."""

    homepage = "https://github.com/abacusmodeling/LibComm"
    url = "https://github.com/abacusmodeling/LibComm/archive/refs/tags/v0.1.1.tar.gz"
    git = "https://github.com/abacusmodeling/LibComm.git"

    maintainers("Growl1234")

    license("LGPL-3.0-only", checked_by="Growl1234")

    version("master", branch="master")
    # Snapshot required by current ABACUS releases; no newer LibComm release is available.
    version("0.1.2-202603", commit="12457e7ebd2092dfb6b5d6d0e1fd956c1eb12c53")
    version("0.1.1", sha256="9c47b6ea9573bffa4232c0bef63714d4c3af820c6b7539cfa6e294ca2b8ba4af")

    depends_on("mpi")

    def install(self, spec, prefix):
        install_tree("include", prefix.include)
