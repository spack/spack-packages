from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Libri(Package):
    """Header-only resolution-of-identity library."""

    homepage = "https://github.com/deepmodeling/LibRI"
    url = "https://github.com/abacusmodeling/LibRI/archive/refs/tags/v0.3.0.0.tar.gz"
    git = "https://github.com/abacusmodeling/LibRI.git"

    maintainers("Growl1234")

    license("LGPL-3.0-only", checked_by="Growl1234")

    version("master", branch="master")
    version("0.3.0.0", sha256="c6910c2cef38dbb93df59576e332b8f28a9f624db1dc46e3d374004ecfdca193")
    # Retain the snapshot for existing environments.
    version("0.2.1.2-202609", commit="6ce3c8480ae38a085746dc81cc4dbb59b8074430")
    version("0.2.1.1", sha256="cd33fd5428400ea696b82c9132878c07bf785847b3f56b1979e25a3a5fc0b311")

    depends_on("mpi")
    depends_on("blas")
    depends_on("lapack")
    depends_on("cereal")
    depends_on("libcomm")

    variant("cuda", default=False, when="@0.3:", description="Enable CUDA support through LibDDLA")

    depends_on("libddla@0.0.7:+cuda", when="+cuda")

    def install(self, spec, prefix):
        install_tree("include", prefix.include)
