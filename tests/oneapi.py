# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from pathlib import Path

import pytest

from spack.package import LibraryList, Spec
from spack.repo import use_repositories


@pytest.mark.parametrize(
    "spec_string,system_flags",
    [
        ("intel-oneapi-mkl@=2026.2.0+shared threads=none", "-lpthread -lm -ldl"),
        ("intel-oneapi-mkl@=2026.2.0~shared threads=none", "-lpthread -lm -ldl"),
        ("intel-oneapi-mpi@=2021.19.0~ilp64~external-libfabric", "-ldl -lrt -lpthread"),
    ],
)
def test_system_libraries_use_linker_search(monkeypatch, tmp_path, spec_string, system_flags):
    repo = Path(__file__).parents[1] / "repos/spack_repo/builtin"
    with use_repositories(str(repo)) as repos:
        spec = Spec(spec_string)
        spec.external_path = str(tmp_path)
        spec._mark_concrete()
        pkg = repos.get_pkg_class(spec.name)(spec)
        module = pkg.module

        def unexpected_system_search(*args, **kwargs):
            pytest.fail("System library discovery must not recurse into foreign SDK sysroots")

        monkeypatch.setattr(module, "find_system_libraries", unexpected_system_search)
        if spec.name == "intel-oneapi-mkl":
            library = tmp_path / ("libmkl_core.so" if "+shared" in spec else "libmkl_core.a")
            monkeypatch.setattr(pkg, "_find_mkl_libs", lambda shared: LibraryList([str(library)]))
        else:
            monkeypatch.setattr(
                module,
                "find_libraries",
                lambda *args, **kwargs: LibraryList([str(tmp_path / "libmpi.so")]),
            )

        libs = pkg.libs
        assert libs.link_flags.endswith(system_flags)
        assert set(libs.directories) <= {str(tmp_path)}
        if spec.name == "intel-oneapi-mkl" and "~shared" in spec:
            assert f"-Wl,--start-group {library} -Wl,--end-group" in libs.link_flags
