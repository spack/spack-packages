# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.makefile import MakefilePackage
from spack.package import *
from spack.util.environment import EnvironmentModifications


class Pflare(MakefilePackage):
    """Library with parallel iterative methods for asymmetric linear systems built on PETSc."""

    homepage = "https://github.com/PFLAREProject/PFLARE"
    url = "https://github.com/PFLAREProject/PFLARE/archive/refs/tags/v1.24.10.tar.gz"
    git = "https://github.com/PFLAREProject/PFLARE.git"

    # Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers("stevendargaville")
    license("MIT", checked_by="stevendargaville")

    version(
        "1.25.0",
        sha256="befb361b39c7601a8ca6f148369313f5755b238d5f6a4cbf91b19b23c93e8952",
        preferred=True,
    )
    version(
        "1.24.11",
        sha256="8bcbee9e58ac3b2627dfbe78ebfac375192fb97d87337b40962d2730935ea1ce",
    )
    version(
        "1.24.10",
        sha256="1d51ea420413d9959ea1a8a9499a663487672f08107838eaa6be11eab1e6fc2a",
    )
    version("main", branch="main")

    # Optionally build the python bindings
    variant("python", default=False, description="Enable PFLARE Python bindings via petsc4py")

    # --- Dependencies ---
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
        
    depends_on("mpi")
    depends_on("blas")
    depends_on("lapack")
    depends_on("metis")
    depends_on("parmetis")

    # PETSc version dependencies
    depends_on("petsc@3.24.1:", when="@1.25.0:")
    depends_on("petsc@3.23.1:3.23.7", when="@:1.24.11")
    # Bugs in 3.24.0 fixed in:
    #  https://gitlab.com/petsc/petsc/-/merge_requests/8768
    #  https://gitlab.com/petsc/petsc/-/merge_requests/8713
    conflicts("^petsc@3.24.0", msg="PETSc 3.24.0 has a known bugs in routines used by PFLARE")
    
    # Optional Python dependencies (needed at build/run time by python/setup.py)
    depends_on("python", when="+python", type=("build", "run"))
    depends_on("py-setuptools", when="+python", type="build")
    depends_on("py-cython", when="+python", type="build")
    depends_on("py-numpy", when="+python", type=("build", "run"))
    depends_on("py-petsc4py", when="+python", type=("build", "run"))

    # ~~~~~~~~~~~~~~~
    # The build itself needs private PETSc headers that aren't included in the petsc install
    # So we tell spack to restage petsc during our build and then we set petsc_src_dir
    # ~~~~~~~~~~~~~~~
    def edit(self, spec, prefix):
        # Stage the PETSc source that matches the concretized dependency
        dep_pkg = self.spec["petsc"].package
        dep_pkg.do_stage()  # fetch+expand PETSc sources into its own stage

        petsc_src_dir = dep_pkg.stage.source_path  # e.g., .../petsc-3.23.6
        link = join_path(self.stage.source_path, "petsc_src_dir")

        # Point our tree at the staged PETSc source
        if os.path.islink(link) or os.path.exists(link):
            try:
                os.unlink(link)
            except OSError:
                pass
        os.symlink(petsc_src_dir, link)

    # No need to override PYTHON/PYTHONPATH here; use Spack’s python wrapper via PATH
    def setup_build_environment(self, env):
        if "+python" in self.spec:
            # Keep user site-packages out of the build
            env.set("PYTHONNOUSERSITE", "1")

    # ~~~~~~~~~~~~~~~
    # The build appends the petsc source files into our include flags
    # ~~~~~~~~~~~~~~~
    def build(self, spec, prefix):
        from spack.util.environment import set_env
        from spack.util.executable import which

        # Use the symlink created in edit()
        petsc_inc_src = join_path(self.stage.source_path, "petsc_src_dir", "include")
        if not os.path.isdir(petsc_inc_src):
            raise InstallError(f"PETSc include directory not found at {petsc_inc_src}")

        extra_inc = f"-I{petsc_inc_src}"
        with set_env(
            CFLAGS=(f"{os.environ.get('CFLAGS', '')} {extra_inc}").strip(),
            CXXFLAGS=(f"{os.environ.get('CXXFLAGS', '')} {extra_inc}").strip(),
            CPPFLAGS=(f"{os.environ.get('CPPFLAGS', '')} {extra_inc}").strip(),
        ):
            # The Makefile has a `build_tests_check` target that builds the library and tests
            make("build_tests_check", parallel=True)
            if "+python" in spec:
                # Use the python wrapper provided by Spack’s build env
                py = which("python")  # resolves to .../python-venv-*/bin/python
                make("python", f"PYTHON={py.path}", parallel=True)

    # ~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~~
    def install(self, spec, prefix):
        args = [f"PREFIX={prefix}"]
        if "+python" in spec:
            pyver = spec["python"].version.up_to(2)
            args.append(f"PYVER={pyver}")
        make("install", *args)

    # ~~~~~~~~~~~~~~~
    # Let dependents query include and link flags
    # ~~~~~~~~~~~~~~~
    def headers(self):
        # Expose the whole include tree (Fortran .mod and C headers)
        hdrs = find_headers("*", self.prefix.include, recursive=True)
        return hdrs

    def libs(self):
        libs = find_libraries("libpflare", self.prefix.lib, shared=True, recursive=False)
        if not libs:
            libs = find_libraries("libpflare", self.prefix.lib, shared=False, recursive=False)
        return libs

    # ~~~~~~~~~~~~~~~
    # Provide environment variables when spack load pflare is called
    # to make it easy for people to build against PFLARE
    # ~~~~~~~~~~~~~~~
    def setup_run_environment(self, env):
        import os

        # Runtime and build path-like vars
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        env.prepend_path("LIBRARY_PATH", self.prefix.lib)
        env.prepend_path("CPATH", self.prefix.include)
        env.prepend_path("CMAKE_PREFIX_PATH", self.prefix)
        env.prepend_path("PKG_CONFIG_PATH", join_path(self.prefix.lib, "pkgconfig"))
        if os.path.isdir(self.prefix.bin):
            env.prepend_path("PATH", self.prefix.bin)

        # Optional: provide ready-to-use flags for simple Makefiles
        env.append_flags("CPPFLAGS", f"-I{self.prefix.include}")
        env.append_flags("CFLAGS", f"-I{self.prefix.include}")
        env.append_flags("CXXFLAGS", f"-I{self.prefix.include}")
        env.append_flags("FFLAGS", f"-I{self.prefix.include}")  # Fortran .mod includes
        env.append_flags("LDFLAGS", f"-L{self.prefix.lib} -Wl,-rpath,{self.prefix.lib}")

        if "+python" in self.spec:
            pyver = self.spec["python"].version.up_to(2)
            pydir = join_path(self.prefix.lib, f"python{pyver}", "site-packages")
            env.prepend_path("PYTHONPATH", pydir)

    # ~~~~~~~~~~~~~~~
    # Cleanup PETSc stage directory after install
    # ~~~~~~~~~~~~~~~
    @run_after("install")
    def cleanup_petsc_stage(self):
        # Avoid leaking a staged PETSc tree on disk
        try:
            self.spec["petsc"].package.stage.destroy()
        except Exception:
            pass

    # ~~~~~~~~~~~~~~~
    # Check setup_run_environment and the python import works after the install
    # ~~~~~~~~~~~~~~~
    @run_after("install")
    def smoke_test_with_run_env(self):
        # Only when +python and tests requested
        if "+python" not in self.spec or not self.run_tests:
            return

        run_env = EnvironmentModifications()
        # Populate what `spack load` would set
        self.setup_run_environment(run_env)
        run_env.set("PYTHONNOUSERSITE", "1")  # keep user site-packages out

        py = self.spec["python"].command
        # Apply (non-context) and restore afterwards
        orig_env = os.environ.copy()
        try:
            run_env.apply_modifications()
            py("-c", "import pflare; print('PFLARE Python import OK')")
        finally:
            os.environ.clear()
            os.environ.update(orig_env)
