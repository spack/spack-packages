# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.util.environment import set_env
from spack_repo.builtin.build_systems.generic import Package

class Kvs(Package):
    """Kyoto Visualization System (KVS) is a multi-platform, open-source C++ library
    for developing scientific visualization applications. KVS provides various classes
    and interfaces, such as isosurace extraction, streamlines and volume rendering,
    to visualize medical data obtained by computerized tomography or magnetic resonance imaging,
    numerical data from computational fluid dynamics and so on."""

    homepage = "https://github.com/TO0603/KVS"
    url = "https://github.com/TO0603/KVS/archive/refs/tags/forDev.tar.gz"

    maintainers("sakamoto-naohito")

    license("BSD-3-Clause")

    version("3.1", sha256="0ab932b0273f7f10972c0cb37de775a2f3923ca8ae26187d1b8c52847147ed84")

    variant("mpi", default=True, description="Enable MPI Support")
    variant("extended_fileformat", default=True, description="Enable extended fileformat")

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
        if "+extended_fileformat" in spec:
            with set_env(SPACK_KVS_DIR=str(prefix), VTK_INCLUDE_PATH=str(spec['vtk'].prefix.include) + "/vtk-9.3", VTK_LIB_PATH=str(spec['vtk'].prefix.lib)):
                make()
                make("install")
        else:
            with set_env(SPACK_KVS_DIR=str(prefix)):
                make()
                make("install")

