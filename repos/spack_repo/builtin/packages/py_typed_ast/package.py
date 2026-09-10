# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems import python
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTypedAst(PythonPackage):
    """A fork of Python 2 and 3 ast modules with type comment support."""

    homepage = "https://github.com/python/typed_ast"
    pypi = "typed-ast/typed_ast-1.4.0.tar.gz"

    license("Apache-2.0")

    version("1.5.4", sha256="39e21ceb7388e4bb37f4c679d72707ed46c2fbf2a5609b8b8ebc4b067d977df2")
    version("1.4.3", sha256="fb1bbeac803adea29cedd70781399c99138358c26d05fcbd23c13016b7f5ec65")
    version("1.4.2", sha256="9fc0b3cb5d1720e7141d103cf4819aea239f7d136acf9ee4a69b047b7986175a")
    version("1.4.1", sha256="8c8aaad94455178e3187ab22c8b01a3837f8ee50e09cf31f1ba129eb293ec30b")

    variant(
        "wheel",
        default=False,
        sticky=True,
        description="Install from wheel (required for bootstrapping Spack)",
    )

    depends_on("c", type="build")  # generated

    depends_on("python@3.3:", type=("build", "link", "run"))
    depends_on("python@3.6:", when="@1.5.4:", type=("build", "link", "run"))
    depends_on("py-setuptools", type="build")


class PythonPipBuilder(python.PythonPipBuilder):
    @when("+wheel")
    def install(self, pkg, spec, prefix):
        args = list(filter(lambda x: x != "--no-index", self.std_args(self.pkg)))
        args += [f"--prefix={prefix}", self.spec.format("typed-ast=={version}")]
        pip(*args)
