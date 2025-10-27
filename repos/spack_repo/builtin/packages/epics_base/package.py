# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class EpicsBase(MakefilePackage):
    """This is the main core of EPICS, the Experimental Physics and Industrial
    Control System, comprising the build system and tools, common and OS-interface
    libraries, network protocol client and server libraries, static and run-time
    database access routines, the database processing code, and standard record,
    device and driver support."""

    homepage = "https://epics-controls.org"
    url = "https://epics-controls.org/download/base/base-7.0.6.1.tar.gz"

    maintainers("glenn-horton-smith")

    version("7.0.9", sha256="acd62c9b97b60caea9303cc3aab922dbf2bc3bfb3d20e0027110ffe4c906a6c7")
    version("7.0.8.1", sha256="6c93a5e09b21392adbb3de423605d428ee4ddb1272fc708a251b082272fa73f5")
    version("7.0.8", sha256="9232b53afa617d0b95cfcb93952fde100342f2e29e829d34fa66ed61410439d4")
    version("7.0.7", sha256="44d6980e19c7ad097b9e3d20c3401fb20699ed346afc307c8d1b44cf7109d475")
    version("7.0.6.1", sha256="8ff318f25e2b70df466f933636a2da85e4b0c841504b9e89857652a4786b6387")
    version("7.0.6", sha256="bc1d9edd0624542870424b90baafebe16af17a317b01aec577757e96830deee0")
    version("7.0.5", sha256="faf8dd3bfa4a3b0036e8b62a5f647a0596bfd579f31c6cc00b2ce2f82bcf9de1")
    version("7.0.4.1", sha256="7b1aa5a0b0a381207b3aa64b4496ffbdd0882ba3d57a09d75b94a9ef1fef668d")
    version("7.0.4", sha256="1f0597b91740742beec49ca1ca59e7b71f63483b7495068b4f0f685c0cda9e69")
    version("7.0.3.1", sha256="1de65638a806be6c0eebc0b7840ed9dd1a1a7879bcb6ab0da88a1e8e456b709c")
    version("7.0.3", sha256="b75f4e5e4146368280295f9443fb9e194a33987449d2e0d5d5fcb2cac4468e6d")
    version("7.0.2.2", sha256="908f0161c9effb6adb74e40476a07e0f832e19ef589993740517911779187611")
    version("7.0.2.1", sha256="b5357d497dad126abfe2d65cfb05f618615c99525bcc2c3c884649c5b11c854f")
    version("7.0.2", sha256="63825d46ab59c4e67b7f3f0e6b1a84073640c2ce6d079da913cddfb1488f1fc2")
    version("7.0.1.1", sha256="f5815868c4b69a40904f3c5c1fb00975ec9eaa0b6fd42cd3ef568e7947b0b1ca")
    version("3.16.2", sha256="fd2e5d37ea151e6a2b2074f8737955a0a21d8945caea1b8517b6e4ecf3c714eb")
    version("3.16.1", sha256="fc01ff8505871b9fa7693a4d5585667587105f34ec5e16a207d07b704d1dc5ed")
    version("3.15.9", sha256="93fcc2f19102d6d211ddc706812391b221267e526f114386ed1e3097c9354c8d")
    version("3.15.8", sha256="1d0171b577e71347fa21154db123ba1910aad025e918b1de16a6ffab97842f4f")
    version("3.15.7", sha256="406019e1aa51afaf60121444aa54ca15f65712184f7c14ddd9a87ea6c232a633")
    version("3.15.6", sha256="537e5249011ce90bdffae057994daedd89ae6351667f0aa89ab6918935caf5bc")
    version(
        "3.15.6-rc1", sha256="865474ca6637d5067134c85b7eabfbcf1a292623b73635c5cc261963e2602f38"
    )
    version("3.15.5", sha256="b66b807baf07f24762a46d62521ded8e04cfbe71b14d43ab8ee65c870f6db07b")
    version("3.15.4", sha256="b4d433c47084ce70f08b8e94aba4e0f6716e50c680b86d905ffc17811649b392")
    version("3.15.3", sha256="76c6d6e487a7c6a1b1b72ce7a7f4a3e2dd6a4617b789c00adf479b96dcc7055e")
    version("3.15.2", sha256="fdf6b8332b60a612781164d6493777fa8684a185981f688f9da0553cc47eb02e")
    version("3.15.1", sha256="25b7ce9cad87f61e39da67dbf0d7e397dcf7ed8b5bff6a90f591481995b32473")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("readline")
    depends_on("perl", type=("build", "run"))

    def url_for_version(self, version):
        url = "https://epics-controls.org/download/base/base-{0}.tar.gz"
        return url.format(version)

    def patch(self):
        filter_file(r"^\s*CC\s*=.*", "CC = " + spack_cc, "configure/CONFIG.gnuCommon")
        filter_file(r"^\s*CCC\s*=.*", "CCC = " + spack_cxx, "configure/CONFIG.gnuCommon")
        filter_file(r"\$\(PERL\)\s+\$\(XSUBPP\)", "$(XSUBPP)", "modules/ca/src/perl/Makefile")

    @property
    def install_targets(self):
        return ["INSTALL_LOCATION={0}".format(self.prefix), "install"]

    def get_epics_host_arch(self):
        perl = which("perl", required=True)
        return perl("%s/perl/EpicsHostArch.pl" % self.prefix.lib, output=str, error=str).strip()

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("EPICS_BASE", self.prefix)

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        epics_host_arch = self.get_epics_host_arch()
        env.set("EPICS_HOST_ARCH", epics_host_arch)
        env.set("EPICS_BASE", self.prefix)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        epics_host_arch = self.get_epics_host_arch()
        env.set("EPICS_HOST_ARCH", epics_host_arch)
        env.set("EPICS_BASE", self.prefix)
        env.prepend_path("PATH", join_path(self.prefix.bin, epics_host_arch))
