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
    required_vars = ["GH_REPO", "GH_PR_NUMBER"]
    missing_vars = [var for var in required_vars if var not in os.environ]
    if missing_vars:
        raise Exception(f"Missing required environment variables: {', '.join(missing_vars)}")

    repository = os.environ["GH_REPO"]
    pr_number = os.environ["GH_PR_NUMBER"]
    token = os.environ.get("GH_TOKEN", "")

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

    if pull_request["draft"]:
        msg("skipping draft pull request")
        return

    existing_reviewers = {reviewer["login"] for reviewer in pull_request["requested_reviewers"]}
    if existing_reviewers:
        msg("existing reviewers:", existing_reviewers)
    else:
        msg("no existing reviewers")

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

    # filter maintainers to those who have triage permissions in the repo
    # users without triage permissions are unable to review PRs
    collab_url = f"{base_url}/collaborators"
    pingable_maintainers = {
        maintainer
        for maintainer in maintainers
        if session.get(f"{collab_url}/{maintainer}", headers=headers, timeout=30).status_code
        == 204
    }

    if maintainers != pingable_maintainers:
        msg(
            "the following package maintainers cannot be added as reviewers "
            "(no collaborator status):",
            sorted(maintainers - pingable_maintainers),
        )

    author = pull_request["user"]["login"]
    reviewers = (pingable_maintainers | existing_reviewers) - {author}

    if existing_reviewers == reviewers:
        msg("reviewers already up-to-date")
        return

    added_reviewers = reviewers - existing_reviewers
    if added_reviewers:
        msg("adding reviewers:", added_reviewers)

    if token:
        resp = session.post(
            f"{pr_url}/requested_reviewers",
            json={"reviewers": list(reviewers)},
            headers=headers,
            timeout=30,
        )
        resp.raise_for_status()


if __name__ == "__main__":
    main()
