# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Madgraph5amc(MakefilePackage):
    """MadGraph5_aMC@NLO is a framework that aims at providing
    all the elements necessary for SM and BSM phenomenology,
    such as the computations of cross sections, the generation
    of hard events and their matching with event generators,
    and the use of a variety of tools relevant to
    event manipulation and analysis."""

    homepage = "https://launchpad.net/mg5amcnlo"
    url = "https://launchpad.net/mg5amcnlo/lts/2.9.x/+download/MG5_aMC_v2.9.20.tar.gz"

    tags = ["hep"]

    # Launchpad can sometimes be slow to respond
    timeout = {"timeout": 60}

    with default_args(fetch_options=timeout):
        version("3.5.9", sha256="1e707fcd18f5b967c3f6220b3e5538622c93472376cae6666c56d0f2c2dd4b92")
        version("3.5.6", sha256="d4f336196303df748074ac92f251db8e6592fca37b3059c2e0f2a764c7e50975")
        version(
            "2.9.20",
            sha256="09a70e2e8b52e504bcaaa6527d3cec9641b043f5f853f2d11fa3c9970b7efae9",
            preferred=True,
        )

    variant(
        "atlas",
        default=False,
        description="Apply changes requested by " + "the ATLAS experimenent on LHC",
    )
    variant("ninja", default=False, description="Use external installation" + " of Ninja")
    variant("collier", default=False, description="Use external installation" + " of Collier")
    variant("pythia8", default=False, description="Use external installation of Pythia8")

    depends_on("fortran", type="build")
    depends_on("cxx", type="build")

    depends_on("gosam-contrib", when="+ninja")
    depends_on("collier", when="+collier")
    depends_on("lhapdf")
    depends_on("fastjet")
    depends_on("py-six", type=("build", "run"))

    depends_on("libtirpc")
    depends_on("pythia8", when="+pythia8")

    patch("gcc14.patch", when="@:3.5.5%gcc@14:")
    patch("madgraph5amc.patch", level=0, when="@:2.9")
    # Fix running from CVMFS on AFS, for example on lxplus at CERN
    patch(
        "https://patch-diff.githubusercontent.com/raw/mg5amcnlo/mg5amcnlo/pull/96.diff?full_index=1",
        sha256="ac6644f1d0ef51d9bdb27a1519261f1cf27d075d39faa278fbc2849acbc5575d",
        when="@3:3.5",
    )

    def edit(self, spec, prefix):
        def set_parameter(name, value):
            config_files.filter(
                "^#?[ ]*" + name + "[ ]*=.*$", name + " = " + value, ignore_absent=True
            )

        config_files = FileFilter(
            join_path("input", ".mg5_configuration_default.txt"),
            join_path("input", "mg5_configuration.txt"),
        )

        if "+ninja" in spec:
            set_parameter("ninja", spec["gosam-contrib"].prefix.lib)

        if "+collier" in spec:
            set_parameter("collier", spec["collier"].prefix.lib)

        set_parameter("output_dependencies", "internal")
        set_parameter("lhapdf", join_path(spec["lhapdf"].prefix.bin, "lhapdf-config"))
        set_parameter("fastjet", join_path(spec["fastjet"].prefix.bin, "fastjet-config"))

        set_parameter("automatic_html_opening", "False")

        set_parameter("cpp_compiler", self.compiler.cxx)
        set_parameter("fortran_compiler", self.compiler.fc)

    def build(self, spec, prefix):
        with working_dir(join_path("vendor", "CutTools")):
            make(parallel=False)

        if "+atlas" in spec:
            if os.path.exists(join_path("bin", "compile.py")):
                compile_py = Executable(join_path("bin", "compile.py"))
            else:
                compile_py = Executable(join_path("bin", ".compile.py"))

            compile_py()

    def install(self, spec, prefix):
        def installdir(dirname):
            install_tree(dirname, join_path(prefix, dirname))

        def installfile(filename):
            install(filename, join_path(prefix, filename))

        for p in os.listdir(self.stage.source_path):
            if os.path.isdir(p):
                installdir(p)
            else:
                if p != "doc.tgz":
                    installfile(p)
                else:
                    mkdirp(prefix.share)
                    install(p, join_path(prefix.share, p))

        install(
            join_path("Template", "LO", "Source", ".make_opts"),
            join_path(prefix, "Template", "LO", "Source", "make_opts"),
        )

        # TODO: Fix for reproducibility, see https://github.com/spack/spack/pull/41128#issuecomment-2305777485
        if "+pythia8" in spec:
            with open("install-pythia8-interface", "w") as f:
                f.write(
                    f"""set pythia8_path {spec["pythia8"].prefix}
                        install mg5amc_py8_interface
                """
                )
            mg5 = Executable(join_path(prefix, "bin", "mg5_aMC"))
            mg5("install-pythia8-interface")

    def url_for_version(self, version):
        major = str(version).split(".")[0]
        minor = str(version).split(".")[1]
        url = f"https://launchpad.net/mg5amcnlo/{major}.0/{major}.{minor}.x/+download/MG5_aMC_v{version}.tar.gz"
        return url
