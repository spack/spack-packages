# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from typing import Optional, Tuple

from spack.package import (
    Builder,
    ClassProperty,
    Executable,
    PackageBase,
    Prefix,
    ProcessError,
    Spec,
    build_system,
    classproperty,
    extends,
    maintainers,
    register_builder,
    tty,
)


def _homepage(cls: "OpamPackage") -> Optional[str]:
    if cls.opam_name:
        return f"https://opam.ocaml.org/packages/{cls.opam_name}"
    return None


class OpamPackage(PackageBase):
    """Specialized class for packages that are built using Opam's
    `opam install` command.
    """

    #: Package name, version, and extension.
    maintainers("green-br")
    # To be used in UI queries that require to know which
    # build-system class we are using
    build_system_class = "OpamPackage"
    #: Legacy buildsystem attribute used to deserialize and install old specs
    default_buildsystem = "opam"

    build_system("opam")

    extends("opam", when="build_system=opam")

    opam_name: Optional[str] = None
    homepage: ClassProperty[Optional[str]] = classproperty(_homepage)


@register_builder("opam")
class OpamBuilder(Builder):
    """The Opam builder provides an ``install`` phase that can be overridden."""

    phases = ("install",)

    #: Names associated with package methods in the old build-system format
    package_methods: Tuple[str, ...] = tuple()

    #: Names associated with package attributes in the old build-system format
    package_attributes = ()

    opam_name: Optional[str] = None

    def install(self, pkg: OpamPackage, spec: Spec, prefix: Prefix) -> None:
        if spec["opam"].satisfies("+user"):
            tty.warn(f"User provided package: {spec['opam']}")
            return
        opam = Executable("opam")
        name = pkg.opam_name
        assert name is not None, "Opam package name is not set"
        args = [
            "exec",
            "--root={0}/root".format(spec["opam"].prefix),
            "--set-root",
            "--",
            "opam",
            "install",
            "--skip-updates",
            "{0}={1}".format(name, spec.version),
        ]
        try:
            opam(*args)
        except ProcessError as e:
            tty.warn(f"opam install failed with {e}")
