# Skill: General Package Version Update (Bulk)

Perform a bulk update of many packages across one or more ecosystems in this Spack repository.
This skill covers the full workflow: inventorying locally modified packages, verifying dependency
changes introduced by new versions, grouping the changes into coherent pull requests, and
submitting all PRs as drafts for human review.

Use the more focused [`py-package-update`](py-package-update.md) skill for smaller, targeted
updates of Python packages.

## Usage

Invoke this skill when the working tree already contains many modified `package.py` files that
need to be committed and submitted, or when you want to refresh a broad set of packages to their
latest upstream releases:

```
Update all locally modified packages and open PRs
Update all packages in the HEP stack to their latest versions
```

## Step-by-Step Instructions

---

### Phase 1 — Inventory the modified packages

#### 1a. List all modified package files

```sh
git diff --name-only HEAD | grep 'packages/' | sort
```

Also check for new (untracked) package directories that should be included:

```sh
git status --short | grep '^\?\?' | grep 'packages/'
```

Note any new packages (entirely new directories), new patch files, and packages with
structural changes beyond just version bumps.

#### 1b. Classify each package

For each modified file record:

- Package name (Spack name with hyphens)
- Highest new version being added
- Whether the change is: version-only, dependency change, build-system change, new package,
  or new patch file

---

### Phase 2 — Verify dependency changes for each package

For every modified package, determine what dependency changes the **new versions** introduce.
This requires comparing the upstream build specification of the new version against the
previously packaged version.

#### 2a. Locate the upstream source

The upstream source is identified by the `pypi`, `url`, or `git` attribute in `package.py`.

- **PyPI packages** (`pypi =`): fetch `https://pypi.org/pypi/<dist-name>/json` to get the
  release list. Download and inspect the `pyproject.toml`, `setup.cfg`, or `setup.py` for the
  new version from the sdist tarball link under `releases[<version>]`.
- **GitHub-hosted packages** (`url =` or `git =`): use the GitHub API or `git ls-remote` to
  check for new tags. Inspect the relevant build config files at the tagged commit.
- **Autotools/CMake packages**: inspect `configure.ac`, `CMakeLists.txt`, and any
  `*Config.cmake.in` or `*-config.cmake.in` files for `find_package`, `pkg_check_modules`, and
  minimum version requirements.

Use parallel sub-agents (one per ecosystem or logical group) to speed up the analysis phase.

#### 2b. Inspect the upstream build config at the new version

| Build system | Files to inspect | What to look for |
|---|---|---|
| Python/PyPI | `pyproject.toml`, `setup.cfg`, `setup.py` | `requires-python`, `dependencies`, `[build-system].requires` |
| CMake | `CMakeLists.txt`, `cmake/Find*.cmake` | `find_package(Foo VERSION X.Y REQUIRED)` |
| Autotools | `configure.ac`, `Makefile.am` | `AC_CHECK_LIB`, `PKG_CHECK_MODULES`, version constraints |
| Meson | `meson.build` | `dependency(...)` calls with version constraints |

#### 2c. Classify each detected change

For every upstream change found:

| Upstream change | Action in `package.py` |
|---|---|
| New runtime dependency added | Add `depends_on("pkg", type=("build","run"), when="@<new_version>:")` |
| New build-only dependency added | Add `depends_on("pkg", type="build", when="@<new_version>:")` |
| Dependency removed | Restrict existing `depends_on` with `when="@:<previous_version>"` |
| Minimum version constraint tightened | Add a new `depends_on` with the tighter constraint gated with `when="@<new_version>:"` |
| Python/language minimum version raised | Add `depends_on("python@X.Y:", ..., when="@<new_version>:")` |
| Build system changed (e.g., autotools → CMake) | Change base class or add conditional `build_system()` |

#### 2d. Version range notation

Spack version ranges are **upper-limit-inclusive**: `@3.8:3.10` includes `3.10` itself.

- Upstream `>=3.8` → `@3.8:`
- Upstream `>=3.8,<3.11` → `@3.8:3.10` (3.10 is the last included version)
- Upstream `>=1.20,<2` → `@1.20:1`
- An exact half-open upper bound `<2` → `:1`

Never write `:3.10.99` or `:1.99` — use the last actual release of the series.

#### 2e. Python package name mapping

Use the `py-` prefix for Python packages (e.g., `numpy` → `py-numpy`, `scipy` → `py-scipy`).
Non-Python dependency names follow standard Spack naming (e.g., `libfoo`, `boost`).

---

### Phase 3 — Apply the changes

Make all edits directly in the local `package.py` files (and add any patch files).

