# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os.path
from typing import List, Optional

from spack.package import PackageBase, join_url


class GNUMirrorPackage(PackageBase):
    """Mixin that takes care of setting url and mirrors for GNU packages."""

    #: Path of the package in a GNU mirror
    gnu_mirror_path: Optional[str] = None

    #: Depth of url spidering to search up the path for new versions
    list_depth: int = 0

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
        self._ensure_gnu_mirror_path_is_set_or_raise()
        # narrow the type for the checker: the call above raises when None
        if self.gnu_mirror_path is None:
            return []
        return [join_url(m, self.gnu_mirror_path, resolve_href=True) for m in self.base_mirrors]

    @property
    def list_url(self):
        if self.gnu_mirror_path is None:
            return None

        mirror_dir = os.path.dirname(self.gnu_mirror_path)
        # Use the canonical ftp.gnu.org mirror for listing; the redirecting
        # ftpmirror.gnu.org does not reliably serve directory indexes.
        return join_url("https://ftp.gnu.org/gnu/", mirror_dir, resolve_href=True)

    def _ensure_gnu_mirror_path_is_set_or_raise(self):
        if self.gnu_mirror_path is None:
            cls_name = type(self).__name__
            msg = "{0} must define a `gnu_mirror_path` attribute [none defined]"
            raise AttributeError(msg.format(cls_name))
