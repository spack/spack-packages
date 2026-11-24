# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import fnmatch
import os

from spack_repo.builtin.build_systems.bundle import BundlePackage

from spack.package import *


class Lhapdfsets(BundlePackage):
    """A set of disretised data files of parton density functions ,
    to be used with the LHAPDF library"""

    homepage = "https://lhapdf.hepforge.org/pdfsets.html"

    tags = ["hep"]

    maintainers("vvolkl", "wdconinc")

    version("6.5.5")

    depends_on("lhapdf", type="build")
    depends_on("tar", type="build")
    depends_on("curl", type="build")

    phases = ["install"]

    # use a dummy executables for spack external support
    executables = [r"^lhapdf$"]

    variant(
        "sets",
        description=(
            "Individual lhapdf sets or patterns to install (all, default, or comma-separated list)"
        ),
        multi=True,
        default="default",
    )

    def available_sets(self):
        with open(join_path(os.path.dirname(__file__), "pdfsets.index")) as index:
            return [line.split()[1] for line in index]

    def resolve_sets(self, requested_sets):
        available_sets = self.available_sets()
        default_sets = ["MMHT2014lo68cl", "MMHT2014nlo68cl", "CT14lo", "CT14nlo"]
        resolved_sets = []
        seen_sets = set()

        for requested_set in requested_sets:
            if requested_set == "all":
                matches = available_sets
            elif requested_set == "default":
                matches = default_sets
            else:
                matches = [
                    available_set
                    for available_set in available_sets
                    if fnmatch.fnmatchcase(available_set, requested_set)
                ]

            for match in matches:
                if match not in seen_sets:
                    seen_sets.add(match)
                    resolved_sets.append(match)

        return resolved_sets

    def install(self, spec, prefix):
        mkdirp(self.prefix.share.lhapdfsets)
        tar = which("tar", required=True)
        curl = which("curl", required=True)
        sets = self.resolve_sets(self.spec.variants["sets"].value)

        with working_dir(self.prefix.share.lhapdfsets):
            for s in sets:
                _filename = "%s.tar.gz" % s
                curl(
                    "-L",
                    "-o",
                    _filename,
                    "http://lhapdfsets.web.cern.ch/lhapdfsets/current/%s" % _filename,
                )
                tar("xfz", _filename)
                os.remove(_filename)

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        env.set("LHAPDF_DATA_PATH", self.prefix.share.lhapdfsets)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("LHAPDF_DATA_PATH", self.prefix.share.lhapdfsets)

    @classmethod
    def determine_spec_details(cls, prefix, exes_in_prefix):
        path = os.environ.get("LHAPDF_DATA_PATH", None)
        if not path:
            return None
        # unfortunately the sets are not versioned -
        # just hardcode the current version and hope it is fine
        return Spec.from_detection("lhapdfsets@6.5.5", external_path=path)
