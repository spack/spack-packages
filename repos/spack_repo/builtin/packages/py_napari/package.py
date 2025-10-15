# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNapari(PythonPackage):
    """napari is a fast, interactive, multi-dimensional image viewer for
    Python. It's designed for browsing, annotating, and analyzing large
    multi-dimensional images. It's built on top of Qt (for the GUI), vispy (for
    performant GPU-based rendering), and the scientific Python stack (numpy,
    scipy)."""

    homepage = "https://www.napari.org"
    pypi = "napari/napari-0.6.5.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("0.6.5", sha256="00663221583467f41fa956a672b0b4cd7a761e2642db41fc3c336d1c82339533")

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-setuptools@69:", type="build")
    depends_on("py-setuptools-scm@8: +toml", type="build")

    depends_on("py-appdirs@1.4.4:", type=("build", "run"))
    depends_on("py-app-model@0.4.0:0.4", type=("build", "run"))
    depends_on("py-cachey@0.2.1:", type=("build", "run"))
    depends_on("py-certifi@2018.1.18:", type=("build", "run"))
    depends_on("py-dask@2021.10.0: +array", type=("build", "run"))
    depends_on("py-imageio@2.20:", type=("build", "run"))
    depends_on("py-jsonschema@3.2.0:", type=("build", "run"))
    depends_on("py-lazy-loader@0.3:", type=("build", "run"))
    depends_on("py-magicgui@0.7.0:", type=("build", "run"))
    depends_on("py-numpy@1.24.2:", type=("build", "run"))
    depends_on("py-numpydoc@1.0.0:", type=("build", "run"))
    depends_on("py-pandas@1.3.3:", type=("build", "run"))
    depends_on("py-pillow@9.0:", type=("build", "run"))
    depends_on("py-pint@0.17:", type=("build", "run"))
    depends_on("py-psutil@5.9.0:", type=("build", "run"))
    depends_on("py-psygnal@0.14.2:", type=("build", "run"))
    depends_on("py-pydantic@2.2.0:", type=("build", "run"))
    depends_on("py-pygments@2.6.0:", type=("build", "run"))
    depends_on("py-pyopengl@3.1.5:", type=("build", "run"))
    depends_on("py-pyyaml@6.0:", type=("build", "run"))
    depends_on("py-qtpy@2.3.1:", type=("build", "run"))
    depends_on("py-scikit-image@0.19.1:+data", type=("build", "run"))
    depends_on("py-scipy@1.10.1:", type=("build", "run"))
    depends_on("py-superqt@0.7.4:", type=("build", "run"))
    depends_on("py-tifffile@2022.7.28:", type=("build", "run"))
    depends_on("py-toolz@0.11.0:", type=("build", "run"))
    depends_on("py-tqdm@4.56.0:", type=("build", "run"))
    depends_on("py-typing-extensions@4.12:", type=("build", "run"))
    depends_on("py-vispy@0.15.2:0.15", type=("build", "run"))
    depends_on("py-wrapt@1.13.3:", type=("build", "run"))

    # Other  napari packages
    depends_on("py-napari-console@0.1.1:", type=("build", "run"))
    depends_on("py-napari-plugin-engine@0.1.9:", type=("build", "run"))
    depends_on("py-napari-svg@0.1.8:", type=("build", "run"))
    depends_on("py-npe2@0.7.9:", type=("build", "run"))
