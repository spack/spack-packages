# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTypesProtobuf(PythonPackage):
    """Typing stubs for protobuf"""

    homepage = "https://github.com/python/typeshed"
    pypi = "types-protobuf/types-protobuf-4.23.0.2.tar.gz"

    license("Apache-2.0", checked_by="V-Karch")

    version("4.23.0.2", sha256="1066b069d4f0e09bdebb64ca4f35cc6b8accf52f808368046ccec96744af0375")

    depends_on("py-setuptools", type="build")
