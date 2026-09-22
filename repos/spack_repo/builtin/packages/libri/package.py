from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Libri(Package):
    """Header-only resolution-of-identity library."""

    homepage = "https://github.com/deepmodeling/LibRI"
    url = "https://github.com/abacusmodeling/LibRI/archive/refs/tags/v0.2.1.1.tar.gz"
    git = "https://github.com/abacusmodeling/LibRI.git"

    maintainers("Growl1234")

    license("LGPL-3.0-only", checked_by="Growl1234")

    version("master", branch="master")
    # Snapshot required by current ABACUS releases; no newer LibRI release is available.
    version("0.2.1.2-202609", commit="6ce3c8480ae38a085746dc81cc4dbb59b8074430")
    version("0.2.1.1", sha256="cd33fd5428400ea696b82c9132878c07bf785847b3f56b1979e25a3a5fc0b311")

    depends_on("mpi")
    depends_on("blas")
    depends_on("lapack")
    depends_on("cereal")
    depends_on("libcomm")

    def install(self, spec, prefix):
        install_tree("include", prefix.include)
