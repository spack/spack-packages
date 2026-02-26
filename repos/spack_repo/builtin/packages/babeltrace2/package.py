# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Babeltrace2(AutotoolsPackage):
    """
    Babeltrace 2: CTF trace processing library, CLI, and Python3 bindings (bt2).
    """

    homepage = "https://babeltrace.org/"
    git = "https://github.com/efficios/babeltrace.git"
    url = "https://github.com/efficios/babeltrace/archive/refs/tags/v2.1.2.tar.gz"

    # Maintaining this package; not the original author of Babeltrace2
    maintainers("minghangli-uni")

    license("MIT")

    version("2.1.2", sha256="92e261e1811f4a7f747ee4bc5ac21c0054cd7906f88ad799fab81f16e08c2122")
    version("2.1.1", sha256="1ad8cea3fc31e8d18e869d0c01581318e534f3976a9f3636fdab4423f1113d47")
    version("2.1.0", sha256="808426a78efdeb1db71c71dba9ddb39902f7cc2604cee698849bc291d0af377e")
    version("2.0.7", sha256="a8c1965590b0cf04b1985881b2a5727a0e49d628a99bdaade4f3e29f0c36e5b1")
    version("2.0.6", sha256="a3a548b3e5b2a1d18c865299f083aa9716fcb6fed4a5713f29a87d3e9e39041c")
    version("2.0.5", sha256="c058f9a2dc0b1287dcc20ef59fc0e13f54b9c43c14ffd58d5dc1c10786884a81")
    version("2.0.4", sha256="37d3e81bc4abc42e4fa99488685eab3458212c6531ccadcf53cf1534d762bf22")
    version("2.0.3", sha256="6cdeaa3bfc12d47936e7c664c5a2610c376ad3d2dfc8cf947137c4b3a2051dd3")
    version("2.0.2", sha256="1c09428fec2d0000bf6f5332da2624b39fbf110477b82d2cb0856dcb74c58afc")

    variant("python", default=True, description="Build Python3 bindings (bt2)")
    variant("plugins", default=True, description="Enable Python plugin provider")
    variant("manpages", default=True, description="Build man pages")

    depends_on("c", type="build")

    depends_on("pkgconfig", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("glib@2.22:", type=("build", "link"))
    depends_on("python@3.4:", when="+python", type=("build", "run"))
    depends_on("py-setuptools", when="+python", type="build")
    depends_on("swig@2.0:", when="+python", type="build")

    depends_on("asciidoc", when="+manpages", type="build")
    depends_on("xmlto", when="+manpages", type="build")

    def setup_build_environment(self, env):
        if self.spec.satisfies("+python"):
            env.set("PYTHON", self.spec["python"].command.path)

    def setup_run_environment(self, env):
        if self.spec.satisfies("+python"):
            pyver = self.spec["python"].version.up_to(2)
            env.prepend_path(
                "PYTHONPATH", join_path(self.prefix.lib, f"python{pyver}", "site-packages")
            )

    def configure_args(self):
        args = []
        if self.spec.satisfies("+python"):
            args.append("--enable-python-bindings")

        if self.spec.satisfies("+plugins"):
            args.append("--enable-python-plugins")

        if self.spec.satisfies("~manpages"):
            args.append("--disable-man-pages")

        return args
