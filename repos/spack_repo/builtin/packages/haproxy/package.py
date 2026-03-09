# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Haproxy(MakefilePackage):
    """
    HAProxy is a single-threaded, event-driven, non-blocking engine
    combining a very fast I/O layer with a priority-based scheduler.
    """

    homepage = "https://www.haproxy.org"
    url = "https://www.haproxy.org/download/2.1/src/haproxy-2.1.0.tar.gz"

    version("3.0.17", sha256="58492710f8c82d81988e94f1188afc84eafd05d77393732241b252a8d14bd8a3")

    # All 2.1.x versions are affected by:
    # CVE-2023-25725, CVE-2023-45539
    with default_args(deprecated=True):
        version("2.1.12", sha256="acebbf932f2703ee287d6e945bd845cde8c9db9a13f7cbb2a99671499c558056")
        version("2.1.1", sha256="57e75c1a380fc6f6aa7033f71384370899443c7f4e8a4ba289b5d4350bc76d1a")
        version("2.1.0", sha256="f268efb360a0e925137b4b8ed431f2f8f3b68327efb2c418b266e535d8e335a0")

    depends_on("c", type="build")  # generated

    def url_for_version(self, version):
        url = "https://www.haproxy.org/download/{0}/src/haproxy-{1}.tar.gz"
        return url.format(version.up_to(2), version)

    def build(self, spec, prefix):
        make("TARGET=generic", "PREFIX=" + prefix)

    def install(self, spec, prefix):
        install_tree(".", prefix)
