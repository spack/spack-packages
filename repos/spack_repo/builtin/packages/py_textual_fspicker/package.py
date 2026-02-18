# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTextualFspicker(PythonPackage):
    """A Textual widget library for picking things in the filesystem"""

    homepage = "https://textual-fspicker.davep.dev/"
    pypi = "textual-fspicker/textual_fspicker-0.5.0.tar.gz"
    license("MIT")

    version("0.5.0", sha256="a27fc1e616814e99c2dfb5be68df0ee8f7f1d53b8ed552419d542c26b45f6f75")

    depends_on("python@3.9:3")
    depends_on("py-textual@1:")
    depends_on("py-hatchling@1.26.3:", type="build")
    depends_on("py-hatch-vcs", type="build")