#### 3a. Adding new versions

**Add only the latest upstream release** — do not add every intermediate patch release.
For example, if the current highest version in `package.py` is `1.2.3` and upstream has released
`1.2.4`, `1.2.5`, and `1.3.0`, add only `1.3.0`. Keeping a long list of patch versions adds
maintenance burden and slows resolution without benefiting users, who can always use the latest.

**Do not remove existing versions.** Removing versions breaks users who have pinned an older
release in their `spack.yaml`. Only add the new entry.

Add the `version(...)` line **above** the currently highest version, maintaining newest-first order.
Obtain SHA256 checksums using `spack checksum`:

```sh
spack checksum <package-name> <new-version>
```

Do not manually compute checksums. Do not modify `url`, `homepage`, `pypi`, `git`, `maintainers`,
or the copyright header unless the upstream release requires it.

#### 3b. Structural changes

When a new version requires a build-system change (e.g., a package switching from Autotools to
CMake at version 2.0):

```python
class Foo(AutotoolsPackage, CMakePackage):
    build_system("autotools", default="autotools", when="@:1")
    build_system("cmake", default="cmake", when="@2:")
```

Keep both base classes active so existing older versions continue to build.

#### 3c. New packages

If a new upstream dependency does not yet exist in the repository, create its `package.py` before
adding the `depends_on(...)` reference. Follow the [`py-package-update`](py-package-update.md)
conventions for Python packages.

---

### Phase 4 — Group changes into coherent PRs

Avoid "kitchen-sink" PRs. Instead, group changes so that each PR is independently reviewable and
mergeable.

#### 4a. Grouping principles

- **Dependency relationships**: if package A depends on package B and both are being updated,
  include them in the same PR. Reviewers can then verify the full dependency chain at once.
- **Ecosystem coherence**: packages that are always released together (e.g., `boto3` + `botocore`
  + `s3transfer`) belong in the same PR.
- **Technology area**: group by general purpose (e.g., X11 display libraries, HEP generators,
  Python packaging infra) to reduce context-switching for reviewers.
- **Size**: aim for 5–25 packages per PR. Fewer is better when the changes are structural or
  involve new build-system classes.

#### 4b. Branch naming

```
pr<NN>-<short-descriptor>
```

Examples: `pr01-xorg-x11-libs`, `pr12-python-packaging-infra`, `pr07-hep-generators`.

Use zero-padded two-digit PR numbers for lexicographic ordering.

#### 4c. Staging branch

Create a single `staging-all-changes` branch that commits **all** modified files in one go.
Then create each per-PR branch from `develop` and selectively cherry-pick files from staging:

```sh
git checkout develop
git checkout -b pr<NN>-<descriptor>
git checkout staging-all-changes -- repos/spack_repo/builtin/packages/<pkg1>/
git checkout staging-all-changes -- repos/spack_repo/builtin/packages/<pkg2>/
# ... repeat for each package in this PR group
git commit -m "<title>

<summary of changes>"
```

This approach keeps each branch independent and rebasing is trivial.

---

### Phase 5 — Check CI / cache status

Before writing PR descriptions, determine which new versions are already in the binary cache
(`cache.spack.io`) and which will need new CI builds. This helps reviewers set expectations.

For each new version of a package, check:

```sh
curl -s "https://cache.spack.io/package/develop/<spack-pkg-name>/specs/" | \
  python3 -c "import sys,re; data=sys.stdin.read(); vers=re.findall(r'\"versions\":\[\"([^\"]+)\"', data); [print(v) for v in sorted(set(vers))]"
```

Packages not appearing in any CI stack output should be noted in the PR description so reviewers
know there is no automated build verification available for them.

---

### Phase 6 — Search for existing PRs

Before opening new PRs, search for open or recently closed PRs that overlap with your changes:

```sh
gh pr list --repo spack/spack-packages --state open --search "<package-name>" --limit 20
```

For each overlapping PR found:

- **Our PR is a strict superset of theirs**: note it in your PR description ("Supersedes #NNNN").
  **Do not close the existing PR yourself.** Post a comment in the existing PR pointing to the
  new PR number:
  ```
  This work has been superseded by #<new-PR>. Please see that PR for the same and additional changes.
  ```
  Let the maintainers or the existing PR author decide whether to close it.
- **Our PR has partial overlap**: note it as a related PR ("Coordinates with #NNNN") and describe
  which packages overlap, so maintainers can sequence the merges.
- **Their PR introduces new packages or constraints we depend on**: mark it as a prerequisite
  ("Requires #NNNN to be merged first") and coordinate with the author.

