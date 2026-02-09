# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMailchecker(PythonPackage):
    """Cross-language email validation. Backed by a database of thousands
    throwable email providers"""

    homepage = "https://github.com/FGRibreau/mailchecker"
    pypi = "mailchecker/mailchecker-4.0.3.tar.gz"

    license("MIT")

    version("4.0.9", sha256="ea94bfcd06d100fef5dc126f51b27269c7285e6939ab49281f21896cfa2160e7")
    version("4.0.3", sha256="00dbe9739c754366233eb3887c5deef987672482a26e814314c3e749fc7b1d1f")

    depends_on("py-setuptools", type="build")
