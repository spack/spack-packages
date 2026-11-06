# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

import requests

import spack.repo

IS_PACKAGE_CHANGE = re.compile(r"repos/spack_repo/builtin/packages/([^/]+)/.*$")


def msg(message: str, entries=()):
    print(message, flush=True)
    for entry in entries:
        print(f"    {entry}", flush=True)


def main():
    # Validate required environment variables
    required_vars = ["GH_REPO", "GH_PR_NUMBER", "MAINTAINER_ROLE"]
    missing_vars = [var for var in required_vars if var not in os.environ]
    if missing_vars:
        raise Exception(f"Missing required environment variables: {', '.join(missing_vars)}")

    repository = os.environ["GH_REPO"]
    pr_number = os.environ["GH_PR_NUMBER"]
    token = os.environ.get("GH_TOKEN", "")
    maintainer_role = os.environ["MAINTAINER_ROLE"]

    headers = {"Accept": "application/vnd.github+json", "User-Agent": "spack-reviewers"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    # use a requests session to attempt to retry failed requests if the GitHub API fails
    session = requests.Session()
    retries = requests.adapters.Retry(
        total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504]
    )
    session.mount("https://", requests.adapters.HTTPAdapter(max_retries=retries))

    base_url = f"https://api.github.com/repos/{repository}"
    pr_url = f"{base_url}/pulls/{pr_number}"
    pull_request_resp = session.get(pr_url, headers=headers, timeout=30)
    if pull_request_resp.status_code != 200:
        raise Exception(
            f"Failed to query GitHub API for PR info [{pull_request_resp.status_code}]: "
            f"{pull_request_resp.text}"
        )
    pull_request = pull_request_resp.json()

    # the workflow trigger already filters to merged PRs, but check again here just in case
    if not pull_request["merged"]:
        msg("pull request was not merged, skipping")
        return

    pull_request_files = session.get(f"{pr_url}/files", headers=headers, timeout=30)
    if pull_request_files.status_code != 200:
        raise Exception(
            f"Failed to query GitHub API for PR files [{pull_request_files.status_code}]: "
            f"{pull_request_files.text}"
        )
    changed_packages = {
        match.group(1)
        for file in pull_request_files.json()
        if (match := IS_PACKAGE_CHANGE.match(file["filename"]))
    }

    if changed_packages:
        msg("changed packages:", changed_packages)
    else:
        msg("no changed packages")
        return

    maintainers: set[str] = set()
    for package in changed_packages:
        try:
            maintainers.update(spack.repo.PATH.get_pkg_class(package).maintainers)
        except spack.repo.UnknownPackageError as e:
            msg(f"warning: {e}")
            pass

    if not maintainers:
        msg("no maintainers for changed packages")
        return

    # only invite maintainers who aren't collaborators: we don't want to modify existing perms
    collab_url = f"{base_url}/collaborators"
    non_collaborators = {
        maintainer
        for maintainer in maintainers
        if session.get(f"{collab_url}/{maintainer}", headers=headers, timeout=30).status_code
        != 204
    }

    if not non_collaborators:
        msg("all maintainers are already collaborators")
        return

    msg(
        f"inviting maintainers as outside collaborators ({maintainer_role}):",
        sorted(non_collaborators),
    )

    # invite as outside collaborators so they can perform PR reviews
    # they will need to accept the invitation before they can review PRs / be pinged
    if token:
        for maintainer in sorted(non_collaborators):
            invite_resp = session.put(
                f"{collab_url}/{maintainer}",
                json={"permission": maintainer_role},
                headers=headers,
                timeout=30,
            )
            if invite_resp.status_code in (201, 204):
                msg(f"invited {maintainer} as an outside collaborator ({maintainer_role})")
            else:
                msg(
                    f"failed to invite {maintainer} as a collaborator "
                    f"[{invite_resp.status_code}]: {invite_resp.text}"
                )


if __name__ == "__main__":
    main()
