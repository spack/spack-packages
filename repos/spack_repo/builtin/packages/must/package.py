# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Must(CMakePackage):
    """MUST detects usage errors of the Message Passing Interface (MPI)
    and reports them to the user. As MPI calls are complex and usage
    errors common, this functionality is extremely helpful for application
    developers that want to develop correct MPI applications. This includes
    errors that already manifest: segmentation faults or incorrect results
    as well as many errors that are not visible to the application developer
    or do not manifest on a certain system or MPI implementation."""

    homepage = "https://www.i12.rwth-aachen.de/go/id/nrbe"
    url = "https://hpc.rwth-aachen.de/must/files/MUST-v1.9.0.tar.gz"

    maintainers("jgalarowicz", "dmont")

    version("1.11.2", sha256="934d41dcf379df65c68853646344736a85d58ecc93e8fc4fe9c4077b2eca9ccb")
    version("1.11.1", sha256="46a3e56691e818df92471865bf5affe1635f9cba3fb364ed8ce7a19c36c1caca")
    version("1.11.0", sha256="9ebe0022b2bf6a6d39af52c8a363058777ce31838971123d5a51a193bcdfcae3")
    version("1.10.0", sha256="fd8a1152f5b7b97f19c62ca0c7875953c6e3a8f5e16502adacd1de0cd3402d25")
    version("1.9.2", sha256="b2c71e9b7bc86b74469acffd8b523acc91f6a6bd2c48f3b91383d074d673b929")
    version("1.9.0", sha256="24998f4ca6bce718d69347de90798600f2385c21266c2d1dd39a87dd8bd1fba4")
    version("1.8.0", sha256="9754fefd2e4c8cba812f8b56a5dd929bc84aa599b2509305e1eb8518be0a8a39")
    version("1.7.2", sha256="616c54b7487923959df126ac4b47ae8c611717d679fe7ec29f57a89bf0e2e0d0")

    variant("test", default=False, description="Enable must internal tests")
    variant("tsan", default=True, description="Enable thread sanitizer")
    variant("graphviz", default=False, description="Use to generate graphs")
    variant("stackwalker", default=False, description="Unwind with stackwalker")
    variant("backward", default=True, description="Unwind with backward-cpp", when="@1.8:")
    variant("typeart", default=False, description="Enable TypeArt build")

    # Don't enable stackwalker, backward simultaneously
    # Use either backward or stackwalker for unwinding
    conflicts("+stackwalker +backward")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")

    depends_on("cmake@3.9:")
    depends_on("python@3.1.5:", type=("build", "link", "run"))
    # must test variant requires llvm
    depends_on("llvm@10.0.0:", when="+test")
    # must typeart typeart variant requires llvm
    depends_on("llvm@10.0.0:", when="+typeart")
    depends_on("mpi")
    depends_on("libxml2")
    depends_on("dyninst", when="+stackwalker")
    depends_on("graphviz", when="+graphviz")

    @run_after("install")
    def install_prebuilds(self):
        """Perform make install-prebuilds"""
        with working_dir(self.build_directory):
            make("prebuilds")
            make("install-prebuilds")

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define_from_variant("ENABLE_TESTS", "test"),
            self.define_from_variant("ENABLE_TYPEART", "typeart"),
            self.define_from_variant("ENABLE_TSAN", "tsan"),
            self.define_from_variant("USE_BACKWARD", "backward"),
        ]

        if spec.satisfies("+stackwalker"):
            args.append(self.define("USE_CALLPATH", True))
            args.append(self.define("STACKWALKER_INSTALL_PREFIX", spec["dyninst"].prefix))

        return args
