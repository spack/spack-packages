# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import importlib.util
import os
import sys
import types
from contextlib import contextmanager
from pathlib import Path

import pytest


@pytest.fixture
def lhapdfsets_package(monkeypatch):
    package_path = (
        Path(__file__).resolve().parent.parent
        / "repos"
        / "spack_repo"
        / "builtin"
        / "packages"
        / "lhapdfsets"
        / "package.py"
    )

    spack_repo = types.ModuleType("spack_repo")
    builtin = types.ModuleType("spack_repo.builtin")
    build_systems = types.ModuleType("spack_repo.builtin.build_systems")
    bundle = types.ModuleType("spack_repo.builtin.build_systems.bundle")

    class BundlePackage:
        pass

    bundle.BundlePackage = BundlePackage

    spack = types.ModuleType("spack")
    package = types.ModuleType("spack.package")

    def noop(*args, **kwargs):
        return None

    class InstallError(Exception):
        pass

    class Spec:
        @staticmethod
        def from_detection(*args, **kwargs):
            return ("spec", args, kwargs)

    class EnvironmentModifications:
        pass

    @contextmanager
    def working_dir(path):
        yield

    package.variant = noop
    package.version = noop
    package.depends_on = noop
    package.maintainers = noop
    package.mkdirp = os.makedirs
    package.which = noop
    package.working_dir = working_dir
    package.join_path = os.path.join
    package.Spec = Spec
    package.InstallError = InstallError
    package.EnvironmentModifications = EnvironmentModifications
    package.__all__ = [
        "variant",
        "version",
        "depends_on",
        "maintainers",
        "mkdirp",
        "which",
        "working_dir",
        "join_path",
        "Spec",
        "InstallError",
        "EnvironmentModifications",
    ]

    monkeypatch.setitem(sys.modules, "spack_repo", spack_repo)
    monkeypatch.setitem(sys.modules, "spack_repo.builtin", builtin)
    monkeypatch.setitem(sys.modules, "spack_repo.builtin.build_systems", build_systems)
    monkeypatch.setitem(sys.modules, "spack_repo.builtin.build_systems.bundle", bundle)
    monkeypatch.setitem(sys.modules, "spack", spack)
    monkeypatch.setitem(sys.modules, "spack.package", package)

    spec = importlib.util.spec_from_file_location("lhapdfsets_package", package_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return object.__new__(module.Lhapdfsets), InstallError


def test_lhapdfsets_default_sets(lhapdfsets_package):
    package, _ = lhapdfsets_package

    assert package.resolve_sets(("default",)) == [
        "MMHT2014lo68cl",
        "MMHT2014nlo68cl",
        "CT14lo",
        "CT14nlo",
    ]


def test_lhapdfsets_pattern_and_deduplication(lhapdfsets_package):
    package, _ = lhapdfsets_package

    resolved_sets = package.resolve_sets(("CT14*", "CT14nlo"))

    assert "CT14lo" in resolved_sets
    assert resolved_sets.count("CT14nlo") == 1


def test_lhapdfsets_unmatched_pattern_raises(lhapdfsets_package):
    package, InstallError = lhapdfsets_package

    with pytest.raises(InstallError, match="did not match any available LHAPDF sets"):
        package.resolve_sets(("DOES_NOT_EXIST_*",))
