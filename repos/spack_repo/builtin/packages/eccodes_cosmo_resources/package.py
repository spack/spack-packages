# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class EccodesCosmoResources(Package):
    """To simplify the usage of the GRIB 2 format within the COSMO Consortium,
    a COSMO GRIB 2 Policy has been defined. One element of this policy is to
    define a unified ecCodes system for the COSMO community, which is compatible
    with all COSMO software. This unified system is split into two parts,
    the vendor distribution of the ecCodes, available from ECMWF and the modified
    samples and definitions used by the COSMO consortium, available in the
    current repository."""

    homepage = "https://github.com/COSMO-ORG/eccodes-cosmo-resources.git"
    url = "https://github.com/COSMO-ORG/eccodes-cosmo-resources/archive/refs/tags/v2.36.0.3.tar.gz"
    git = "https://github.com/COSMO-ORG/eccodes-cosmo-resources.git"

    maintainers("huppd", "lxavier", "victoria-cherkas")

    version("2.36.0.3", tag="v2.36.0.3")
    version("2.25.0.3", tag="v2.25.0.3")
    version("2.25.0.2", tag="v2.25.0.2")
    version("2.25.0.1", tag="v2.25.0.1")
    version("2.18.0.1", tag="v2.18.0.1")

    depends_on("eccodes")
    depends_on("eccodes@2.36.4", type=("build", "link", "run"), when="@2.36.0.3")
    depends_on("eccodes@2.25.0", type=("build", "link", "run"), when="@2.25.0.1:2.25.0.3")
    depends_on("eccodes@2.18.0", type=("build", "link", "run"), when="@2.18.0.1")

    def setup_run_environment(self, env):
        eccodes_definition_path = ":".join(
            [
                self.prefix + "/cosmoDefinitions/definitions/",
                self.spec["eccodes"].prefix + "/share/eccodes/definitions/",
            ]
        )
        env.prepend_path("GRIB_DEFINITION_PATH", eccodes_definition_path)
        env.prepend_path("ECCODES_DEFINITION_PATH", eccodes_definition_path)

        eccodes_samples_path = self.prefix + "/cosmoDefinitions/samples/"
        env.prepend_path("GRIB_SAMPLES_PATH", eccodes_samples_path)
        env.prepend_path("ECCODES_SAMPLES_PATH", eccodes_samples_path)

    def setup_dependent_build_environment(self, env, dependent_spec):
        self.setup_run_environment(env)

    def install(self, spec, prefix):
        mkdir(prefix.cosmoDefinitions)
        mkdir(prefix.cosmoDefinitions + "/definitions")
        mkdir(prefix.cosmoDefinitions + "/samples")
        install_tree("definitions", prefix.cosmoDefinitions + "/definitions")
        install_tree("samples", prefix.cosmoDefinitions + "/samples")
        install("RELEASE", prefix.cosmoDefinitions)
