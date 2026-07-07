# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
#
# Important feature: a set of salome-xxx packages must have all the same version
# - except salome-med that is also fixed but by another number version

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class SalomeConfiguration(Package):
    """salome-configuration is a part of SALOME platform and define general
    build tools for the platform."""

    maintainers("franciskloss")

    homepage = "https://www.salome-platform.org"
    git = "https://github.com/SalomePlatform/configuration.git"

    version("9.15.0", sha256="01dd367a167383fbc03ca8de47e127c87f4a9d4c826c68768ac3a2bfd5f998f7")
    version("9.14.0", sha256="9ff6cacfc272ef75211dee555b67acc50ec9dee1862676d429c24c13a60c6052")
    version("9.13.0", sha256="b0bb296536cefb3b5e063a57fab8b66b510ff76d766fbd462ee10dedac3c4872")
    version("9.12.0", sha256="81841371edfcf03a5099900f4205a37c56bfd9390f88dd9024e966bfb2e20f86")
    version("9.11.0", sha256="a72f2cc828fbe769f0376cdbc60ee4c3573b4f9ceec5906ffe6bb7f010d08ee7")

    def url_for_version(self, version):
        url = "https://github.com/SalomePlatform/configuration/archive/refs/tags/V{0}.tar.gz"
        return url.format(version.underscored)

    patch("SalomeMacros.patch", working_dir="./cmake")
    patch("FindSalomeHDF5.patch", working_dir="./cmake", when="@:9.7.0")

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        env.set("CONFIGURATION_ROOT_DIR", self.prefix)

    def install(self, spec, prefix):
        install_tree(".", prefix)
