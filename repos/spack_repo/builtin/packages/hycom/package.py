# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Hycom(MakefilePackage):
    """HYCOM (HYbrid Coordinate Ocean Model) is a primitive equation ocean
    general circulation model that evolved from the Miami Isopycnic-Coordinate
    Ocean Model (MICOM). It uses a hybrid vertical coordinate system combining
    isopycnal, sigma, and z-level coordinates for optimal ocean simulation.
    """

    homepage = "https://www.hycom.org"
    url = "https://github.com/HYCOM/HYCOM-src/archive/refs/tags/2.3.01.tar.gz"
    git = "https://github.com/HYCOM/HYCOM-src.git"

    maintainers("wjunlu")

    version("master", branch="master")
    version("2.3.01", sha256="0635e5f10d983f949da105dc32432b663dd6b0d43966086e9f5510df69ad9350")
    version("2.3.00", sha256="83037b093c2d613efa32471a424b447e201d25d058632a3802a3838760d1a094")

    variant("mpi", default=True, description="Enable MPI support")
    variant(
        "eos", default="sig2", description="Equation of state sigma type", values=("sig0", "sig2")
    )
    variant(
        "eos_term",
        default="17t",
        description="EOS number of terms",
        values=("7t", "9t", "12t", "17t"),
    )

    parallel = False

    depends_on("c", type="build")
    depends_on("fortran", type="build")
    depends_on("mpi", when="+mpi")
    depends_on("gmake", type="build")

    def _write_config(self):
        spec = self.spec
        if "+mpi" in spec:
            fc = spec["mpi"].mpifc
            build_type = "mpi"
            cppflags_extra = "-DMPI"
        else:
            fc = spack_fc
            build_type = "one"
            cppflags_extra = ""

        cc = spack_cc

        if spec.satisfies("%gcc"):
            fcfflags = "-fPIC -O2 -fdefault-real-8 -fdefault-double-8"
            if spec.satisfies("%gcc@10:"):
                fcfflags += " -fallow-argument-mismatch"
        elif spec.satisfies("%intel") or spec.satisfies("%oneapi"):
            fcfflags = "-O3 -fp-model precise -no-fma -r8 -warn nogeneral"
        elif spec.satisfies("%nvhpc") or spec.satisfies("%pgi"):
            fcfflags = "-O2 -Kieee -r8"
        else:
            fcfflags = "-O2"
        ccflags = "-O"

        cppflags = "-DREAL8 -DENDIAN_IO -DTIMER -DRELO {0} $(CPP_EXTRAS)".format(cppflags_extra)

        arch_name = "spack"
        config_content = (
            "FC            = {fc}\n"
            "FCFFLAGS      = {fcfflags}\n"
            "CC            = {cc}\n"
            "CCFLAGS       = {ccflags}\n"
            "CPP           = cpp -P\n"
            "CPPFLAGS      = {cppflags}\n"
            "LD            = $(FC)\n"
            "LDFLAGS       = $(FCFFLAGS)\n"
            "EXTRALIBS     =\n"
            "\n"
            "SHELL         = /bin/sh\n"
            "RM            = \\rm -f\n"
            "\n"
            ".c.o:\n"
            "\t$(CC) $(CPPFLAGS) $(CCFLAGS)  -c $*.c\n"
            "\n"
            ".F90.o:\n"
            "\t$(FC) $(CPPFLAGS) $(FCFFLAGS) -c $*.F90\n"
        ).format(fc=fc, fcfflags=fcfflags, cc=cc, ccflags=ccflags, cppflags=cppflags)

        config_path = join_path(
            self.stage.source_path, "config", "{0}_{1}".format(arch_name, build_type)
        )
        with open(config_path, "w") as f:
            f.write(config_content)

        return arch_name, build_type

    def _cpp_extras(self):
        spec = self.spec
        eos_sig = "-DEOS_SIG2" if spec.variants["eos"].value == "sig2" else "-DEOS_SIG0"
        eos_term_map = {"7t": "-DEOS_7T", "9t": "-DEOS_9T", "12t": "-DEOS_12T", "17t": "-DEOS_17T"}
        eos_term = eos_term_map[spec.variants["eos_term"].value]
        return "{0} {1} -DMASSLESS_1MM".format(eos_sig, eos_term)

    def edit(self, spec, prefix):
        self._arch_name, self._build_type = self._write_config()

    @property
    def build_targets(self):
        return [
            "hycom",
            "ARCH={0}".format(self._arch_name),
            "TYPE={0}".format(self._build_type),
            "CPP_EXTRAS={0}".format(self._cpp_extras()),
        ]

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("hycom", prefix.bin)
        mkdirp(prefix.share)
        install("dimensions.h", prefix.share)
