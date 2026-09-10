# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFluflLock(PythonPackage):
    """NFS-safe file locking with timeouts for POSIX and Windows"""

    homepage = "https://flufllock.readthedocs.io"
    pypi = "flufl.lock/flufl_lock-9.0.0.tar.gz"

    license("Apache-2.0")

    version("9.0.0", sha256="270a46e754af3937735cdd4f8a8f43a2dc4e5c40a24fdf972f5dc6db0862e8bb")
    version("5.0.4", sha256="09ffef831d57c4d182e398e97bb74ad8c8ffbd1710175a5a0b0f057095db12f1")
    version("5.0.3", sha256="94df161caa489d74afc26df8c0b640770923ecc0c6c5d331fbeabe7b91d306cb")
    version("3.2", sha256="a8d66accc9ab41f09961cd8f8db39f9c28e97e2769659a3567c63930a869ff5b")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("python@3.10:", when="@9:", type=("build", "run"))
    depends_on("py-setuptools", when="@:5.0.4", type="build")
    depends_on("py-hatchling", when="@9:", type="build")
    depends_on("py-atpublic", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-typing-extensions", when="@:5.0.4^python@:3.7", type=("build", "run"))

    def url_for_version(self, version):
        url = "https://pypi.io/packages/source/f/flufl.lock/{0}-{1}.tar.gz"
        if version >= Version("8"):
            filename = "flufl_lock"
        else:
            filename = "flufl.lock"
        return url.format(filename, version)
