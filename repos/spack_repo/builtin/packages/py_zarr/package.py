# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyZarr(PythonPackage):
    """Zarr is a Python package providing an implementation of chunked,
    compressed, N-dimensional arrays."""

    homepage = "https://zarr.readthedocs.io"
    pypi = "zarr/zarr-2.3.2.tar.gz"
    git = "https://github.com/zarr-developers/zarr-python.git"

    license("MIT")

    version("3.1.2", sha256="688e4eb79045c110128cd16f301f2f58fa19507b1803dcbea0ea894e66e06274")
    version("3.0.6", sha256="6ef23c740e34917a2a1099471361537732942e49f0cabe95c9b7124cd0d6d84f")
    version("3.0.1", sha256="033859c5603dc9c29e53af494ede24b42f1b761d2bb625466990a3b8a9afb792")
    version("2.18.7", sha256="b2b8f66f14dac4af66b180d2338819981b981f70e196c9a66e6bfaa9e59572f5")
    version("2.17.0", sha256="6390a2b8af31babaab4c963efc45bf1da7f9500c9aafac193f84cf019a7c66b0")
    version("2.10.2", sha256="5c6ae914ab9215631bb95c09e76b9b9b4fffa70fec0c7bca26b68387d858ebe2")
    version("2.6.1", sha256="fa7eac1e4ff47ff82d09c42bb4679e18e8a05a73ee81ce59cee6a441a210b2fd")
    version("2.5.0", sha256="d54f060739208392494c3dbcbfdf41c8df9fa23d9a32b91aea0549b4c5e2b77f")
    version("2.4.0", sha256="53aa21b989a47ddc5e916eaff6115b824c0864444b1c6f3aaf4f6cf9a51ed608")
    version("2.3.2", sha256="c62d0158fb287151c978904935a177b3d2d318dea3057cfbeac8541915dfa105")

    with default_args(type="build"):
        depends_on("py-hatchling@1.27:", when="@3.1.1:")
        depends_on("py-hatchling", when="@3:")
        depends_on("py-hatch-vcs", when="@3:")

        # Historical dependencies
        depends_on("py-setuptools@64:", when="@2.13.4:2")
        depends_on("py-setuptools@40.8:", when="@2.5:2")
        depends_on("py-setuptools@38.6:", when="@2.4:2")
        depends_on("py-setuptools@18.1:", when="@:2")
        depends_on("py-setuptools-scm@8.1:", when="@2.18.4:2")
        depends_on("py-setuptools-scm@1.5.5:", when="@:2")

    with default_args(type=("build", "run")):
        depends_on("python@3.11:", when="@2.18.4:")
        depends_on("python@3.10:", when="@2.18.3:")
        depends_on("python@3.9:", when="@2.17:")
        depends_on("python@3.8:", when="@2.13.4:")
        depends_on("python@3.8:3", when="@2.13.0:2.13.3")
        depends_on("python@3.7:3", when="@2.9:2.12")
        depends_on("python@3.6:3", when="@2.6:2.8")
        depends_on("python@3.5:", when="@2.4:2.5")
        depends_on("py-packaging@22:", when="@3:")
        depends_on("py-numpy@1.26:", when="@3.1:")
        depends_on("py-numpy@1.25:", when="@3:")
        depends_on("py-numpy@1.24:", when="@2.18.3:")
        depends_on("py-numpy@1.23:", when="@2.17.2:")
        depends_on("py-numpy@1.21.1:", when="@2.16.1:")
        depends_on("py-numpy@1.20,1.21.1:", when="@2.13.4:")
        depends_on("py-numpy@1.7:")
        # https://github.com/zarr-developers/zarr-python/issues/1818
        depends_on("py-numpy@:1", when="@:2.17")
        depends_on("py-numcodecs@0.14:+crc32c", when="@3:")
        depends_on("py-numcodecs@0.10:0.13,0.14.2:0.15", when="@2.18.7")
        depends_on("py-numcodecs@0.10:0.13,0.14.2:", when="@2.18.4:2.18.6")
        depends_on("py-numcodecs@0.10:", when="@2.13:")
        depends_on("py-numcodecs@0.6.4:", when="@2.4:")
        depends_on("py-numcodecs@0.6.2:")
        depends_on("py-typing-extensions@4.9:", when="@3:")
        depends_on("py-donfig@0.8:", when="@3:")

        # Historical dependencies
        depends_on("py-asciitree", when="@:2")
        depends_on("py-fasteners", when="@:2")
