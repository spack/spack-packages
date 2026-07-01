# Skill: Python Package Update

Update one or more `py-*` packages in this Spack repository to their latest upstream release.
This skill is a Python-focused specialization of [`package-update`](package-update.md), which
covers the full bulk-update workflow including staging branches, CI cache checks, and PR grouping
strategy. Read that skill first for conventions and phases that apply equally here.

This skill handles targeted updates of one or a small group of related Python packages: fetching
the new version metadata, updating `package.py` with the new version and SHA256 checksum,
reconciling dependency changes from the upstream build spec, and opening a draft PR.

## Usage

Invoke this skill by providing one or more package names (using either the Spack name with
hyphens or the directory name with underscores):

```
Update py-dask
Update py-dask, py-dask-expr, py-dask-awkward
```

To update all packages in an ecosystem, name the root package:

```
Update py-scipy ecosystem
```

## Step-by-Step Instructions

### Step 1 — Identify the target packages

- Resolve each provided name to a directory under
  `repos/spack_repo/builtin/packages/` (replace hyphens with underscores).
- For an ecosystem update, also identify packages that `depends_on` the named root package
  and that are likely to release in lockstep (e.g., `py-dask-expr` when updating `py-dask`).
- List all packages you will update before proceeding.

### Step 2 — Determine the latest upstream version

For each package:

#### 2a. Check PyPI

Fetch `https://pypi.org/pypi/<pypi-name>/json` where `<pypi-name>` is derived from the `pypi =`
field in `package.py` (the first path component). Parse `info.version` for the latest stable
release and `releases` for all available versions. Skip pre-releases (versions containing `a`,
`b`, `rc`, or `.dev`) unless the existing `package.py` already tracks pre-releases.

#### 2b. Check the upstream git history (when a `git` attribute is present)

If `package.py` has a `git =` attribute, fetch the repository's tags or releases. Also look at
the commit messages and any included `pyproject.toml` / `setup.cfg` / `CMakeLists.txt` diffs
to understand what changed between the current packaged version and the new version.

#### 2c. Decide whether an update is needed

If the latest stable release on PyPI (or git) matches the highest version already listed in
`package.py`, log "already up to date" and skip that package. Do not open a PR for it.

Follow the version-selection rules from [`package-update`](package-update.md) Phase 3a: add the
latest patch release for each supported minor series, not every intermediate patch. For example,
if `package.py` currently has `1.2.3` and upstream has released `1.2.4`, `1.2.5`, and `1.3.0`,
add `1.2.5` and `1.3.0`; you do not need to add `1.2.4`.

### Step 3 — Fetch the new release artifact and compute SHA256

Use the `spack checksum` command to download the release artifact and emit a correctly formatted
`version(...)` line with the SHA256 checksum already filled in:

```sh
spack checksum <package-name> <new-version>
```

For example:
```sh
spack checksum py-dask 2025.7.0
```

This will output a line such as:
```python
version("2025.7.0", sha256="c3a0d4e78882e85ea81dbc71e6459713e45676e2d17e776c2f3f19848039e4cf")
```

**Remove any trailing `# FIXME` comment** before committing — `spack checksum` appends `# FIXME`
to lines whose checksums it cannot immediately verify inline. These must be stripped; they clutter
the diff and the style checker will flag them:

```sh
sed -i 's/  # FIXME$//' repos/spack_repo/builtin/packages/<pkg>/package.py
```

Do not manually construct download URLs or compute SHA256 values — always use `spack checksum`.

### Step 4 — Reconcile dependency changes from upstream

Compare the build spec of the **new** version against the **currently packaged** version to
identify dependency changes:

| File to inspect | Relevant sections |
|---|---|
| `pyproject.toml` | `[project].dependencies`, `[project.optional-dependencies]`, `[build-system].requires`, `[project].requires-python` |
| `setup.cfg` | `install_requires`, `extras_require`, `setup_requires`, `python_requires` |
| `setup.py` | `install_requires`, `setup_requires`, `python_requires` in `setup()` |
| `CMakeLists.txt` | `find_package(Python ...)`, `find_package(...)` |
| `requirements*.txt` | All entries |

