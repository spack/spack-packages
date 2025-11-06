# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyYarl(PythonPackage):
    """The module provides handy URL class for URL parsing and changing."""

    homepage = "https://github.com/aio-libs/yarl"
    pypi = "yarl/yarl-1.4.2.tar.gz"

    license("Apache-2.0")

    version("1.22.0", sha256="bebf8557577d4401ba8bd9ff33906f1376c877aa78d1fe216ad01b4d6745af71")
    version("1.18.3", sha256="ac1801c45cbf77b6c99242eeff4fffb5e4e73a800b5c4ad4fc0be5def634d2e1")
    version("1.9.2", sha256="04ab9d4b9f587c06d801c2abfe9317b77cdf996c65a90d5e84ecc45010823571")
    version("1.8.1", sha256="af887845b8c2e060eb5605ff72b6f2dd2aab7a761379373fd89d314f4752abbf")
    version("1.7.2", sha256="45399b46d60c253327a460e99856752009fcee5f5d3c80b2f7c0cae1c38d56dd")
    version("1.4.2", sha256="58cd9c469eced558cd81aa3f484b2924e8897049e06889e8ff2510435b7ef74b")
    version("1.3.0", sha256="024ecdc12bc02b321bc66b41327f930d1c2c543fa9a561b39861da9388ba7aa9")

    with default_args(type="build"):
        depends_on("c")
        depends_on("py-expandvars", when="@1.18:")
        depends_on("py-setuptools@47:", when="@1.9.3:")
        depends_on("py-setuptools@40:", when="@1.7.2:")
        depends_on("py-setuptools")
        depends_on("py-tomli", when="@1.9.3: ^python@:3.10")
        # requires https://github.com/cython/cython/commit/ea38521bf59edef9e6d22cbabf44229848091a76
        depends_on("py-cython@3:", when="@1.15.4:")
        depends_on("py-cython")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:", when="@1.15.3:")
        depends_on("python@3.8:", when="@1.9.5:")
        depends_on("python@3.7:", when="@1.8:")

        depends_on("py-idna@2.0:")
        depends_on("py-multidict@4.0:")
        depends_on("py-propcache@0.2.1:", when="@1.19:")
        depends_on("py-propcache@0.2:", when="@1.14:")

        # Historical dependencies
        depends_on("py-typing-extensions@3.7.4:", when="@1.7.2:1.9.4 ^python@:3.7")

    @run_before("install", when="@:1.9")
    def fix_cython(self):
        if self.spec.satisfies("@1.7.2:"):
            pyxfile = "yarl/_quoting_c"
        else:
            pyxfile = "yarl/_quoting"

        cython = self.spec["py-cython"].command
        cython("-3", "-o", pyxfile + ".c", pyxfile + ".pyx", "-Iyarl")
