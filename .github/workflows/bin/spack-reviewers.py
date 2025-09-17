# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

import requests

import spack.repo

IS_PACKAGE_CHANGE = re.compile(r"repos/spack_repo/builtin/packages/([^/]+)/.*$")


def main():
    repository = os.environ["GH_REPO"]
    pr_number = os.environ["GH_PR_NUMBER"]
    token = os.environ["GH_TOKEN"]

    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    base_url = f"https://api.github.com/repos/{repository}"
    pr_url = f"{base_url}/pulls/{pr_number}"
    pull_request = requests.get(pr_url, headers=headers).json()

    if pull_request["draft"]:
        print(f"[PR #{pr_number}]: skipping draft pull request")
        return

    pull_request_files = requests.get(f"{pr_url}/files", headers=headers)

    existing_reviewers = {reviewer["login"] for reviewer in pull_request["requested_reviewers"]}
    maintainers = set()

    for file in pull_request_files.json():
        if match := IS_PACKAGE_CHANGE.match(file["filename"]):
            package = match.group(1)

            # add maintainers from packages here
            try:
                pkg_maintainers = spack.repo.PATH.get_pkg_class(package).maintainers
                maintainers.update(pkg_maintainers)
            except spack.repo.UnknownPackageError:
                pass

    # filter maintianers to those who have triage permissions in the repo
    # users without triage permissions are unable to review PRs
    pingable_maintainers = set()
    for maintainer in maintainers:
        resp = requests.get(f"{base_url}/collaborators/{maintainer}", headers=headers)
        if resp.status_code == 204:
            pingable_maintainers.add(maintainer)

    author = pull_request["user"]["login"]
    reviewers = (pingable_maintainers | existing_reviewers) - {author}

    if existing_reviewers == reviewers:
        print(f"[PR #{pr_number}]: reviewers already up-to-date")
        return

    added_reviewers = reviewers - existing_reviewers
    if added_reviewers:
        print(f"[PR #{pr_number}]: adding reviewer(s):")
        for reviewer in sorted(added_reviewers):
            print(f"    @{reviewer}")

    if token:
        resp = requests.post(
            f"{pr_url}/requested_reviewers", json={"reviewers": list(reviewers)}, headers=headers
        )
        resp.raise_for_status()


if __name__ == "__main__":
    main()
