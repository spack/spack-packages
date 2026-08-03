# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytecplot(PythonPackage):
    """The pytecplot library is a high level API that connects your
    Python script to the power of the Tecplot 360 visualization engine.
    It offers line plotting, 2D and 3D surface plots in a variety of formats,
    and 3D volumetric visualization. Familiarity with Tecplot 360 and the
    Tecplot 360 macro language is helpful, but not required."""

    homepage = "https://www.tecplot.com/docs/pytecplot/"
    pypi = "pytecplot/pytecplot-1.4.2.tar.gz"

    license("Frameworx-1.0")

    version("1.7.4", sha256="cb4456f004267140a35925a4b46c41a20ec15051fcb2404ab3d6077d6cec18a7")
    version("1.7.3", sha256="b15c36bdaaebef45c6f4226ca0df1f734a3e7f965fa7511bb9f60146ba8af52a")
    version("1.7.2", sha256="99da22558f8ca1bb18afbb5f68edd4f42204e42eba88e7bc81ec9f2633872198")
    version("1.7.1", sha256="0e80e2cd9c1a144801da360ab61b5652dea41c85471b021d7b3841310315aa23")
    version("1.7.0", sha256="efeaecdea12c18d7701c7996fd5733495d0e90f029c80c186ed36d2a5fe78609")
    version("1.6.3", sha256="baa59da561b827da035391957c30bf867dfcdc8ed8799dde08caa9b6a42dc1ab")
    version("1.6.2", sha256="164dcf10c962579604c04f1445c8e67a40fb767bcc1953786181b958991c94ed")
    version("1.6.1", sha256="5cade45096ccfcceee8c0f989688c69710dbcc0b7450ed5f97531a12dc2d6b7e")
    version("1.6.0", sha256="68c9f84233a698122662cb1cc85c4330760abcd0fae69ee11ed2467b5d20c689")
    version("1.5.4", sha256="394324241b43fd7fccb85383f25d2793831f06e692848b21f12be263c7fd6740")
    version("1.5.3", sha256="a42310d191b865c094be105632655326d81dea2f22af517c0f6efdbc9639e7b3")
    version("1.5.2", sha256="a790fb018752ef40a4dc9b7d4823528644a4ad45294a2d1998ee58faceb851b9")
    version("1.4.2", sha256="586a2ee947314ddd2f28be5523911dd298465b8f6a9145ba351866d5d695ef0d")

    variant("extras", default=False, description="Enable extra functionality.")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-flatbuffers", type=("build", "run"))
    depends_on("py-protobuf", type=("build", "run"))
    depends_on("py-pyzmq", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"), when="+extras")
    depends_on("py-ipython", type=("build", "run"), when="+extras")
    depends_on("py-pillow", type=("build", "run"), when="+extras")
    depends_on("tecplot@2017r1:", type=("build", "run"))
