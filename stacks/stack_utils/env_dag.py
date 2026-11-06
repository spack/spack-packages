"""Helper module for working with environments with heirarchy defined by reuse.

ex.
    >>> seed_dirs = find_spack_yaml_dirs(Path(p) for p in args.paths)
    >>> nodes = load_environments(seed_dirs, concrete_env_dir)
    >>> order = topo_sort(nodes)
    >>> compute_ancestors(nodes, order)
"""

import argparse
import json
import os
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

try:
    import spack.environment as ev
    import spack.spec
except ImportError:
    sys.exit(
        "error: could not import the 'spack' modules.\n"
        "This module requires core spack tools not present in the Package API. e.g.:\n"
        "    spack python -c \"import util.env_dag; util.env_dag.load_environments()\""
    )


IGNORE_DIRS = {".spack-env", ".git"}


# --------------------------------------------------------------------------
# Discovery: find environments and the reuse-from DAG between them
# --------------------------------------------------------------------------


@dataclass
class EnvNode:
    name: str  # human label, relative to --concrete-env-dir
    path: Path  # absolute, resolved directory containing spack.yaml
    requested: bool  # explicitly named by the user vs. pulled in as context
    has_lock: bool
    env: Optional["ev.Environment"] = None
    parent_names: Set[str] = field(default_factory=set)
    ancestor_names: Set[str] = field(default_factory=set)


def find_spack_yaml_dirs(paths: Iterable[Path]) -> List[Path]:
    """Recursively find directories containing a spack.yaml under `paths`."""
    found = []
    for path in paths:
        path = path.resolve()
        if (path / "spack.yaml").is_file():
            found.append(path)
            continue
        for dirpath, dirnames, filenames in os.walk(path):
            dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
            if "spack.yaml" in filenames:
                found.append(Path(dirpath).resolve())
    return found


def label_for(path: Path, concrete_env_dir: Path) -> str:
    try:
        return str(path.relative_to(concrete_env_dir))
    except ValueError:
        return str(path)


def reuse_from_paths(env: "ev.Environment", concrete_env_dir: Path) -> List[Path]:
    """Resolve the `spack:concretizer:reuse:from` environment paths."""
    reuse_cfg = env.manifest.configuration.get("concretizer", {}).get("reuse")
    if not isinstance(reuse_cfg, dict):
        return []
    sources = reuse_cfg.get("from", [])
    paths = []
    old_value = os.environ.get("SPACK_CONCRETE_ENV_DIR")
    os.environ["SPACK_CONCRETE_ENV_DIR"] = str(concrete_env_dir)
    try:
        for source in sources:
            if source.get("type") != "environment" or "path" not in source:
                continue
            expanded = os.path.expandvars(source["path"])
            paths.append(Path(expanded).resolve())
    finally:
        if old_value is None:
            os.environ.pop("SPACK_CONCRETE_ENV_DIR", None)
        else:
            os.environ["SPACK_CONCRETE_ENV_DIR"] = old_value
    return paths



def load_environments(
    seed_dirs: List[Path], concrete_env_dir: Path
) -> Dict[str, EnvNode]:
    """Load seed environments plus any reuse-from ancestors, transitively."""
    nodes: Dict[str, EnvNode] = {}  # keyed by resolved absolute path string
    requested = {str(p) for p in seed_dirs}
    queue = list(seed_dirs)

    while queue:
        path = queue.pop(0)
        key = str(path)
        if key in nodes:
            continue

        has_lock = (path / "spack.lock").is_file()
        env_obj = None
        parent_paths: List[Path] = []
        if not (path / "spack.yaml").is_file():
            print(f"warning: skipping {path} - no spack.yaml found", file=sys.stderr)
            continue

        try:
            env_obj = ev.Environment(path)
        except Exception as err:  # noqa: BLE001 - report and continue
            print(f"warning: failed to load environment {path}: {err}", file=sys.stderr)

        if env_obj is not None:
            parent_paths = reuse_from_paths(env_obj, concrete_env_dir)

        if not has_lock:
            print(
                f"warning: {path} has no spack.lock",
                file=sys.stderr,
            )

        node = EnvNode(
            name=label_for(path, concrete_env_dir),
            path=path,
            requested=key in requested,
            has_lock=has_lock,
            env=env_obj,
        )
        nodes[key] = node

        for parent_path in parent_paths:
            node.parent_names.add(label_for(parent_path, concrete_env_dir))
            if str(parent_path) not in nodes:
                queue.append(parent_path)

    # parent_names above were recorded by label; re-derive using the final
    # label->key mapping so the graph is keyed consistently by label.
    by_label: Dict[str, EnvNode] = {node.name: node for node in nodes.values()}
    return by_label


def topo_sort(nodes: Dict[str, EnvNode]) -> List[str]:
    """Kahn's algorithm: parents (reuse sources) before their dependents."""
    in_degree = {name: 0 for name in nodes}
    children: Dict[str, List[str]] = defaultdict(list)
    for name, node in nodes.items():
        for parent in node.parent_names:
            if parent not in nodes:
                continue  # dangling reference, already warned about elsewhere
            children[parent].append(name)
            in_degree[name] += 1

    ready = sorted(name for name, deg in in_degree.items() if deg == 0)
    order: List[str] = []
    while ready:
        name = ready.pop(0)
        order.append(name)
        for child in sorted(children[name]):
            in_degree[child] -= 1
            if in_degree[child] == 0:
                ready.append(child)
        ready.sort()

    if len(order) != len(nodes):
        remaining = sorted(set(nodes) - set(order))
        raise RuntimeError(
            "cycle detected in the environment reuse graph, involving: "
            + ", ".join(remaining)
        )
    return order


def compute_ancestors(nodes: Dict[str, EnvNode], order: List[str]) -> None:
    """Populate node.ancestor_names (transitive closure of parent_names)."""
    for name in order:
        node = nodes[name]
        ancestors: Set[str] = set()
        for parent in node.parent_names:
            if parent not in nodes:
                continue
            ancestors.add(parent)
            ancestors |= nodes[parent].ancestor_names
        node.ancestor_names = ancestors


