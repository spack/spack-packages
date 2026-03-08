# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTblib(PythonPackage):
    """Traceback fiddling library. Allows you to pickle tracebacks."""

    homepage = "https://github.com/ionelmc/python-tblib"
    pypi = "tblib/tblib-1.6.0.tar.gz"

    license("BSD-2-Clause")

    version("3.1.0", sha256="06404c2c9f07f66fee2d7d6ad43accc46f9c3361714d9b8426e7f47e595cd652")  # FIXME
    version("3.0.0", sha256="93622790a0a29e04f0346458face1e144dc4d32f493714c6c3dff82a4adb77e6")  # FIXME
    version("2.0.0", sha256="a6df30f272c08bf8be66e0775fad862005d950a6b8449b94f7c788731d70ecd7")  # FIXME
    version("1.7.0", sha256="059bd77306ea7b419d4f76016aef6d7027cc8a0785579b5aad198803435f882c")  # FIXME
    version("1.6.0", sha256="229bee3754cb5d98b4837dd5c4405e80cfab57cb9f93220410ad367f8b352344")
    version("1.4.0", sha256="bd1ad564564a158ff62c290687f3db446038f9ac11a0bf6892712e3601af3bcd")

    depends_on("python@2.7:2.8,3.5:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
