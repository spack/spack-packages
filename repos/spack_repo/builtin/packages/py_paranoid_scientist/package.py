# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyParanoidScientist(PythonPackage):
    """Runtime verification and automated testing for scientific code."""

    homepage = "https://github.com/mwshinn/paranoidscientist"
    pypi = "paranoid_scientist/paranoid_scientist-0.2.3.tar.gz"

    license("MIT")

    version("0.2.3", sha256="074b40185a7d923373218144eaa7799b0b78b660f0975a313696caa972016929")

    with default_args(type="build"):
        depends_on("py-setuptools")
