# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGpaw(PythonPackage, CudaPackage):
    """GPAW is a density-functional theory (DFT) Python code based on the
    projector-augmented wave (PAW) method and the atomic simulation environment
    (ASE)."""

    homepage = "https://gpaw.readthedocs.io/index.html"
    pypi = "gpaw/gpaw-25.7.0.tar.gz"

    maintainers("alikhamze", "Chronum94")

    license("GPL-3.0-or-later", checked_by="alikhamze")

    version("25.7.0", sha256="93ac829bba36be74eab0d7deef5eb798613c04edbce196837208d206cf39c431")
    version("25.1.0", sha256="80236e779784df3317e7da395dc59ea403bc0213bb3a68d02c17957162e972ea")
    version("24.6.0", sha256="fb48ef0db48c0e321ce5967126a47900bba20c7efb420d6e7b5459983bd8f6f6")
    version("23.9.1", sha256="19a24840b876003528864b7a0b38fc0d456800b83b8666b1f724273660745b47")
    version("23.6.1", sha256="ff56d323a499972c8991770a6ab0334a6dd18df36e9c94360e0aa1ddf8867dfd")

    variant("mpi", default=True, description="Build with MPI support")
    variant("scalapack", default=True, description="Build with ScaLAPACK support")
    variant("fftw", default=True, description="Build with FFTW support")
    variant("libvdwxc", default=True, description="Build with libvdwxc support")
    variant("elpa", default=True, description="Build with ELPA support")
    variant("openmp", default=True, description="Build with OpenMP support")
    variant("cuda", default=False, when="@23.6:", description="Build with CUDA GPU support")

    # Build dependencies
    depends_on("c", type="build")
    depends_on("py-setuptools", type="build")

    # Version-agnostic required dependencies
    depends_on("blas")
    depends_on("lapack")

    # Version-specific required dependencies
    with when("@25.7.0:"):
        depends_on("libxc")
        depends_on("python@3.9:", type=("build", "run"))
        depends_on("py-ase@3.25.0:", type=("build", "run"))
        depends_on("py-numpy", type=("build", "run"))
        depends_on("py-scipy@1.6.0:", type=("build", "run"))
        depends_on("py-gpaw-data", type=("run"))

    with when("@25.1.0"):
        depends_on("libxc")
        depends_on("python@3.9:", type=("build", "run"))
        depends_on("py-ase@3.23.0:", type=("build", "run"))
        depends_on("py-numpy", type=("build", "run"))
        depends_on("py-scipy@1.6.0:", type=("build", "run"))

    with when("@24.1.0:24.6.0"):
        depends_on("libxc@:6.2.2")
        depends_on("python@3.8:", type=("build", "run"))
        depends_on("py-ase@3.23.0:", type=("build", "run"))
        depends_on("py-numpy@1.17:1.26.4", type=("build", "run"))
        depends_on("py-scipy@1.6.0:", type=("build", "run"))

    with when("@23.6.1:23.9.1"):
        depends_on("libxc@:6.2.2")
        depends_on("python@3.7:", type=("build", "run"))
        depends_on("py-ase@3.22.1:", type=("build", "run"))
        depends_on("py-numpy@1.17:1.26.4", type=("build", "run"))
        depends_on("py-scipy@1.6.0:", type=("build", "run"))

    # Variant dependencies and conflicts
    depends_on("mpi", when="+mpi", type=("build", "link", "run"))
    depends_on("fftw-api", when="+fftw")
    depends_on("scalapack", when="+scalapack")
    depends_on("libvdwxc", when="+libvdwxc")
    depends_on("cuda", when="+cuda")
    depends_on("py-cupy +cuda", when="+cuda")
    depends_on("openmpi +cuda", when="+cuda +mpi", type=("build", "link", "run"))
    conflicts("cuda_arch=none", when="+cuda", msg="CUDA arch required when building cuda variant.")
    conflicts("elpa", when="+cuda", msg="CUDA and ELPA have not been tested together.")
    # Fixed elpa version due to compilation/linking errors on older and newer versions.
    # Tested for versions @23.6.1:25.1.0
    depends_on("elpa@2022.11.001", when="+elpa")

    def patch(self):
        spec = self.spec
        # For build notes see https://wiki.fysik.dtu.dk/gpaw/install.html

        libxc = spec["libxc"]
        blas = spec["blas"]
        lapack = spec["lapack"]

        libs = blas.libs + lapack.libs + libxc.libs

        include_dirs = [blas.prefix.include, lapack.prefix.include, libxc.prefix.include]

        runtime_library_dirs = []

        bools = ""

        if "+mpi" in spec:
            libs += spec["mpi"].libs
            include_dirs.append(spec["mpi"].prefix.include)

        if "+scalapack" in spec:
            libs += spec["scalapack"].libs
            include_dirs.append(spec["scalapack"].prefix.include)
            scalapack_macros = repr(
                [("GPAW_NO_UNDERSCORE_CBLACS", "1"), ("GPAW_NO_UNDERSCORE_CSCALAPACK", "1")]
            )
            bools += "scalapack = True\n"

        if "+fftw" in spec:
            libs += spec["fftw-api"].libs
            include_dirs.append(spec["fftw-api"].prefix.include)
            bools += "fftw = True\n"

        if "+libvdwxc" in spec:
            libs += spec["libvdwxc"].libs
            include_dirs.append(spec["libvdwxc"].prefix.include)
            bools += "libvdwxc = True\n"

        if "+elpa" in spec:
            libs += spec["elpa"].libs
            include_dirs.append(spec["elpa"].prefix.include)
            bools += "elpa = True\n"
            runtime_library_dirs += spec["elpa"].libs.directories

        if "+openmp" in spec:
            openmp_compile_args = ["-fopenmp"]
            openmp_link_args = ["-fopenmp"]

        if "+cuda" in spec:
            bools += "gpu = True\n"
            include_dirs.append(spec["cuda"].prefix.include)
            libs += spec["cuda"].libs
            libs += ["cudart", "cublas"]
            gpu_compile_args = ["-O3", "-g"]
            for f in spec.variants["cuda_arch"].value:
                gpu_compile_args.append("-gencode")
                gpu_compile_args.append(f"arch=compute_{f},code=sm_{f}")

        lib_dirs = list(libs.directories)
        libs = list(libs.names)
        rpath_str = ":".join(self.rpath)

        with open("siteconfig.py", "w") as f:
            f.write(bools)
            f.write(f"libraries = {repr(libs)}\n")
            f.write(f"include_dirs = {repr(include_dirs)}\n")
            f.write(f"library_dirs = {repr(lib_dirs)}\n")
            f.write(f"extra_link_args += ['-Wl,-rpath={rpath_str}']\n")
            if "+mpi" in spec:
                if spec.satisfies("@:19.8.1"):
                    f.write("define_macros += [('PARALLEL', '1')]\n")
            if "+scalapack" in spec:
                f.write(f"define_macros += {scalapack_macros}\n")
            if "+elpa" in spec:
                f.write(f"runtime_library_dirs = {repr(runtime_library_dirs)}\n")
            if "+openmp" in spec:
                f.write(f"extra_compile_args += {openmp_compile_args}\n")
                f.write(f"extra_link_args += {openmp_link_args}\n")
            if "+cuda" in spec:
                f.write("gpu_target = 'cuda'\n")
                f.write("gpu_compiler = 'nvcc'\n")
                f.write(f"gpu_compile_args = {gpu_compile_args}\n")
