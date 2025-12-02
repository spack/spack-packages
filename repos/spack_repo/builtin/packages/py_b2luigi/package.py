# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install b2luigi
#
# You can edit this file again by typing:
#
#     spack edit b2luigi
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class PyB2luigi(Package):
    """b2luigi is a helper package constructed around luigi that helps you schedule working packages (so-called tasks) locally or on a batch system. Apart from the very powerful dependency management system by luigi, b2luigi extends the user interface and has a built-in support for the queue systems, e.g. LSF and HTCondor."""

    homepage = "https://b2luigi.belle2.org/"
    url = "https://github.com/belle2/b2luigi"

    # To be decided
    #maintainers("github_user1", "github_user2")

    version("1.2.5", sha256="179c9c1b4ef3c816d3b40d199690f03517a8747d7b0b104fc7d7f53112dbdf3d")
    version("1.2.4", sha256="c6789c49542c6c2a1b76a92dfc0d52a818f13c9b46cefc5cbd0ea9297f06ad51")
    version("1.2.3", sha256="6819ef042f208f5703c7be8112bfc3708600f834fd21a92a941a5adf20563829")
    version("1.2.2", sha256="2e3711fcf1c584dabb8e1bed07d7a9d08453843247daacc45856089ed77ab744")
    version("1.2.1", sha256="2c46d4edbb66189a4e31616ab7251c6d2a61f385b7a945fd6cd2682adf7e1b1e")
    version("1.2.0", sha256="d1f9ec55ef0f11c9d98e4f0586266c8dd9f75e204151359fb8e0f00110c780be")

    depends_on("python@3.8:3.12", type=("build", "run"))
    depends_on("py-luigi@3.0.2:", type=("build", "run"))
    depends_on("py-parse@1.8:", type=("build", "run"))
    depends_on("py-gitpython@2.1.11:", type=("build", "run"))
    depends_on("py-colorama@0.3.9:", type=("build", "run"))
    depends_on("py-cachetools@2.1.1:", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-reretry", type=("build", "run"))                              
