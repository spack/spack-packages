# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.generic import Package
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Pareval(Package, CudaPackage, ROCmPackage):
    """ParEval benchmark for evaluating LLMs' parallel code generation capabilities"""

    homepage = "https://github.com/parallelcodefoundry/pareval"
    url = "https://github.com/parallelcodefoundry/pareval/archive/refs/tags/v1.2.tar.gz"
    git = "https://github.com/parallelcodefoundry/pareval.git"

    maintainers("Dando18")

    license("MIT", checked_by="Dando18")

    version("develop", branch="develop")
    version("1.2", sha256="8b374afc07bc177a3ba335ff1fe782b3a1943bbcd2dd7ac0a62dedfa4f44f651")
    version("1.1", sha256="c07bf9b1027afed97281eb2fbcbe8f3d819ac12045ba9d1a7a90d5488f92cc53")
    version("1.0", sha256="314cf62e421c9382f4344d7da57f3dcdf9ab3e1272afd6a7badabf0ffe80f294")

    variant("generate", default=True, description="Build support for LLM generation")
    variant("evaluate", default=True, description="Build support for running evaluation drivers")
    variant("mpi", default=True, description="Build MPI driver support")
    variant("kokkos", default=True, description="Build Kokkos driver support")

    depends_on("py-tqdm")

    with when("+generate"):
        depends_on("py-transformers")
        depends_on("py-torch")
        depends_on("py-datasets")

    with when("+evaluate"):
        depends_on("cxx")
        depends_on("gmake")
        depends_on("cmake")
        depends_on("mpi", when="+mpi")
        depends_on("kokkos@4.1.00 +threads", when="+kokkos")

    def install(self, spec, prefix):
        mkdirp(prefix.pareval)
        install_tree("bin", prefix.bin)

        if spec.satisfies("+evaluate"):
            with working_dir(join_path(self.stage.source_path, "drivers", "cpp")):
                make()

            install_tree(join_path(self.stage.source_path, "drivers"), prefix.pareval.drivers)

        if spec.satisfies("+generate"):
            install_tree(join_path(self.stage.source_path, "generate"), prefix.pareval.generate)

    def setup_run_environment(self, env: EnvironmentModifications):
        env.set("PAREVAL_ROOT", self.prefix.pareval)
