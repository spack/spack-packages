# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import platform
import re

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from llnl.util.filesystem import install_tree

from spack.package import *
from spack.util.environment import set_env


class Pbvr(MakefilePackage):
    """CS/IS-PBVR is a scientific visualization application designed
    based on Particle-Based Volume Rendering (PBVR). This application
    is capable of multivariate visualization and three-dimensional point cloud visualization
    in addition to standard visualization functions such as volume rendering
    and isosurfaces for 3D volume data obtained from simulations and measuring instruments.
    In addition, the framework for distributed processing of optimized PBVR is characterized
    by the ability to remotely visualize large-scale time-series volume data in remote locations
    at high speed. As a method of remote visualization, you can choose between
    client-server (CS) visualization, which visualizes volume data stored in remote storage,
    and in-situ (IS) visualization, which visualizes simulations simultaneously and
    in the same environment. This application is being developed at the Center
    for Computational Science and e-Systems of the Japan Atomic Energy Agency."""

    phases = ["build", "install"]

    homepage = "https://github.com/CCSEPBVR/CS-IS-PBVR"
    url = "https://github.com/CCSEPBVR/CS-IS-PBVR/archive/refs/tags/v3.5.0.tar.gz"

    maintainers("sakamoto-naohito")

    license("LGPL-3.0-only AND BSD-3-Clause")

    version("3.5.0", sha256="264c82d9e94b6f8477952ce2f80834332dbc9047db694f7f3ba2ab07c7c92aae")

    variant("client", default=True, description="Build Client Program")
    variant("mpi", default=True, description="Enable MPI Support")
    variant("extended_fileformat", default=True, description="Enable extended fileformat")

    depends_on("gmake", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("mpi", when="+mpi")
    depends_on("qt-base@6.2.4+opengl", when="+client")
    depends_on("qt-svg@6.2.4+widgets", when="+client")
    depends_on("vtk@9.3.1~mpi", when="~mpi")
    depends_on("vtk@9.3.1+mpi", when="+mpi")
    depends_on("freeglut", when="+client")

    patch("kvs-conf.patch", when="~client~extended_fileformat")
    patch("kvs-extended-fileformat-conf.patch", when="~client+extended_fileformat")
    patch("kvs-client-conf.patch", when="+client~extended_fileformat")
    patch("kvs-client-extended-fileformat-conf.patch", when="+client+extended_fileformat")

    patch("pbvr-conf.patch", when="~mpi")
    patch("pbvr-conf-mpi.patch", when="+mpi")
    patch("makefile-machine-gcc-omp.patch", when="~mpi")
    patch("makefile-machine-gcc-mpi-omp.patch", when="+mpi")

    requires("%cxx=gcc")

    def patch(self):
        source_dir = self.stage.source_path
        for root, dirs, files in os.walk(source_dir):
            for fname in files:
                path = os.path.join(root, fname)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                    if "KVS_DIR" in content:
                        filter_file("KVS_DIR", "SPACK_KVS_DIR", path)
                except Exception:
                    pass

    def build(self, spec, prefix):
        # Workaround for qmake's $$system() not capturing command output correctly.
        # This issue is caused by a known bug in certain Linux kernel versions.
        # To avoid it, Qt is built with the '-no-feature-forkfd_pidfd' option to disable
        # the use of new process management features that rely on pidfd.
        # Note: Red Hat fixed this kernel issue in version 4.18.0-392 and later.
        is_rhel8_bug_fixed = False
        release_str = platform.uname().release
        match = re.match(r"^(\d+\.\d+\.\d+)-([\d\.]+)\.el8", release_str)
        if match and not is_rhel8_bug_fixed:
            base_version = match.group(1)
            build_number = match.group(2).split(".")[0]
            full_version = f"{base_version}.{build_number}"
            if Version(full_version) < Version("4.18.0.392"):
                raise InstallError(
                    f"The kernel version of this system is ${full_version}.\n"
                    "You get an error when running qmake after installing qt-base"
                    " on Red Hat Enterprise Linux 8 versions older than 8.7.\n"
                    "You need to fix the package.py file for qt-base,"
                    " so please refer to the following URL.\n"
                    "https://github.com/CCSEPBVR/CS-IS-PBVR/wiki/BuildforLinux_JP"
                )

        with set_env(
            KVS_CPP="g++",
            SPACK_KVS_DIR=prefix,
            VTK_VERSION="9.3",
            VTK_INCLUDE_PATH=str(spec["vtk"].prefix.include) + "/vtk-9.3",
            VTK_LIB_PATH=str(spec["vtk"].prefix.lib),
        ):
            # Build KVS
            build_dir = join_path(self.stage.source_path, "KVS")
            with working_dir(build_dir):
                make()
                make("install")

            # Build Client
            if "+client" in spec:
                qmake = Executable(spec["qt-base"].prefix.bin.qmake)
                build_dir = join_path(self.stage.source_path, "Client/build")
                os.makedirs(build_dir)
                with working_dir(build_dir):
                    qmake("../pbvr_client.pro")
                    make()

            # Build Sevrer
            with working_dir(join_path(self.stage.source_path, "CS_server")):
                make()

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("CS_server/pbvr_server", prefix.bin)
        install("CS_server/Filter/pbvr_filter", prefix.bin)
        install("CS_server/KVSMLConverter/Example/Release/kvsml-converter", prefix.bin)

        if "+client" in spec:
            install("Client/build/App/pbvr_client", prefix.bin)
            src = self.stage.source_path
            install_tree(
                join_path(src, "Client/build/App/Shader"), join_path(prefix.bin, "Shader")
            )
            install_tree(
                join_path(src, "Client/build/App/Font"), join_path(prefix.bin, "Font")
            )
