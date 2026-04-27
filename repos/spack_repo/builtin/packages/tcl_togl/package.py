# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class TclTogl(AutotoolsPackage):
    """Tcl-Togl provides a platform independent Tcl/Tk widget
    for using OpenGL rendering contexts"""

    homepage = "https://togl.sourceforge.net/"
    url = "https://downloads.sourceforge.net/project/togl/Togl/2.0/Togl2.0-src.tar.gz"
    maintainers("gjsd2")

    license("BSD")

    version("2.0", sha256="b7d4a90bbad3aca618d505ee99e7fd8fb04c829f63231dda2360f557ba3f7610")

    variant("64bit", default=False, description="Build and link with shared libraries")
    variant("64bit-vis", default=False, description="Enable 64bit Sparc VIS support")
    variant("load", default=True, description='Allow dynamic loading and "load" command')
    variant("rpath", default=False, description="Disable rpath support")
    variant("shared", default=True, description="Build and link with shared libraries")
    variant("stubs", default=True, description="Build and link with stub libraries")
    variant("symbols", default=True, description="Build with debugging symbols")
    variant("threads", default=True, description="Build with threads")
    variant("wince", default=False, description="Enable Win/CE support")

    with when("build_system=autotools"):
        with default_args(type="build"):
            depends_on("autoconf")
            depends_on("automake")
            depends_on("libtool")

    depends_on("mesa")

    depends_on("c", type="build")
    depends_on("tk@8.1:")
    depends_on("tcl@8.1:")
    depends_on("libxmu")

    extends("tcl")

    def configure_args(self):
        args = []

        for enable_variant in (
            "64bit",
            "64bit-vis",
            "load",
            "rpath",
            "shared",
            "stubs",
            "symbols",
            "threads",
            "wince",
        ):
            args.extend(self.enable_or_disable(enable_variant))

        for with_dep in ("tcl", "tk"):
            args.append(f"--with-{with_dep}={self.spec[with_dep].prefix.lib}")
        args.append(f"--prefix={self.prefix}")
        args.append(f"--exec-prefix={self.prefix}")

        return args

    def setup_dependent_run_environment(self, env, dependent_spec):
        env.prepend_path(
            "LD_LIBRARY_PATH", join_path(self.prefix.lib, f"Togl{self.version.up_to(2)}")
        )
