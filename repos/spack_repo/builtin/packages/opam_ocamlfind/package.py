# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.opam import OpamPackage

from spack.package import *


class OpamOcamlfind(OpamPackage):
    """A library manager for OCaml.
    Findlib is a library manager for OCaml. It provides
    a convention how to store libraries, and a file
    format ("META") to describe the properties of libraries.
    There is also a tool (ocamlfind) for interpreting
    the META files, so that it is very easy to use
    libraries in programs and scripts."""

    has_code = False

    maintainers("green-br")

    version("1.9.8")

    depends_on("c", type="build")  # generated
    depends_on("opam", type=("build", "run"))

    opam_name = "ocamlfind"
