# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBinary(PythonPackage):
    """binary provides a bug-free and easy way to convert between and within binary (IEC) and
    decimal (SI) units.
    """

    homepage = "https://github.com/ofek/binary"
    pypi = "binary/binary-1.0.2.tar.gz"

    license("MIT OR Apache-2.0")

    version("1.0.2", sha256="a6ba0af9579098b18dd2ec0b08bd409d8a5c4e5e5a301104b053ad40137264a8")

    with default_args(type="build"):
        depends_on("py-hatchling")
        depends_on("py-hatch-vcs")
