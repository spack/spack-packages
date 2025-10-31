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

    source_files = [
        ("makefile", "32937aef6969550ca3c762b5dd61b1520635cc46e773e35e56c5718f75838cee"),
        ("genwin.c", "d392d2db625dc8c90b00f2a86028a3a45d121e15eb403b51c2f9b01692ab10d9"),
        ("genwin.h", "1c701d87bf6200bfa40faa16fe665828a010727ef1aa0e8a1e5823605165fb86"),
        ("lnfac.h", "5048e4f3dc3a7ea420d4eb4912a661f285634fbb205411b647b1f00c3fe3a0d2"),
        ("nmerge.c", "c8a4bb4c960acf7fcd7509b635766b618efdab9f09aec36443040759eca3bce3"),
        ("runnseg", "2830a5a1c5ea1a879cf3a415dfbb23db7a81e84d41698ddf765f2e1ef42e7c78"),
    ]

    for source, sha256 in source_files:
        resource(
            name=source,
            url=f"ftp://ftp.ncbi.nih.gov/pub/seg/nseg/{source}",
            sha256=sha256,
            expand=False,
            placement=source,
        )

    build_directory = "nseg"

    @run_before("build")
    def prepare_source(self):
        # create the build dir
        mkdirp(self.build_directory)

        # move the primary source file in
        copy("nseg.c", join_path(self.build_directory, "nseg.c"))

        # move all of the single-file resources into the build dir
        for source, _ in self.source_files:
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
