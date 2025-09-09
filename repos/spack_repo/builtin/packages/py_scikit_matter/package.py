# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyScikitMatter(PythonPackage):
    """Toolbox of methods developed in the computational chemical and materials science community
    following the scikit-learn API."""

    homepage = "https://scikit-matter.readthedocs.io/en/latest/"
    pypi = "skmatter/skmatter-0.3.2.tar.gz"

    maintainers("RMeli")

    license("BSD3-Clause", checked_by="RMeli")

    version("0.3.2", sha256="2af37cb094658645d7f67492b35344fc23768568108cca425c1ed5bcfd261f2b")

    variant("examples", default=False, description="Examples")

    # pyproject.toml
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-setuptools-scm@8:", type="build")

    depends_on("py-scikit-learn@1.7", type=("build", "run"))
    depends_on("py-scipy@1.15:", type=("build", "run"))

    depends_on("py-matplotlib", type=("build", "run"), when="+examples")
    depends_on("py-pandas", type=("build", "run"), when="+examples")
    depends_on("py-tqdm", type=("build", "run"), when="+examples")
