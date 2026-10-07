# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Cice(Package):
    """CICE is a computationally efficient model for simulating the growth, melting,
    and movement of polar sea ice."""

    homepage = "https://github.com/CICE-Consortium/CICE"
    url = "https://github.com/CICE-Consortium/CICE/archive/refs/tags/CICE6.6.3.tar.gz"

    maintainers("apcraig")

    license("BSD-3-Clause")

    version("6.6.3", sha256="efc16625486b46f01409c568f532978690bb37cc12d8b8a121601ffe047e89f4")
    version("6.6.2", sha256="1a265ca44a2d7182cd670ff2023d0ff98bedce7cff7c68fe374de9084ba96b39")
    version("6.6.1", sha256="2b10591ea0052fe5a183679a4e9f6e083ddbb46537bfa765af0cbe8ed57d0a9e")
    version("6.6.0", sha256="542531dfa6fd09f1a6b0c2c6c7a48ae7ffe7cae88e136c7da80ba7fdb5e09bca")
    version("6.5.1", sha256="cec43994f9d6feaddeed0eb4753fe5abdfa5db3355d1f84cf9791672b967d66a")
    version("6.5.0", sha256="e070acb19bcce43bb4268ae7888f273021d246c8f91b1ca56141c9a4fdef5fc3")
    version("6.4.2", sha256="5d713dd1852930dc7f97896eaf626046f8e021f1c828ea83a4ce15682ad7793b")
    version("6.4.1", sha256="9879f1cd298b7079c7d60b088a5f928d5507626c91d71470f7aeaa54da830657")
    version("6.4.0", sha256="fafbc14e5bc3644f9bd1cbf3db81ef28c83431a78a662974588b597cd3d6155a")
    version("6.3.1", sha256="ee5326c3c34287a49b1bd560da02618a9015e26c2a87dc5199dbe1a230c8f6cf")

    variant("mpi", default=True, description="Activates MPI support")
    variant(
        "target_dir",
        default="src",
        description="Directory name where CICE is installed",
        values=str,
    )

    depends_on("c", type="build")
    depends_on("fortran", type="build")

    depends_on("netcdf-fortran")
    depends_on("mpi", when="+mpi")

    # Ensure directory exists before install
    @run_before("install")
    def make_target_dir(self):
        target_name = self.spec.variants["target_dir"].value
        mkdirp(join_path(self.prefix, target_name))

    def install(self, spec, prefix):
        # Stage the source tree for user config
        target_name = spec.variants["target_dir"].value
        src_dest = join_path(prefix, target_name)

        install_tree(".", src_dest)

        tty.msg(
            f"CICE source staged at {src_dest}. Run cice.setup from that "
            "directory to create a case; spack does not build or "
            "run the model."
        )
