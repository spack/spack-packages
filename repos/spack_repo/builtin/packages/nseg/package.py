# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Nseg(MakefilePackage):
    """NSEG - Low complexity sequence identification"""

    homepage = "ftp://ftp.ncbi.nih.gov/pub/seg/nseg/"
    url = "ftp://ftp.ncbi.nih.gov/pub/seg/nseg/nseg.c"

    version(
        "1.0",
        sha256="afae364fbe51caa1eccb704ed0b954437a3ef48a0cd3bf473f4b61d6fde9617e",
        expand=False,
    )

    source_files = ["makefile", "genwin.c", "genwin.h", "lnfac.h", "nmerge.c", "runnseg"]
    resource(
        name=source_files[0],
        url="ftp://ftp.ncbi.nih.gov/pub/seg/nseg/makefile",
        sha256="32937aef6969550ca3c762b5dd61b1520635cc46e773e35e56c5718f75838cee",
        expand=False,
        placement=source_files[0],
    )

    resource(
        name=source_files[1],
        url="ftp://ftp.ncbi.nih.gov/pub/seg/nseg/genwin.c",
        sha256="d392d2db625dc8c90b00f2a86028a3a45d121e15eb403b51c2f9b01692ab10d9",
        expand=False,
        placement=source_files[1],
    )

    resource(
        name=source_files[2],
        url="ftp://ftp.ncbi.nih.gov/pub/seg/nseg/genwin.h",
        sha256="1c701d87bf6200bfa40faa16fe665828a010727ef1aa0e8a1e5823605165fb86",
        expand=False,
        placement=source_files[2],
    )

    resource(
        name=source_files[3],
        url="ftp://ftp.ncbi.nih.gov/pub/seg/nseg/lnfac.h",
        sha256="5048e4f3dc3a7ea420d4eb4912a661f285634fbb205411b647b1f00c3fe3a0d2",
        expand=False,
        placement=source_files[3],
    )

    resource(
        name=source_files[4],
        url="ftp://ftp.ncbi.nih.gov/pub/seg/nseg/nmerge.c",
        sha256="c8a4bb4c960acf7fcd7509b635766b618efdab9f09aec36443040759eca3bce3",
        expand=False,
        placement=source_files[4],
    )

    resource(
        name=source_files[5],
        url="ftp://ftp.ncbi.nih.gov/pub/seg/nseg/runnseg",
        sha256="2830a5a1c5ea1a879cf3a415dfbb23db7a81e84d41698ddf765f2e1ef42e7c78",
        expand=False,
        placement=source_files[5],
    )

    build_directory = "nseg"

    @run_before("build")
    def prepare_source(self):
        # create the build dir
        mkdirp(self.build_directory)

        # move the primary source file in
        copy("nseg.c", join_path(self.build_directory, "nseg.c"))

        # move all of the single-file resources into the build dir
        for source in self.source_files:
            src = "{0}/{1}/{2}".format(self.stage.source_path, source, source)
            dest = "{0}/{1}".format(self.build_directory, source)
            copy(src, dest)

        if self.spec.satisfies("%fj"):
            sfiles = ["genwin.c", "nseg.c"]
            for s_name in sfiles:
                filter_file(
                    "return;", "return 0;", join_path(self.build_directory, s_name), string=True
                )

    def install(self, spec, prefix):
        with working_dir(self.build_directory):
            mkdirp(prefix.bin)
            install("nseg", prefix.bin)
            install("nmerge", prefix.bin)
