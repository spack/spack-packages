# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from typing import List,  Optional

from spack.url import parse_name_and_version
from spack.package import PackageBase, classproperty, join_url


class GNUMirrorPackage(PackageBase):
    """Mixin that takes care of setting url and mirrors for GNU packages."""

    @classproperty
    def gnu_mirror_path(cls) -> str:
        """Path of the package in a GNU mirror."""
        cls_name = type(self).__name__
        msg = "{0} must define a `gnu_mirror_path` attribute [none defined]"
        raise NotImplementedError(msg.format(cls_name))

    #: List of GNU mirrors used by Spack
    base_mirrors = [
        "https://ftpmirror.gnu.org/",
        "https://ftp.gnu.org/gnu/",
        # Fall back to http if https didn't work (for instance because
        # Spack is bootstrapping curl)
        "http://ftpmirror.gnu.org/",
    ]

    @property
    def urls(self) -> List[str]:
        return [join_url(m, self.gnu_mirror_path, resolve_href=True) for m in self.base_mirrors]
