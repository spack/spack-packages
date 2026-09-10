# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLit(PythonPackage):
    """lit is a portable tool for executing LLVM and Clang style test suites,
    summarizing their results, and providing indication of failures. lit is
    designed to be a lightweight testing tool with as simple a user
    interface as possible."""

    pypi = "lit/lit-0.5.0.tar.gz"

    version("18.1.8", sha256="47c174a186941ae830f04ded76a3444600be67d5e5fb8282c3783fba671c4edb")
    version("17.0.6", sha256="dfa9af9b55fc4509a56be7bf2346f079d7f4a242d583b9f2e0b078fd0abae31b")
    version("16.0.6", sha256="84623c9c23b6b14763d637f4e63e6b721b3446ada40bf7001d8fee70b8e77a9a")
    version("15.0.7", sha256="ed08ac55afe714a193653df293ae8a6ee6c45d6fb11eeca72ce347d99b88ecc8")
    version("14.0.6", sha256="86ee8fce0613ba6c48db85afb6a08d4885b947870e98193c2248d106d8e8a274")
    version("13.0.1", sha256="c6ca0b36e2581f51db690a9b907b64847bb289448fe7222d0dafd7f83dde34e8")
    version("12.0.1", sha256="d2957aac5d560e98662a9fe7a2f5a485d2320ded2ef26e065e4fe871967ecf07")
    version("0.7.1", sha256="ecef2833aef7f411cb923dac109c7c9dcc7dbe7cafce0650c1e8d19c243d955f")
    version("0.5.0", sha256="3ea4251e78ebeb2e07be2feb33243d1f8931d956efc96ccc2b0846ced212b58c")

    depends_on("py-setuptools", type="build")
