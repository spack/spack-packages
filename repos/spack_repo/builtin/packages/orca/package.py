# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import platform

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

_versions = {
    "avx2-6.1.1": {
        "Linux-x86_64": "5eaf676f9711a38835d609264321a30266b487b65477547802dedee982bc82d5"
    },
    "6.1.1": {
        "Linux-aarch64": "927c9f165ac6ec7547d543215a5d02c662c691c1659ba5bcd3d687817e8a6757",
        "Linux-x86_64": "a0bc1d6d2c3c00620367bbc5dbf2b3a7018abc92d1ff65f06cec46f75350b9be",
    },
    "avx2-6.0.1": {
        "Linux-x86_64": "f31f98256a0c6727b6ddfe50aa3ac64c45549981138d670a57e90114b4b9c9d2"
    },
    "6.0.1": {
        "Linux-aarch64": "0699cbccb6dbee66e14e69c4bb1300b35820b4222afdd7371e50aa23fe28be48",
        "Linux-x86_64": "5e9b49588375e0ce5bc32767127cc725f5425917804042cdecdfd5c6b965ef61",
    },
    "avx2-6.0.0": {
        "Linux-x86_64": "02c21294efe7b1b721e26cb90f98ee15ad682d02807201b7d217dfe67905a2fd"
    },
    "6.0.0": {"Linux-x86_64": "219bd1deb6d64a63cb72471926cb81665cbbcdec19f9c9549761be67d49a29c6"},
    "5.0.4": {"Linux-x86_64": "c4ea5aea60da7bcb18a6b7042609206fbeb2a765c6fa958c5689d450b588b036"},
    "5.0.3": {"Linux-x86_64": "b8b9076d1711150a6d6cb3eb30b18e2782fa847c5a86d8404b9339faef105043"},
    "4.2.1": {"Linux-x86_64": "a84b6d2706f0ddb2f3750951864502a5c49d081836b00164448b1d81c577f51a"},
    "4.2.0": {"Linux-x86_64": "01096466e41a5232e5a18af7400e48c02a6e489f0d5d668a90cdd2746e8e22e2"},
}


class Orca(Package):
    """An ab initio, DFT and semiempirical SCF-MO package

    Note: Orca is licensed software. You will need to create an account
    on the Orca homepage and download Orca yourself. Spack will search
    your current directory for the download file. Alternatively, add this
    file to a mirror so that Spack can find it. For instructions on how to
    set up a mirror, see https://spack.readthedocs.io/en/latest/mirrors.html"""

    homepage = "https://cec.mpg.de"
    maintainers("snehring")
    manual_download = True

    license("LGPL-2.1-or-later")

    for ver, packages in _versions.items():
        key = "{0}-{1}".format(platform.system(), platform.machine())
        sha_val = packages.get(key)
        if sha_val:
            version(ver, sha256=sha_val, deprecated=packages.get("deprecated", False))

    depends_on("libevent", type="run")
    depends_on("libpciaccess", type="run")

    # Map Orca version with the required OpenMPI version
    # OpenMPI@4.1.1 has issues in pmix environments, hence 4.1.2 here
    openmpi_versions = {
        "4.2.0": "3.1.4",
        "4.2.1": "3.1.4",
        "5.0.3": "4.1.2",
        "5.0.4": "4.1.2",
        "6.0.0": "4.1.6",
        "6.0.1": "4.1.6",
        "6.1.1": "4.1.8",
        "avx2-6.0.0": "4.1.6",
        "avx2-6.0.1": "4.1.6",
        "avx2-6.1.1": "4.1.8",
    }
    for orca_version, openmpi_version in openmpi_versions.items():
        depends_on(
            "openmpi@{0}".format(openmpi_version), type="run", when="@{0}".format(orca_version)
        )

    def url_for_version(self, version):
        openmpi_version = self.openmpi_versions[version.string].replace(".", "")
        if openmpi_version == "412":
            openmpi_version = "411"

        ver_parts = version.string.split("-")
        ver_underscored = ver_parts[-1].replace(".", "_")
        features = ver_parts[:-1]
        orca_arch = "linux_x86-64"
        if platform.system() == "Linux" and platform.machine() == "aarch64":
            orca_arch = "linux_arm64"
        feat = "_avx2" if "avx2" in features else ""
        url = f"file://{os.getcwd()}/orca_{ver_underscored}_{orca_arch}_shared_openmpi{openmpi_version}{feat}.tar.xz"

        if self.spec.satisfies("@=avx2-6.0.0"):
            url = f"file://{os.getcwd()}/orca_{ver_underscored}_{orca_arch}_avx2_shared_openmpi{openmpi_version}.tar.xz"

        return url

    def install(self, spec, prefix):
        mkdirp(prefix.bin)

        install_tree(".", prefix.bin)

        # Check "mpirun" usability when building against OpenMPI
        # with Slurm scheduler and add a "mpirun" wrapper that
        # calls "srun" if need be
        if "^openmpi ~legacylaunchers schedulers=slurm" in self.spec:
            mpirun_srun = join_path(os.path.dirname(__file__), "mpirun_srun.sh")
            install(mpirun_srun, prefix.bin.mpirun)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.bin)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["libevent"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["libpciaccess"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["openmpi"].prefix.lib)
