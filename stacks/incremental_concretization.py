import argparse
import pathlib
import sys
from stack_utils.env_dag import (
    compute_ancestors,
    find_spack_yaml_dirs,
    load_environments,
    topo_sort,
)

from spack.concretize_ui import TerminalUI

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-p",
        "--platform",
        default="linux",
        choices=("linux", "darwin", "win64"),
        help="OS/Platform.",
    )
    parser.add_argument(
        "-t", "--target",
        default="x86",
        choices=("x86", "aarch64"),
        help="Target architecture."
    )
    parser.add_argument("-i", "--include", action="append", help="Stacks to include.")
    parser.add_argument("-x", "--exclude", action="append", help="Stacks to exclude.")
    parser.add_argument("-f", "--force", action="store_true", help="Force reconcretization.")

    parser.add_argument("prefix", type=pathlib.Path, help="Force reconcretization.")

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    env_prefix = (args.prefix / args.platform / args.target).resolve()
    print(f"Searching in {env_prefix.as_posix()}")

    env_paths = []
    for p in env_prefix.iterdir():
        if not p.is_dir():
            continue
        if args.include and p.name not in args.include:
            continue
        if args.exclude and p.name in args.exclude:
            continue
        env_paths.append(p)

    seed_dirs = find_spack_yaml_dirs(env_paths)
    if not seed_dirs:
        print("error: no environments (spack.yaml) found under the given paths", file=sys.stderr)
        return 1


    nodes = load_environments(seed_dirs, args.prefix.resolve())
    order = topo_sort(nodes)
    compute_ancestors(nodes, order)

    for stack in order:
        if args.exclude and any((x in stack) for x in args.exclude):
            if nodes[stack].has_lock:
                print(f"Skipping concretization of {stack}")
                continue
            else:
                print(f"Cannot skip non-concrete environment {stack}")

        if not nodes[stack].env:
            print(f"error: no environment for {stack} to concretize", file=sys.stderr)
            return 1

        if nodes[stack].has_lock and not args.force:
            print(f"Already concrete: {stack}...")
            continue

        print(f"Concretizing {stack}...")
        with nodes[stack].env:
            with nodes[stack].env.write_transaction():
                nodes[stack].env.concretize(force=args.force, ui=TerminalUI())
        print(f"Concretizing {stack}...Done")


if __name__ == "__main__":
    sys.exit(main())
