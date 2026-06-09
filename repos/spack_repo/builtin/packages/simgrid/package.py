# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Simgrid(CMakePackage):
    """SimGrid is a framework for developing simulators of distributed
    applications targetting distributed platforms, which can in turn be
    used to prototype, evaluate and compare relevant platform configurations,
    system designs, and algorithmic approaches.
    """

    homepage = "https://simgrid.org/"
    url = "https://github.com/simgrid/simgrid/releases/download/v3.27/simgrid-3.27.tar.gz"
    git = "https://framagit.org/simgrid/simgrid.git"

    maintainers("viniciusvgp")

    license("LGPL-2.1-or-later")

    version("4.1", sha256="e16750bd13f5d3c0fb2370d79ba8eee124ee47f9e48c113bd23af9d9782d198b")
    version("4.0", sha256="c9f07122d43f61f1f0a21be2e42ef2cd6290abbf9b697926430f44ca2786bdea")
    version("3.36", sha256="cfdf6b98270c59be5c112457793c540bdd6a10deece91cbdb4793fbda190b95d")
    version("3.35", sha256="b4570d3de18d319cbd2e16c5a669f90760307673c0cc9940d4d11cfc537e69a8")
    version("3.34", sha256="161f1c6c0ebb588c587aea6388114307bb31b3c6d5332fa3dc678151f1d0564d")
    version("3.32", sha256="837764eb81562f04e49dd20fbd8518d9eb1f94df00a4e4555e7ec7fa8aa341f0")
    version("3.31", sha256="4b44f77ad40c01cf4e3013957c9cbe39f33dec9304ff0c9c3d9056372ed4c61d")
    version("3.30", sha256="0cad48088c106e72efb42fb423e65d77fc9053cc03d6f3a5ff7ba4c712bb4eb8")
    version("3.29", sha256="83e8afd653555eeb70dc5c0737b88036c7906778ecd3c95806c6bf5535da2ccf")
    version("3.28", sha256="558276e7f8135ce520d98e1bafa029c6c0f5c2d0e221a3a5e42c378fe0c5ef2c")
    version("3.27", sha256="51aeb9de0434066e5fec40e785f5ea9fa934afe7f6bfb4aa627246e765f1d6d7")
    version("3.26", sha256="ac50da1eacc5a53b094a988a8ecde09962c29320f346b45e74dd32ab9d9f3e96")
    version(
        "3.25",
        sha256="0b5dcdde64f1246f3daa7673eb1b5bd87663c0a37a2c5dcd43f976885c6d0b46",
        url="https://github.com/simgrid/simgrid/releases/download/v3.25/SimGrid-3.25.tar.gz",
    )
    version(
        "3.24",
        sha256="c976ed1cbcc7ff136f6d1a8eda7d9ccf090e0e16d5239e6e631047ae9e592921",
        url="https://github.com/simgrid/simgrid/releases/download/v3.24/SimGrid-3.24.tar.gz",
    )
    version(
        "3.23",
        sha256="c3c86673abf0a2685337f1f520a7782d9611cd18d0374f35e1d98652fdbbaf86",
        url="https://github.com/simgrid/simgrid/releases/download/v3.23/SimGrid-3.23.tar.gz",
    )
    version(
        "3.22",
        sha256="4fdff0a8e4c81f8edf6f7eedfa32e19748abe688d156ea9240178c558c8bad33",
        url="https://github.com/simgrid/simgrid/releases/download/v3_22/SimGrid-3.22.tar.gz",
    )
    with default_args(deprecated=True):
        version(
            "3.21",
            sha256="d2a6e9021016dd39a2b6f8d5d18c8223f6885746c5269550d19ba29c47c0c6a0",
            url="https://github.com/simgrid/simgrid/releases/download/v3_21/SimGrid-3.21.tar.gz",
        )
        version(
            "3.20",
            sha256="4d4757eb45d87cf18d990d589c31d223b0ea8cf6fcd8c94fca4d38162193cef6",
            url="https://github.com/simgrid/simgrid/releases/download/v3.20/SimGrid-3.20.tar.gz",
        )

    version("develop", branch="master")

    variant("doc", default=False, description="Build documentation")
    variant("smpi", default=True, description="SMPI provides MPI")
    variant("examples", default=False, description="Install examples")
    variant("mc", default=False, description="Model checker")
    variant("msg", default=False, description="Enables the old MSG interface")
    variant("python", default=False, description="Enables the Python bindings")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated
    extends("python", when="+python")  # generated

    # does not build correctly with some old compilers -> rely on packages
    depends_on("boost@:1.69.0", when="@:3.21")
    depends_on("boost+exception")

    conflicts(
        "%gcc@10:",
        when="@:3.23",
        msg="simgrid <= v3.23 cannot be built with gcc >= 10,"
        " please use an older release (e.g., %gcc@:9).",
    )

    conflicts("+msg", when="@3.34:", msg="MSG was removed from SimGrid v3.33.")

    # fix compilation with GCC 14 for v3.34
    patch(
        "https://github.com/simgrid/simgrid/commit/e4ecb51dcdf597fb02340d7855dafd0da9bd9018.patch?full_index=1",
        sha256="80cbe0eed635ff1864f0c2945763c8561b86c08c0c2b60d2ee5a57e1659ccc3d",
        when="@3.34",
    )

    def setup_dependent_package(self, module, dependent_spec):
        if self.spec.satisfies("+smpi"):
            self.spec.smpicc = join_path(self.prefix.bin, "smpicc")
            self.spec.smpicxx = join_path(self.prefix.bin, "smpicxx")
            self.spec.smpifc = join_path(self.prefix.bin, "smpif90")
            self.spec.smpif77 = join_path(self.prefix.bin, "smpiff")

    def cmake_args(self):
        spec = self.spec
        args = [self.define_from_variant("enable_python", "python")]

        if not spec.satisfies("+doc"):
            args.append("-Denable_documentation=OFF")
        if spec.satisfies("+mc"):
            args.append("-Denable_model-checking=ON")
        if spec.satisfies("+msg"):
            args.append("-Denable_msg=ON")
        return args

    def install(self, spec, prefix):
        """Make the install targets"""
        with working_dir(self.build_directory):
            make("install")
            if spec.satisfies("+examples"):
                install_tree(join_path(self.build_directory, "examples"), prefix.examples)