For each change detected:

- **New dependency added upstream** → add a `depends_on("py-<name>", type=(...))` entry in
  `package.py`, gated with `when="@<new_version>:"` if older versions remain in the file.
- **Dependency removed upstream** → restrict the existing `depends_on` with
  `when="@:<previous_version>"`.
- **Version constraint tightened upstream** (e.g., `>=1.20` → `>=1.24`) → add a new `depends_on`
  with the tighter constraint gated with `when="@<new_version>:"`.
- **Python version requirement changed** → update the `depends_on("python@X.Y:", ...)` entry
  accordingly, scoped to the new version range.

#### Version range notation

Spack version ranges are **upper-limit-inclusive**: `@3.8:3.10` includes `3.10` itself.

- Upstream `>=3.8` → `@3.8:`
- Upstream `>=3.8,<3.11` → `@3.8:3.10` (3.10 is the last included version)
- Upstream `>=1.20,<2` → `@1.20:1`
- A half-open upper bound `<2` → `:1`

Never write `:3.10.99` or `:1.99` — use the last actual release of the series.

**Do not add upper bounds speculatively.** Only add an upper bound when the upstream package
explicitly declares a strict incompatibility with a newer version. Do not write `@1.5:2` merely
because version 3 of a dependency hasn't been tested.

#### Python package name mapping

Use the `py-` prefix for all Python packages (e.g., `numpy` → `py-numpy`, `scipy` → `py-scipy`).
If a mapping is uncertain, note it as a TODO comment in the PR description.

#### New packages as dependencies

If a required upstream dependency does not yet exist in the repository, create its `package.py`
in the same PR or a prerequisite PR before adding the `depends_on(...)` reference. A dangling
dependency reference will fail CI.

### Step 5 — Edit `package.py`

Make the following changes to each package file:

1. **Add a new `version(...)` entry** immediately above the existing most-recent version line.
   Follow the existing ordering (newest first). Use the output of `spack checksum` and strip
   any `# FIXME` comment.

2. **Update or add `depends_on(...)` entries** as determined in Step 4. Preserve the existing
   grouping style (build deps first, then runtime deps; grouped by dependency package).

3. **Do not remove old versions.** Removing a version breaks users who have pinned an older
   release in their `spack.yaml`. Only add; never subtract.

4. **Do not modify** the copyright header, SPDX identifier, imports, docstring, `homepage`,
   `pypi`, `url`, `git`, `maintainers`, or `license` lines unless a change is specifically
   required by the upstream release.

### Step 6 — Validate the changes

- Confirm the new `version(...)` line is syntactically valid Python and has no `# FIXME` suffix.
- Confirm all new `depends_on` entries use the `py-` prefix and have a `type=` argument.
- Confirm any version range upper bounds are written in inclusive form (e.g., `:3.10`, not
  `:3.10.99`).
- Run the style checker and package audit before pushing (see
  [`package-update`](package-update.md) Phase 8 for the full commands):

  ```sh
  .ci/style_check.sh develop          # shows what would be fixed
  .ci/style_check.sh --fix develop    # auto-fixes formatting
  . spack-core/share/spack/setup-env.sh && spack audit packages
  ```

### Step 7 — Search for existing PRs

Before opening a new PR, search for open PRs that may overlap:

```sh
gh pr list --repo spack/spack-packages --state open --search "<package-name>" --limit 20
```

**Existing PRs that already include any of the same version upgrades take priority.** Remove
those packages from your PR and list the existing PR as a `Needs:` dependency (see Step 8d).
Follow the full coordination rules in [`package-update`](package-update.md) Phase 6.
Do not close another author's PR — post a comment instead.

