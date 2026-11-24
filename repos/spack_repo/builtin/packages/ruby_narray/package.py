# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.ruby import RubyPackage

from spack.package import *


class RubyNarray(RubyPackage):
    """Numo::NArray is an Numerical N-dimensional Array class for fast
    processing and easy manipulation of multi-dimensional numerical data,
    similar to numpy.ndaray."""

    homepage = "https://github.com/ruby-numo/numo-narray"
    url = "https://rubygems.org/downloads/numo-narray-0.9.2.1.gem"
    git = "https://github.com/ruby-numo/numo-narray.git"

    license("BSD-3-Clause")

    version("master", branch="master")
    version(
        "0.9.2.1",
        sha256="eed76b47eebe1288ffd878b387f1882f4863d8e6ab5dd61453768139e14adceb",
        expand=False,
    )
    version(
        "0.9.1.8",
        sha256="e25b8be2ec605c644535ed4ae250529242d695f64d75ed1d62f7da78e339166f",
        expand=False,
    )

    depends_on("c", type="build")  # generated
    depends_on("gmake", type="build")

    depends_on("ruby@2.2:", type=("build", "run"))
    depends_on("ruby@:2", type=("build", "run"), when="@:0.9.1.8")
