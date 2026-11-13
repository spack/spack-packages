"""Script to check for spec reuse within and between environments

In order to ensure that enviroments are not floating and building unexpected
duplicates of packages this script does a consistentcy check at the end of
each pipeline generation step. The out of this script is a summary report and
all of the spec diffs of the unexpected duplicates. This is then used to help
understand why duplicates are occuring and what needs to be changed to remove
them or if they should be added to the exceptions list.

Run with Spack's own interpreter so ``spack.*`` is importable, e.g.:

    spack python stacks/reuse_score.py stacks/linux/x86

Algorithm
---------
1. Discover environments (directories containing ``spack.yaml``) under the
   given paths, and read each one's ``spack:concretizer:reuse:from`` entries
   of type ``environment`` to build a DAG of "which environment intends to
   reuse specs from which other environment". Any referenced environment
   that lives outside the requested paths is pulled in automatically so it
   can still be used as reuse context.
2. Process environments in topological order (parents/reuse-sources before
   their dependents). For every concrete spec in an environment's lockfile:
     - If its dag hash was already seen in a previously processed
       environment, it was successfully reused -- nothing to report.
     - If the hash is new but another environment already produced a
       *different* hash for the same ``name@version``, that is a
       "duplicate" and gets classified as:
         * intra-environment  -- both builds live in the same environment
         * in-hierarchy-miss  -- the new environment declares (transitively)
           that it reuses from the environment that owns the existing hash,
           but ended up building it again anyway
         * cross-hierarchy    -- the two owning environments have no
           ancestor/descendant relationship at all (siblings or unrelated
           stacks); the recommendation is to migrate the abstract spec up
           to a common stack ancestor of both (or introduce one)
3. Emit a report of all duplicates (with a spec diff explaining what
   differs between the two builds) plus a "reuse score":

       score = (D_total - D_root) / D_total

   where D_total is the total number of duplicate spec instances detected
   and D_root is how many of those duplicate instances were themselves root
   specs (i.e. explicitly requested, not just pulled in transitively).
   Range is [0, 1). Lower is better: it means the bulk of the detected
   duplication is at the root (explicit, likely intentional) rather than
   buried in the dependency DAG (implicit, usually unintentional and the
   more expensive kind of duplication to carry through a pipeline).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Literal, Optional, Set, Tuple

from stack_utils.env_dag import (
    compute_ancestors,
    find_spack_yaml_dirs,
    load_environments,
    topo_sort,
)

try:
    import spack.environment as ev
    import spack.spec
except ImportError:
    sys.exit(
        "error: could not import the 'spack' package.\n"
        "Run this script with Spack's own interpreter, e.g.:\n"
        "    spack python stacks/reuse_score.py <env-dir> [<env-dir> ...]"
    )


# --------------------------------------------------------------------------
# Duplicate detection
# --------------------------------------------------------------------------

Category = Literal["intra-environment",  "in-hierarchy-miss", "cross-hierarchy"]


@dataclass
class Duplicate:
    name: str
    version: str
    new_env: str
    new_hash: str
    new_is_root: bool
    existing_env: str
    existing_hash: str
    existing_is_root: bool
    category: Category
    diff: List[str]
    recommendation: str


def build_reverse_index(env: "ev.Environment") -> Dict[str, Set[str]]:
    """Map dag_hash -> set of names of packages that depend on it directly."""
    parents: Dict[str, Set[str]] = defaultdict(set)
    for root in env.concrete_roots():
        for node in root.traverse():
            for dep in node.dependencies():
                parents[dep.dag_hash()].add(node.name)
    return parents


def diff_specs(a: "spack.spec.Spec", b: "spack.spec.Spec") -> List[str]:
    lines: List[str] = []

    if str(a.version) != str(b.version):
        lines.append(f"version: {a.version} vs {b.version}")

    va = {k: str(v) for k, v in a.variants.items()}
    vb = {k: str(v) for k, v in b.variants.items()}
    for key in sorted(set(va) | set(vb)):
        if va.get(key) != vb.get(key):
            lines.append(f"variant {key}: {va.get(key, '<absent>')} vs {vb.get(key, '<absent>')}")

    da = {dep.name: dep for dep in a.dependencies()}
    db = {dep.name: dep for dep in b.dependencies()}
    for name in sorted(set(da) | set(db)):
        sa, sb = da.get(name), db.get(name)
        if sa is None:
            lines.append(f"dependency {name}: <absent> vs {sb.version} ({sb.dag_hash()[:8]})")
        elif sb is None:
            lines.append(f"dependency {name}: {sa.version} ({sa.dag_hash()[:8]}) vs <absent>")
        elif sa.dag_hash() != sb.dag_hash():
            if str(sa.version) != str(sb.version):
                lines.append(f"dependency {name}: {sa.version} vs {sb.version}")
            else:
                lines.append(
                    f"dependency {name}: same version {sa.version}, "
                    f"different build ({sa.dag_hash()[:8]} vs {sb.dag_hash()[:8]})"
                )

    if not lines:
        lines.append("no variant/immediate-dependency differences - divergence is deeper in the DAG")
    return lines


def find_common_ancestor(nodes: Dict[str, EnvNode], env_a: str, env_b: str) -> Optional[str]:
    """Pick the most specific (deepest) common reuse-ancestor of two envs."""
    common = nodes[env_a].ancestor_names & nodes[env_b].ancestor_names
    if not common:
        return None
    return max(common, key=lambda name: len(nodes[name].ancestor_names))


def classify(
    nodes: Dict[str, EnvNode], new_env: str, existing_env: str
) -> Category:
    if new_env == existing_env:
        return "intra-environment"
    if existing_env in nodes[new_env].ancestor_names:
        return "in-hierarchy-miss"
    if new_env in nodes[existing_env].ancestor_names:
        return "in-hierarchy-miss"
    return "cross-hierarchy"


def recommendation_for(
    nodes: Dict[str, EnvNode], category: Category, name: str, new_env: str, existing_env: str
) -> str:
    if category == "intra-environment":
        return (
            f"'{name}' is built twice inside '{new_env}' itself; check whether both "
            "builds are truly required (e.g. a bootstrap vs. main toolchain) or "
            "whether a `packages:` requirement/preference can unify them."
        )
    if category == "in-hierarchy-miss":
        return (
            f"'{new_env}' declares reuse from '{existing_env}' but rebuilt '{name}' "
            "anyway; compare the diff below to see what constraint diverged "
            "(often a `packages:` require/prefer or unify:when_possible letting "
            "an unrelated root spec pull in a different version)."
        )
    common = find_common_ancestor(nodes, new_env, existing_env)
    if common:
        return (
            f"'{new_env}' and '{existing_env}' do not reuse from each other; migrate "
            f"the abstract spec for '{name}' up into their common ancestor stack "
            f"'{common}' so both environments reuse the same build."
        )
    return (
        f"'{new_env}' and '{existing_env}' do not reuse from each other and share no "
        f"common ancestor stack; consider introducing one (e.g. a shared base) that "
        f"both can declare in `concretizer:reuse:from` and hosting '{name}' there."
    )


def detect_duplicates(
    nodes: Dict[str, EnvNode], order: List[str]
) -> Tuple[List[Duplicate], Dict[str, "spack.spec.Spec"]]:
    global_hash_owner: Dict[str, str] = {}  # dag_hash -> owning env name
    nv_index: Dict[Tuple[str, str], Dict[str, str]] = defaultdict(dict)  # (name, ver) -> {hash: env}
    spec_by_hash: Dict[str, "spack.spec.Spec"] = {}
    root_hash_of: Dict[str, Set[str]] = {}  # env -> set of root hashes
    duplicates: List[Duplicate] = []

    for env_name in order:
        print(env_name)
        node = nodes[env_name]
        if node.env is None:
            continue

        root_hashes = {s.dag_hash() for s in node.env.concrete_roots()}
        root_hash_of[env_name] = root_hashes

        for spec in node.env.all_specs():
            h = spec.dag_hash()
            spec_by_hash.setdefault(h, spec)

            if h in global_hash_owner:
                continue  # exact build reused - nothing to report

            global_hash_owner[h] = env_name
            key = (spec.name, str(spec.version))
            existing_for_key = nv_index[key]

            if existing_for_key:
                new_is_root = h in root_hashes
                for existing_hash, existing_env in existing_for_key.items():
                    existing_is_root = existing_hash in root_hash_of.get(existing_env, set())
                    category = classify(nodes, env_name, existing_env)
                    recommendation = recommendation_for(
                        nodes, category, spec.name, env_name, existing_env
                    )
                    duplicates.append(
                        Duplicate(
                            name=spec.name,
                            version=key[1],
                            new_env=env_name,
                            new_hash=h,
                            new_is_root=new_is_root,
                            existing_env=existing_env,
                            existing_hash=existing_hash,
                            existing_is_root=existing_is_root,
                            category=category,
                            diff=diff_specs(spec_by_hash[existing_hash], spec),
                            recommendation=recommendation,
                        )
                    )

            existing_for_key[h] = env_name

    return duplicates, spec_by_hash


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

CATEGORY_TITLES = {
    "cross-hierarchy": "Non-overlapping hierarchical reuse failures",
    "in-hierarchy-miss": "In-hierarchy reuse misses",
    "intra-environment": "Intra-environment duplicates",
}


def compute_score(duplicates: List[Duplicate]) -> Optional[float]:
    total = len(duplicates)
    if total == 0:
        return None
    root_count = sum(1 for d in duplicates if d.new_is_root)
    return (total - root_count) / total


def render_report(nodes: Dict[str, EnvNode], order: List[str], duplicates: List[Duplicate], show_root: bool) -> str:
    out = []
    out.append("=" * 78)
    out.append("Environments processed (topological order)")
    out.append("=" * 78)
    for name in order:
        node = nodes[name]
        tag = "requested" if node.requested else "reuse-source context"
        lock = "ok" if node.env is not None else "NO LOCKFILE"
        parents = ", ".join(sorted(node.parent_names)) or "(none)"
        out.append(f"- {name} [{tag}, {lock}]")
        out.append(f"    reuses from: {parents}")

    total = len(duplicates)
    root_count = sum(1 for d in duplicates if d.new_is_root)
    score = compute_score(duplicates)

    out.append("")
    out.append("=" * 78)
    out.append("Duplicate report")
    out.append("=" * 78)

    by_category: Dict[str, List[Duplicate]] = defaultdict(list)
    for dup in duplicates:
        by_category[dup.category].append(dup)

    for category in ("cross-hierarchy", "in-hierarchy-miss", "intra-environment"):
        entries = by_category.get(category, [])
        out.append("")
        out.append(f"--- {CATEGORY_TITLES[category]} ({len(entries)}) ---")
        if not entries:
            out.append("(none)")
            continue
        for dup in entries:
            if not show_root and dup.new_is_root:
                continue

            root_marker = " [ROOT]" if dup.new_is_root else ""
            out.append(
                f"\n{dup.name}@{dup.version}{root_marker}\n"
                f"  existing build: {dup.existing_env}  ({dup.existing_hash})\n"
                f"  new build:      {dup.new_env}  ({dup.new_hash})"
            )
            for line in dup.diff:
                out.append(f"    {line}")
            out.append(f"  recommendation: {dup.recommendation}")

    out.append("")
    out.append("=" * 78)
    out.append("Reuse score")
    out.append("=" * 78)
    out.append(f"Total duplicate instances (D_total): {total}")
    out.append(f"Duplicate instances that are root specs (D_root): {root_count}")
    if score is None:
        out.append("Score: N/A (no duplicates detected)")
    else:
        out.append(f"Score: {score:.3f}  (= (D_total - D_root) / D_total; lower is better)")

    out.append("")
    out.append("By environment (duplicates introduced when this env was processed):")
    per_env: Dict[str, int] = defaultdict(int)
    for dup in duplicates:
        per_env[dup.new_env] += 1
    for name in order:
        if per_env.get(name):
            out.append(f"  {name}: {per_env[name]}")

    return "\n".join(out)


def render_json(nodes: Dict[str, EnvNode], order: List[str], duplicates: List[Duplicate]) -> dict:
    score = compute_score(duplicates)
    return {
        "environments": [
            {
                "name": name,
                "requested": nodes[name].requested,
                "has_lock": nodes[name].env is not None,
                "reuses_from": sorted(nodes[name].parent_names),
            }
            for name in order
        ],
        "duplicates": [
            {
                "name": d.name,
                "version": d.version,
                "category": d.category,
                "new_env": d.new_env,
                "new_hash": d.new_hash,
                "new_is_root": d.new_is_root,
                "existing_env": d.existing_env,
                "existing_hash": d.existing_hash,
                "existing_is_root": d.existing_is_root,
                "diff": d.diff,
                "recommendation": d.recommendation,
            }
            for d in duplicates
        ],
        "score": {
            "total_duplicates": len(duplicates),
            "root_duplicates": sum(1 for d in duplicates if d.new_is_root),
            "value": score,
        },
    }


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="+",
        help="Environment directories (containing spack.yaml/spack.lock), or "
        "root directories to search recursively for them.",
    )
    parser.add_argument(
        "--concrete-env-dir",
        default=None,
        help="Value to substitute for ${SPACK_CONCRETE_ENV_DIR} when resolving "
        "'concretizer:reuse:from' paths, and the root used for human-readable "
        "environment labels. Defaults to this script's own directory (stacks/), "
        "matching stacks/concretize_all.sh.",
    )

    # Report Generation Arguments
    parser.add_argument("-o", "--output", default=None, help="Write the text report to this file instead of stdout.")
    parser.add_argument("--json", default=None, help="Also write a structured JSON report to this path.")
    roots_parser = parser.add_mutually_exclusive_group()
    roots_parser.add_argument("--show-roots", action="store_true", dest="show_roots", default=False, help="Show duplicated roots.")
    roots_parser.add_argument("--no-show-roots", action="store_false", dest="show_roots", help="Don't show duplicated roots.")
    return parser.parse_args(argv)


def main(argv: List[str]) -> int:
    args = parse_args(argv)

    concrete_env_dir = (
        Path(args.concrete_env_dir).resolve()
        if args.concrete_env_dir
        else Path(__file__).resolve().parent
    )

    seed_dirs = find_spack_yaml_dirs(Path(p) for p in args.paths)
    if not seed_dirs:
        print("error: no environments (spack.yaml) found under the given paths", file=sys.stderr)
        return 1

    nodes = load_environments(seed_dirs, concrete_env_dir)
    order = topo_sort(nodes)
    compute_ancestors(nodes, order)

    duplicates, _ = detect_duplicates(nodes, order)

    report = render_report(nodes, order, duplicates, args.show_roots)
    if args.output:
        Path(args.output).write_text(report + "\n")
    else:
        print(report)

    if args.json:
        Path(args.json).write_text(json.dumps(render_json(nodes, order, duplicates), indent=2))

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
