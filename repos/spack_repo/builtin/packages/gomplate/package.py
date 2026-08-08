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

    version("5.2.0", sha256="fb08872f54f776863a30adcd58dce0437529d0e6a468839d107803bbff1d0b23")
    version("5.1.0", sha256="b6763aaf2c52a2e57a02f5e4cae199166b1ae8df8beb43ef5c927bb10ca775fc")
    version("4.3.3", sha256="d15c66230d72bdc13b0155f28d391c55cac45b7fdbe1ff4a73db8ee263471a3d")

    depends_on("go@1.26:", type="build", when="@5.1.0:")
    depends_on("go@1.25:", type="build", when="@5:")
    depends_on("go@1.24.5:", type="build")

    build_directory = "cmd/gomplate"

    @property
    def ldflags(self):
        version_path = go("list", "../../version", output=str).strip()
        return [f"-X {version_path}.Version={self.spec.version}"]
