#!/usr/bin/env spack-python
#
# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

"""Sync the source mirror with the package repository -- without concretizing.

Usage: sync-src-mirror.py <sha256-file> [--upload-to s3://bucket]

``<sha256-file>`` contains one sha256 digest per line, obtained by listing the
content-addressed ``_source-cache/archive/`` prefix of the mirror.

This script:
 1. finds every source artifact (version tarball, resource, or patch)
    that is missing from the mirror;
 2. Fetches it with spack's own fetch strategies that honor per-package
    ``fetch_options``, mirrors, and checksum verification; and
 3. Uploads each verified artifact to the mirror with
   ``aws s3 cp``.

Uploads are one at a time, to bound disk usage.
Without ``--upload-to``, it just lists what is missing.

This behaves like `spack mirror create --all`, in that all resources and
patches are included regardless of their ``when=`` conditions, since the mirror
should hold artifacts for every possible configuration. Only sha256-addressed
URL fetches are considered, which matches the content-addressed mirror
layout; git/svn/etc. versions have no place in ``_source-cache/archive``.

Artifacts are stored at ``_source-cache/archive/<sha256[:2]>/<sha256>[.<ext>]``,
computed with the same ``default_mirror_layout()`` spack itself uses.

Individual fetch failures (dead upstream URLs etc.) are tolerated; they will
simply be retried on the next run.

TODO: Parts of this should likely be integrated with `spack mirror create`
eventually. This exists in spack-packages because `spack mirror create --all`
currently concretizes specs when run from an environment, and it's hard to write
an environment to fetch only artifacts needed by certain package versions without
reconcretizing. Once that is done, replace this script.

"""

import argparse
from typing import Dict, List, Optional, Set, Tuple

import spack.error
import spack.fetch_strategy
import spack.package_base
import spack.patch
import spack.repo
import spack.spec
import spack.stage
from spack.mirrors.layout import default_mirror_layout
from spack.util import tty
from spack.util.executable import Executable, which

#: Cap on artifacts mirrored per run so a single nightly job is bounded.
#: Artifacts mirrored successfully drop out of the missing list, so anything
#: past the cap is picked up by subsequent runs.
MAX_ARTIFACTS = 1000

#: digest -> (mirror path, fetcher, human-readable label)
Entry = Tuple[str, spack.fetch_strategy.URLFetchStrategy, str]


def entry_for_fetcher(
    fetcher: spack.fetch_strategy.FetchStrategy,
    label: str,
    mirrored: Set[str],
    spec: Optional[spack.spec.Spec] = None,
    extra_urls: Optional[List[str]] = None,
) -> Optional[Tuple[str, Entry]]:
    """Return ``(digest, (mirror_path, fetcher, label))`` if ``fetcher`` is a
    sha256-addressed URL fetch missing from the mirror, else ``None``."""
    if not isinstance(fetcher, spack.fetch_strategy.URLFetchStrategy):
        return None

    # Only sha256 digests: the content-addressed layout assumes them. Note
    # that for compressed patches this is the *archive* sha256, which is what
    # addresses the mirror entry.
    digest = fetcher.digest
    if not digest or len(digest) != 64 or digest in mirrored:
        return None

    try:
        # The alias argument is only used for the human-readable symlink,
        # which we never create; digest_path is the content-addressed path.
        layout = default_mirror_layout(fetcher, "unused", spec)
    except spack.error.MirrorError as e:
        tty.warn(str(e))
        return None

    # Fold any fallback URLs into the fetcher's mirrors so fetch() tries them
    for url in extra_urls or ():
        if url != fetcher.url and url not in fetcher.mirrors:
            fetcher.mirrors.append(url)

    return digest, (layout.digest_path, fetcher, label)


