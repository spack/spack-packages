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
#     spack install pbvr
#
# You can edit this file again by typing:
#
#     spack edit pbvr
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import os
from spack.package import *
from spack.util.environment import set_env
from llnl.util.filesystem import install_tree
from spack_repo.builtin.build_systems.makefile import MakefilePackage

class Pbvr(MakefilePackage):
    """FIXME: Put a proper description of your package here."""
    phases = ['build', 'install']

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/CCSEPBVR/CS-IS-PBVR"
    url = "https://github.com/CCSEPBVR/CS-IS-PBVR/archive/refs/tags/v3.4.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    # FIXME: Add proper versions here.
    # version("1.2.4")
    version("3.4.0", sha256="4edbe420304b9436ab88829c0ff8465b27e10b26293288d5db3c84c3236e699c")

    variant("mpi", default=True, description="Enable MPI Support")
    variant("extended_fileformat", default=True, description="Enable extended fileformat")

    depends_on("gmake", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # FIXME: Add dependencies if required.
    # depends_on("foo")
    depends_on("mpi", when="+mpi")
    depends_on("qt-base@6.2.4+opengl")
    depends_on("qt-svg@6.2.4")
    depends_on("kvs~mpi~extended_fileformat", when="~mpi~extended_fileformat")
    depends_on("kvs~mpi+extended_fileformat", when="~mpi+extended_fileformat")
    depends_on("kvs+mpi~extended_fileformat", when="+mpi~extended_fileformat")
    depends_on("kvs+mpi+extended_fileformat", when="+mpi+extended_fileformat")
    depends_on("vtk@9.3.1~mpi", when="~mpi")
    depends_on("vtk@9.3.1+mpi", when="+mpi")

    patch("pbvr-conf.patch", when="~mpi")
    patch("pbvr-conf-mpi.patch", when="+mpi")
    patch("makefile-machine-gcc-omp.patch", when="~mpi")
    patch("makefile-machine-gcc-mpi-omp.patch", when="+mpi")
    patch("pbvr-server-main-tf-min.patch", when="@3.4.0")

    def patch(self):
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

    def edit(self, spec, prefix):
        # FIXME: Edit the Makefile if necessary
        # FIXME: If not needed delete this function
        # makefile = FileFilter("Makefile")
        # makefile.filter("CC = .*", "CC = cc")
        pass

    def build(self, spec, prefix):
        # Build Client
        with set_env(SPACK_KVS_DIR=str(spec['kvs'].prefix), VTK_VERSION="9.3", VTK_INCLUDE_PATH=str(spec['vtk'].prefix.include) + "/vtk-9.3", VTK_LIB_PATH=str(spec['vtk'].prefix.lib)):
            # Build Client
            qmake = Executable(spec['qt-base'].prefix.bin.qmake)
            build_dir = join_path(self.stage.source_path, 'Client/build')
            os.makedirs(build_dir)
            with working_dir(build_dir):
                qmake("../pbvr_client.pro")
                make()                                                                                              
            # Build Sevrer
            make('-C', 'CS_server')

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('CS_server/pbvr_server', prefix.bin)
        install('CS_server/Filter/pbvr_filter', prefix.bin)
        install('CS_server/KVSMLConverter/Example/Release/kvsml-converter', prefix.bin)
        install('Client/build/App/pbvr_client', prefix.bin)

        src = self.stage.source_path
        install_tree(os.path.join(src, 'Client/Shader'), os.path.join(prefix.bin, 'Shader'))
        install_tree(os.path.join(src, 'Client/Font'), os.path.join(prefix.bin, 'Font'))
