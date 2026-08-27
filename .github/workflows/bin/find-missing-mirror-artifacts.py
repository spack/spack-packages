# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

"""Print one line per source artifact (version tarball, resource, or patch)
that is missing from the source mirror -- without concretizing anything.

Usage: spack python find-missing-mirror-artifacts.py <sha256-file>

``<sha256-file>`` contains one sha256 digest per line, obtained by listing the
content-addressed ``_source-cache/archive/`` prefix of the mirror.

Each output line is tab-separated::

    <sha256> TAB <mirror-path> TAB <url> [TAB <url> ...]

``mirror-path`` is the content-addressed location in the mirror
(``_source-cache/archive/<sha256[:2]>/<sha256>[.<ext>]``), computed with the
same ``default_mirror_layout()`` spack itself uses, so files uploaded to these
paths are found by ``spack fetch``. The URLs are candidate download locations
in order of preference.

Unlike ``spack mirror create``, nothing here requires concretization: URLs and
checksums for version tarballs, resources, and patches are all known
statically from package.py files. Conditional resources and patches are
included regardless of their ``when=`` conditions, since the mirror should
hold artifacts for every possible configuration. Only sha256-addressed URL
fetches are considered, which matches the content-addressed mirror layout;
git/svn/etc. versions have no place in ``_source-cache/archive``.
"""

import sys
from typing import Dict, List, Optional, Set, Tuple

import spack.error
import spack.fetch_strategy
import spack.package_base
import spack.patch
import spack.repo
import spack.spec
from spack.mirrors.layout import default_mirror_layout
from spack.util import tty

#: Cap on artifacts emitted per run so a single nightly job is bounded.
#: Artifacts mirrored successfully drop out of the missing list, so anything
#: past the cap is picked up by subsequent runs.
MAX_ARTIFACTS = 1000

#: digest -> (mirror path, candidate urls)
Entry = Tuple[str, List[str]]


def entry_for_fetcher(
    fetcher: spack.fetch_strategy.FetchStrategy,
    mirrored: Set[str],
    spec: Optional[spack.spec.Spec] = None,
    extra_urls: Optional[List[str]] = None,
) -> Optional[Tuple[str, Entry]]:
    """Return ``(digest, (mirror_path, urls))`` if ``fetcher`` is a
    sha256-addressed URL fetch missing from the mirror, else ``None``."""
    if not isinstance(fetcher, spack.fetch_strategy.URLFetchStrategy):
        return None

    # Only sha256 digests: the content-addressed layout and the workflow's
    # sha256sum verification both assume them. Note that for compressed
    # patches this is the *archive* sha256, which is what addresses the
    # mirror entry.
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

    urls = list(fetcher.candidate_urls)
    for url in extra_urls or ():
        if url not in urls:
            urls.append(url)

    return digest, (layout.digest_path, urls)


def missing_artifacts(mirrored: Set[str]) -> Dict[str, Entry]:
    """Map each missing sha256 to its mirror path and candidate URLs."""
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

            entry = entry_for_fetcher(fetcher, mirrored, spec=version_spec, extra_urls=extra_urls)
            if entry:
                entries[entry[0]] = entry[1]

        # Resources, regardless of their when= conditions
        for resource_list in pkg_cls.resources.values():
            for resource in resource_list:
                entry = entry_for_fetcher(resource.fetcher, mirrored)
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
            entry = entry_for_fetcher(patch.fetcher(), mirrored)
            if entry:
                entries.setdefault(entry[0], entry[1])

    return entries


def main(sha256_file: str) -> None:
    with open(sha256_file) as f:
        # Store shas as a set / hash-table for faster key lookups
        mirrored = {line.strip() for line in f if line.strip()}

    entries = missing_artifacts(mirrored)

    if len(entries) > MAX_ARTIFACTS:
        tty.warn(
            f"Limiting to first {MAX_ARTIFACTS} missing artifacts. "
            f"Detected {len(entries)} missing."
        )

    for digest, (path, urls) in list(entries.items())[:MAX_ARTIFACTS]:
        print("\t".join([digest, path, *urls]))


if __name__ == "__main__":
    main(sys.argv[1])
