# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re
import subprocess

import requests

IS_PACKAGE = re.compile(r"repos/spack_repo/builtin/packages/([^/]+)/package.py$")


def main():
    repository = os.environ["GH_REPO"]
    pr_number = os.environ["GH_PR_NUMBER"]
    token = os.environ["GH_TOKEN"]

    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    base_url = f"https://api.github.com/repos/{repository}/pulls/{pr_number}"
    pull_request = requests.get(base_url, headers=headers).json()

    pull_request_files = requests.get(f"{base_url}/files", headers=headers)

    existing_reviewers = {reviewer["login"] for reviewer in pull_request["requested_reviewers"]}
    maintainers = set()

    for file in pull_request_files.json():
        if match := IS_PACKAGE.match(file["filename"]):
            package = match.group(1)

            # add maintainers from packages here
            result = subprocess.run(
                ["spack", "maintainers", package], capture_output=True, text=True, check=False
            )
            maintainers.update(result.stdout.split())

    author = pull_request["user"]["login"]
    reviewers = (maintainers | existing_reviewers) - {author}

    if existing_reviewers == reviewers:
        print(f"[PR #{pr_number}]: reviewers already up-to-date")
        return

    added_reviewers = reviewers - existing_reviewers
    if added_reviewers:
        print(f"[PR #{pr_number}]: adding reviewer(s): @{' @'.join(added_reviewers)}")

    if token:
        resp = requests.post(
            f"{base_url}/requested_reviewers", json={"reviewers": list(reviewers)}, headers=headers
        )
        # https://docs.github.com/en/rest/pulls/review-requests
        # endpoint may return status code 422 for users who are not collaborators
        # or have not accepted their invites to the organization yet
        if resp.status_code != 422:
            resp.raise_for_status()


if __name__ == "__main__":
    main()
