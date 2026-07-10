# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import sys

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class Meson(PythonPackage):
    """Meson is a portable open source build system meant to be both
    extremely fast, and as user friendly as possible."""

    homepage = "https://mesonbuild.com/"
    url = "https://github.com/mesonbuild/meson/archive/0.49.0.tar.gz"

    tags = ["build-tools"]

    maintainers("eli-schwartz", "michaelkuhn")

    license("Apache-2.0")

    version("1.11.1", sha256="1a2219422be4a66ad0e8daed125c2a3d5c963458e289203eae22edf3224f5d3e")
    version("1.10.2", sha256="4f3c6fe1d163fb6d5b52094035fc29d14cf4a254c3ac29544ba0a3d5a739c7ba")
    version("1.10.1", sha256="3d4768a76fc63dc4c562edc7892de17b54dfaa7309d148e805b0d763bc085e00")
    version("1.8.5", sha256="1cd0b5b013b4208ab450f5aca93b592b707f3fb2afe96b101dc710e6e5a8245c")
    version("1.7.2", sha256="3640ef596523393100df31ba790bc5fe732215e9711a66b673a21c4eb39bc8f1")
    version("1.6.1", sha256="4889795777b536ea1a351982f3ef7c7b06a786ccb47036daba63cc5757c59edb")
    version("1.5.2", sha256="fb41882bef26ffc02647d9978cba502a4accdf2e94c0a6dc9cc498dd7463381e")
    version("1.4.2", sha256="11d1336fe35e1ade57510a846a31d7dc2e3b6ac1e2491c2831bce5a2a192ba0d")
    version("1.3.2", sha256="683082fb3c5cddf203b21d29bdf4c227e2f7964da5324a15e1a5f7db94322b4b")
    version("1.2.2", sha256="1caa0ef6082e311bdca9836e7907f548b8c3f041a42ed41f0ff916b83ac7dddd")
    version("1.1.1", sha256="1c3b9e1a3a36b51adb5de498d582fd5cbf6763fadbcf151de9f2a762e02bd2e6")
    version("1.0.2", sha256="1f1239c3091668643f7d2086663d6afd8cc87fbab84fe7462bc18b9ba6d65de8")

    with default_args(deprecated=True):
        version("1.8.4", sha256="57dfa56ead471eec31d624d76c819e743a4dd0f6e8b4cd503e63d97604d11c2c")
        version("1.8.2", sha256="6b878fb0f6f0318cbd54e13539f89a1a8305791668e8e93ffd59d82722888dac")
        version("1.7.0", sha256="a6ca46e2a11a0278bb6492ecd4e0520ff441b164ebfdef1e012b11beb848d26e")

    depends_on("py-setuptools@42:", type=("build", "run"))
    depends_on("ninja@1.8.2:", type="run")

    # By default, Meson strips the rpath on installation. This patch disables
    # rpath modification completely to make sure that Spack's rpath changes
    # are not reverted.
    patch("rpath-0.64.patch")

    # Python 3.12 detection support
    patch("python-3.12-support.patch", when="@1.1:1.2.2")

    executables = ["^meson$"]

    @classmethod
    def determine_version(cls, exe):
        return Executable(exe)("--version", output=str, error=str).rstrip()

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        # https://github.com/pybind/pybind11/issues/595
        if self.spec.satisfies("platform=darwin"):
            env.set("STRIP", "strip -x")

    def _meson_bin_dir(self):
        bin_dir = self.spec.prefix.bin
        if sys.platform == "win32":
            bin_dir = self.spec.prefix.scripts
        return bin_dir

    def setup_dependent_package(self, module, dependent_spec):
        module.meson = Executable(self._meson_bin_dir().meson)
