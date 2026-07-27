# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGeemap(PythonPackage):
    """A Python package for interactive mapping using Google Earth Engine and ipyleaflet."""

    homepage = "https://github.com/gee-community/geemap"
    pypi = "geemap/geemap-0.35.1.tar.gz"

    license("MIT")

    version("0.36.3", sha256="5307cb29eeae6ce1a3b4fee3a8a09ae091d5e5afc05c2b4d4d3007d7e24ec257")
    version("0.36.1", sha256="378bbaaf87a74f70f021ae727d8310871fe35a7fc4b14321dbc698a56730426c")
    version("0.36.0", sha256="cb5da3bc6414d4b75dc97a333e46cadc2492de992741abcb09d5b875e6f65823")
    version("0.35.1", sha256="98f3f17fb1d07a6fe43b06f03fb680e10517adfd96002184015a3d4fe92435d6")

    with default_args(type="build"):
        depends_on("py-hatchling", when="@0.36:")
        depends_on("py-hatch-jupyter-builder@0.5:", when="@0.36:")

        # Historical dependencies
        depends_on("py-setuptools@64:", when="@:0.35")
        depends_on("py-setuptools-scm@8:", when="@:0.35")

    with default_args(type=("build", "run")):
        depends_on("py-anywidget", when="@0.36:")
        depends_on("py-bqplot")
        depends_on("py-earthengine-api@1.5.12:", when="@0.36.1:")
        depends_on("py-earthengine-api@1:")
        depends_on("py-eerepr@0.1:", when="@0.36:")
        depends_on("py-eerepr@0.0.4:")
        depends_on("py-folium@0.17:")
        depends_on("py-geocoder")
        depends_on("py-ipyevents")
        depends_on("py-ipyfilechooser@0.6:")
        depends_on("py-ipyleaflet@0.19.2:")
        depends_on("py-matplotlib")
        depends_on("py-numpy")
        depends_on("py-pandas")
        depends_on("py-plotly")
        depends_on("py-pyperclip")
        depends_on("py-pyshp@2.3.1:")
        depends_on("py-python-box")
        depends_on("py-scooby")

        # Historical dependencies
        depends_on("py-colour", when="@:0.36.0")
        depends_on("py-ipytree", when="@:0.36.2")
