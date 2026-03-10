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

**Add only the latest patch release per minor series** — do not add every intermediate patch
release. For each `major.minor` series, add only the highest patch version. For example, if
`package.py` currently has `1.2.3` and upstream has released `1.2.4`, `1.2.5`, and `1.3.0`,
add `1.2.5` (latest of the 1.2.x series, if you need the 1.2.x entry at all) and `1.3.0`
(latest of the new 1.3.x series). In most cases you only need the single latest release.
Keeping a long list of patch versions adds maintenance burden and slows resolution without
benefiting users, who can always use the latest.

**Do not remove existing versions.** Removing versions breaks users who have pinned an older
release in their `spack.yaml`. Only add new entries.

Add the `version(...)` line **above** the currently highest version, maintaining newest-first order.
Obtain SHA256 checksums using `spack checksum`:

```sh
spack checksum <package-name> <new-version>
```

> **Remove `# FIXME` comments from version lines.** `spack checksum` appends `# FIXME` to
> `version(...)` lines when it cannot immediately verify the checksum against an existing entry.
> These comments must be removed before committing — they are not informative once checksums are
> confirmed and will be flagged as noise in review. After running `spack checksum`, strip any
> trailing `# FIXME` from every version line you add:
>
> ```python
> # Wrong — do not commit this:
> version("1.3.0", sha256="abc123...")  # FIXME
>
> # Correct:
> version("1.3.0", sha256="abc123...")
> ```
>
> A quick way to remove all such comments in bulk before committing:
> ```sh
> sed -i 's/  # FIXME$//' repos/spack_repo/builtin/packages/<pkg>/package.py
> ```

Do not manually compute checksums. Do not modify `url`, `homepage`, `pypi`, `git`, `maintainers`, `license`
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

If an upstream dependency does not yet exist in the repository, create the package before adding the `depends_on(...)` reference.
The `spack create` command will generate a recipe scaffold.

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

#### 4b. Branch naming and PR title

**Branch name:**
```
pr<NN>-<short-descriptor>
```

Examples: `pr01-xorg-x11-libs`, `pr12-python-packaging-infra`, `pr07-hep-generators`.

Use zero-padded two-digit PR numbers for lexicographic ordering.

**PR title** — prefer the canonical form:

```
<pkgname>: add v<version>
```

For a single package: `py-dask: add v2025.7.0`

When multiple packages in the same ecosystem are updated together, name the PR after the
root/primary package:

```
<root-pkg>: add v<version>
<root-pkg>, <pkg2>, <pkg3>: add v<version>
<root-pkg> and related packages: add v<version>
```

Examples:
- `py-awkward: add v2.9.0` (even though awkward-cpp is also bumped)
- `py-boto3, py-botocore, py-s3transfer: add v1.42.x`
- `boost: add v1.90.0`
- `harfbuzz, cairo, pango: add v<version>` (rendering stack, listed dependency-first)

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

Before opening new PRs, search for open PRs that overlap with your changes:

```sh
gh pr list --repo spack/spack-packages --state open --search "<package-name>" --limit 20
```

**Existing PRs that include any of the same version upgrades take priority.** For each
overlapping PR found, apply the following rules:

- **An existing PR already upgrades some of the same packages**: those packages belong to that
  PR. **Remove them from your PR** and instead list the existing PR as a dependency using the
  `Needs:` block in your PR description (see template in Phase 7). Your PR must not be merged
  before the dependency PR is merged.

  Example `Needs:` block:
  ```markdown
  ## Needs
  - [ ] #1234
  ```

  Post a comment in the existing PR to signal awareness:
  ```
  This PR (#<new-PR>) depends on your work here. I've removed the overlapping packages
  from my PR and listed this one as a prerequisite.
  ```

- **An existing PR introduces new packages or constraints our new `depends_on` entries
  reference**: mark it as a prerequisite with the same `Needs:` block and coordinate with the
  author so both PRs can be merged in the correct order.

- **The overlap is only incidental** (same package, different version ranges that do not
  conflict): note it as a related PR in the "Related PRs" section and describe the relationship
  so maintainers can sequence the merges.

> **Do not close other authors' PRs.** Even for your own previous PRs, prefer posting a comment
> rather than closing them. Human reviewers make the final call on which PR to merge.

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

