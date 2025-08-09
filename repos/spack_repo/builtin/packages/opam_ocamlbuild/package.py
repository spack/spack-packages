# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.opam import OpamPackage

from spack.package import *


class OpamOcamlbuild(OpamPackage):
    """OCamlbuild is a build system with builtin rules to
    easily build most OCaml projects"""

    has_code = False

    maintainers("green-br")

    version("0.16.1")

    depends_on("c", type="build")  # generated
    depends_on("opam", type=("build", "run"))

    opam_name = "ocamlbuild"
