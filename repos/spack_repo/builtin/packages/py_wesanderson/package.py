# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyWesanderson(PythonPackage):
    """color palettes from Wes Anderson films, based on Karthik Ram's R version."""

    homepage = "https://pypi.org/project/wesanderson"
    pypi = "wesanderson/wesanderson-0.0.3.tar.gz"

    version("0.0.4", sha256="5488539b772d6b355c4cc8877f7f3c503f01cc2624181e98567586390f609bfd")
    version("0.0.3", sha256="76f5df93b51babcb6e4ca47776846aeefa0234054fee76cbbbae74f9658aabfa")

    depends_on("py-setuptools", type="build")
