# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Geomodel(CMakePackage):
    """GeoModel is a user-friendly C++ Toolkit and Suite for
    HEP Detector Description with minimal dependencies."""

    homepage = "https://gitlab.cern.ch/GeoModelDev/GeoModel"
    url = "https://gitlab.cern.ch/GeoModelDev/GeoModel/-/archive/4.6.0/GeoModel-4.6.0.tar.bz2"
    git = "https://gitlab.cern.ch/GeoModelDev/GeoModel"

    maintainers("wdconinc", "stephenswat")

    license("Apache-2.0", checked_by="wdconinc")

    version("6.27.0", sha256="621f7d18d39fff1d9cced1b9c985b92cb35effb5afb4072b1aac2627729f54c5")
    version("6.26.0", sha256="01e51cc118ca84d865ef09583d119927712cab765b3953ebb7c69d9076c00b43")
    version("6.25.0", sha256="9f0a6c43e5c620eec1e39c6e4e3f4fa33fd6decda3079479393b55f1d1d12c24")
    version("6.24.0", sha256="739c6e13156eacde5a47ca84f9ea0a4cf6e90482cbd47e7310b980a81cfd281a")
    version("6.23.0", sha256="f39f2d1dc62693fd8358d0ca54716a5123bfa844458eb61f182a09dee292305a")
    version("6.22.0", sha256="6e23db099c3c7603d13c13dfac1152db484a69c0b9b962ec0ab495ae3299f2cd")
    version("6.21.0", sha256="44712cbe821eadfd74b187906686b52cf16d824c330d93a98d00f29c3e683314")
    version("6.20.0", sha256="e8ecb860658d94a6582be4b607111d9b81f3c38c9e46b8d6f4aae88573b5b878")
    version("6.19.0", sha256="d78e9035bd520c5aae007ee5806116ac0a9077b99927bd8810ced49295e1f44d")
    version("6.18.0", sha256="c32a7e1946bc7710f873e0e64b977cd3aad49e480833c728592428fd6aab34e4")
    version("6.17.0", sha256="61c9e68e41fae9dc697e90440bb668d364df952b1d53f034d2384e6720e8823c")
    version("6.16.0", sha256="bdecb722f1e45a7fccab05ded30ac231d6362ece3e681a203f40a1ed2f40be10")
    version("6.15.0", sha256="6e71a2b76972bd2940d035cdb96a8083a04b4ebe93ea95404b5aed39049c76da")
    version("6.14.0", sha256="b294f624145f922efd1da4016b79e698cabb0034cc6791841648d7845fd9fb15")
    version("6.13.0", sha256="8f1ebfe7fb502af078ed535410160becca2eb81286b94154b43c89873a3c45ad")
    version("6.12.0", sha256="4fa32672c6cb3d9b89ddf5e9566d0c283e5769768db6236883d72fecdd6207cd")
    version("6.11.1", sha256="f7b47ff4ed264e1bfb013e6cdb724e7532109f1d58ab5774656e6ff871afb362")
    version("6.11.0", sha256="fc9fdd7d64b623586089949d9790182dcd93ebb35a05198c91eac8adbbbfd778")
    version("6.10.0", sha256="968a0f7c8108b14f22041ca0c6ae8a3293175131c6f61055527ecdefe8c7839a")
    version("6.9.0", sha256="ea34dad8a0cd392e06794b8a1b7407dd6ad617fefd19fb4cccdf36b154749793")
    version("6.8.0", sha256="4dfd5a932955ee2618a880bb210aed9ce7087cfadd31f23f92e5ff009c8384eb")
    version("6.7.0", sha256="bfa69062ba191d0844d7099b28c0d6c3c0f87e726dacfaa21dba7a6f593d34bf")
    version("6.6.0", sha256="3cefeaa409177d45d3fa63e069b6496ca062991b0d7d71275b1748487659e91b")
    version("6.5.0", sha256="8a2f71493e54ea4d393f4c0075f3ca13df132f172c891825f3ab949cda052c5f")
    version("6.4.0", sha256="369f91f021be83d294ba6a9bdbe00077625e9fe798a396aceece8970e7dd5838")
    version("6.3.0", sha256="d2b101e06d20a8a3b638e6021f517a939f49ea6d8347ce40c927c27efe66b28c")
    version("6.2.0", sha256="99bb3908bf710ce5ba0bcdd192942705a183a9f2886079df091dc69423b7bdf1")
    version("6.1.0", sha256="2974f0e35e07cd44170d29ef106ec1ee50cb3fa3ba88382bea7394eb341dcd32")
    version("6.0.0", sha256="7263d44ae2b99da9bc45cf0bbda64b2d8bdce1b350328fe41fce001d5266c3a1")
    version("5.6.0", sha256="51e6570e119c2d3037b594779bb78d78b524c41132fac38d83ae162b5b6ffe54")
    version("5.4.0", sha256="82cd08bea5791d862244211f8367cd6f5698b311e4862b2eb5584f835d551821")
    version("5.3.0", sha256="d30c31f387716415542f3424a7f64ab62ef640a4e6f832243944918f7daca080")
    version("5.1.0", sha256="bbe7d6ea46fe750d9421fb741b2340d16afcddbf5d6aeafab09d60577d55f93d")
    version("4.6.0", sha256="d827dc79a5555fd7b09d1b670fc6f01f91476d0edf98ccd644c624f18fb729ca")

    variant(
        "visualization", default=False, description="Enable the build of GeoModelVisualization"
    )
    variant("geomodelg4", default=False, description="Enable the build of GeoModelG4")
    variant("fullsimlight", default=False, description="Enable the build of FullSimLight")
    variant("fsl", default=False, description="Enable the build of FSL and FullSimLight")
    variant("examples", default=False, description="Enable the build of GeoModelExamples")
    variant("tools", default=False, description="Enable the build of GeoModelTools")
    variant(
        "hepmc3",
        default=False,
        description="Build GeoModel tools with support for the HepMC3 exchange format",
        when="+fullsimlight",
    )
    variant(
        "pythia",
        default=False,
        description="Build GeoModel tools with support for the Pythia event generator",
        when="+fullsimlight",
    )

    variant(
        "cxxstd",
        default="17",
        values=("17", "20", "23"),
        multi=False,
        description="Use the specified C++ standard when building",
    )

    # GeoModel 6.11 requires std::format and C++20
    with when("@6.11:"):
        conflicts("cxxstd=17")
        conflicts("%gcc@:12")
        conflicts("%clang@:16")

    conflicts("+fullsimlight", when="+fsl", msg="FSL triggers the build of the FullSimLight")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.16:", type="build")
    depends_on("cmake@:3", when="@:6.10", type="build")

    depends_on("eigen@3.2.9:3", when="@:6.20")
    depends_on("eigen@3.2.9:5", when="@6.21:")
    depends_on("nlohmann-json@3.6.1:")
    depends_on("sqlite@3.7.17:")
    depends_on("xerces-c@3.2.3:")

    depends_on("geant4", when="+geomodelg4")
    depends_on("geant4", when="+fullsimlight")
    depends_on("hdf5+cxx", when="+fullsimlight")
    depends_on("hepmc3", when="+hepmc3")
    depends_on("pythia8", when="+pythia")
    with when("+visualization"):
        depends_on("hdf5+cxx")
        depends_on("qmake")
        with when("^[virtuals=qmake] qt"):
            depends_on("qt +gui +opengl +sql")
            # https://gitlab.cern.ch/GeoModelDev/GeoModel/-/merge_requests/567
            conflicts("@6.23:")
        with when("^[virtuals=qmake] qt-base"):
            depends_on("qt-base +gui +opengl +sql +widgets")
            depends_on("qt-5compat", when="@6.22:")
        depends_on("coin3d")
        depends_on("soqt")
        depends_on("gl")
        depends_on("egl", when="@6.11:")

    depends_on("googletest", when="@6.11", type="build")
    depends_on("googletest", when="@6.12:", type="test")

    def cmake_args(self):
        args = [
            self.define_from_variant("GEOMODEL_BUILD_VISUALIZATION", "visualization"),
            self.define_from_variant("GEOMODEL_BUILD_GEOMODELG4", "geomodelg4"),
            self.define_from_variant("GEOMODEL_BUILD_FULLSIMLIGHT", "fullsimlight"),
            self.define_from_variant("GEOMODEL_BUILD_FSL", "fsl"),
            self.define_from_variant("GEOMODEL_BUILD_EXAMPLES", "examples"),
            self.define_from_variant("GEOMODEL_BUILD_TOOLS", "tools"),
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define(
                "GEOMODEL_USE_QT6", self.spec.satisfies("+visualization ^[virtuals=qmake] qt-base")
            ),
        ]

        if self.spec.satisfies("@6.12:"):
            args.append(self.define("GEOMODEL_BUILD_TESTING", self.run_tests))

        return args
