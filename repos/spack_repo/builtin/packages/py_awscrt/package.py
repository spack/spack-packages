# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAwscrt(PythonPackage):
    """Python 3 bindings for the AWS Common Runtime."""

    homepage = "https://docs.aws.amazon.com/sdkref/latest/guide/common-runtime.html"
    pypi = "awscrt/awscrt-0.16.16.tar.gz"

    maintainers("climbfuji", "teaguesterling")

    license("Apache-2.0")

    version("0.31.2", sha256="552555de1beff02d72a1f6d384cd49c5a7c283418310eae29d21bcb749c65792")
    version("0.29.2", sha256="c78d81b1308d42fda1eb21d27fcf26579137b821043e528550f2cfc6c09ab9ff")
    version("0.20.9", sha256="243785ac9ee64945e0479c2384325545f29597575743ce84c371556d1014e63e")
    version("0.19.19", sha256="1c1511535dee146a6c26a382ed3ead56259a105b3b7d7d823553ae567d038dfe")
    version("0.19.18", sha256="350b6efd8ebee082ea3f3e52c59a3c3ec594cdaf01db8b4853dceb9fec90c89d")
    version("0.16.16", sha256="13075df2c1d7942fe22327b6483274517ee0f6ae765c4e6b6ae9ef5b4c43a827")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3.1:", type=("build"))
    depends_on("openssl", type=("build"), when="platform=linux")
    depends_on("py-setuptools", type=("build"))
    # awscrt>=0.29 requires setuptools.command.bdist_wheel introduced in v71.
    depends_on("py-setuptools@75.3.1:", when="@0.29:", type=("build"))

    # On Linux, tell aws-crt-python to use libcrypto from spack (openssl)
    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        with when("platform=linux"):
            env.set("AWS_CRT_BUILD_USE_SYSTEM_LIBCRYPTO", "1")
