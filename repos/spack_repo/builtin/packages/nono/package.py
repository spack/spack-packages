# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Nono(CargoPackage):
    """Runtime security - zero trust, zero setup, zero latency sandboxing."""

    homepage = "https://nono.sh/"
    url = "https://github.com/nolabs-ai/nono/archive/refs/tags/v0.82.0.tar.gz"

    maintainers("kwryankrattiger")

    license("APACHE-2.0", checked_by="kwryankrattiger")

    version("0.82.0", sha256="7a2db3faa14a6218d336d62ed14e0447a9876c3a26478dab25854929774cd680")

    executables = [r"^nono$"]
    build_directory = "crates/nono-cli"