### Step 8 — Group packages and open a draft PR

Group related packages (same ecosystem, or packages that release in lockstep) into a single PR.
Aim for 1–10 packages per PR for Python ecosystem updates.

#### 8a. Branch naming

```
update/<ecosystem-or-package>-<new_version>
```

Examples: `update/dask-2025.7.0`, `update/scipy-1.15.0`.

#### 8b. Commit message

Write one commit per logical group of related packages:

```
<pkg1>, <pkg2>: add v<version>

Updated packages: <list with old → new version for each>
```

#### 8c. PR title

```
<pkgname>: add v<version>
```

For multiple packages in the same ecosystem, name after the root package:

```
<root-pkg>: add v<version>
<root-pkg>, <pkg2>, <pkg3>: add v<version>
```

Examples: `py-dask: add v2025.7.0`, `py-boto3, py-botocore, py-s3transfer: add v1.42.x`

#### 8d. PR description

Use the following template:

```markdown
## Summary

Updated the following Python packages to their latest upstream release:

| Package | Old version | New version |
|---------|-------------|-------------|
| `py-<name>` | `<old>` | `<new>` |

## Dependency changes

<List any dependency additions, removals, or constraint updates. If none, write "No dependency changes.">

## Upstream changes

<Brief summary of what changed upstream — link to the changelog, release notes, or relevant
commits. If the upstream changelog was consulted, quote the most relevant line(s).>

## CI build status

**In CI stacks (binary cache available):** <list, or check cache.spack.io>
**Not in any CI stack (will trigger new builds):** <list, or "N/A">

## Needs

<List prerequisite PRs that must be merged before this one. If none, omit this section.>
- [ ] #<PR-number>

## Related PRs

<List any coordinating PRs with partial overlap. If none, write "None.">

---
> ⚠️ This PR was prepared with AI assistance from GitHub Copilot.
> It will only be marked ready for review after human review of all changes.
```

#### 8e. Open as draft

Always open the PR in **draft** mode:

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

#### 8f. Link to issues

If a GitHub issue exists that requested this update (search open issues for the package name),
add `Closes #<issue>` to the PR description.

## Conventions Reference

- Package directory names use underscores: `py_numpy` (not `py-numpy`).
- Spack package names use hyphens: `py-numpy`.
- Python package dependencies always use the `py-` prefix: `depends_on("py-numpy", ...)`.
- All `depends_on` calls must include a `type=` argument.
- Versions are listed newest-first in `package.py`.
- Add only the latest upstream release; do not list every intermediate patch version.
- Never remove existing versions.
- Never add speculative upper-bound constraints.
- All packages are licensed under `Apache-2.0 OR MIT`; do not change the header.
- The `pypi =` field value is `<dist-name>/<filename>` matching the PyPI sdist filename.
- Always open PRs as draft; human reviewers mark them ready.

## Example

Given `py-dask` currently at `2024.12.1` and PyPI showing `2025.7.0` as latest:

```sh
spack checksum py-dask 2025.7.0
# → version("2025.7.0", sha256="c3a0d4e78...")  # FIXME
# Strip the # FIXME before committing.
```

```python
# Before
version("2024.12.1", sha256="bac809af21c2dd7eb06827bccbfc612504f3ee6435580e548af912828f823195")

# After (new entry added above, no # FIXME)
version("2025.7.0", sha256="c3a0d4e78882e85ea81dbc71e6459713e45676e2d17e776c2f3f19848039e4cf")
version("2024.12.1", sha256="bac809af21c2dd7eb06827bccbfc612504f3ee6435580e548af912828f823195")
```

If `pyproject.toml` for `2025.7.0` tightens `py-packaging` from `>=20` to `>=21`:

```python
depends_on("py-packaging@20:", type="build", when="@2022.10.2:2024.12.1")
depends_on("py-packaging@21:", type="build", when="@2025.7.0:")
```