> **Do not close other authors' PRs.** Even for your own previous PRs, prefer posting a comment
> rather than closing them, unless you are certain the newer PR is a complete and correct
> replacement. Human reviewers make the final call.

---

### Phase 7 — Open draft PRs

#### 7a. PR description template

Every PR must use the following template. Replace `<...>` placeholders throughout:

```markdown
## Summary

Updated the following packages to their latest upstream releases:

| Package | Old version | New version |
|---------|-------------|-------------|
| `<name>` | `<old>` | `<new>` |

## Dependency changes

<List each change: package, what changed, which version introduced the change.
If none, write "No dependency changes.">

## CI build status

**In CI stacks (binary cache available):** <list>
**Not in any CI stack (will trigger new builds):** <list, or "N/A">

## Related PRs

<List any superseded, coordinating, or prerequisite PRs. If none, write "None.">

---
> ⚠️ This PR was prepared with AI assistance from GitHub Copilot.
> It will only be marked ready for review after human review of all changes.
```

#### 7b. Open as draft

Always open PRs in **draft** mode:

```sh
gh pr create \
  --draft \
  --base develop \
  --head <fork-owner>:<branch> \
  --title "<title>" \
  --body-file <body-file> \
  --repo spack/spack-packages
```

Writing the body to a temporary file avoids shell quoting issues with multi-line descriptions.

#### 7c. Post follow-up comments on related existing PRs

After creating your PRs, post a comment on each existing PR that is superseded or coordinated
with yours. Include the new PR number(s) so that maintainers can easily cross-reference:

```sh
gh pr comment <existing-PR-number> \
  --repo spack/spack-packages \
  --body "This work has been superseded by #<new-PR>, which includes the same changes as a subset of a broader update. Please see #<new-PR> for context."
```

---

### Phase 8 — Validate before marking ready

Before removing the draft status from any PR, verify:

1. All `version(...)` lines were generated by `spack checksum` (correct SHA256).
2. All new `depends_on` entries use the correct Spack name (with `py-` prefix for Python).
3. All `depends_on` calls have a `type=` argument.
4. All upper-bound version constraints are written in inclusive form.
5. No pre-existing unrelated code was modified.
6. If a new package was added, it has a proper `homepage`, `url`/`pypi`/`git`, `license`, and
   at least one `version(...)` with a correct checksum.
7. CI or the binary cache provides coverage for at least the most commonly used versions.

---

## Conventions Reference

| Convention | Rule |
|---|---|
| Directory names | Use underscores: `py_numpy`, `libfoo_bar` |
| Spack package names | Use hyphens: `py-numpy`, `libfoo-bar` |
| Python deps | Always use `py-` prefix in `depends_on()` |
| `type=` on all deps | Required; never omit |
| Version ordering | Newest first |
| New versions to add | Latest release only — do not add every intermediate patch |
| Old versions | Never remove existing versions |
| Version upper bounds | Inclusive form: `:3.10`, `:1`, never `:3.10.99` |
| PR state | Always open as draft; human removes draft status |
| Closing PRs | Never close another author's PR; post a comment instead |
| Copyright header | Do not modify |
| License identifier | All packages: `Apache-2.0 OR MIT` |
| AI attribution | Required in every PR description (see template above) |

## Common Pitfalls

- **Do not add every patch version** — add only the latest upstream release. If upstream has
  released `1.2.4`, `1.2.5`, and `1.3.0` and the repo has `1.2.3`, add only `1.3.0`. Users
  who need a specific patch can pin it themselves; listing every patch clutters the file.
- **Do not remove old versions** — removing a version breaks users who have pinned it. Only
  add; never subtract.
- **Do not compute SHA256 manually** — always use `spack checksum`. Manual checksums are
  error-prone.
- **Do not add an upper bound speculatively** — e.g., do not write `@1.5:2` just because version
  3 of a dep hasn't been tested. Only add upper bounds when the upstream package declares a
  strict incompatibility.
- **Dual build-system packages** — when a new major version switches build systems, keep both
  base classes and use `build_system()` with `when=` guards, so older versions still build.
- **Naming collision** — confirm the new package name doesn't already exist under a different
  name before creating a new package.
- **New package as a dep** — if you add `depends_on("py-foo")` but `py-foo` doesn't exist yet
  in the repo, create it in the same PR or a prerequisite PR. A dangling dependency reference
  will fail CI.
- **`py-sspilib` / Windows-only packages** — some packages only install on specific platforms.
  Use `sys_type()` or `when="platform=windows"` guards as appropriate.
