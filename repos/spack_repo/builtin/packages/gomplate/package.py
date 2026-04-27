# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Gomplate(GoPackage):
    """
    gomplate is a template renderer which supports a growing list of datasources,
    such as: JSON (including EJSON - encrypted JSON), YAML, AWS EC2 metadata, Hashicorp
    Consul and Hashicorp Vault secrets.
    """

    homepage = "https://gomplate.ca/"
    url = "https://github.com/hairyhenderson/gomplate/archive/refs/tags/v4.3.3.tar.gz"

    maintainers("ebagrenrut")

    license("MIT")

    version("4.3.3", sha256="d15c66230d72bdc13b0155f28d391c55cac45b7fdbe1ff4a73db8ee263471a3d")

    depends_on("go@1.24.5:", type="build")

    def build(self, spec, prefix):
        # Retrieve the "path" (in Go namespace parlance) to the version object because
        # we need to set its Version attribute. This is similar to what is done in the
        # gomplate Makefile.
        gomplate_version_path = self.module.go("list", "./version", output=str).strip()
        with working_dir(f"{join_path(self.build_directory, 'cmd', self.name)}"):
            # When building, set gomplate's version.Version to the value in the version
            # object for this package
            self.module.go(
                "build",
                "-p",
                str(make_jobs),
                "-ldflags",
                f"-s -w -X {gomplate_version_path}.Version={self.version}",
                "-o",
                f"{join_path(self.build_directory, self.name)}",
            )
