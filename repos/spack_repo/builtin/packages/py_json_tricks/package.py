# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyJsonTricks(PythonPackage):
    """Extra features for Python's JSON: comments, order, numpy, pandas,
    datetimes, and many more! Simple but customizable."""

    homepage = "https://github.com/mverleg/pyjson_tricks"
    pypi = "json_tricks/json_tricks-3.17.3.tar.gz"

    license("BSD-3-Clause")

    version("3.17.3", sha256="71561eedad7c22dde019e9a38ff8c46ebd91da789e31e2513f627dd2cbbdbf56")

    depends_on("py-setuptools", type="build")
