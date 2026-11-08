# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import shlex
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
from spack_repo.builtin.build_systems import oneapi

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


def test_static_cluster_linking_preserves_system_library_flags(monkeypatch, tmp_path):
    repo = Path(__file__).parents[1] / "repos/spack_repo/builtin"
    with use_repositories(str(repo)) as repos:
        # Pin the CI version for layout checks; disable ILP64 and external libfabric
        # to keep the mocked dependency setup minimal. No MPI installation is needed.
        spec = Spec("intel-oneapi-mpi@=2021.19.0~ilp64~external-libfabric")
        spec.external_path = str(tmp_path)
        spec._mark_concrete()
        mpi = repos.get_pkg_class(spec.name)(spec)
        monkeypatch.setattr(
            mpi.module,
            "find_libraries",
            lambda *args, **kwargs: LibraryList([str(tmp_path / "libmpi.so")]),
        )
        archive = str(tmp_path / "libmkl_scalapack_lp64.a")
        libs = oneapi.IntelOneApiStaticLibraryList(
            LibraryList([archive]) + mpi.libs, LibraryList(["pthread", "m", "dl"])
        )
        assert libs.link_flags == (
            f"-Wl,--start-group {archive} {tmp_path / 'libmpi.so'} -ldl -lrt -lpthread "
            "-Wl,--end-group -lpthread -lm -ldl"
        )
        assert libs.directories == []


@pytest.mark.skipif(
    sys.platform != "linux",
    reason="The link test needs GNU ld group flags and librt, which only exist on Linux",
)
def test_static_cluster_flags_link(tmp_path):
    cc, ar = shutil.which("cc"), shutil.which("ar")
    if not cc or not ar:
        pytest.skip("A native C compiler and ar are required for the link test")

    obj = tmp_path / "cluster.o"
    archive = tmp_path / "libcluster.a"
    shared = tmp_path / "libmpi.so"
    output = tmp_path / "sample"
    subprocess.run(
        [cc, "-x", "c", "-c", "-o", str(obj), "-"],
        input="int cluster(void) { return 0; }",
        universal_newlines=True,
        check=True,
    )
    subprocess.run([ar, "cr", str(archive), str(obj)], check=True)
    subprocess.run(
        [cc, "-x", "c", "-shared", "-fPIC", "-o", str(shared), "-"],
        input="int mpi(void) { return 0; }",
        universal_newlines=True,
        check=True,
    )
    libs = oneapi.IntelOneApiStaticLibraryList(
        LibraryList([str(archive), str(shared), "dl", "rt", "pthread"]),
        LibraryList(["pthread", "m", "dl"]),
    )
    subprocess.run(
        [cc, "-x", "c", "-", "-x", "none", "-o", str(output), *shlex.split(libs.ld_flags)],
        input="int cluster(void); int mpi(void); int main(void) { return cluster() + mpi(); }",
        universal_newlines=True,
        check=True,
    )
    subprocess.run([str(output)], check=True)