def missing_artifacts(mirrored: Set[str]) -> Dict[str, Entry]:
    """Map each missing sha256 to its mirror path, fetcher, and label."""
    entries: Dict[str, Entry] = {}
    repo = spack.repo.PATH.get_repo("builtin")

    for pkg_cls in repo.all_package_classes():
        # Manual-download packages cannot be fetched by URL
        if pkg_cls.manual_download:
            continue

        try:
            pkg = pkg_cls(spack.spec.Spec(pkg_cls.name))
        except Exception as e:
            tty.warn(f"{pkg_cls.name}: could not instantiate package: {e}")
            continue

        # Version tarballs. Restrict to versions with a sha256 up front; that
        # skips git/manual versions cheaply and mirrors the filtering done by
        # the content-addressed layout itself.
        for version, version_dict in pkg_cls.versions.items():
            sha256 = version_dict.get("sha256")
            if not isinstance(sha256, str) or sha256 in entries or sha256 in mirrored:
                continue

            # Skip versions we may not redistribute (proprietary sources)
            version_spec = spack.spec.Spec(f"{pkg_cls.name}@={version}")
            if not pkg_cls.redistribute_source(version_spec):
                continue

            try:
                fetcher = spack.package_base.for_package_version(pkg, version)
                # Fall back to any other URLs the package knows for this
                # version (url_for_version, urls list, ...)
                extra_urls = pkg.all_urls_for_version(version)
            except Exception as e:
                tty.warn(f"{pkg_cls.name}@{version}: could not determine URL: {e}")
                continue

            entry = entry_for_fetcher(
                fetcher, str(version_spec), mirrored, spec=version_spec, extra_urls=extra_urls
            )
            if entry:
                entries[entry[0]] = entry[1]

        # Resources, regardless of their when= conditions
        for resource_list in pkg_cls.resources.values():
            for resource in resource_list:
                entry = entry_for_fetcher(
                    resource.fetcher, f"{pkg_cls.name} resource {resource.name}", mirrored
                )
                if entry:
                    entries.setdefault(entry[0], entry[1])

    # Patches come from the repo's patch index rather than per-package
    # ``patches`` attributes: the index also covers patches applied to
    # dependencies via ``depends_on(..., patches=...)``, which spack looks up
    # by sha256 from the ``patches=`` variant. Accessing the index builds the
    # repo's data cache if needed. FilePatch (no ``url`` key) lives in the
    # repo itself and needs no mirroring. Note that compressed patches are
    # mirrored by their *archive* sha256, not the index key, which is the
    # sha256 of the uncompressed patch.
    for sha256, by_pkg in repo.get_patch_index().index.items():
        for patch_dict in by_pkg.values():
            if "url" not in patch_dict:
                continue
            try:
                # the sha256 is removed from entries on write to save space,
                # since it is the index key; add it back (see Patch.to_dict())
                patch_dict = dict(patch_dict, sha256=sha256)
                patch = spack.patch.from_dict(patch_dict, repository=spack.repo.PATH)
            except Exception as e:
                tty.warn(f"could not read patch: {patch_dict.get('url')}: {e}")
                continue
            assert isinstance(patch, spack.patch.UrlPatch)
            entry = entry_for_fetcher(
                patch.fetcher(), f"{patch.owner} patch {patch.url}", mirrored
            )
            if entry:
                entries.setdefault(entry[0], entry[1])

    return entries


def mirror_artifact(
    path: str, fetcher: spack.fetch_strategy.FetchStrategy, s3_url: str, aws: Executable
) -> None:
    """Fetch one artifact, verify its checksum, and upload it to the mirror.

    The stage (and the downloaded file with it) is destroyed on exit either
    way, so disk usage stays bounded to one artifact at a time.
    """
    with spack.stage.Stage(fetcher) as stage:
        stage.fetch()
        stage.check()
        aws("s3", "cp", stage.archive_file, f"{s3_url}/{path}", "--no-overwrite", "--no-progress")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sha256_file", help="file with one mirrored sha256 digest per line")
    parser.add_argument(
        "--upload-to", metavar="S3_URL", help="mirror url (s3://bucket); omit to just list"
    )
    args = parser.parse_args()

    # fail fast if we can't upload before fetching anything
    aws = which("aws", required=True) if args.upload_to else None

    with open(args.sha256_file) as f:
        # Store shas as a set / hash-table for faster key lookups
        mirrored = {line.strip() for line in f if line.strip()}

    entries = missing_artifacts(mirrored)
    if not entries:
        tty.msg("Mirror is up to date")
        return

    if len(entries) > MAX_ARTIFACTS:
        tty.warn(
            f"Limiting to first {MAX_ARTIFACTS} missing artifacts. "
            f"Detected {len(entries)} missing."
        )

    uploaded, failed = 0, 0
    for digest, (path, fetcher, label) in list(entries.items())[:MAX_ARTIFACTS]:
        print(f"{label}: {path}")
        if not args.upload_to:
            continue

        try:
            mirror_artifact(path, fetcher, args.upload_to.rstrip("/"), aws)
            uploaded += 1
        except Exception as e:
            tty.warn(f"could not mirror {label}: {e}")
            failed += 1

    if args.upload_to:
        tty.msg(f"Uploaded {uploaded} artifacts to the mirror; {failed} failed")
    else:
        tty.msg(f"{len(entries)} artifacts missing from the mirror (listed only; no --upload-to)")


if __name__ == "__main__":
    main()
