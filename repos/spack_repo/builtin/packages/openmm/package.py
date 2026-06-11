# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Openmm(CMakePackage, CudaPackage, ROCmPackage):
    """A high performance toolkit for molecular simulation. Use it as
    a library, or as an application. We include extensive language
    bindings for Python, C, C++, and even Fortran. The code is open
    source and actively maintained on Github, licensed under MIT and
    LGPL. Part of the Omnia suite of tools for predictive biomolecular
    simulation."""

    homepage = "https://openmm.org/"
    url = "https://github.com/openmm/openmm/archive/7.4.1.tar.gz"

    version("8.5.1", sha256="16b2c2a4ce959be223ba4cc00dcb22a5d84ae3fb8c3948643632f6bda1ce6944")
    version("8.5.0", sha256="7e55c9399244731a4beebfe7fb72ecae2bbd02d14ff12b7544280584b9ca952f")
    version("8.1.1", sha256="347ad9f04dd88a673f7871127d9f23a75caf2c1a460a3f21f3328a24dc6547d0")
    version("8.0.0", sha256="dc63d7b47c8bb7b169c409cfd63d909ed0ce1ae114d37c627bf7a4231acf488e")
    version("7.7.0", sha256="51970779b8dc639ea192e9c61c67f70189aa294575acb915e14be1670a586c25")
    version("7.6.0", sha256="5a99c491ded9ba83ecc3fb1d8d22fca550f45da92e14f64f25378fda0048a89d")
    version("7.5.1", sha256="c88d6946468a2bde2619acb834f57b859b5e114a93093cf562165612e10f4ff7")
    version("7.5.0", sha256="516748b4f1ae936c4d70cc6401174fc9384244c65cd3aef27bc2c53eac6d6de5")
    version("7.4.1", sha256="e8102b68133e6dcf7fcf29bc76a11ea54f30af71d8a7705aec0aee957ebe3a6d")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    variant("python", default=True, description="Build Python bindings")
    variant("fortran", default=True, description="Build C and Fortran wrappers")
    variant("opencl", default=False, description="Build with OpenCL")
    variant("examples", default=False, description="Build example executables")
    variant("docs", default=False, description="Build API documentation")
    variant("shared", default=True, description="Build shared libraries")
    variant("static", default=False, description="Build static libraries")

    conflicts("+rocm", when="@:8.1.1", msg="OpenMM HIP platform was first released in 8.2.0")
    conflicts("~shared~static", msg="OpenMM must build at least one library type")
    conflicts("~shared+python", msg="OpenMM Python bindings require shared libraries")
    conflicts("~shared+fortran", msg="OpenMM C and Fortran wrappers require shared libraries")

    depends_on("cmake@3.17:", type="build", when="@7.5.1:")
    depends_on("cmake@3.1:", type="build")
    # https://github.com/openmm/openmm/issues/3317
    depends_on("doxygen@:1.9.1", type="build", when="@:7.6.0+python")
    depends_on("doxygen@:1.9.1", type="build", when="@:7.6.0+fortran")
    depends_on("doxygen@:1.9.1", type="build", when="@:7.6.0+docs")
    depends_on("doxygen", type="build", when="@7.7:+python")
    depends_on("doxygen", type="build", when="@7.7:+fortran")
    depends_on("doxygen", type="build", when="@7.7:+docs")
    depends_on("swig", type="build", when="+python")
    depends_on("fftw", when="@:7")
    depends_on("python@2.7:", type=("build", "run"), when="@:7+python")
    depends_on("python@3:", type=("build", "run"), when="@8:+python")
    depends_on("python@3.10:", type=("build", "run"), when="@8.5:8.5+python")
    depends_on("python@2.7:", type="build", when="@:7+fortran")
    depends_on("python@3:", type="build", when="@8:+fortran")
    depends_on("python@3.10:", type="build", when="@8.5:8.5+fortran")
    depends_on("python@2.7:", type="build", when="@:7+docs")
    depends_on("python@3:", type="build", when="@8:+docs")
    depends_on("python@3.10:", type="build", when="@8.5:8.5+docs")
    depends_on("py-setuptools", type="build", when="+python")
    depends_on("py-cython", type="build", when="+python")
    depends_on("py-numpy", type=("build", "run"), when="+python")
    depends_on("py-sphinx", type="build", when="+docs")
    depends_on("py-breathe", type="build", when="+docs")
    depends_on("py-jinja2", type="build", when="+docs+python")
    depends_on("cuda", when="+cuda", type=("build", "link", "run"))
    depends_on("hip +rocm", when="+rocm", type=("build", "link", "run"))
    depends_on("opencl", when="+opencl", type=("build", "link", "run"))
    extends("python", when="+python")

    @property
    def install_targets(self):
        targets = []

        if "+docs" in self.spec:
            targets.append("C++ApiDocs")
            if "+python" in self.spec:
                targets.append("PythonApiDocs")

        targets.append("install")

        if "+python" in self.spec and "+docs" not in self.spec:
            targets.append("PythonInstall")

        return targets

    # Backport <https://github.com/openmm/openmm/pull/3154> to
    # `openmm@7.5.1+cuda`, which is the version currently required by
    # `py-alphafold`.
    patch(
        "https://github.com/openmm/openmm/commit/71bc7c8c70ffbccd82891dec7fd4f4deb99af64d.patch?full_index=1",
        sha256="9562e03eb8d43ba4d8f0f7b2a3326cc464985fc148804cf9e4340fd7a87bb8e7",
        when="@7.5.1+cuda",
    )

    def patch(self):
        install_string = (
            f'set(PYTHON_SETUP_COMMAND "install --prefix={self.prefix} '
            '--single-version-externally-managed --root=/")'
        )

        filter_file(
            r"set\(PYTHON_SETUP_COMMAND \"install.*",
            install_string,
            "wrappers/python/CMakeLists.txt",
        )

    @property
    def python_site_packages(self):
        python_version = self.spec["python"].version.up_to(2)
        return join_path(self.prefix.lib, f"python{python_version}", "site-packages")

    def _setup_openmm_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib.plugins)
        env.set("OPENMM_PLUGIN_DIR", self.prefix.lib.plugins)
        env.set("OPENMM_INCLUDE_PATH", self.prefix.include)
        env.set("OPENMM_LIB_PATH", self.prefix.lib)
        if "+python" in self.spec:
            env.prepend_path("PYTHONPATH", self.python_site_packages)

    def _setup_cuda_environment(self, env: EnvironmentModifications) -> None:
        spec = self.spec
        if "+cuda" in spec:
            env.set("OPENMM_CUDA_COMPILER", self.spec["cuda"].prefix.bin.nvcc)
            env.set("CUDA_HOST_COMPILER", self.compiler.cxx)

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define_from_variant("OPENMM_BUILD_CUDA_LIB", "cuda"),
            self.define_from_variant("OPENMM_BUILD_HIP_LIB", "rocm"),
            self.define_from_variant("OPENMM_BUILD_OPENCL_LIB", "opencl"),
            self.define_from_variant("OPENMM_BUILD_PYTHON_WRAPPERS", "python"),
            self.define_from_variant("OPENMM_BUILD_C_AND_FORTRAN_WRAPPERS", "fortran"),
            self.define_from_variant("OPENMM_BUILD_EXAMPLES", "examples"),
            self.define_from_variant("OPENMM_GENERATE_API_DOCS", "docs"),
            self.define_from_variant("OPENMM_BUILD_SHARED_LIB", "shared"),
            self.define_from_variant("OPENMM_BUILD_STATIC_LIB", "static"),
            self.define("BUILD_TESTING", self.run_tests),
        ]

        if "+rocm" in spec:
            args.extend(
                [
                    self.define("HIP_DIR", spec["hip"].prefix.lib.cmake.hip),
                    self.define("HIPRTC_DIR", spec["hip"].prefix.lib.cmake.hiprtc),
                ]
            )

        return args

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        self._setup_openmm_environment(env)
        self._setup_cuda_environment(env)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        self._setup_openmm_environment(env)
        self._setup_cuda_environment(env)

    def setup_dependent_run_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        self.setup_run_environment(env)

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        self.setup_build_environment(env)
