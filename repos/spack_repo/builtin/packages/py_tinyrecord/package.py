# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTinyrecord(PythonPackage):
    """Atomic transactions for TinyDB."""

    homepage = "https://github.com/eugene-eeo/tinyrecord"
    pypi = "tinyrecord/tinyrecord-0.2.0.tar.gz"

    license("MIT")

    version("0.2.0", sha256="eb6dc23601be359ee00f5a3d31a46adf3bad0a16f8d60af216cd67982ca75cf4")

    depends_on("py-setuptools", type="build")
