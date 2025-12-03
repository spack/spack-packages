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

    pypi = "b2luigi/b2luigi-1.2.6.tar.gz"
    
    # To be decided
    #maintainers("github_user1", "github_user2")

    # We start at 1.2.6 as this was the change from retry2->tenacity dependency
    # as py_tenacity is a spack package
    version("1.2.6", sha256="TODO INSERT SH256 WHEN VERSION IS AVAILABLE")

    depends_on("python@3.8:3.12", type=("build", "run"))
    depends_on("py-luigi@3.0.2:", type=("build", "run"))
    depends_on("py-parse@1.8:", type=("build", "run"))
    depends_on("py-gitpython@2.1.11:", type=("build", "run"))
    depends_on("py-colorama@0.3.9:", type=("build", "run"))
    depends_on("py-cachetools@2.1.1:", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-tenacity@8:9", type=("build", "run"))                              
