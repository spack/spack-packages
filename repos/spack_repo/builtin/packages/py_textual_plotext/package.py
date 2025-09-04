# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTextualPlotext(PythonPackage):
    """A Textual widget wrapper library for Plotext"""

    homepage = "https://github.com/Textualize/textual-plotext"
    pypi = "textual-plotext/textual_plotext-1.0.1.tar.gz"

    version("1.0.1", sha256="836f53a3316756609e194129a35c2875638e7958c261f541e0a794f7c98011be")
    version("1.0.0", sha256="6e8e608ca9da52b4f171fa4adb0e80cbcd8e668f1334e9e4d7fbfd064d393a4f")

    depends_on("python@3.8:3")
    depends_on("py-poetry-core")
    depends_on("py-textual@5:")
    depends_on("py-plotext@5.2.8:5")
    depends_on("py-platformdirs")
