# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlModuleBuildTiny(PerlPackage):
    """Module::Build::Tiny - A tiny replacement for Module::Build"""

    homepage = "https://metacpan.org/pod/Module::Build::Tiny"
    url = "https://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-Tiny-0.039.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version(
        "0.052", sha256="bd10452c9f24d4b4fe594126e3ad231bab6cebf16acda40a4e8dc784907eb87f"
    )  # FIXME
    version(
        "0.051", sha256="74fdce35e8cd4d787bc2d4fc1d43a291b7bbced4e94dc5fc592bd81ca93a98e9"
    )  # FIXME
    version(
        "0.050", sha256="8010be2fa1cad8cc971f6c727034b53ee21a95497384b9c2eb071b7b00ea0b5c"
    )  # FIXME
    version(
        "0.049", sha256="61b0207708dc1899dad2111f92afa6f88c26e8e9c946e28a0dbbb9e9b8082f18"
    )  # FIXME
    version("0.048", sha256="79a73e506fb7badabdf79137a45c6c5027daaf6f9ac3dcfb9d4ffcce92eb36bd")
    version("0.044", sha256="cb053a3049cb717dbf4fd7f3c7ab7c0cb1015b22e2d93f38b1ffc47c078322fd")
    version("0.039", sha256="7d580ff6ace0cbe555bf36b86dc8ea232581530cbeaaea09bccb57b55797f11c")

    depends_on("perl-module-build", type="build")
    depends_on("perl-extutils-config", type=("build", "run"))
    depends_on("perl-extutils-helpers", type=("build", "run"))
    depends_on("perl-extutils-installpaths", type=("build", "run"))
