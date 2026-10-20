# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class BclConvert(Package):
    """Illumina standalone BCL Convert.

    BCL Convert converts the base call (BCL) files produced by Illumina
    sequencing instruments into FASTQ files (demultiplexing included).

    This is a proprietary, pre-built binary distributed by Illumina as an
    RPM. The RPM must be downloaded manually (Illumina licence/registration
    required) and placed in the directory from which ``spack install`` is run
    (or in the directory named by ``$BCL_CONVERT_RPM_DIR``).
    """

    homepage = "https://support.illumina.com/sequencing/sequencing_software/bcl-convert.html"

    manual_download = True

    # Directory holding the manually downloaded RPM: the current working
    # directory when spack is invoked (captured at import time, so it survives
    # Spack changing directory during the build), unless overridden by
    # $BCL_CONVERT_RPM_DIR.
    rpm_dir = os.environ.get("BCL_CONVERT_RPM_DIR", os.getcwd())

    # Pre-built x86_64 binary built for EL9 (glibc >= 2.34).
    requires(
        "platform=linux target=x86_64:",
        msg="bcl-convert is only distributed for x86_64 Linux",
    )

    # sha256 of bcl-convert-4.6.2-2.el9.x86_64.rpm
    version(
        "4.6.2",
        sha256="0444e13c86b7ffea5d155399fe6537e6a67546f5ca8dfabd8f273606c47e6550",
        expand=False,
    )

    # Runtime: binary links liblzma.so.5 (+ libc/libm), and dlopen()s libnuma
    # for NUMA-aware threading when available.
    depends_on("xz", type="run")
    depends_on("numactl", type="run")

    # Extract the payload of the RPM.
    depends_on("libarchive programs=bsdtar", type="build")

    def url_for_version(self, version):
        # The manually downloaded RPM is expected in rpm_dir (the directory
        # spack was run from, unless $BCL_CONVERT_RPM_DIR is set).
        return "file://{0}/bcl-convert-{1}-2.el9.x86_64.rpm".format(self.rpm_dir, version)

    @property
    def download_instr(self):
        return (
            "bcl-convert requires a manual download of the Illumina RPM.\n"
            "Download bcl-convert-{0}-2.el9.x86_64.rpm from\n  {1}\n"
            "and run `spack install` from the directory containing it (currently {2}),\n"
            "or set BCL_CONVERT_RPM_DIR to that directory."
        ).format(self.spec.version, self.homepage, self.rpm_dir)

    def install(self, spec, prefix):
        rpm = self.stage.archive_file
    
        bsdtar = Executable(
            join_path(spec["libarchive"].prefix.bin, "bsdtar")
        )
    
        with working_dir("rpm-extract", create=True):
            bsdtar("-xf", rpm)
    
            mkdirp(prefix.bin)
            install(
                join_path("usr", "bin", "bcl-convert"),
                prefix.bin,
            )
    
        set_executable(join_path(prefix.bin, "bcl-convert"))

    def setup_run_environment(self, env):
        # The vendor binary has no RPATH; make sure it can find liblzma/libnuma
        # from Spack rather than relying on the host.
        for dep in ("xz", "numactl"):
            for libdir in ("lib", "lib64"):
                path = join_path(self.spec[dep].prefix, libdir)
                if os.path.isdir(path):
                    env.prepend_path("LD_LIBRARY_PATH", path)

    def test_version(self):
        """check that bcl-convert runs and reports its version"""
        exe = which(self.prefix.bin.join("bcl-convert"))
        out = exe("--version", output=str, error=str)
        assert str(self.spec.version) in out
