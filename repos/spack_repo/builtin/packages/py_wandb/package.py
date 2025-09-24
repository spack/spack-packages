# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyWandb(PythonPackage):
    """A tool for visualizing and tracking your machine learning experiments."""

    homepage = "https://github.com/wandb/wandb"
    pypi = "wandb/wandb-0.13.9.tar.gz"

    maintainers("thomas-bouvier")

    license("MIT")

    version("0.21.0", sha256="473e01ef200b59d780416062991effa7349a34e51425d4be5ff482af2dc39e02")
    version("0.16.6", sha256="86f491e3012d715e0d7d7421a4d6de41abef643b7403046261f962f3e512fe1c")
    version("0.13.9", sha256="0a17365ce1f18306ce7a7f16b943094fac7284bb85f4e52c0685705602f9e307")

    depends_on("rust", type="build")
    depends_on("go@1.24.4:", type="build", when="@0.21.0:")
    depends_on("go@1.22.1:", type="build", when="@0.16.6:")
    depends_on("py-hatchling", type=("build", "run"), when="@0.17:")
    depends_on("py-setuptools@61:", type=("build", "run"), when="@0.16.6:")
    depends_on("py-setuptools", type=("build", "run"))
    depends_on("python@3.8:", type=("build", "run"), when="@0.19:")
    depends_on("python@3.7:", type=("build", "run"), when="@0.16:")
    depends_on("python@3.6:", type=("build", "run"), when="@0.13:")

    depends_on("py-pyyaml", type=("build", "run"))

    depends_on(
        "py-protobuf@3.19:6", type=("build", "run"), when="@0.19.10: platform=linux ^python@3.10:"
    )
    depends_on(
        "py-protobuf@3.15:6", type=("build", "run"), when="@0.19.10: platform=linux ^python@3.9"
    )
    depends_on(
        "py-protobuf@3.12:6", type=("build", "run"), when="@0.19.10: platform=linux ^python@:3.8"
    )
    depends_on(
        "py-protobuf@3.19:5",
        type=("build", "run"),
        when="@0.17.1:0.19.9 platform=linux ^python@3.10:",
    )
    depends_on(
        "py-protobuf@3.15:5",
        type=("build", "run"),
        when="@0.17.1:0.19.9 platform=linux ^python@3.9",
    )
    depends_on(
        "py-protobuf@3.12:5",
        type=("build", "run"),
        when="@0.17.1:0.19.9 platform=linux ^python@:3.8",
    )
    depends_on(
        "py-protobuf@3.19:4", type=("build", "run"), when="@:0.17.0 platform=linux ^python@3.10:"
    )
    depends_on(
        "py-protobuf@3.15:4", type=("build", "run"), when="@:0.17.0 platform=linux ^python@3.9"
    )
    depends_on(
        "py-protobuf@3.12:4", type=("build", "run"), when="@:0.17.0 platform=linux ^python@:3.8"
    )
    conflicts("^py-protobuf@4.21.0,5.28.0")

    depends_on("py-typing-extensions@4.8:4", type=("build", "run"), when="@0.20:")
    depends_on("py-typing-extensions@4.4:4", type=("build", "run"), when="@0.19.9:")
    depends_on("py-typing-extensions@4.4:4", type=("build", "run"), when="@0.18.4: ^python@:3.11")
    depends_on("py-typing-extensions", type=("build", "run"), when="^python@:3.9")

    depends_on("py-pydantic@:2", type=("build", "run"), when="@0.19.9:")
    depends_on("py-pydantic@2.6:2", type=("build", "run"), when="@0.19.0:0.19.8")
    depends_on("py-platformdirs", type=("build", "run"), when="@0.17:")
    depends_on("py-click@7.1:", type=("build", "run"), when="@0.15.5:")
    depends_on("py-click@7:", type=("build", "run"), when="@0.13")
    conflicts("^py-click@8.0.0")
    depends_on("py-gitpython@1:", type=("build", "run"))
    conflicts("^py-gitpython@3.1.29")
    depends_on("py-requests@2", type=("build", "run"))
    depends_on("py-sentry-sdk@2:", type=("build", "run"), when="@0.18.4:")
    depends_on("py-sentry-sdk@1:", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"), when="@0.20:")
    depends_on("py-eval-type-backport", type=("build", "run"), when="@0.19: ^python@:3.9")

    # Historical dependencies
    depends_on("py-setproctitle", type=("build", "run"), when="@:0.20")
    depends_on("py-psutil@5:", type=("build", "run"), when="@:0.19")
    depends_on("py-dockerpy-creds@0.4:", type=("build", "run"), when="@:0.19")
    depends_on("py-appdirs@1.4.3:", type=("build", "run"), when="@:0.16")
    depends_on("py-pathtools", type=("build", "run"), when="@:0.15")
