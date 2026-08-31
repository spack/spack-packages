# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Tpp(MakefilePackage):
    """Tools for MS data representation, MS data visualization, peptide identification
    and validation, protein identification, quantification, and annotation, data storage
    and mining, and biological inference."""

    homepage = "http://tools.proteomecenter.org/wiki/software_tpp.html"
    svn = "https://svn.code.sf.net/p/sashimi/code/trunk"

    license("GPL-2.0-or-later AND LGPL-2.1-or-later")

    maintainers("w8jcik")

    version(
        "7.3.0",
        sha256="625744b0ccf29dd8cb34f9082da85d910133c4f303a64ea05f56da719283f2fe",
        url="https://sourceforge.net/projects/sashimi/files/Trans-Proteomic%20Pipeline%20%28TPP%29/TPP%20v7.3%20%28Trade%20Wind%29%20rev%200/TPP_7.3.0-src.tgz/download",
    )

    version("6.3.3", svn="https://svn.code.sf.net/p/sashimi/code/tags/release_6-3-3")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("argtable", when="@7:")
    depends_on("libarchive")
    depends_on("zlib", when="@6.3.3:")

    with default_args(type=("build", "run")):
        depends_on("perl@5.10:")

        depends_on("perl-cgi")
        depends_on("perl-xml-parser")
        depends_on("perl-xml-twig")
        depends_on("perl-findbin-libs")
        depends_on("perl-json")
        depends_on("perl-tie-ixhash")
        depends_on("perl-statistics-regression")
        depends_on("perl-statistics-r")

    conflicts("%gcc@15:", msg="Hardklor fails to build with GCC 15")
    conflicts("@7.0 %gcc@14:", msg="HDF5 from TPP 7.0 fails to build with GCC 14")
    conflicts("@:6 %gcc@12:", msg="ProteoWizard from TPP 6 fails to build with GCC 12")

    def edit(self, spec, prefix):
        with open("site.mk", "w", encoding="utf-8") as file:
            file.write(f'INSTALL_DIR = "{prefix}"\n')

        filter_file(
            "cd $(EXPAT_SRC); ./configure",
            "cd $(EXPAT_SRC); CC=$(C) CXX=$(CC) ./configure",
            "extern/Makefile",
            string=True,
        )

        filter_file(
            "cd $(FANN_SRC); ./configure",
            "cd $(FANN_SRC); CC=$(C) CXX=$(CC) ./configure",
            "extern/Makefile",
            string=True,
        )

        filter_file(
            "cd $(GSL_SRC); ./configure",
            "cd $(GSL_SRC); CC=$(C) CXX=$(CC) ./configure",
            "extern/Makefile",
            string=True,
        )

        filter_file(
            "cd $(HDF5_SRC); ./configure",
            "cd $(HDF5_SRC); CC=$(C) CXX=$(CC) ./configure",
            "extern/Makefile",
            string=True,
        )

        filter_file(
            "cd $(LIBARCHIVE_SRC); ./configure",
            "cd $(LIBARCHIVE_SRC); CC=$(C) CXX=$(CC) ./configure",
            "extern/Makefile",
            string=True,
        )

        filter_file(
            "cd $(LIBGD_SRC); ./configure",
            "cd $(LIBGD_SRC); CC=$(C) CXX=$(CC) ./configure",
            "extern/Makefile",
            string=True,
        )

        filter_file(
            "cd $(LIBPNG_SRC); ./configure",
            "cd $(LIBPNG_SRC); CC=$(C) CXX=$(CC) ./configure",
            "extern/Makefile",
            string=True,
        )

        if spec.satisfies("@6.3.3:"):
            # Prevent MSToolkit from building zlib

            filter_file(r"^ZLIB\s*=.*$", "ZLIB = ", "extern/MSToolkit/Makefile")

            # Point Hardklor to external zlib

            filter_file(
                "LIBS = $(BUILD_LIB)/libmstoolkitlite.a",
                f"LIBS = $(BUILD_LIB)/libmstoolkitlite.a {self.spec['zlib'].libs.link_flags}",
                "extern/Hardklor/Makefile",
                string=True,
            )

            # Link against external zlib

            if spec.satisfies("@7:"):
                filter_file(
                    "LIBS := -lmstoolkitlite -lhardklor -lpepxml -lmzimltools ",
                    f"LIBS := -lmstoolkitlite -lhardklor -lpepxml -lmzimltools {self.spec['zlib'].libs.link_flags} ",  # noqa: E501
                    "extern/kojak/kojak-2.1.0/Makefile",
                    string=True,
                )

            if spec.satisfies("@7.0"):
                filter_file(
                    "LIBS := -lmstoolkitlite -lhardklor -lpepxml -lmzimltools ",
                    f"LIBS := -lmstoolkitlite -lhardklor -lpepxml -lmzimltools {self.spec['zlib'].libs.link_flags} ",  # noqa: E501
                    "extern/magnum/magnum-Official_1.3.2/Makefile",
                    string=True,
                )

            if spec.satisfies("@7.1:"):
                filter_file(
                    "LIBS := -lmstoolkitlite -lhardklor -lpepxml -lmzimltools ",
                    f"LIBS := -lmstoolkitlite -lhardklor -lpepxml -lmzimltools {self.spec['zlib'].libs.link_flags} ",  # noqa: E501
                    "extern/magnum/mhoopmann-magnum-948173b/Makefile",
                    string=True,
                )

        # Fixes for ProteoWizard

        if self.spec.satisfies("@:7.0 %gcc@13:"):
            for path in [
                "extern/ProteoWizard/pwiz-src/pwiz/data/msdata/BinaryDataEncoder.hpp",
                "extern/ProteoWizard/pwiz-src/pwiz/data/msdata/MSData.hpp",
                "extern/ProteoWizard/pwiz-src/pwiz/utility/misc/BinaryData.hpp",
                "src/Quantitation/StPeter/StPeter2Matrix/CProteinMasterList.h",
            ]:
                filter_file(
                    "#include <vector>", "#include <vector>\n#include <cstdint>", path, string=True
                )

            filter_file(
                "#define _CSTPETERMATRIX_H",
                "#define _CSTPETERMATRIX_H\n#include <cstdint>",
                "src/Quantitation/StPeter/StPeter2Matrix/CStPeterMatrix.h",
                string=True,
            )

        # Fixes for Kojak

        if self.spec.satisfies("@7: %gcc@13:"):
            filter_file(
                '#include "KLog.h"',
                '#include "KLog.h"\n#include <cstdint>',
                "extern/kojak/kojak-2.1.0/KLog.cpp",
                string=True,
            )

        # Fixes for Magnum

        if self.spec.satisfies("@7.1:7.2 %gcc@13:"):
            filter_file(
                '#include "MDB.h"',
                '#include "MDB.h"\n#include <cstdint>',
                "extern/magnum/mhoopmann-magnum-948173b/MDB.cpp",
                string=True,
            )

            filter_file(
                '#include "MLog.h"',
                '#include "MLog.h"\n#include <cstdint>',
                "extern/magnum/mhoopmann-magnum-948173b/MLog.cpp",
                string=True,
            )

            filter_file(
                "#include <vector>",
                "#include <vector>\n#include <cstdint>",
                "extern/magnum/mhoopmann-magnum-948173b/MStructs.h",
                string=True,
            )

        if self.spec.satisfies("@7.0 %gcc@13:"):
            filter_file(
                '#include "MDB.h"',
                '#include "MDB.h"\n#include <cstdint>',
                "extern/magnum/magnum-Official_1.3.2/MDB.cpp",
                string=True,
            )

            filter_file(
                '#include "MLog.h"',
                '#include "MLog.h"\n#include <cstdint>',
                "extern/magnum/magnum-Official_1.3.2/MLog.cpp",
                string=True,
            )

            filter_file(
                "#include <vector>",
                "#include <vector>\n#include <cstdint>",
                "extern/magnum/magnum-Official_1.3.2/MStructs.h",
                string=True,
            )

        # Fixes for TPP

        if self.spec.satisfies("@7.1:7.2 %gcc@13:"):
            filter_file(
                '#include "CProteinMasterList.h"',
                '#include "CProteinMasterList.h"\n#include <cstdint>',
                "src/Quantitation/StPeter/StPeter2Matrix/CProteinMasterList.cpp",
                string=True,
            )

            filter_file(
                '#include "CStPeterMatrix.h"',
                '#include "CStPeterMatrix.h"\n#include <cstdint>',
                "src/Quantitation/StPeter/StPeter2Matrix/CStPeterMatrix.cpp",
                string=True,
            )

        if self.spec.satisfies("@7.1:7.2 %gcc@12:"):
            filter_file(
                "unzip -d $(COMET_SRC) $(COMET_ZIP);",
                "unzip -d $(COMET_SRC) $(COMET_ZIP); sed $(SED_OPT) 's/ -fconcepts//g' $(COMET_SRC)/CometSearch/Makefile",  # noqa: E501
                "extern/Makefile",
                string=True,
            )

    def build(self, spec, prefix):
        make_flags = []

        if spec.satisfies("@6.3.3:"):
            make_flags.append(f"ZLIB_LDFLAGS={self.spec['zlib'].libs.link_flags}")

        libarchive_ldflags = [self.spec["libarchive"].libs.link_flags]

        if self.spec.satisfies("^libarchive compression=bz2lib"):
            libarchive_ldflags.append("-lbz2")

        if self.spec.satisfies("^libarchive compression=lz4"):
            libarchive_ldflags.append("-llz4")

        if self.spec.satisfies("^libarchive compression=lzo2"):
            libarchive_ldflags.append("-llzo2")

        if self.spec.satisfies("^libarchive compression=lzma"):
            libarchive_ldflags.append("-llzma")

        if self.spec.satisfies("^libarchive compression=zlib"):
            libarchive_ldflags.append("-lz")

        if self.spec.satisfies("^libarchive compression=zstd"):
            libarchive_ldflags.append("-lzstd")

        if self.spec.satisfies("^libarchive+iconv"):
            libarchive_ldflags.extend(["-liconv", "-lcharset"])

        make_flags.append(f"LIBARCHIVE_LDFLAGS={' '.join(libarchive_ldflags)}")

        make("boost", *make_flags)  # otherwise pwiz fails
        make("comet", *make_flags, parallel=False)
        make("expat", *make_flags, parallel=False)
        make("fann", *make_flags, parallel=False)
        make("gsl", *make_flags, parallel=False)
        make("hdf5", *make_flags, parallel=False)
        make("libgd", *make_flags, parallel=False)
        make("pwiz", *make_flags)

        make("extern", *make_flags)
        make("params", *make_flags, parallel=False)  # race condition with tandem
        make("all", *make_flags)

    def install(self, spec, prefix):
        make("install", parallel=False)
