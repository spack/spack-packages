# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install kvs
#
# You can edit this file again by typing:
#
#     spack edit kvs
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
from spack.util.environment import set_env
from spack_repo.builtin.build_systems.generic import Package

class Kvs(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/TO0603/KVS"
    url = "https://github.com/TO0603/KVS/archive/refs/tags/forDev.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    # FIXME: Add proper versions here.
    # version("1.2.4")
    version("3.1", sha256="0ab932b0273f7f10972c0cb37de775a2f3923ca8ae26187d1b8c52847147ed84")

    variant("mpi", default=True, description="Enable MPI Support")
    variant("extended_fileformat", default=True, description="Enable extended fileformat")

    # FIXME: Add dependencies if required.
    # depends_on("foo")
    depends_on("gmake", type="build")
    depends_on("cxx", type="build")

    depends_on("mpi", when="+mpi")
    depends_on("qt-base@6.2.4+opengl")
    depends_on("qt-svg@6.2.4+widgets")
    depends_on("vtk@9.3.1~mpi", when="~mpi+extended_fileformat")
    depends_on("vtk@9.3.1+mpi", when="+mpi+extended_fileformat")

    patch("kvs-conf.patch", when="~extended_fileformat")
    patch("kvs-conf-extended-fileformat.patch", when="+extended_fileformat")

    def patch(self):
        import os

        source_dir = self.stage.source_path

        for root, dirs, files in os.walk(source_dir):
            for fname in files:
                path = os.path.join(root, fname)

                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    if "KVS_DIR" in content:
                        filter_file("KVS_DIR", "SPACK_KVS_DIR", path)
                except Exception:
                    pass

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        if "+extended_fileformat" in spec:
            with set_env(SPACK_KVS_DIR=str(prefix), VTK_INCLUDE_PATH=str(spec['vtk'].prefix.include) + "/vtk-9.3", VTK_LIB_PATH=str(spec['vtk'].prefix.lib)):
                make()
                make("install")
        else:
            with set_env(SPACK_KVS_DIR=str(prefix)):
                make()
                make("install")

