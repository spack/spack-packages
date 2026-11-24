# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.packages.qt_base.package import QtBase, QtPackage

from spack.package import *


class QtWebsockets(QtPackage):
    """WebSocket is a web-based protocol designed to enable a two-way
    interactive communication session between a client application
    and a remote host. It enables the two entities to send data back
    and forth if the initial handshake succeeds."""

    url = QtPackage.get_url(__qualname__)
    git = QtPackage.get_git(__qualname__)
    list_url = QtPackage.get_list_url(__qualname__)

    maintainers("wdconinc")

    license("BSD-3-Clause")

    version("6.11.2", commit="3eab06de7076a83514e98c2403baa433d137b013", submodules=True)
    version("6.11.1", commit="451920600d7f0b8a4b458bba56a2dd303e587026", submodules=True)
    version("6.10.2", commit="2b969cb983d1e22df0e6fc6ece54043942090bd8", submodules=True)
    version("6.10.1", commit="ba2ada87ef9027650efb6251e7fc05519f484e95", submodules=True)
    version("6.10.0", commit="a81ae8a7ca0f152e1d30dcf70cc65a63e8fd5c36", submodules=True)
    version("6.9.3", commit="5071d82808f292c08de30d1e6e54cf83ffb218ba", submodules=True)
    version("6.9.2", commit="9f5916fb7af335f173b63bc33b35954a0ae81348", submodules=True)
    version("6.9.1", commit="aed12a0013dffe3e0cd564fb23e83299affda941", submodules=True)
    version("6.9.0", commit="0707110b34e99ae48b61dbd3087f2edfcc940f93", submodules=True)
    version("6.8.3", commit="621eb11be893be975d0ddd5b1230838bb0bf8810", submodules=True)
    version("6.8.2", commit="f98fdcb40cc9a13cad3a3e2ec6fac915057771ec", submodules=True)
    version("6.8.1", commit="0ec0f302905b2154f8ccec4a761fdccf07692c66", submodules=True)
    version("6.8.0", commit="6f1afa8a1e9487813e06fb55ee14baa5dc76b8bb", submodules=True)
    version("6.7.3", commit="ceb4d5996aac377fa6622b418de0e9ffa1b63588", submodules=True)
    version("6.7.2", commit="6d040c4762d63746d8c98f65bb3c93acd5df956f", submodules=True)

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("qt-base +network")

    for _v in QtBase.versions:
        v = str(_v)
        depends_on("qt-base@" + v, when="@" + v)

    def cmake_args(self):
        return super().cmake_args() + []
