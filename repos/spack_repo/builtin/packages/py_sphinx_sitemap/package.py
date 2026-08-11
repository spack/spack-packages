# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySphinxSitemap(PythonPackage):
    """A Sphinx extension to generate multiversion and multilanguage
    sitemaps.org compliant sitemaps for the HTML version of your Sphinx
    documentation."""

    homepage = "https://github.com/jdillard/sphinx-sitemap"
    pypi = "sphinx-sitemap/sphinx_sitemap-2.9.0.tar.gz"

    license("MIT")

    version("2.9.0", sha256="70f97bcdf444e3d68e118355cf82a1f54c4d3c03d651cd17fe87398b26e25e21")

    depends_on("py-setuptools", type="build")
    depends_on("py-sphinx@1.2:", type=("build", "run"))
    depends_on("py-sphinx-last-updated-by-git", type=("build", "run"))
