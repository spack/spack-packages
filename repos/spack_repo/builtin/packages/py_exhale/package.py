# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyExhale(PythonPackage):
    """Automatic C++ library api documentation generation: breathe doxygen in
    and exhale it out."""

    homepage = "https://github.com/svenevs/exhale"
    pypi = "exhale/exhale-0.3.6.tar.gz"

    maintainers("svenevs")

    license("BSD-3-Clause")

    version("0.3.7", sha256="752a96d0a59456511d933311d4a81f642cd668296eacd2561905727d5ed6b0d8")
    version("0.3.6", sha256="ab41be313e1236bd4386e4696fb35f37ce8103c2059cf8d1f083da5411bb74d7")

    depends_on("python@3.8:", when="@0.3.7:", type=("build", "run"))
    depends_on("python@3.7:", when="@:0.3.6", type=("build", "run"))
    depends_on("py-setuptools@42:", type="build")
    depends_on("py-breathe@4.33.1:", when="@0.3.7:", type="build")
    depends_on("py-breathe@4.32.0:", when="@:0.3.6", type="build")
    depends_on("py-docutils@0.12:", when="@:0.3.6", type="build")
    depends_on("py-sphinx@4.3.2:", when="@0.3.7:", type="build")
    depends_on("py-sphinx@3:4", when="@:0.3.6", type="build")
    depends_on("py-beautifulsoup4", type=("build", "run"))
    depends_on("py-lxml", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
