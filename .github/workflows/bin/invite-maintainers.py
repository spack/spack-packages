# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# This script runs with an admin-capable token, so it intentionally does not
# import Spack or any package code.

import os
import re
import sys

import requests

# MAINTAINERS is generated from a job that imports package.py files.
# Although those files were merged into develop, we still validate usernames
# to limit chances of a rogue username containing dangerous escape characters.
VALID_USERNAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]{0,38}$")


def msg(message: str, entries=()):
    print(message, flush=True)
    for entry in entries:
        print(f"    {entry}", flush=True)


def get_expired_invitations(session, headers, base_url):
    """Return expired invitation ids on the repo, keyed by lowercased invitee login."""
    expired = {}
    url = f"{base_url}/invitations?per_page=100"
    while url:
        resp = session.get(url, headers=headers, timeout=30)
        resp.raise_for_status()
        for invitation in resp.json():
            if invitation.get("expired") and invitation.get("invitee"):
                expired[invitation["invitee"]["login"].lower()] = invitation["id"]
        url = resp.links.get("next", {}).get("url")
    return expired


def main():
    required_vars = ["GH_REPO", "GH_TOKEN", "MAINTAINERS", "MAINTAINER_ROLE"]
    missing_vars = [var for var in required_vars if var not in os.environ]
    if missing_vars:
        raise Exception(f"Missing required environment variables: {', '.join(missing_vars)}")

    repository = os.environ["GH_REPO"]
    token = os.environ["GH_TOKEN"]
    maintainers = set(os.environ["MAINTAINERS"].split())
    maintainer_role = os.environ["MAINTAINER_ROLE"]

    if not maintainers:
        msg("no maintainers to invite")
        return

    invalid = sorted(m for m in maintainers if not VALID_USERNAME.match(m))
    if invalid:
        raise Exception(f"invalid GitHub usernames in MAINTAINERS: {invalid}")

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "spack-invite-maintainers",
    }

    # use a requests session to attempt to retry failed requests if the GitHub API fails
    session = requests.Session()
    retries = requests.adapters.Retry(
        total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504]
    )
    session.mount("https://", requests.adapters.HTTPAdapter(max_retries=retries))

    # only invite maintainers who aren't collaborators: we don't want to modify existing perms
    base_url = f"https://api.github.com/repos/{repository}"
    collab_url = f"{base_url}/collaborators"
    non_collaborators = []
    failed = []
    for maintainer in sorted(maintainers):
        resp = session.get(f"{collab_url}/{maintainer}", headers=headers, timeout=30)
        if resp.status_code == 404:
            non_collaborators.append(maintainer)
        elif resp.status_code != 204:
            msg(
                f"failed to check collaborator status for {maintainer} "
                f"[{resp.status_code}]: {resp.text}"
            )
            failed.append(maintainer)

    if not non_collaborators:
        if failed:
            msg("failed to invite:", failed)
            sys.exit(1)
        msg("all maintainers are already collaborators")
        return

    msg(f"inviting maintainers as outside collaborators ({maintainer_role}):", non_collaborators)

    # invite as outside collaborators so they can perform PR reviews
    # they will need to accept the invitation before they can review PRs / be pinged
    expired_invitations = get_expired_invitations(session, headers, base_url)
    for maintainer in non_collaborators:
        # delete an expired invitation first so a fresh one is sent
        invitation_id = expired_invitations.get(maintainer.lower())
        if invitation_id is not None:
            delete_resp = session.delete(
                f"{base_url}/invitations/{invitation_id}", headers=headers, timeout=30
            )
            if delete_resp.status_code != 204:
                msg(
                    f"failed to delete expired invitation for {maintainer} "
                    f"[{delete_resp.status_code}]: {delete_resp.text}"
                )
                failed.append(maintainer)
                continue
            msg(f"deleted expired invitation for {maintainer}")

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
            failed.append(maintainer)

    if failed:
        msg("failed to invite:", failed)
        sys.exit(1)


if __name__ == "__main__":
    main()
