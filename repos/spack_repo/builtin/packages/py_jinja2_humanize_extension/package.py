# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyJinja2HumanizeExtension(PythonPackage):
    """A jinja2 extension to use humanize library inside jinja2 templates."""

    homepage = "https://github.com/metwork-framework/jinja2_humanize_extension"
    pypi = "jinja2_humanize_extension/jinja2_humanize_extension-0.4.0.tar.gz"

    version("0.4.0", sha256="e7d69b1c20f32815bbec722330ee8af14b1287bb1c2b0afa590dbf031cadeaa0")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools", when="^python@3.11:", type="build")

    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-humanize@3.14:", type=("build", "run"))
