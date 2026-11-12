# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLangsmith(PythonPackage):
    """Client library to connect to the LangSmith LLM Tracing and Evaluation Platform."""

    homepage = "https://smith.langchain.com/"
    pypi = "langsmith/langsmith-0.0.10.tar.gz"

    license("MIT")

    version("0.8.7", sha256="1d0f2b4bcfbf26e9e37bf978dfe23e50d4c90bf1a0f26717879d56f941465a85")
    version("0.1.81", sha256="585ef3a2251380bd2843a664c9a28da4a7d28432e3ee8bcebf291ffb8e1f0af0")
    version(
        "0.1.1",
        sha256="09df0c2ca9085105f97a4e4f281b083e312c99d162f3fe2b2d5eefd5c3692e60",
        expand=False,
    )
    version("0.0.11", sha256="7c1be28257d6c7279c85f81e6d8359d1006af3b1238fc198d13ca75c8fe421c8")
    version("0.0.10", sha256="11e5db0d8e29ee5583cabd872eeece8ce50738737b1f52f316ac984f4a1a58c5")
    version("0.0.7", sha256="2f18e51cfd4e42f2b3cf00fa87e9d03012eb7269cdafd8e7c0cf7aa828dcc03e")

    depends_on("python@3.10:", type=("build", "run"), when="@0.4.38:")
    depends_on("python@3.8.1:", type=("build", "run"))
    depends_on("py-hatchling", type="build", when="@0.4.10:")
    depends_on("py-pydantic@2", type=("build", "run"), when="@0.6:")
    depends_on("py-pydantic@1:2", type=("build", "run"), when="@0.1.81:")
    depends_on("py-requests@2:", type=("build", "run"), when="@0.4.10:")
    depends_on("py-requests@2", type=("build", "run"))
    depends_on("py-orjson@3.9.14:", type=("build", "run"), when="@0.4.10:")
    depends_on("py-orjson@3.9.14:3", type=("build", "run"), when="@0.1.81:0.4.9")
    depends_on("py-httpx@0.23:0", type=("build", "run"), when="@0.1.100:")
    depends_on("py-requests-toolbelt@1:", type=("build", "run"), when="@0.1.130:")
    depends_on("py-zstandard@0.23:", type=("build", "run"), when="@0.2.5:")
    depends_on("py-packaging@23.2:", type=("build", "run"), when="@0.3.11:")
    depends_on("py-uuid-utils@0.12:0", type=("build", "run"), when="@0.4.53:")
    depends_on("py-xxhash@3:", type=("build", "run"), when="@0.6.7:")
    depends_on("py-websockets@15:", type=("build", "run"), when="@0.8.6:")

    # Historical dependencies
    depends_on("py-poetry-core", type="build", when="@:0.4.9")
    depends_on("py-pydantic@1", type=("build", "run"), when="@:0.1.1")
