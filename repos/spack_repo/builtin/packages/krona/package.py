# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Krona(Package):
    """Interactively explore metagenomes and more from a web browser."""

    homepage = "https://github.com/marbl/Krona"
    url = "https://github.com/marbl/Krona/releases/download/v2.8.1/KronaTools-2.8.1.tar"

    license("BSD-3-Clause")

    version("2.8.1", sha256="f3ab44bf172e1f846e8977c7443d2e0c9676b421b26c50e91fa996d70a6bfd10")

    depends_on("perl", type=("build", "run"))

    def patch(self):
        filter_file(
            "my \$scriptPath = abs_path\('scripts'\);",  # noqa: W605
            "my $scriptPath = '{0}';".format(join_path(self.spec.prefix, "scripts")),
            "install.pl",
        )

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)
        install_pl = Executable(join_path(self.stage.source_path, "install.pl"))
        install_pl("--prefix", prefix)
