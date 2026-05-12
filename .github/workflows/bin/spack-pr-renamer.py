#!/usr/bin/env python3

# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

import requests

IS_PACKAGE_CHANGE = re.compile(r"repos/spack_repo/builtin/packages/([^/]+)/.*$")
VERSION_LINE = re.compile(r'[\s]+version\([\s+\+]*"([^"]+)"[^\)]*\)')


def main():
    # Validate required environment variables
    required_vars = ["GH_REPO", "GH_PR_NUMBER"]
    missing_vars = [var for var in required_vars if var not in os.environ]
    if missing_vars:
        raise Exception(f"Missing required environment variables: {', '.join(missing_vars)}")

    repository = os.environ["GH_REPO"]
    pr_number = os.environ["GH_PR_NUMBER"]
    token = os.environ.get("GH_TOKEN", "")

    headers = {"Accept": "application/vnd.github+json", "User-Agent": "spack-pr-renamer"}
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

    # Check if the PR has been manually renamed by a user
    # Get PR events to check for rename history
    events_resp = session.get(f"{base_url}/issues/{pr_number}/events", headers=headers, timeout=30)
    if events_resp.status_code == 200:
        events = events_resp.json()
        for event in events:
            if event["event"] == "renamed":
                # If any non-bot user renamed it, respect their choice
                actor = event.get("actor", {}).get("login", "")
                if actor and "[bot]" not in actor and actor != "github-actions":
                    print(f"PR was manually renamed by {actor}, respecting user preference")
                    return

    # Get PR files
    pull_request_files = session.get(f"{pr_url}/files", headers=headers, timeout=30)
    if pull_request_files.status_code != 200:
        raise Exception(
            f"Failed to query GitHub API for PR files [{pull_request_files.status_code}]: "
            f"{pull_request_files.text}"
        )

    files = pull_request_files.json()

    # Only process single-file package changes
    if len(files) != 1:
        print("skipping multi-file PR")
        return

    file = files[0]
    match = IS_PACKAGE_CHANGE.match(file["filename"])
    if not match:
        print("skipping non-package PR")
        return

    package_name = match.group(1).replace("_", "-")
    current_title = pull_request["title"]
    labels = {label["name"] for label in pull_request["labels"]}
    new_title = None

    # Handle new-package label
    if "new-package" in labels:
        # Verify this is truly a new package (not a rename/move)
        if file["status"] == "added":
            new_title = f"{package_name}: new package"

    # Handle new-version label (but not if also has new-variant)
    elif "new-version" in labels and "new-variant" not in labels:
        # Get PR diff to extract version changes
        diff_resp = session.get(
            f"{base_url}/pulls/{pr_number}.diff",
            headers=headers,
            timeout=30,
        )
        if diff_resp.status_code != 200:
            raise Exception(
                f"Failed to get PR diff [{diff_resp.status_code}]: {diff_resp.text}"
            )

        diff_text = diff_resp.text
        deleted_versions = set(VERSION_LINE.findall(diff_text.replace("\n+", "\n ")))
        added_versions = sorted(
            set(VERSION_LINE.findall(diff_text.replace("\n-", "\n "))) - deleted_versions
        )

        if added_versions:
            # Format versions with 'v' prefix if they start with a digit
            versions = [f"v{v}" if v[0].isdigit() else v for v in added_versions]

            if len(versions) < 4:
                new_title = f"{package_name}: add {', '.join(versions)}"
            else:
                new_title = f"{package_name}: add {versions[0]} -> {versions[-1]}"

    # Update title if needed
    if new_title and current_title != new_title:
        print(f"Renaming PR #{pr_number}: {current_title} -> {new_title}")

        if token:
            resp = session.patch(
                pr_url,
                json={"title": new_title},
                headers=headers,
                timeout=30,
            )
            resp.raise_for_status()
    else:
        print("PR title already up-to-date or no rename needed")


if __name__ == "__main__":
    main()
