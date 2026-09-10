# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Autossh(AutotoolsPackage):
    """autossh is a program to start a copy of ssh and monitor it,
    restarting it as necessary should it die or stop passing traffic."""

    homepage = "https://www.harding.motd.ca/autossh/"
    url = "https://www.harding.motd.ca/autossh/autossh-1.4g.tgz"

    license("custom")

    version("1.4g", sha256="5fc3cee3361ca1615af862364c480593171d0c54ec156de79fc421e31ae21277")

    depends_on("c", type="build")  # generated

    depends_on("libnsl")
    depends_on("openssh")
