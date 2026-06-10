# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCylcFlow(PythonPackage):
    """A workflow engine for cycling systems."""

    homepage = "https://cylc.org"
    pypi = "cylc-flow/cylc-flow-8.1.4.tar.gz"
    git = "https://github.com/cylc/cylc-flow.git"

    maintainers("LydDeb", "climbfuji")

    license("GPL-3.0-only")

    version(
        "8.6.4",
        sha256="ba65eee781b26986030ab2ab6bd44bed5c77f4164ae02f5b093b3e452cab35a7",
        url="https://files.pythonhosted.org/packages/source/c/cylc-flow/cylc_flow-8.6.4.tar.gz",
    )
    version(
        "8.5.4",
        sha256="3997e51bb31905027d96374e29d0e61eb84bd7dd816cd6c426eae3467a984bb2",
        url="https://files.pythonhosted.org/packages/source/c/cylc-flow/cylc_flow-8.5.4.tar.gz",
    )
    version(
        "8.4.2",
        sha256="6d0b3129c9779db764fc6e4b4c397a5b117accdf4e9089cd5edcd5023618aa17",
        url="https://files.pythonhosted.org/packages/source/c/cylc-flow/cylc_flow-8.4.2.tar.gz",
    )
    version(
        "8.3.6",
        sha256="43ddda5fa047a6cd19bd1eea6e7ece028f9d535eecce004203a46c7c135d2d8c",
        url="https://files.pythonhosted.org/packages/source/c/cylc-flow/cylc_flow-8.3.6.tar.gz",
        deprecated=True,
    )
    version("8.2.3", sha256="dd5bea9e4b8dad00edd9c3459a38fb778e5a073da58ad2725bc9b84ad718e073", deprecated = True)
    version("8.2.0", sha256="cbe35e0d72d1ca36f28a4cebe9b9040a3445a74253bc94051a3c906cf179ded0", deprecated = True)
    version("8.1.4", sha256="d1835ac18f6f24f3115c56b2bc821185484e834a86b12fd0033ff7e4dc3c1f63", deprecated = True)

    depends_on("python@3.12:", type=("build", "run"), when="@8.6:")
    depends_on("py-setuptools@49:66,68:", type=("build", "run"), when="@:8.2")

    depends_on("py-aiofiles@0.7", type=("build", "run"), when="@:8.1")
    depends_on("py-ansimarkup@1.0.0:", type=("build", "run"))
    depends_on("py-async-timeout@3.0.0:", type=("build", "run"), when="@:8.5 ^python@:3.10")
    depends_on("py-colorama@0.4:1", type=("build", "run"))
    depends_on("py-graphql-core@3.2", type=("build", "run"), when="@8.5:")
    depends_on("py-graphene@2.1:2", type=("build", "run"), when="@:8.4")
    depends_on("py-graphene@3.4", type=("build", "run"), when="@8.5:")

    depends_on("py-jinja2@3.0", type=("build", "run"))
    depends_on("py-metomi-isodatetime@3.0", type=("build", "run"), when="@:8.2.0")
    depends_on("py-metomi-isodatetime@3:3.1", type=("build", "run"), when="@8.2.3:")
    depends_on("py-packaging", type=("build", "run"), when="@8.3:")
    depends_on("py-protobuf@4.21.2:4.21", type=("build", "run"), when="@:8.2")
    depends_on("py-protobuf@4.24.4:4.24", type=("build", "run"), when="@8.3:8.5")
    depends_on("py-protobuf@5:7", type=("build", "run"), when="@8.6:")
    depends_on("py-psutil@5.6.0:", type=("build", "run"))
    depends_on("py-pyzmq@22:", type=("build", "run"), when="@8.2:")
    depends_on("py-pyzmq@22", type=("build", "run"), when="@:8.1")

    depends_on("py-importlib-metadata", type=("build", "run"), when="@:8.2 ^python@:3.7")
    depends_on("py-importlib-metadata@5:", type=("build", "run"), when="@8.3:8.5 ^python@:3.11")
    depends_on("py-urwid@2:2.6.1,2.6.4:2", type=("build", "run"))
    depends_on("py-rx", type=("build", "run"), when="@:8.4")
    depends_on("py-promise", type=("build", "run"), when="@:8.4")
    depends_on("py-tomli@2:", type=("build", "run"), when="^python@:3.10")

    # Non-Python dependencies for creating graphs.
    # We want at least the pangocairo variant for
    # graphviz so that we can create output as png.
    depends_on("graphviz+pangocairo", type="run")

    # Undocumented dependency, but needed for 8.4
    depends_on("py-typing-extensions", type="run", when="@8.4")
