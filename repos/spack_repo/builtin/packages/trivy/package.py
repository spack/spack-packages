# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Trivy(GoPackage):
    """Trivy is a comprehensive and versatile security scanner."""

    homepage = "https://trivy.dev/"
    url = "https://github.com/aquasecurity/trivy/archive/refs/tags/v0.61.0.tar.gz"

    maintainers("RobertMaaskant")

    license("Apache-2.0", checked_by="RobertMaaskant")

    version("0.70.0", sha256="ff9ac06468aab89802388f16d1d179f4680db714afbf6a8132a417d288aa008e")
    version("0.69.3", sha256="3ca5fa62932273dd7eef3b6ec762625da42304ebb8f13e4be9fdd61545ca1773")
    version("0.64.1", sha256="9e23c90bd1afd9c369f1582712907e8e0652c8f5825e599850183af174c65666")
    version("0.64.0", sha256="95f958c5cf46e063660c241d022a57f99309208c9725d6031b048c9c414ecfa7")
    version("0.63.0", sha256="ac26dcb16072e674b8a3bffa6fbd817ec5baa125660b5c49d9ad8659e14d0800")
    version("0.62.1", sha256="1b8000f08876dd02203021414581275daa69db00fab731351dbcf2a008ebe82a")
    version("0.62.0", sha256="2b0b4df4bbfebde00a14a0616f5013db4cbba0f021a780a7e3b717a2c2978493")
    version("0.61.1", sha256="f6ad43e008c008d67842c9e2b4af80c2e96854db8009fba48fc37b4f9b15f59b")
    version("0.61.0", sha256="1e97b1b67a4c3aee9c567534e60355033a58ce43a3705bdf198d7449d53b6979")

    depends_on("go@1.25.8:", type="build", when="@0.70.0:")
    depends_on("go@1.25.6:", type="build", when="@0.69.1:")
    depends_on("go@1.24.4:", type="build", when="@0.64:")
    depends_on("go@1.24.2:", type="build", when="@0.62:")
    depends_on("go@1.24:", type="build")

    build_directory = "cmd/trivy"

    # Required to correctly set the version
    # https://github.com/aquasecurity/trivy/blob/v0.61.0/goreleaser.yml#L11
    @property
    def build_args(self):
        extra_ldflags = [f"-X 'github.com/aquasecurity/trivy/pkg/version/app.ver=v{self.version}'"]

        args = super().build_args

        if "-ldflags" in args:
            ldflags_index = args.index("-ldflags") + 1
            args[ldflags_index] = args[ldflags_index] + " " + " ".join(extra_ldflags)
        else:
            args.extend(["-ldflags", " ".join(extra_ldflags)])

        return args

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("@0.67.0:"):
            env.set("GOEXPERIMENT", "jsonv2")
