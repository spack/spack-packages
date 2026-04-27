# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import re

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Slurm(AutotoolsPackage):
    """Slurm is an open source, fault-tolerant, and highly scalable cluster
    management and job scheduling system for large and small Linux clusters.

    Slurm requires no kernel modifications for its operation and is relatively
    self-contained. As a cluster workload manager, Slurm has three key
    functions. First, it allocates exclusive and/or non-exclusive access to
    resources (compute nodes) to users for some duration of time so they can
    perform work. Second, it provides a framework for starting, executing,
    and monitoring work (normally a parallel job) on the set of allocated
    nodes. Finally, it arbitrates contention for resources by managing a
    queue of pending work.
    """

    homepage = "https://slurm.schedmd.com"
    url = "https://github.com/SchedMD/slurm/archive/slurm-21-08-8-2.tar.gz"

    maintainers("w8jcik")

    license("GPL-2.0-or-later")

    version("25-05-1-1", sha256="b568c761a6c9d72358addb3bb585456e73e80a02214ce375d2de8534f9ddb585")
    version("24-11-6-1", sha256="282708483326f381eb001a14852a1a82e65e18f37b62b7a5f4936c0ed443b600")
    version(
        "23-11-11-1", sha256="e9234e664ce30be206f73c0ff1a5f33e0ce32be35ece812eac930fcaa9da2c2f"
    )
    version("23-11-1-1", sha256="31506df24c6d24e0ea0329cac1395ab9b645bbde1518f5c469f7711df5e22c11")
    version("23-11-0-1", sha256="3780773a80b73ea2edb4353318b4220188f4eda92c31ab3a2bdd3a4fdec76be9")
    version("23-02-7-1", sha256="3f60ad5b5a492312d1febb9f9167caa3aee7f8438bb032590a993f5a65c5e4db")
    version("23-02-6-1", sha256="ed44d4e591c0f91874d535cb8c9ea67dd2a38bfa4e96fa6c71687293f6a1d3bb")
    version("23-02-5-1", sha256="4fee743a34514d8fe487080048256f5ee032374ed5f42d0eae342110dcd59edf")
    version("23-02-4-1", sha256="7290143a71ce2797d0df3423f08396fd5c0ae4504749ff372d6860b2d6a3a1b0")
    version("23-02-3-1", sha256="c41747e4484011cf376d6d4bc73b6c4696cdc0f7db4f64174f111bb9f53fb603")
    version("23-02-2-1", sha256="71edcf187a7d68176cca06143adf98e8f332d42cdf000cb534b03b13834ad537")
    version("23-02-1-1", sha256="d827553496ee9158bbf6a862b563cfd48566e6d815ad2f8349950fe6f04934da")
    version("22-05-9-1", sha256="c9aaa2362b5bf7a4745c8bf90e8dd2ca50802f1241dd1f5220aec8448c09b514")
    version("22-05-8-1", sha256="8c8f6a26a5d51e6c63773f2e02653eb724540ee8b360125c8d7732314ce737d6")
    version("22-05-7-1", sha256="2ad7e8a415d54d45977ab64b4e73c891154d2f41a04505fedf6f8d3df385acb1")
    version("21-08-8-2", sha256="876d7dfa716990d7e579cfb9c6ffc123258e03a1450e993ade596d2ee90afcdd")
    version("21-08-8-1", sha256="47d4dd2f391abcb856ecfddb51145c86ead89554f24efb586c59f0e38491ff36")
    version("20-11-9-1", sha256="98d36f3487e95af610db305a3ee1c1a7d370a3e1efef9fabee8b0edb98a6604b")

    variant("gtk", default=False, description="Enable GTK+ support")
    variant("mariadb", default=False, description="Use MariaDB instead of MySQL")

    variant("hwloc", default=False, description="Enable hwloc support")
    variant("hdf5", default=False, description="Enable hdf5 support")
    variant("readline", default=True, description="Enable readline support")
    variant("pmix", default=False, description="Enable PMIx support", when="@22-05:")
    variant(
        "sysconfdir",
        default="PREFIX/etc",
        values=any,
        description="Set system configuration path (possibly /etc/slurm)",
    )
    variant("restd", default=False, description="Enable the slurmrestd server")
    variant("nvml", default=False, description="Enable NVML autodetection")
    variant("cgroup", default=False, description="Enable cgroup plugin")
    variant("pam", default=False, description="Enable PAM support")
    variant("rsmi", default=False, description="Enable ROCm SMI support")
    variant(
        "multiple_slurmd",
        default=False,
        description="Enable support for multiple slurmd instances",
    )

    # TODO: add variant for BG/Q and Cray support

    # TODO: add variant for TLS (slurm@25-05:)

    # TODO: add variant for RRD (librrd) (slurm@23-02:)

    # TODO: add support for checkpoint/restart (BLCR)

    # TODO: add support for lua

    depends_on("c", type="build")  # generated

    depends_on("curl")
    depends_on("glib")
    depends_on("json-c")
    depends_on("lz4")
    depends_on("munge")
    depends_on("openssl")
    depends_on("pkgconfig", type="build")
    depends_on("readline", when="+readline")
    depends_on("zlib-api")

    depends_on("gtkplus", when="+gtk")
    depends_on("hdf5", when="+hdf5")
    depends_on("hwloc", when="+hwloc")
    depends_on("mariadb", when="+mariadb")

    depends_on("pmix@:5", when="+pmix")

    depends_on("http-parser", when="+restd")
    depends_on("libyaml", when="+restd")
    depends_on("libjwt", when="+restd")

    depends_on("cuda", when="+nvml")
    depends_on("dbus", when="+cgroup")
    depends_on("linux-pam", when="+pam")
    depends_on("rocm-smi-lib", when="+rsmi")

    executables = ["^srun$", "^salloc$"]

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str).rstrip()
        match = re.search(r"slurm(?:-wlm)?\s*([0-9.]+)", output)
        return match.group(1) if match else None

    def configure_args(self):
        spec = self.spec

        args = [
            "--with-libcurl={0}".format(spec["curl"].prefix),
            "--with-json={0}".format(spec["json-c"].prefix),
            "--with-lz4={0}".format(spec["lz4"].prefix),
            "--with-munge={0}".format(spec["munge"].prefix),
            "--with-ssl={0}".format(spec["openssl"].prefix),
            "--with-zlib={0}".format(spec["zlib-api"].prefix),
        ]

        if "~gtk" in spec:
            args.append("--disable-gtktest")

        if "~readline" in spec:
            args.append("--without-readline")

        if "+hdf5" in spec:
            args.append("--with-hdf5={0}".format(spec["hdf5"].prefix.bin.h5cc))
        else:
            args.append("--without-hdf5")

        if "+restd" in spec:
            args.append("--enable-slurmrestd")
            args.append("--with-http-parser={0}".format(spec["http-parser"].prefix))
            args.append("--with-jwt={0}".format(spec["libjwt"].prefix))
        else:
            args.append("--disable-slurmrestd")

        if "+hwloc" in spec:
            args.append("--with-hwloc={0}".format(spec["hwloc"].prefix))
        else:
            args.append("--without-hwloc")

        if "+pmix" in spec:
            args.append("--with-pmix={0}".format(spec["pmix"].prefix))
        else:
            args.append("--without-pmix")

        if spec.satisfies("+nvml"):
            args.append(f"--with-nvml={spec['cuda'].prefix}")

        if spec.satisfies("+pam"):
            args.append(f"--with-pam_dir={spec['linux-pam'].prefix}")

        if spec.satisfies("+rsmi"):
            args.append(f"--with-rsmi={spec['rocm-smi-lib'].prefix}")

        if spec.satisfies("+multiple_slurmd"):
            args.append("--enable-multiple-slurmd")

        sysconfdir = spec.variants["sysconfdir"].value
        if sysconfdir != "PREFIX/etc":
            args.append("--sysconfdir={0}".format(sysconfdir))

        return args

    def install(self, spec, prefix):
        make("install")
        make("-C", "contribs/pmi2", "install")
