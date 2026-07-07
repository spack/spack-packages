# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Libmodbus(AutotoolsPackage):
    """libmodbus is a free software library to send/receive data
    according to the Modbus protocol.This library is written in C
    and supports RTU (serial) and TCP (Ethernet) communications."""

    homepage = "https://libmodbus.org/"
    url = "https://github.com/stephane/libmodbus/releases/download/v3.1.10/libmodbus-3.1.10.tar.gz"

    license("LGPL-2.1-or-later")

    version("3.1.10", sha256="899be4e25ab7fe5799d43f9567510d6f063d2e8f56136dd726b6fd976f9b2253")

    depends_on("c", type="build")  # generated
