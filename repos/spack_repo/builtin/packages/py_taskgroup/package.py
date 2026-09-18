# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTaskgroup(PythonPackage):
    """Backport of asyncio.TaskGroup, asyncio.Runner and asyncio.timeout."""

    homepage = "https://github.com/graingert/taskgroup"
    pypi = "taskgroup/taskgroup-0.2.2.tar.gz"

    license("MIT")

    version("0.2.2", sha256="078483ac3e78f2e3f973e2edbf6941374fbea81b9c5d0a96f51d297717f4752d")

    depends_on("py-flit-core@3.2:3", type="build")
