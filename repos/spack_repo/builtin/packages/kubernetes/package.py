# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Kubernetes(Package):
    """Kubernetes is an open source system for managing containerized
    applications across multiple hosts. It provides basic mechanisms
    for deployment, maintenance, and scaling of applications."""

    homepage = "https://kubernetes.io"
    url = "https://github.com/kubernetes/kubernetes/archive/refs/tags/v1.32.2.tar.gz"

    maintainers("alecbcs")

    license("Apache-2.0")

    version("1.36.1", sha256="1ebfa65cc95fbeb2ef4aad6832a3fae4edb88516e43b6437b69a40895803e0e8")
    version("1.35.5", sha256="c058972b598acb8fe08bc23e630e7e7582d86050bc78468c3026396a53ebc64b")
    version("1.35.4", sha256="46a0dead69674fb2bdf33f5ef1deadab123a96becfafef6043f399ae53761f4f")
    version("1.35.3", sha256="4374809bf135137568135384209f160acdab7372f2608fa60ca3513782db4f03")
    version("1.34.8", sha256="1eae3875e830dd72c1b600cdd4c12aca95449a951a95dcea368a9cb4bdf88ed4")
    version("1.34.7", sha256="764f22a1c1f6e90c2de1b3075a8c34f6d365d6f08c56eefe7020e5da20bdd3a3")
    version("1.34.6", sha256="cc88a9e51d05c048876a474feb6e353fd9e9fe64bb95f5cfced27a0b29d28790")
    version("1.33.12", sha256="4a33a8f8a098f245eefc39b5dd1e62feb81bcb76b470ca454a88fef6a688b6f6")
    version("1.33.11", sha256="52461ed85b0a0ac693f5d1841e90b8c65e91e9341c253c168968db2b9d53048e")
    version("1.33.10", sha256="a4dd3abd7da2f4f50ffe79583682a1f990856903b5d200948c12e69e632dd8ff")
    version("1.33.2", sha256="5588bb13437c0e6881f58ede88d200301c3d28b8ce124d58d3e7ed781d1d8d40")
    version("1.33.1", sha256="f89203e326de4c827a23ef9aa430d8a3133f62cfa1f5a894e8c85784f01bf055")
    version("1.32.13", sha256="3b48c21be36b5d7e387dcd7bd1914b223b3aeb55ae7ded4cdc5244dd943accc1")
    version("1.32.6", sha256="12a18280b2006a0e338a7ec470c2ec7f7c955bc81c7d265f955a2ed7e4bfb3f9")
    version("1.32.3", sha256="b1ed5abe78a626804aadc49ecb8ade6fd33b27ab8c23d43cd59dc86f6462ac09")
    version("1.31.14", sha256="ddca4935c8b6a3b4b6cd896c6b24bdd1b17d7a7004d12fca8b8b01ac727ddc5a")
    version("1.31.10", sha256="5b35c0dde86ca2ff870f6f20fd028d98a7e83ab2816afd20016896c39347e8c5")
    version("1.31.7", sha256="92005ebd010a8d4fe3a532444c4645840e0af486062611a4d9c8d862414c3f56")
    version("1.30.14", sha256="ad003cc133346d20ae091a540a42bf9adbcf124ec2959004a636fd1e9694f534")
    version("1.30.11", sha256="f30e4082b6a554d4a2bfedd8b2308a5e6012287e15bec94f72987f717bab4133")

    depends_on("c", type="build")

    with default_args(type="build"):
        depends_on("bash")
        depends_on("gmake")

        depends_on("go@1.26:", when="@1.36:")
        depends_on("go@1.25:", when="@1.35:")
        depends_on("go@1.24:", when="@1.33:")
        depends_on("go@1.23:", when="@1.32:")
        depends_on("go@1.22:", when="@1.30:")
        depends_on("go@1.21:", when="@1.29:")
        depends_on("go@1.20:", when="@1.27:")

    phases = ["build", "install"]

    def build(self, spec, prefix):
        components = [
            "cmd/kubeadm",
            "cmd/kubelet",
            "cmd/kube-apiserver",
            "cmd/kube-controller-manager",
            "cmd/kube-proxy",
            "cmd/kube-scheduler",
        ]

        make(f"WHAT={' '.join(components)}")

    def install(self, spec, prefix):
        install_tree("_output/bin", prefix.bin)
