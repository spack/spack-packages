# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Kind(GoPackage):
    """
    kind is a tool for running local Kubernetes clusters using Docker
    container "nodes". It was primarily designed for testing Kubernetes
    itself, but may be used for local development or CI.
    """

    homepage = "https://kind.sigs.k8s.io"
    url = "https://github.com/kubernetes-sigs/kind/archive/refs/tags/v0.32.0.tar.gz"

    license("Apache-2.0")

    version("0.32.0", sha256="e2e1eb04fed4eed0715cc1c5938453d1edbf92b3c097ebec0a05d0903ba15508")

    depends_on("go@1.17:", type="build")

    depends_on("podman", type="run")
