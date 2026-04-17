# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Kubectl(GoPackage):
    """
    Kubectl is a command-line interface for Kubernetes clusters.
    """

    homepage = "https://kubernetes.io"
    url = "https://github.com/kubernetes/kubernetes/archive/refs/tags/v1.32.2.tar.gz"

    maintainers("alecbcs")

    license("Apache-2.0")

    version("1.35.3", sha256="4374809bf135137568135384209f160acdab7372f2608fa60ca3513782db4f03")
    version("1.34.6", sha256="cc88a9e51d05c048876a474feb6e353fd9e9fe64bb95f5cfced27a0b29d28790")
    version("1.33.10", sha256="a4dd3abd7da2f4f50ffe79583682a1f990856903b5d200948c12e69e632dd8ff")
    version("1.33.4", sha256="308f9ca06aa3b7c16021006cf831681a002f25a7c8c4a1809d354d9e0c79fc72")
    version("1.33.2", sha256="5588bb13437c0e6881f58ede88d200301c3d28b8ce124d58d3e7ed781d1d8d40")
    version("1.33.1", sha256="f89203e326de4c827a23ef9aa430d8a3133f62cfa1f5a894e8c85784f01bf055")
    version("1.32.13", sha256="3b48c21be36b5d7e387dcd7bd1914b223b3aeb55ae7ded4cdc5244dd943accc1")
    version("1.32.8", sha256="8adb887537e654c106b5ad11d5891cba2d2458004b58167a9245d9847ed9ea4b")
    version("1.32.6", sha256="12a18280b2006a0e338a7ec470c2ec7f7c955bc81c7d265f955a2ed7e4bfb3f9")
    version("1.32.3", sha256="b1ed5abe78a626804aadc49ecb8ade6fd33b27ab8c23d43cd59dc86f6462ac09")
    version("1.31.14", sha256="ddca4935c8b6a3b4b6cd896c6b24bdd1b17d7a7004d12fca8b8b01ac727ddc5a")
    version("1.31.12", sha256="29a6b9cc83bd44a1b2aa26c496d45e71db065327df06751c61815c4ca3e9229f")
    version("1.31.10", sha256="5b35c0dde86ca2ff870f6f20fd028d98a7e83ab2816afd20016896c39347e8c5")
    version("1.31.7", sha256="92005ebd010a8d4fe3a532444c4645840e0af486062611a4d9c8d862414c3f56")
    version("1.30.14", sha256="ad003cc133346d20ae091a540a42bf9adbcf124ec2959004a636fd1e9694f534")
    version("1.30.11", sha256="f30e4082b6a554d4a2bfedd8b2308a5e6012287e15bec94f72987f717bab4133")

    depends_on("bash", type="build")
    depends_on("go@1.25:", type="build", when="@1.35:")
    depends_on("go@1.24:", type="build", when="@1.33:")
    depends_on("go@1.23:", type="build", when="@1.32:")
    depends_on("go@1.22:", type="build", when="@1.30:")
    depends_on("go@1.21:", type="build", when="@1.29:")
    depends_on("go@1.20:", type="build", when="@1.27:")

    build_directory = "cmd/kubectl"

    # Required to correctly set the version
    # Method discovered by following the trail below
    #
    # 1. https://github.com/kubernetes/kubernetes/blob/v1.32.2/Makefile#L1
    # 2. https://github.com/kubernetes/kubernetes/blob/v1.32.2/build/root/Makefile#L97
    # 3. https://github.com/kubernetes/kubernetes/blob/v1.32.2/hack/make-rules/build.sh#L25
    # 4. https://github.com/kubernetes/kubernetes/blob/v1.32.2/hack/lib/init.sh#L61
    # 5. https://github.com/kubernetes/kubernetes/blob/v1.32.2/hack/lib/version.sh#L151-L183
    @property
    def build_args(self):
        kube_ldflags = [
            f"-X 'k8s.io/client-go/pkg/version.gitVersion=v{self.version}'",
            f"-X 'k8s.io/client-go/pkg/version.gitMajor={self.version.up_to(1)}'",
            f"-X 'k8s.io/client-go/pkg/version.gitMinor={str(self.version).split('.')[1]}'",
            f"-X 'k8s.io/component-base/version.gitVersion=v{self.version}'",
            f"-X 'k8s.io/component-base/version.gitMajor={self.version.up_to(1)}'",
            f"-X 'k8s.io/component-base/version.gitMinor={str(self.version).split('.')[1]}'",
        ]

        args = super().build_args

        if "-ldflags" in args:
            ldflags_index = args.index("-ldflags") + 1
            args[ldflags_index] = args[ldflags_index] + " " + " ".join(kube_ldflags)
        else:
            args.extend(["-ldflags", " ".join(kube_ldflags)])

        return args
