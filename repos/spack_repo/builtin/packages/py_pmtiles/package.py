# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *

class PyPmtiles(PythonPackage):

    homepage = "https://docs.protomaps.com/"
    pypi = "pmtiles/pmtiles-3.5.0.tar.gz"
    git = "https://github.com/protomaps/PMTiles"

    license("BSD-3-Clause", checked_by="Chrismarsh")

    version("3.5.0", sha256="2b849ede4e006aa0ba9d508a4d77400dd5117d5da74346e057dc9e28bad8e9f0")

    # https://github.com/protomaps/PMTiles/blob/main/python/pmtiles/setup.py
    depends_on("py-setuptools", type="build")
