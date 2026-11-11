# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from datetime import datetime, timezone
import tarfile

from spack_repo.builtin.build_systems.go import GoBuilder as BuiltinGoBuilder
from spack_repo.builtin.build_systems.go import GoPackage as BuiltinGoPackage

from spack.package import *


class GolangciLint(BuiltinGoPackage):
    """golangci-lint is a fast Go linters runner. It runs linters in parallel,
    uses caching, supports YAML configuration, integrates with all major IDEs,
    and includes over a hundred linters."""

    homepage = "https://github.com/golangci/golangci-lint"
    url = "https://github.com/golangci/golangci-lint/archive/refs/tags/v2.15.0.tar.gz"

    license("GPL-3.0-only")

    maintainers("ebagrenrut")

    version("2.15.0", sha256="5411598703f014f1128b209f3d46da6f9f2c99a68783c90f846b4db1c8c08742")

    depends_on("go@1.26:", type="build")

    class GoBuilder(BuiltinGoBuilder):
        """This custom GoBuilder allows us to override the build_directory
        and ldflags properties while adding a commit_id property."""

        @property
        def build_directory(self):
            return join_path(self.stage.source_path, "cmd", self.pkg.name)

        @property
        def commit_id(self) -> str:
            archive = self.stage.archive_file

            try:
                with tarfile.open(archive, "r:gz") as content:
                    # Headers should be the first thing in the tarball
                    headers = content.next()

                    # `git archive` adds `pax_headers`, which contain the commit ID
                    # in the `comment` attribute
                    if headers and hasattr(headers, "pax_headers"):
                        commit_id = headers.pax_headers.get("comment")

                        if commit_id:
                            return commit_id.strip()

            except Exception:
                tty.warn("Could not extract git commit ID from source archive")

            return "(unknown)"

        @property
        def ldflags(self) -> List[str]:
            return [
                f"-X main.version={self.pkg.version}",
                f"-X main.commit={self.commit_id}",
                f"-X main.date={datetime.now(timezone.utc).isoformat(timespec='seconds')}",
            ]
