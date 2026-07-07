# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpencensusContext(PythonPackage):
    """OpenCensus Runtime Context."""

    homepage = "https://github.com/census-instrumentation/opencensus-python/tree/master/context/opencensus-context"
    url = "https://pypi.io/packages/py2.py3/o/opencensus-context/opencensus_context-0.1.1-py2.py3-none-any.whl"

    license("Apache-2.0")

    version("0.1.3", sha256="073bb0590007af276853009fac7e4bab1d523c3f03baf4cb4511ca38967c6039")
    version("0.1.1", sha256="1a3fdf6bec537031efcc93d51b04f1edee5201f8c9a0c85681d63308b76f5702")
