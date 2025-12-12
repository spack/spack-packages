# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySdnotify(PythonPackage):
    """This is a pure Python implementation of the systemd sd_notify protocol."""

    homepage = "https://github.com/bb4242/sdnotify"
    pypi = "sdnotify/sdnotify-0.3.2.tar.gz"

    license("MIT", checked_by="bgeltz")

    version("0.3.2", sha256="73977fc746b36cc41184dd43c3fe81323e7b8b06c2bb0826c4f59a20c56bb9f1")

    depends_on("python@3", type=("build", "run"))
    depends_on("py-setuptools", type="build")
