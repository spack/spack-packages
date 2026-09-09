# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySphinxCopybutton(PythonPackage):
    """A small sphinx extension to add a "copy" button to code blocks."""

    homepage = "https://github.com/executablebooks/sphinx-copybutton"
    pypi = "sphinx-copybutton/sphinx-copybutton-0.2.12.tar.gz"

    license("MIT")

    version("0.5.2", sha256="4cf17c82fb9646d1bc9ca92ac280813a3b605d8c421225fd9913154103ee1fbd")
    version("0.5.0", sha256="a0c059daadd03c27ba750da534a92a63e7a36a7736dcf684f26ee346199787f6")
    version("0.4.0", sha256="8daed13a87afd5013c3a9af3575cc4d5bec052075ccd3db243f895c07a689386")
    version("0.3.0", sha256="4becad3a1e7c50211f1477e34fd4b6d027680e1612f497cb5b88cf85bccddaaa")
    version("0.2.12", sha256="9492883786984b6179c92c07ab0410237b26efa826adfa792acfd17b91a63e5c")

    depends_on("py-setuptools", type="build")
    depends_on("py-sphinx@1.8:", type=("build", "run"))
