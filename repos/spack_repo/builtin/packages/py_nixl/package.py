# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNixl(PythonPackage, CudaPackage):
    """NVIDIA Inference Xfer Library (NIXL)"""

    homepage = "https://github.com/ai-dynamo/nixl"
    url = "https://github.com/ai-dynamo/nixl/archive/refs/tags/0.4.1.tar.gz"

    license("Apache-2.0")

    depends_on("c")
    depends_on("cxx")

    version("0.5.0", sha256="694cfc209b659cf235caeda1d11bc875cf4bc95a19d2028fe25abcf019ee1246")
    version("0.4.1", sha256="54672c6d4b0a303690880526c2dbff4ddc45ad7b8321ca602240a316abd86508")

    variant("etcd", description="Use ETCD for metadata distribution and coordination")

    with default_args(type="build"):
        # https://github.com/ai-dynamo/nixl/blob/0.4.1/pyproject.toml
        depends_on("py-meson-python")
        depends_on("py-pybind11")
        depends_on("patchelf")
        depends_on("py-pyyaml")
        depends_on("py-types-pyyaml")
        depends_on("py-pytest")

        # for its subproject abseil-cpp
        depends_on("pkgconfig")
        depends_on("cmake")

    with default_args(type=["build", "run"]):
        # https://github.com/ai-dynamo/nixl/blob/0.4.1/pyproject.toml
        depends_on("py-torch+cuda")
        depends_on("py-numpy")

    depends_on("ucx+cuda")
    depends_on("etcd-cpp-apiv3", wwhen="+etcd")

    requires("+cuda")

    def config_settings(self, spec, prefix):
        settings = {
            "setup-args": {
                "-Ducx_path": spec["ucx"].prefix,
                "-Dgds_path": spec["cuda"].prefix,
                "-Dcudapath_inc": spec["cuda"].prefix.include,
                "-Dcudapath_lib": spec["cuda"].prefix.lib64,
                "-Dcudapath_stub": spec["cuda"].prefix.lib64.stubs,
            }
        }
        if self.spec.satisfies("+etcd"):
            settings["setup-args"]["-Detcd_inc_path"]=spec["etcd"].prefix.include
            settings["setup-args"]["-Detcd_lib_path"]=spec["etcd"].prefix.lib
        return settings
