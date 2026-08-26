# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

"""Print one ``pkg@=version`` spec per line for every checksummed package
version that is not yet present in the source mirror.

Usage: spack python find-missing-mirror-specs.py <sha256-file>

``<sha256-file>`` contains one sha256 digest per line, obtained by listing the
content-addressed ``_source-cache/archive/`` prefix of the mirror. Only
URL-based versions with a ``sha256`` are considered, which matches the
content-addressed layout (``archive/<sha256[:2]>/<sha256>.<ext>``) used by
``spack mirror create`` and mirrors the filtering done by
``spack repo show-version-updates --no-manual-packages --only-redistributable
--no-git-versions``.
"""

import sys
from typing import Dict, List

import spack.repo
import spack.spec
from spack.util import tty
from spack.version import StandardVersion


def main(sha256_file: str) -> None:
    with open(sha256_file) as f:
        # Store shas as a set / hash-table for faster key lookups
        mirrored = {line.strip() for line in f if line.strip()}

    specs_to_output: List[spack.spec.Spec] = []

    repo = spack.repo.PATH.get_repo("builtin")

    for pkg_cls in repo.all_package_classes():
        # Filter out manual packages
        if pkg_cls.manual_download:
            continue

        # Get all versions with checksums; no sha256 means not a
        # content-addressed URL fetch (e.g. a git version)
        version_to_checksum: Dict[StandardVersion, str] = {
            version: version_dict["sha256"]
            for version, version_dict in pkg_cls.versions.items()
            if "sha256" in version_dict
        }

        for version, sha256 in version_to_checksum.items():
            if sha256 in mirrored:
                continue
            version_spec = spack.spec.Spec(pkg_cls.name)
            version_spec.constrain(f"@={version}")
            specs_to_output.append(version_spec)

    # Filter out non-redistributable packages
    specs_to_output = [
        spec for spec in specs_to_output if repo.get_pkg_class(spec.name).redistribute_source(spec)
    ]

    # Output specs one per line for use by `spack mirror create`
    # limit to a maximum of 100 specs at a time due to GitHub
    # runner disk space limitations. Skipped specs will be
    # retried on the next scheduled job.
    specs_to_output_num = len(specs_to_output)
    if specs_to_output_num > 100:
        tty.warn(f"Limiting to first 100 missing specs. Detected {specs_to_output_num} missing.")

    for spec in specs_to_output[:100]:
        print(spec)


if __name__ == "__main__":
    main(sys.argv[1])
