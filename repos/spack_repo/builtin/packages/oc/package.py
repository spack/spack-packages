# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Oc(GoPackage):
    """The OpenShift Command Line, part of OKD."""

    homepage = "https://okd.io"
    git = "https://github.com/openshift/oc.git"

    maintainers("alecbcs")

    license("Apache-2.0")

    version("main", branch="main")
    version("4.21.0-202601121715", commit="345800dc3c4164fbca313c1cbfb383f262547903")

    variant("gssapi", default=False, description="Enable GSSAPI authentication support")

    depends_on("c", type="build")
    depends_on("go@1.22.5:", type="build", when="@4.20:")

    depends_on("gnupg")
    depends_on("libassuan")

    depends_on("krb5", when="+gssapi")

    build_directory = "cmd/oc"
    cgo_enabled = True

    @property
    def build_args(self):
        args = super().build_args
        tags = ["include_gcs", "include_oss", "containers_image_openpgp"]

        if self.spec.satisfies("+gssapi"):
            tags.append("gssapi")

        args.extend(["-tags", " ".join(tags)])
        return args
