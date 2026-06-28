# Skill: PR Review

Review a pull request in this Spack package repository for correctness, completeness, and
justification. CI already handles automated checks (style, license headers, SHA256 checksums,
`spack audit`), so this review focuses on what automation cannot verify.

## Usage

Invoke this skill by providing a PR number:

```
Review PR #<number>
```

## Review Checklist

Work through the following in order. For each item, clearly state your finding and whether it
passes, has a concern, or is a blocking issue.

### 1. Fetch the PR

- Retrieve the PR metadata (title, description, author, labels) and the full diff.
- Identify which packages are being modified. List them upfront so the rest of the review is
  scoped.

### 2. PR Description Quality

Check that the PR description adequately justifies the changes:

- Does it explain **why** this update is being made (e.g., new upstream release, bug fix,
  security patch, new feature needed by a dependent package)?
- If it references an issue or upstream release, are those links present?
- For version bumps, does it mention what changed upstream (e.g., changelog highlights)?
- Flag vague descriptions like "update to latest version" with no further explanation as a
  concern, not a blocker.

### 3. Version Currency

For every package version being added or updated:

- If the package uses a non-PyPI source (e.g., a GitHub `url` or `git` attribute), check the upstream repository's tags or releases page to verify the submitted version is the latest.
- Query PyPI (`https://pypi.org/pypi/<package-name>/json`) to retrieve the current latest stable release. Compare it to the version being added. If the PR adds version X but PyPI already shows a newer stable release Y, flag this.
- Do **not** flag pre-releases (alpha, beta, rc) as missing unless the PR explicitly targets
  pre-releases.

### 4. Dependency Completeness

For each changed package, examine the upstream build configuration to verify that all dependency
changes are reflected in `package.py`. Use links to the commit that introduced the dependency change to allow reviewers to validate the changes, or justify by quoting the release notes if the package has no git attribute.

#### 4a. Locate the upstream build spec

Identify the upstream source from the `pypi`, `url`, or `git` field in the package. Then look at
the build configuration file relevant to the version being added:

| Upstream file | What to look for |
|---|---|
| `pyproject.toml` | `[project].dependencies`, `[project.optional-dependencies]`, `[build-system].requires` |
| `setup.cfg` | `install_requires`, `extras_require`, `setup_requires` |
| `setup.py` | `install_requires`, `setup_requires` in `setup()` call |
| `CMakeLists.txt` | `find_package(Python ...)`, `find_package(...)` calls |
| `requirements*.txt` | All listed packages |

#### 4b. Compare against `package.py`

For each dependency in the upstream build spec:

- Is there a corresponding `depends_on(...)` in `package.py`? If a runtime dep is missing, that
  is a **blocking issue**.
- Are version constraints in `depends_on(...)` consistent with the constraints declared upstream?
  A looser constraint is acceptable; a stricter constraint without justification is a concern.
- Are build-only deps (e.g., listed only in `[build-system].requires` or `setup_requires`) marked
  `type="build"` rather than `type=("build", "run")`?
- Have any deps that were removed upstream (compared to the previous version's spec) been removed
  from `package.py` as well? Missing removals are a concern.
- Are newly required deps for the new version gated with a `when="@<new_version>:"` constraint
  when older versions remain present?

#### 4c. Ecosystem consistency

If the PR touches multiple related packages (e.g., `py-dask` and `py-dask-expr`), verify that
inter-package version constraints are mutually consistent.

### 5. Spack Conventions

Spot-check that the changes follow Spack package conventions. CI catches most of these, but flag
obvious issues:

- Package class name follows `PyPackageName` CamelCase derived from the PyPI name.
- `pypi =` field (if present) uses the canonical PyPI distribution name and filename.
- New `depends_on` entries use the `py-` prefix for Python packages.
- `type=` annotation is present on all `depends_on` calls (no bare `depends_on` without type).

## Output Format

Structure your review as follows:

```
## PR Review: #<number> — <title>

**Packages reviewed:** <list>

### PR Description
<PASS|CONCERN|BLOCKING> — <finding>

### Version Currency
<one entry per package>
<PASS|CONCERN|BLOCKING> — <finding>

### Dependency Completeness
<one entry per package, with sub-bullets for individual deps if needed>
<PASS|CONCERN|BLOCKING> — <finding>

### Spack Conventions
<PASS|CONCERN|BLOCKING> — <finding, or "No issues found.">

---
**Summary:** <Overall verdict: ready to merge / needs minor changes / needs major changes>
<Optional: list the most important action items for the PR author>
```

Use **BLOCKING** for issues that must be resolved before merging, **CONCERN** for items worth
discussing but not necessarily blockers, and **PASS** when a section looks correct.
