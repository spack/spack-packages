# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Velero(GoPackage):
    """
    Velero is an open source tool to safely backup and restore, perform disaster recovery,
    and migrate Kubernetes cluster resources and persistent volumes.
    """

    homepage = "https://velero.io/"
    url = "https://github.com/velero-io/velero/archive/refs/tags/v1.18.0.tar.gz"

    maintainers("RobertMaaskant")

    license("Apache-2.0", checked_by="RobertMaaskant")

    version("1.18.0", sha256="e94e51437b7cc54b633fcd253d5003494382e4de69c34992463588f248ba409c")

    depends_on("go@1.25.7:", type="build", when="@1.18.0:")

    depends_on("kubectl", type="run")

    build_directory = "cmd/velero"

    # Required to correctly set the version
    # Based on https://github.com/velero-io/velero/blob/v1.18.0/Dockerfile#L35
    @property
    def ldflags(self):
        return [f"-X 'github.com/vmware-tanzu/velero/pkg/buildinfo.Version=v{self.spec.version}'"]