<List and justify each change: package, what changed, which version introduced the change. Always include links to the commit that introduced the dependency change to allow reviewers to validate, or justify by quoting the release notes if the package has no git attribute.
If none, write "No dependency changes.">

## Version diff links

For packages whose source is hosted on GitHub or GitLab, include a comparison link
from the previous Spack version to the newly added version. This greatly aids reviewers
in assessing the scope of changes without leaving the PR:

- [pkg-name: old → new](https://github.com/org/repo/compare/old-tag...new-tag)

To generate these links automatically, inspect the `git =` and `url =` attributes in
`package.py` to determine:
1. The hosting service (GitHub → `/compare/`, GitLab → `/-/compare/`)
2. The tag format (inferred from the `url` pattern: `v{ver}`, `{ver}`, or `prefix-{ver}`)
3. The previous Spack version (highest version in `develop` strictly below the new one)

For packages hosted elsewhere (SourceForge, custom tarballs without a `git =`) omit the link.
If `n_new > 1` (multiple intermediate versions were skipped), add a note like `(+N intermediate)`.

## CI build status

**In CI stacks (binary cache available):** <list>
**Not in any CI stack (will trigger new builds):** <list, or "N/A">

## Needs

<List prerequisite PRs that must be merged before this one, using unchecked task items.
If none, omit this section entirely.>
- [ ] #<PR-number>

## Related PRs

<List any coordinating PRs that partially overlap but are not strict prerequisites. If none, write "None.">

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

#### Run style and audit checks locally before pushing

Run the style checker against the `develop` base to catch formatting issues before CI sees them.
The repository uses `flake8`, `isort`, and `black` via a wrapper script:

```sh
# Check only (shows what would be fixed):
.ci/style_check.sh develop

# Auto-fix formatting issues:
.ci/style_check.sh --fix develop
```

The script requires a `spack-core` directory (a clone of `spack/spack`) to be present in the
repository root. Create it if absent:

```sh
git clone https://github.com/spack/spack spack-core
```

After fixing, verify the checks pass cleanly:

```sh
.ci/style_check.sh develop   # should print "style checks passed"
```

Run the package audit to catch semantic errors (missing dependencies, invalid version specs, etc.):

```sh
. spack-core/share/spack/setup-env.sh
spack audit packages
spack audit configs
spack audit externals
```

The audit output is per-repository (not per-PR), so filter results to only the packages you
changed. Pre-existing errors in unmodified packages can be ignored.

If style or audit issues are found after a commit has already been pushed, fix them and amend:

```sh
# Fix, then amend the branch's commit:
.ci/style_check.sh --fix develop
git add -u
git commit --amend --no-edit
git push <fork-remote> <branch> --force-with-lease
```

#### CI timing

After a PR is pushed, two rounds of CI feedback are available:

| Stage | When results appear | What is checked |
|---|---|---|
| First-stage checks (GitHub Actions) | ~10 minutes | Style (`flake8`/`isort`/`black` via `.ci/style_check.sh`), audit (`spack audit`), license headers, package naming conventions |
| Full pipeline (GitLab CI at `gitlab.spack.io/spack/spack-packages`) | up to 1 hour | Package builds across all supported compilers and platforms; any build failures are visible here |

Wait for first-stage results before asking a reviewer to look at the PR — style and audit
failures are quick to fix and should be resolved before human review. Wait for (or note the
status of) the full GitLab pipeline before marking the PR ready for review, so that build
failures from the new versions are visible and can be addressed.

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

- **Add only the latest patch per minor series** — for each `major.minor` series, include
  only the highest patch release. If upstream released `1.2.4`, `1.2.5`, `1.3.0`, `1.3.1`,
  and the repo has `1.2.3`, add only `1.2.5` (if a 1.2.x entry is needed) and `1.3.1`. In
  most cases only the single overall latest version is required. If you used `spack checksum`
  and inadvertently generated a long list of patch versions, run the helper script
  `scripts/fix_patch_versions.py` to keep only the highest patch per minor series before
  committing.
- **Do not remove old versions** — removing a version breaks users who have pinned it. Only
  add; never subtract.
- **Do not compute SHA256 manually** — always use `spack checksum`. Manual checksums are
  error-prone.
- **Remove `# FIXME` from version lines** — `spack checksum` appends `# FIXME` to lines whose
  checksums it cannot verify inline. Always strip these before committing. The style checker
  does not catch them, but they clutter the diff and confuse reviewers.
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
