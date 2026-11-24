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


def find_maintainers() -> set:
    repository = os.environ["GH_REPO"]
    pr_number = os.environ["GH_PR_NUMBER"]
    token = os.environ["GH_TOKEN"]

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "spack-find-maintainers",
    }

    # use a requests session to attempt to retry failed requests if the GitHub API fails
    session = requests.Session()
    retries = requests.adapters.Retry(
        total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504]
    )
    session.mount("https://", requests.adapters.HTTPAdapter(max_retries=retries))

    pr_url = f"https://api.github.com/repos/{repository}/pulls/{pr_number}"
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
        return set()

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

    if not changed_packages:
        msg("no changed packages")
        return set()
    msg("changed packages:", changed_packages)

    maintainers: set = set()
    for package in changed_packages:
        try:
            maintainers.update(spack.repo.PATH.get_pkg_class(package).maintainers)
        except spack.repo.UnknownPackageError as e:
            msg(f"warning: {e}")

    if maintainers:
        msg("maintainers of changed packages:", sorted(maintainers))
    else:
        msg("no maintainers for changed packages")
    return maintainers


def main():
    required_vars = ["GH_REPO", "GH_PR_NUMBER", "GH_TOKEN", "GITHUB_OUTPUT"]
    missing_vars = [var for var in required_vars if var not in os.environ]
    if missing_vars:
        raise Exception(f"Missing required environment variables: {', '.join(missing_vars)}")

    maintainers = find_maintainers()
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"maintainers={' '.join(sorted(maintainers))}\n")


if __name__ == "__main__":
    main()
