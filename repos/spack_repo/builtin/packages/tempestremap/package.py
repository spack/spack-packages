# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Tempestremap(AutotoolsPackage):
    """TempestRemap is a conservative, consistent and monotone remapping
    package for arbitrary grid geometry with support for finite volumes
    and finite elements.

    There is still quite a bit of work to be done, but any feedback is
    appreciated on the software in its current form
    """

    homepage = "https://github.com/ClimateGlobalChange/tempestremap"
    url = "https://github.com/ClimateGlobalChange/tempestremap/archive/v2.0.5.tar.gz"

    maintainers("iulian787", "vijaysm", "paullric", "xylar", "andrewdnolan")

    version("2.2.0", sha256="548b902701ec7c3b6970e0c83c6b93bfb7fb38ecc30b6ef89de8182efd948fa3")
    version("2.1.6", sha256="d2208b5d6952eba5003ee7abcf22f46a254ba03f6b76dcc4d246068573d424e2")
    version("2.1.5", sha256="1c8976b20555330294523114d18ecdd6e885df7af1887710a7a5a96e403770d3")
    version("2.1.4", sha256="94e0bb4e1be9ec7282936f4d89996e0b99d89166fff14995bb7a3d3964577ebe")
    version("2.1.3", sha256="f3925871b9bc19c39002665970283a6f70ec5e159f0c87c74d1ef4f7efa4c26a")
    version("2.1.2", sha256="18421e1b81ecb5b2aa3bb8f3e9df084586d90c13b27960b78202d264f587934e")
    version("2.1.1", sha256="f5ea21f82b358ba127550fc1f49e701cba0379d22ce030c274135109f678b980")
    version("2.1.0", sha256="2dfae7d81d685eafd36da3b4a989676c0b2800b91e4fdac3e5ceb7a20eff99f2")
    version("2.0.5", sha256="8618f5cbde450922efa1d77e67b062c557788b0cf4304adca30237afe3ade887")
    version("2.0.4", sha256="8349eeb604e97b13d2ecde8626a69e579a7af70ad0e8a6925a8bb4306a4963a4")
    version("2.0.3", sha256="b4578c2cb101ba091a10dc914e15ac968257f5db27ca78bc9fb5dbd70bce191f")
    version("2.0.2", sha256="2347bf804d19d515cb630a76b87e6dc6edcc1a828ff8c0f2a8a28e77794bad13")
    version("2.0.1", sha256="a3f1bef8cc413a689d429ac56f2bcc2e1d282d99797c3375233de792a7448ece")
    version("2.0.0", sha256="5850e251a4ad04fc924452f49183e5e12c38725832a568e57fa424a844b8a000")

    depends_on("cxx", type="build")  # generated

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")

    depends_on("netcdf-c")
    depends_on("blas")
    depends_on("lapack")

    def configure_args(self):
        spec = self.spec
        options = []
        options.append("--with-netcdf=%s" % spec["netcdf-c"].prefix)
        options.append("--with-blas=%s" % spec["blas"].libs.ld_flags)
        options.append("--with-lapack=%s" % spec["lapack"].libs.ld_flags)
        return options
