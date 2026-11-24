# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.userspace_rcu.package import UserspaceRcu

from spack.package import *


class Liburcu(UserspaceRcu):
    __doc__ = f"""{UserspaceRcu.__doc__}

    This package is a duplicate of ``userspace-rcu``, the upstream project name.
    It is kept as a thin, fully deprecated alias so existing specs that
    reference ``liburcu`` continue to resolve. Build logic is inherited from
    :class:`UserspaceRcu`; use ``userspace-rcu`` for new work.
    """

    _name = "liburcu"

    # Redeclare every UserspaceRcu version as deprecated, so a version added
    # only to the canonical package cannot appear here without deprecated=True.
    for v, vargs in UserspaceRcu.versions.items():
        version(str(v), **dict(vargs, deprecated=True))
