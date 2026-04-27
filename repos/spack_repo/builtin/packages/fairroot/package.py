# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Fairroot(CMakePackage):
    """C++ simulation, reconstruction and analysis framework for particle physics experiments"""

    homepage = "http://fairroot.gsi.de"
    url = "https://github.com/FairRootGroup/FairRoot/archive/v18.8.2.tar.gz"
    git = "https://github.com/FairRootGroup/FairRoot.git"
    maintainers("dennisklein", "fuhlig1", "jezwilkinson")

    tags = ["hep"]
    version("develop", branch="dev")
    version("19.0.0", sha256="6ad650ece4b673f72f4ddfe2bffeb671239c775b672b4e99673e7145ea6d8ab2")
    version("18.8.2", sha256="0bc9bafd9583f8a4c92977647c1eb360d66f45fbc6c81a15c5a1613640934684")

    variant(
        "cxxstd",
        default="17",
        values=("17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )
    variant("sim", default=True, description="Enable simulation engines and event generators")
    variant("examples", default=False, description="Install examples")

    depends_on("cmake@3.13.4:", type="build")
    depends_on("cmake@3.18:", type="build", when="@19:")
    depends_on("boost@1.68.0: +container +serialization")
    depends_on("faircmakemodules@0.2:", when="@18:")
    depends_on("fairlogger@1.4.0:")
    depends_on("fairmq@1.4.11:")

    # Version-specific fairsoft release dependencies
    depends_on("fairsoft-bundle")
    depends_on("fairsoft-bundle@2025-05", when="@18.8.2:")

    depends_on("flatbuffers")
    depends_on("fmt", when="@19:")
    depends_on("geant3", when="+sim")
    depends_on("geant4", when="+sim")
    depends_on("geant4-vmc", when="+sim")
    depends_on("googletest@1.7.0:")
    depends_on("msgpack-c@3.1:", when="+examples")
    depends_on("protobuf")
    depends_on("pythia6", when="+sim")
    depends_on("pythia8", when="+sim")
    depends_on("root+http+xml+gdml")
    depends_on("vgm", when="+sim")
    depends_on("vmc", when="@18.4: ^root@6.18:")
    depends_on("yaml-cpp", when="@18.2:")
    for std in ("17", "20"):
        for dep in ("root", "fairmq"):
            depends_on("{0} cxxstd={1}".format(dep, std), when="cxxstd={0}".format(std))

    def setup_build_environment(self, env):
        super(Fairroot, self).setup_build_environment(env)
        env.unset("SIMPATH")
        env.unset("FAIRSOFT_ROOT")

    def cmake_args(self):
        options = []
        options.append("--log-level=VERBOSE")
        if self.spec.satisfies("@18.4:"):
            cxxstd = self.spec.variants["cxxstd"].value
            if cxxstd != "default":
                options.append("-DCMAKE_CXX_STANDARD={0}".format(cxxstd))
        if self.spec.satisfies("@:18,develop"):
            options.append("-DROOTSYS={0}".format(self.spec["root"].prefix))
            options.append("-DPYTHIA8_DIR={0}".format(self.spec["pythia8"].prefix))

        options.append("-DBUILD_EXAMPLES:BOOL=%s" % ("ON" if "+examples" in self.spec else "OFF"))

        if self.spec.satisfies("^boost@:1.69.99"):
            options.append("-DBoost_NO_BOOST_CMAKE=ON")
        options.append("-DBUILD_PROOF_SUPPORT=OFF")
        return options

    @property
    def root_library_path(self):
        if self.spec.satisfies("^root@:6.25"):
            return "LD_LIBRARY_PATH"
        return "ROOT_LIBRARY_PATH"

    def common_env_setup(self, env):
        # So that root finds the shared library / rootmap
        env.prepend_path(self.root_library_path, self.prefix.lib)

    def setup_run_environment(self, env):
        self.common_env_setup(env)

    def setup_dependent_run_environment(self, env, dependent_spec):
        self.common_env_setup(env)
