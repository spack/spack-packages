# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBackportsSslMatchHostname(PythonPackage):
    """The ssl.match_hostname() function from Python 3.5"""

    pypi = "backports.ssl_match_hostname/backports.ssl_match_hostname-3.5.0.1.tar.gz"

    version("3.7.0.1", sha256="bb82e60f9fbf4c080eabd957c39f0641f0fc247d9a16e31e26d594d8f42b9fd2")
    version("3.5.0.1", sha256="502ad98707319f4a51fa2ca1c677bd659008d27ded9f6380c79e8932e38dcdf2")

    # pip silently replaces distutils with setuptools
    depends_on("py-setuptools", type="build")
