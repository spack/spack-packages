# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Unzip(MakefilePackage):
    """Unzip is a compression and file packaging/archive utility."""

    homepage = "http://www.info-zip.org/Zip.html"
    url = "https://downloads.sourceforge.net/infozip/unzip60.tar.gz"

    license("custom")

    version("6.0", sha256="036d96991646d0449ed0aa952e4fbe21b476ce994abc276e49d30e686708bd37")

    depends_on("c", type="build")  # See the logs: unzip's build only runs cc.

    # clang and oneapi need this patch, likely others
    # There is no problem with it on gcc, so make it a catch all
    patch("configure-cflags.patch")
    patch("strip.patch")

    # Fixed a buffer overflow
    # https://src.fedoraproject.org/rpms/unzip/c/2ee90c9b5cc4e48e4481f40f08153d1a335b701f
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/2ee90c9b5cc4e48e4481f40f08153d1a335b701f/f/unzip-6.0-attribs-overflow.patch",
        sha256="74bc961e8013a4058687a3730590a709b7889203beb74a4a8369ba0301bef0e2",
    )
    # Solve problem with symlink errors in archive with many files
    # https://src.fedoraproject.org/rpms/unzip/c/197087d9bc61cf08b4fc8f7846695c6304ffa195
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/197087d9bc61cf08b4fc8f7846695c6304ffa195/f/unzip-6.0-symlink.patch",
        sha256="fde8f9d6dbc5e9dc59f4497de8e4e313fd74318eaf5f33421acd74442fd10706",
    )
    # CVE-2014-9636
    # https://src.fedoraproject.org/rpms/unzip/c/df221ec2aca0a4c225e2c462b3a2dc7cd7a4be29
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/df221ec2aca0a4c225e2c462b3a2dc7cd7a4be29/f/unzip-6.0-cve-2014-8140.patch",
        sha256="64f64985270e026c01d2c19c6b66c218cf5bcfc7cf3d4a44e601fad41975ec73",
    )
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/df221ec2aca0a4c225e2c462b3a2dc7cd7a4be29/f/unzip-6.0-overflow.patch",
        sha256="c9a863e570bdaf2637c43bf1bba3d97808a1b0504d85418f6a8550ac286788f2",
    )
    # CVE-2014-8139, CVE-2014-8141
    # https://src.fedoraproject.org/rpms/unzip/c/f6883dfa8599e8b93a75c8f85f08879be28a5910
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/f6883dfa8599e8b93a75c8f85f08879be28a5910/f/unzip-6.0-cve-2014-8139.patch",
        sha256="337131428f491b7030f96ee5b8ef3d8f5963730d1619b2754c624f4616d79adb",
    )
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/f6883dfa8599e8b93a75c8f85f08879be28a5910/f/unzip-6.0-cve-2014-8141.patch",
        sha256="b7a14c33db93d1e5b4fc6ce113b4b99ff7a81ed56f46c87e001f22ec085e0273",
    )
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/f6883dfa8599e8b93a75c8f85f08879be28a5910/f/unzip-6.0-overflow-long-fsize.patch",
        sha256="251d5755ffb1e9701434c545fcda0fbfc2a16372f9d807fd07606b1364a1b55b",
    )
    # Fix heap overflow and infinite loop when invalid input is given
    # https://src.fedoraproject.org/rpms/unzip/c/36af2c8ca922dc45b55f600ffd9d0b9fcd520fd9
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/36af2c8ca922dc45b55f600ffd9d0b9fcd520fd9/f/unzip-6.0-heap-overflow-infloop.patch",
        sha256="b6f64d7b57e74ceaa794dd13a6937f063ec915343f3d5d88b0f81c919e7bf171",
    )
    # CVE-2016-9844
    # https://src.fedoraproject.org/rpms/unzip/c/ee4e72f3fc47f04af21d4860cc2604cf69d37dac
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/ee4e72f3fc47f04af21d4860cc2604cf69d37dac/f/0001-Fix-CVE-2016-9844-rhbz-1404283.patch",
        sha256="7d8e5c77ad99f9bf56d4cbf224b5635367feb44f81745dec84b44365f8f5eb16",
    )
    # CVE-2018-1000035
    # https://src.fedoraproject.org/rpms/unzip/c/8d5c0ff1a961f1052df9b86884a8b5d4587adaa5
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/8d5c0ff1a961f1052df9b86884a8b5d4587adaa5/f/unzip-6.0-cve-2018-1000035-heap-based-overflow.patch",
        sha256="aced0f27191a67f9b8b3fdc5995938a64fd87cea64a0bbba2106e06137ef91c2",
    )
    # CVE-2018-18384
    # https://src.fedoraproject.org/rpms/unzip/c/84dde352234b72fd10f5e288dee67e75199ee0c1
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/84dde352234b72fd10f5e288dee67e75199ee0c1/f/unzip-6.0-cve-2018-18384.patch",
        sha256="47e9deff12845e71de98cd19506a51c21d756a61bb67c0b17e77b84bdbe9fb84",
    )
    # Fix possible zipbomb
    # https://src.fedoraproject.org/rpms/unzip/c/0cde67cbab320b39c4c9d357e50c956e77b9dbf5
    # https://src.fedoraproject.org/rpms/unzip/c/a2a4f62759e625676e77436c7e5037e6fd0d9e13
    # https://src.fedoraproject.org/rpms/unzip/c/a6d716afe05ebb723d223e397945aaa437f045bc
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/0cde67cbab320b39c4c9d357e50c956e77b9dbf5/f/unzip-zipbomb-part1.patch",
        sha256="24582ff3dcd926d1a46caf8506f76999d2525dd66e36f50b25dca50799695f12",
    )
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/0cde67cbab320b39c4c9d357e50c956e77b9dbf5/f/unzip-zipbomb-part2.patch",
        sha256="f88b9d4119a1e256f3335a2d2c142dd95d13d7c5f9e5ecd4371e547249f3557c",
    )
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/0cde67cbab320b39c4c9d357e50c956e77b9dbf5/f/unzip-zipbomb-part3.patch",
        sha256="ee9e26018190a515572b66a26118916843aa1002131a86b5c52769dc663b7acb",
    )
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/a2a4f62759e625676e77436c7e5037e6fd0d9e13/f/unzip-zipbomb-part4.patch",
        sha256="179330daaf395b631025d23ec666c227707caa8859a872cc39d3ea0e2a645e97",
    )
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/a2a4f62759e625676e77436c7e5037e6fd0d9e13/f/unzip-zipbomb-part5.patch",
        sha256="44599c80ea507c1fcfb8fb58b4c9d8d18f3157de453c1e0469a703322deb042a",
    )
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/a2a4f62759e625676e77436c7e5037e6fd0d9e13/f/unzip-zipbomb-part6.patch",
        sha256="81ca46cfd3cf732de8cf78c57790ed7d5c73a5e8d41943b8f6313cede6004f3e",
    )
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/a6d716afe05ebb723d223e397945aaa437f045bc/f/unzip-zipbomb-switch.patch",
        sha256="59c0983b53801d3080684bc616d3570ccacfe471f3a8c442916b87f2f3bfa334",
    )
    patch(
        "https://src.fedoraproject.org/rpms/unzip/raw/c98fc67064eee9a7437bc3dc5bce3432c3571d5c/f/unzip-zipbomb-manpage.patch",
        sha256="4e5a081aa8d0ad9aa5ceeda9eaeefbb6a7e7666d6b7a5b81cb0a61a3ff99a942",
    )

    def flag_handler(self, name, flags):
        if name == "cflags":
            # https://src.fedoraproject.org/rpms/unzip/blob/d68244a849ae9f4e7f130a3d25156207212c5c36/f/unzip-gnu89-build.patch
            # the patch does not work directly because the Makefile calls generic and not
            # generic_gcc
            if self.spec.satisfies("%gcc@15:"):
                flags.append("-std=gnu89")

        return (flags, None, None)

    def get_make_args(self):
        make_args = ["-f", join_path("unix", "Makefile")]

        cflags = []
        if not self.spec.satisfies("%nvhpc"):
            cflags.append("-Wno-error=implicit-function-declaration")
            cflags.append("-Wno-error=implicit-int")
        cflags.append("-DLARGE_FILE_SUPPORT")

        make_args.append(f"LOC={' '.join(cflags)}")
        return make_args

    @property
    def build_targets(self):
        target = "macosx" if "platform=darwin" in self.spec else "generic"
        return self.get_make_args() + [target]

    def url_for_version(self, version):
        return f"http://downloads.sourceforge.net/infozip/unzip{version.joined}.tar.gz"

    @property
    def install_targets(self):
        return self.get_make_args() + [f"prefix={self.prefix}", "install"]
