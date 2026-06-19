# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class RocprofilerComputeViewer(CMakePackage):
    """ROCprof Compute Viewer (RCV) is a tool for visualizing and analyzing GPU
    thread trace data collected using rocprofv3."""

    homepage = "https://github.com/ROCm/rocprof-compute-viewer"
    git = "https://github.com/ROCm/rocprof-compute-viewer"

    tags = ["rocm"]
    maintainers("etiennemlb", "srekolam", "renjithravindrankannath", "afzpatel")
    license("MIT")

    def url_for_version(self, version):
        url = "https://github.com/ROCm/rocprof-compute-viewer/archive/refs/tags/{0}.tar.gz"
        return url.format(version)

    version("0.1.6", sha256="22de1dfb0dd2ac38cb67825f6477f13e271a8fea1cd91fa3d429f8f36a93992b")

    depends_on("cxx", type="build")

    depends_on("qt@5:6", type=("build", "link"))

    def cmake_args(self):
        args = [
            self.define("QT_VERSION_MAJOR", self.spec["qt"].version.up_to(1)),
            self.define("RCV_DISABLE_OPENGL", not self.spec["qt"].satisfies("+opengl")),
        ]
        return args

    def install(self, spec, prefix):
        with working_dir(self.build_directory):
            binaries = ["rocprof-compute-viewer"]
            mkdirp(prefix.bin)
            for binary in binaries:
                install(binary, prefix.bin)
