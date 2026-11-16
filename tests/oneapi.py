# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import shlex
import shutil
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest
from spack_repo.builtin.build_systems import oneapi

from spack.package import EnvironmentModifications, LibraryList, Spec
from spack.repo import use_repositories


@pytest.mark.parametrize(
    "variants,c_wrappers,intel_fortran",
    [
        ("~generic-names~classic-names", ["mpiicx", "mpiicpx"], ["mpiifx"] * 3),
        ("~generic-names+classic-names", ["mpiicc", "mpiicpc"], ["mpiifort"] * 3),
        ("+generic-names~classic-names", ["mpicc", "mpicxx"], ["mpif77", "mpif90", "mpifc"]),
    ],
)
@pytest.mark.parametrize(
    "compiler_spec,gnu_fortran",
    [
        ("%c=gcc %fortran=gcc", True),
        ("%c=intel-oneapi-compilers %fortran=gcc", True),
        ("%c=gcc %fortran=intel-oneapi-compilers", False),
        ("%c=gcc %fortran=intel-oneapi-compilers-classic", False),
        ("%c=gcc", False),
    ],
)
def test_mpi_wrappers_follow_dependent_fortran(
    tmp_path, monkeypatch, variants, c_wrappers, intel_fortran, compiler_spec, gnu_fortran
):
    """A reused binary MPI must select modules for each dependent's Fortran compiler."""
    repo = Path(__file__).parents[1] / "repos/spack_repo/builtin"
    with use_repositories(str(repo)) as repos:
        # The MPI installation's C compiler says nothing about the consumer's
        # Fortran module format (including when that consumer also uses GCC C).
        spec = Spec("intel-oneapi-mpi@=2021.18.0 " + variants + " %c=gcc")
        spec.external_path = str(tmp_path)
        spec._mark_concrete()
        mpi = repos.get_pkg_class(spec.name)(spec)
        dependent = Spec("hdf5@=1.14.6 " + compiler_spec)
        dependent._mark_concrete()
        module = dependent.package.module
        wrappers = SimpleNamespace(
            spack_cc="/spack/cc",
            spack_cxx="/spack/c++",
            spack_fc="/spack/fc",
            spack_f77="/spack/f77",
        )
        # These globals normally come from Spack's build-environment setup.
        for name, value in vars(wrappers).items():
            monkeypatch.setattr(module, name, value, raising=False)
        mpi.setup_dependent_package(module, dependent)
        env = EnvironmentModifications()
        mpi.setup_dependent_build_environment(env, dependent)
        values = {}
        env.apply_modifications(values)

        fortran = ["mpif77", "mpif90", "mpifc"] if gnu_fortran else intel_fortran
        names = c_wrappers + fortran
        paths = [str(mpi.component_prefix.bin.join(name)) for name in names]
        assert [values[key] for key in ("MPICC", "MPICXX", "MPIF77", "MPIF90", "MPIFC")] == paths
        assert [spec.mpicc, spec.mpicxx, spec.mpif77, spec.mpifc] == [
            paths[0],
            paths[1],
            paths[2],
            paths[4],
        ]
        assert values["I_MPI_FC"] == values["I_MPI_F90"] == wrappers.spack_fc
        assert values["I_MPI_F77"] == wrappers.spack_f77
        # Selecting GNU wrappers must not change the next dependent's selection.
        assert [Path(p).name for p in mpi.wrapper_paths()] == c_wrappers + intel_fortran


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
