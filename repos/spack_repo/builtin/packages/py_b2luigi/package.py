# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyB2luigi(PythonPackage):
    """b2luigi is a helper package constructed around luigi that helps you schedule working
    packages (so-called tasks) locally or on a batch system. Apart from the very
    powerful dependency management system by luigi, b2luigi extends the user interface
    and has a built-in support for the queue systems, e.g. LSF and HTCondor."""

    homepage = "https://github.com/belle2/b2luigi"
    pypi = "b2luigi/b2luigi-1.2.6.tar.gz"

    license("GNU")

    tags = ["hep"]

    # To be decided
    # maintainers("github_user1", "github_user2")

    # We start at 1.2.6 as this was the change from retry2->tenacity dependency
    version("1.2.6", sha256="9f3be756f0961ca2241d36d9a9174ea5a23ebd7787cbfa78632047aae25f1202")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-luigi@3.0.2:", type=("build", "run"))
    depends_on("py-parse@1.8:", type=("build", "run"))
    depends_on("py-gitpython@2.1.11:", type=("build", "run"))
    depends_on("py-colorama@0.3.9:", type=("build", "run"))
    depends_on("py-cachetools@2.1.1:", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-tenacity@8", type=("build", "run"))
