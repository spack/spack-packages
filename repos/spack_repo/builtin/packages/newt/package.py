# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Newt(AutotoolsPackage):
    """A library for text mode user interfaces."""

    homepage = "https://pagure.io/newt"
    url = "https://pagure.io/releases/newt/newt-0.52.21.tar.gz"

    license("LGPL-2.0-only")

    version("0.52.25", sha256="ef0ca9ee27850d1a5c863bb7ff9aa08096c9ed312ece9087b30f3a426828de82")
    version("0.52.21", sha256="265eb46b55d7eaeb887fca7a1d51fe115658882dfe148164b6c49fccac5abb31")
    version("0.52.20", sha256="8d66ba6beffc3f786d4ccfee9d2b43d93484680ef8db9397a4fb70b5adbb6dbc")
    version("0.52.19", sha256="08c0db56c21996af6a7cbab99491b774c6c09cef91cd9b03903c84634bff2e80")

    # newt prior to 0.51.21 did not allow one to specify where to find Python and would
    # only look in /usr. Avoid using Python with earlier versions.
    variant("python", when="@0.52.21:", default=False, description="Build the snack python module")

    depends_on("c", type="build")  # generated

    depends_on("gettext")
    depends_on("popt")
    depends_on("slang")

    depends_on("python", when="@0.52.21: +python")

    # Beginning with newt 0.52.25, snack is installed into Python's site-packages, but
    # we prefer the module to stay within newt's prefix
    patch("0001-adjust-snack-installation.patch", when="@0.51.25: +python")

    def configure_args(self):
        args = []

        # If --without-python is not specified, configure will try to find Python on
        # PATH.
        if self.spec.satisfies("~python") or self.version < Version("0.52.21"):
            args.append("--without-python")

        if self.spec.satisfies("+python"):
            args.append(f"--with-python=python{self.spec['python'].version.up_to(2)}")

        return args

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        super().setup_build_environment(env)
        # Without these flags, newt does not link properly against libintl from
        # spack-provided gettext
        env.set("CPPFLAGS", f"-I{self.spec['gettext'].prefix.include}")
        env.set("LDFLAGS", f"-L{self.spec['gettext'].prefix.lib}")
        env.set("LIBS", "-lintl")

    @when("+python")
    def setup_dependent_run_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        env.prepend_path(
            "PYTHONPATH",
            f"{self.spec.prefix.lib}/python{self.spec['python'].version.up_to(2)}/site-packages",
        )
