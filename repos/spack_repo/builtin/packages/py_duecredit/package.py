# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDuecredit(PythonPackage):
    """Publications (and donations) tracer."""

    homepage = "https://github.com/duecredit/duecredit"
    pypi = "duecredit/duecredit-0.9.1.tar.gz"

    license("BSD-2-Clause-FreeBSD")

    version("0.11.2", sha256="7b5c1ae10927f9e02cf4d54e2c74a8aa00cd29c38d637defe3c948d3d8e9f33a")
    version("0.10.2", sha256="fe73a20e4fbb2d972ba01edf37dec1b0ba1e646efe5ef4ccaf0c6724ca287d42")
    version("0.9.2", sha256="0e0fd87e9e46ce6c94308e9f780c203fe836d89628404f8bf5af96a7457bed1c")
    version("0.9.1", sha256="f6192ce9315b35f6a67174761291e61d0831e496e8ff4acbc061731e7604faf8")
    version("0.6.5", sha256="da3746c24f048e1b2e9bd15c001f0f453a29780ebb9d26367f478a63d15dee9b")

    with default_args(type="build"):
        depends_on("py-setuptools@77.0.3:", when="@0.11:")
        depends_on("py-setuptools")
        depends_on("py-setuptools-scm", when="@0.11:")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:", when="@0.11:")
        depends_on("python@3.8:", when="@0.10:")

        depends_on("py-citeproc-py@0.5:", when="@11:")
        depends_on("py-citeproc-py@0.4:")
        depends_on("py-looseversion", when="@0.10:")
        depends_on("py-packaging", when="@0.10:")
        depends_on("py-requests")

        # Historical dependencies
        depends_on("py-six", when="@:0.92")
        depends_on("py-importlib-metadata", when="@0.9 ^python@:3.7")
