# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMsgspec(PythonPackage):
    """A fast serialization and validation library, with builtin support
    for JSON, MessagePack, YAML, and TOML."""

    pypi = "msgspec/msgspec-0.19.0.tar.gz"

    license("BSD-3-Clause")

    version("0.19.0", sha256="604037e7cd475345848116e89c553aa9a233259733ab51986ac924ab1b976f8e")

    depends_on("py-setuptools", type="build")
