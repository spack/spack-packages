# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

import requests
import yaml


def import_labels_config(path: str):
    with open(path) as fd:
        try:
            label_patterns = yaml.safe_load(fd)
        except yaml.YAMLError as exc:
            raise Exception(f"Unable to load {path}\n{exc}")

        # compile all the regexes above, and ensure that all pattern dict values are lists
        for label, pattern_dict in label_patterns.items():
            for attr in pattern_dict.keys():
                patterns = pattern_dict[attr]
                if not isinstance(patterns, list):
                    patterns = [patterns]
                pattern_dict[attr] = [re.compile(s) for s in patterns]

    return label_patterns


def main():
    labels_config_path = os.environ.get("LABELS_CONFIG")
    repository = os.environ.get("GH_REPO")
    pr_number = os.environ.get("GH_PR_NUMBER")
    token = os.environ.get("GH_TOKEN")

    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    label_patterns = import_labels_config(labels_config_path)

    url = f"https://api.github.com/repos/{repository}/pulls/{pr_number}"
    pull_request = requests.get(url, headers=headers).json()

    pull_request_files = requests.get(url + "/files", headers=headers)

    labels = set()

    for file in pull_request_files.json():
        # Add our own "package" attribute to the file, if it's a package
        match = re.match(
            r"repos/spack_repo/builtin/packages/([^/]+)/package.py$", file["filename"]
        )
        file["package"] = match.group(1) if match else ""

        # If the file's attributes match any patterns in label_patterns, add
        # the corresponding labels.
        for label, pattern_dict in label_patterns.items():
            attr_matches = []
            # Pattern matches for for each attribute are or'd together
            for attr, patterns in pattern_dict.items():
                # 'patch' is an example of an attribute that is not required to
                # appear in response when listing pull request files.  See here:
                #
                #    https://docs.github.com/en/rest/pulls/pulls#list-pull-requests-files
                #
                # If we don't get some attribute in the response, no labels that
                # depend on finding a match in that attribute should be added.
                attr_matches.append(
                    any(p.search(file[attr]) for p in patterns) if attr in file else False
                )
            # If all attributes have at least one pattern match, we add the label
            if all(attr_matches):
                labels.add(label)

    existing_labels = {label["name"] for label in pull_request["labels"]}
    if existing_labels == labels:
        print(f"[PR #{pr_number}]: labels already up-to-date")
        return

    added_labels = labels - existing_labels
    if added_labels:
        print(f"[PR #{pr_number}]: Adding label(s): [{'] ['.join(added_labels)}]")

    removed_labels = existing_labels - labels
    if removed_labels:
        print(f"[PR #{pr_number}]: Removing label(s): [{'] ['.join(removed_labels)}]")

    if token:
        resp = requests.put(
            f"https://api.github.com/repos/{repository}/issues/{pr_number}/labels",
            json={"labels": list(labels)},
            headers=headers,
        )
        resp.raise_for_status()


if __name__ == "__main__":
    main()
