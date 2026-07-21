# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from typing import List

from spack.package import Package, PackageBase, version


def check(condition, msg):
    """Raise an install error if condition is False."""
    if not condition:
        raise InstallError(msg)


class CmakeHints(Package):
    """A dummy package that uses cmake."""

    homepage = "https://www.example.com"
    url = "https://www.example.com/cmake-hints-1.0.tar.gz"
    version("1.0", md5="4cb3ff35b2472aae70f542116d616e63")

    def dependent_cmake_args(self, pkg: PackageBase) -> List[str]:
        return ['-DCMAKE_HINTS_ARG:STRING="Foo"']
