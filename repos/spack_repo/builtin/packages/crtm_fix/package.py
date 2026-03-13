# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class CrtmFix(Package):
    """CRTM coefficient files"""

    homepage = "https://github.com/NOAA-EMC/crtm"
    url = "ftp://ftp.ssec.wisc.edu/pub/s4/CRTM/fix_REL-2.4.0_emc.tgz"

    maintainers(
        "BenjaminTJohnson", "edwardhartnett", "AlexanderRichert-NOAA", "Hang-Lei-NOAA", "climbfuji"
    )

    version("3.1.2.0", sha256="4cfcba3030f13799c7543a9322669e3963038abf95f3eb5117bd909dea63fb4b")
    version("3.1.1.3", sha256="a69778ff6bec7a1b7a76b79dbc94f442c1ed51fca1c4014464aada2730e63ca7")
    version("3.1.1.2", sha256="c2e289f690d82a3aa82d2239cbb567cd514fa0f476a8b498ceba11670685ca66")
    version(
        "2.4.0.1_emc", sha256="6e4005b780435c8e280d6bfa23808d8f12609dfd72f77717d046d4795cac0457"
    )
    version("2.4.0_emc", sha256="d0f1b2ae2905457f4c3731746892aaa8f6b84ee0691f6228dfbe48917df1e85e")

    # All of these are legacy settings. Linking files from subdirectories
    # to the top-level directory will be removed in the near future
    variant("link-big-endian", default=True, description="Link big endian fix files to top-level 'fix' dir")
    variant("link-little-endian", default=False, description="Link little endian fix files to top-level 'fix' dir")
    variant("link-netcdf", default=True, description="Link netcdf fix files to top-level 'fix' dir")
    variant("link-testfiles", default=False, description="Link test files to top-level 'fix' dir", when="@3:")

    conflicts("+link-big-endian", when="+link-little-endian", msg="Cannot link both litte endian and big endian fix files to top-level 'fix' dir")

    def url_for_version(self, version):
        if version == Version("2.4.0.1_emc"):
            url = "ftp://ftp.ssec.wisc.edu/pub/s4/CRTM/fix_REL-2.4.0_emc_07112023.tgz"
        else:
            url = f"ftp://ftp.ssec.wisc.edu/pub/s4/CRTM/fix_REL-{version}.tgz"
        return url

    def install(self, spec, prefix):
        spec = self.spec
        if spec.version in [Version("2.4.0.1_emc")]:
            fix_source_dir = self.stage.source_path
        else:
            fix_source_dir = join_path(self.stage.source_path, "fix")
        install_tree(fix_source_dir, self.prefix.fix)

        # Everything below is legacy code that will be deprecated (removed)
        # by the end of 2026: symlink certain versions of files to the
        # top-level "fix" directory in the install prefix.
        endian_dirs = []
        if spec.satisfies("+link-big-endian"):
            endian_dirs.append("Big_Endian")
        elif spec.satisfies("+link-little-endian"):
            endian_dirs.append("Little_Endian")

        if spec.satisfies("+link-netcdf"):
            endian_dirs.extend(["netcdf", "netCDF"])

        with working_dir(self.prefix.fix):
            fix_files = []
            for d in endian_dirs:
                fix_files = fix_files + find(".", "*/{}/*".format(d), recursive=False)
                fix_files = fix_files + find(".", "*/*/{}/*".format(d), recursive=False)
                fix_files = fix_files + find(".", "*/*/*/{}/*".format(d), recursive=False)
            if self.spec.satisfies("~link-testfiles"):
                fix_files = [f for f in fix_files if "test_data/" not in f]
            fix_files = [f for f in fix_files if os.path.isfile(f)]

            # Big_Endian amsua_metop-c.SpcCoeff.bin is incorrect
            # Little_Endian amsua_metop-c_v2.SpcCoeff.bin is what it's supposed to be.
            # Link the incorrect file as noACC (DH 2026/02/19 why???),
            # then link the correct file under the original name.
            amc_sc_bad_target = None
            if "+link-big-endian" in spec and (
                spec.version in [Version("2.4.0_emc"), Version("2.4.0.1_emc")]
            ):
                amc_sc_bad_target = join_path(
                    "SpcCoeff", "Big_Endian", "amsua_metop-c.SpcCoeff.bin"
                )
                amc_sc_good_target = join_path(
                    "SpcCoeff", "Little_Endian", "amsua_metop-c_v2.SpcCoeff.bin"
                )
                amc_sc_bad_link = "amsua_metop-c.SpcCoeff.noACC.bin"
                amc_sc_good_link = "amsua_metop-c.SpcCoeff.bin"

            for f in fix_files:
                target = f.replace(self.prefix.fix, "").lstrip("/")
                link = os.path.split(f)[1]
                if amc_sc_bad_target and amc_sc_bad_target==target:
                    symlink(amc_sc_bad_target, amc_sc_bad_link)
                    symlink(amc_sc_good_target, amc_sc_good_link)
                else:
                    # https://github.com/JCSDA/spack-stack/issues/1910#issuecomment-3930004524
                    if os.path.islink(link):
                        os.remove(link)
                    symlink(target, link)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("CRTM_FIX", self.prefix.fix)
