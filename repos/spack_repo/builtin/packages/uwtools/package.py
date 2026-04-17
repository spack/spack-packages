# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class Uwtools(PythonPackage):
    """UW Tools is a modern, open-source Python package that helps
    automate common tasks needed for many standard numerical weather
    prediction (NWP) workflows. It also provides drivers to automate
    the configuration and execution of Unified Forecast System (UFS)
    components, providing flexibility, interoperability, and
    usability to various UFS Applications."""

    homepage = "https://uwtools.readthedocs.io/en/stable/"
    url = "https://github.com/ufs-community/uwtools/archive/refs/tags/v2.7.1.tar.gz"
    git = "https://github.com/ufs-community/uwtools.git"

    maintainers("NaureenBharwaniNOAA", "christinaholtNOAA", "elcarpenterNOAA", "maddenp-cu")

    license("GPL-2.0-or-later", checked_by="WeirAE")

    version("main", branch="main")
    # Latest three minor releases per deprecation policy
    version("2.8.2", sha256="634f7fbc33cd9439f43df00c1d904266b9c51b3f386c2141c26c1229d4d95a34")
    version("2.7.2", sha256="56816d543664792258bfa7dfb7e4cc66f794959dc92dc3710021f40a2b8571a4")
    version("2.6.2", sha256="d0922ddd2b3bdbeb925c2e4694f929f3e966145d2929e74ab9f9c9ecd27b674a")

    depends_on("py-pip", type="build")
    # Maximum Python version limited here for compatibility with the JCSDA unified environment
    depends_on("python@3.9:3.11")
    depends_on("py-setuptools", type="build")
    depends_on("py-f90nml@1.4")
    depends_on("py-jinja2@3.1")
    depends_on("iotaa@1.1", when="@2.6")
    depends_on("iotaa@1.2", when="@2.7")
    depends_on("iotaa@1.3:2.0", when="@2.8:")
    depends_on("py-jsonschema@4.17:")
    depends_on("py-jsonschema@4.18:4.23", when="@:2.11")
    depends_on("py-lxml@5.2", when="@2.7")
    depends_on("py-lxml@5.2:5.4", when="@2.8:")
    depends_on("py-lxml@5.3", when="@:2.6")
    depends_on("py-python-dateutil@2.9:", when="@2.8:")
    depends_on("py-pyyaml@6.0")
    depends_on("py-requests@2.32")

    build_directory = "src"
