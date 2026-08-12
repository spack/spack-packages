# Self Compiler Migration Log

Date: 2026-08-07
Workspace: `/usr/WS1/taller1/ALE3D/SPACK_SELFCOMPILER/spack-packages`

## Original Prompt (Verbatim)

```text
Can you get rid of uses of self.compiler in all the project files in repos/spack_repo/builtin/packages/ ? For example, replace self.compiler.cc with self["c"].cc, self.compiler.cxx with self["cxx"].cxx, self.compiler.fc with self["fortran"].fortran, self.compiler.cc_pic_flag with self["c"].pic_flag, self.compiler.cxx_pic_flag with self["cxx"].pic_flag . If this appears in a format string, make sure the quotes are correct (for example, if outer quotes are " ", you may need to use self['cxx'] instead of self["cxx"])
```

## Why These Changes Were Made

- The requested goal was to remove `self.compiler` usage from `repos/spack_repo/builtin/packages`.
- The replacement API is language-specific, so compiler executables and flags were moved to the matching compiler package:
  - C: `self["c"]`
  - C++: `self["cxx"]`
  - Fortran: `self["fortran"]`
- Mixed-language packages could not be converted with a single blind substitution. OpenMP flags, PIC flags, and compiler executable references were chosen based on the actual compile or link language in each site.
- Some format strings and f-strings needed quote changes so the rewritten Python remained valid.
- A few comments and non-API package-local names were updated so they would no longer look like real `self.compiler` API usage.

## What Was Changed

- All `self.compiler` references under `repos/spack_repo/builtin/packages` were removed.
- Direct attribute rewrites included patterns such as:
  - `self.compiler.cc` -> `self["c"].cc`
  - `self.compiler.cxx` -> `self["cxx"].cxx`
  - `self.compiler.fc` / `self.compiler.f77` -> `self["fortran"].fortran`
  - `self.compiler.cc_pic_flag` -> `self["c"].pic_flag`
  - `self.compiler.cxx_pic_flag` -> `self["cxx"].pic_flag`
  - `self.compiler.name` -> `self.spec.compiler.name`
  - `self.compiler.version` -> `self.spec.compiler.version`
- Dynamic standard-flag lookups were rewritten to `standard_flag(...)` where needed.
- OpenMP flags were rewritten by language context instead of globally:
  - C compile/link contexts use `self["c"].openmp_flag`
  - C++ compile/link contexts use `self["cxx"].openmp_flag`
  - Fortran compile/link contexts use `self["fortran"].openmp_flag`

## Mixed-Language Files That Needed Manual Decisions

- `repos/spack_repo/builtin/packages/openmx/package.py`
- `repos/spack_repo/builtin/packages/mumps/package.py`
- `repos/spack_repo/builtin/packages/superlu_mt/package.py`
- `repos/spack_repo/builtin/packages/mpas_model/package.py`
- `repos/spack_repo/builtin/packages/erf/package.py`
- `repos/spack_repo/builtin/packages/sw4lite/package.py`
- `repos/spack_repo/builtin/packages/npb/package.py`
- `repos/spack_repo/builtin/packages/ncl/package.py`
- `repos/spack_repo/builtin/packages/onednn/package.py`
- `repos/spack_repo/builtin/packages/srilm/package.py`
- `repos/spack_repo/builtin/packages/stream/package.py`
- `repos/spack_repo/builtin/packages/xabclib/package.py`
- `repos/spack_repo/builtin/packages/planck_likelihood/package.py`

## Notable Special Cases

- `repos/spack_repo/builtin/packages/openfoam/package.py` keeps `self.compiler_name`. That is intentional package state, not the removed Spack compiler API.
- Comment-only references that still mentioned `self.compiler` were updated to match the new implementation.

## Current Status

- Scope completed: `repos/spack_repo/builtin/packages`
- Remaining `self.compiler` references in that tree: none
- Files changed in that tree: 325

## Verification Performed

- Scan for remaining references:

```bash
rg -n "self\\.compiler\\b" repos/spack_repo/builtin/packages
```

Result: no matches.

- Python syntax check for changed package files:

```bash
python3 -m py_compile $(git diff --name-only -- repos/spack_repo/builtin/packages)
```

Result: success.

- Whitespace / patch-format check:

```bash
git diff --check -- repos/spack_repo/builtin/packages
```

Result: clean.

## If You Continue Later

- Start with:

```bash
rg -n "self\\.compiler\\b" repos/spack_repo/builtin/packages
```

- If new package files were added after this session, apply the same language-based rule instead of a blind substitution.
- For future mixed-language edits, choose the compiler package based on the language actually driving the compile or link step.
