# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from typing import Optional

from spack_repo.builtin.build_systems.bundle import BundlePackage

from spack.package import *
from spack.package import ClassProperty, PackageBase, classproperty, install_tree, mkdirp


def _url(cls: "Geant4DataPackage") -> Optional[str]:
    if cls.g4dirname:
        return f"{cls.datasets_url}/{cls.g4dirname}.1.0.tar.gz"
    return None


class Geant4DataPackage(PackageBase):
    """Base class to be used by each dependency in Geant4Data"""

    #: URL to parent directory for dataset downloads
    datasets_url = "https://geant4-data.web.cern.ch/geant4-data/datasets"
    url: ClassProperty[Optional[str]] = classproperty(_url)

    #: Directory name inside 'share' (e.g., G4EMLOW) before version is appended
    g4dirname: Optional[str] = None

    #: G4-prefixed environment variable (e.g., G4LEDATA)
    g4envvar: Optional[str] = None

    @property
    def datadir(self):
        """Data directory at :file:`share/data/{g4dirname}{version}`"""
        s = self.spec
        self._ensure_g4dirname_is_set_or_raise()
        return join_path(s.prefix.share, "data", f"{self.g4dirname}{s.version}")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        self._ensure_g4envvar_is_set_or_raise()
        env.set(self.g4envvar, self.datadir)

    def install(self, spec, prefix):
        """Install by copying to the data prefix."""
        datadir = self.datadir
        mkdirp(datadir)
        install_tree(self.stage.source_path, datadir)

    def _ensure_g4dirname_is_set_or_raise(self):
        self.validate_or_raise_attr("g4dirname")

    def _ensure_g4envvar_is_set_or_raise(self):
        self.validate_or_raise_attr("g4envvar")

    def url_for_version(self, version):
        """Default version string.

        This override of ``url`` is necessary for most of the G4 packages, since
        ``data/G4FOO.1.2.3.tar.gz`` is parsed as version ``4FOO.1.2.3``.

        This method is overridden by some subclasses.
        """
        return f"{self.datasets_url}/{self.g4dirname}.{version}.tar.gz"

    def validate_or_raise_attr(self, attr):
        if getattr(self, attr) is None:
            cls = type(self)
            raise AttributeError(f"{cls.__name__} must define a `{attr}` attribute [none defined]")


class Geant4Data(BundlePackage):
    """A bundle package to hold Geant4 data packages"""

    homepage = "http://geant4.cern.ch"

    maintainers("drbenmorgan")

    tags = ["hep"]

    version("11.4.0")
    version("11.3.0")
    version("11.2.2")
    version("11.2.0")
    version("11.1.0")
    version("11.0.0")
    version("10.7.4")
    version("10.7.3")
    version("10.7.2")
    version("10.7.1")
    version("10.7.0")
    version("10.6.3")
    version("10.6.2")
    version("10.6.1")
    version("10.6.0")
    version("10.5.1")
    version("10.4.3")
    version("10.4.0")
    version("10.3.3")
    version("10.0.4")

    variant("tendl", default=True, when="@10.3:", description="Enable G4TENDL")
    variant("nudexlib", default=True, when="@11.3:", description="Enable G4NUDEXLIB")
    variant("urrpt", default=True, when="@11.3:", description="Enable G4URRPT")

    # Add install phase so we can create the data "view"
    phases = ["install"]

    # Declare deps per dataset package, mapping each dataset version (see
    # other packager recipes) to the Geant4 version range that uses it.
    # - When adding a new version of Geant4, you should only need to update the topmost line
    #   of each dataset (if at all): constrain its version and add a new version.
    # - Dataset ordering is based on cmake/Modules/G4DatasetDefinitions.cmake
    # - Because datasets do not use patch verisons `.0`, and G4 dataset lookup expects exactly
    #   matching versions, we *always* use `@={dataset}` for the dependencies.
    _datasets = {
        "g4ndl": {
            "4.7.1": "11.2.2:",
            "4.7": "11.1:11.2.1",
            "4.6": "10.6:11.0",
            "4.5": "10.3:10.5",
            "4.4": "10.0",
        },
        "g4emlow": {
            "8.8": "11.4:",
            "8.6.1": "11.3",
            "8.5": "11.2",
            "8.2": "11.1",
            "8.0": "11.0",
            "7.13": "10.7",
            "7.9.1": "10.6",
            "7.7": "10.5",
            "7.3": "10.4",
            "6.50": "10.3",
            "6.35": "10.0",
        },
        "g4photonevaporation": {
            "6.1.2": "11.4:",
            "6.1": "11.3",
            "5.7": "10.7:11.2",
            "5.5": "10.6",
            "5.3": "10.5",
            "5.2": "10.4",
            "4.3.2": "10.3.1:10.3",
            "3.0": "10.0",
        },
        "g4radioactivedecay": {
            "6.1.2": "11.3:",
            "5.6": "10.7:11.2",
            "5.4": "10.6",
            "5.3": "10.5",
            "5.2": "10.4",
            "5.1.1": "10.3.1:10.3",
            "4.0": "10.0.4",
        },
        "g4particlexs": {
            "4.2": "11.4:",
            "4.1": "11.3",
            "4.0": "11.0:11.2",
            "3.1.1": "10.7.1:10.7",
            "3.1": "10.7.0",
            "2.1": "10.6",
            "1.1": "10.5",
        },
        "g4neutronxs": {
            # Replaced by g4particlexs in G4@10.5
            "1.4": "10.0:10.4",
        },
        "g4pii": {
            "1.3": "10:",
        },
        "g4realsurface": {
            "2.2": "10.7:",
            "2.1.1": "10.4.2:10.6",
            "2.1": "10.4.0:10.4.1",
            "1.0": "10.0.4:10.3",
        },
        "g4saiddata": {
            "2.0": "10.5:",
            "1.1": "10.0.4:10.4",
        },
        "g4abla": {
            "3.3": "11.2:",
            "3.1": "10.4:11.1",
            "3.0": "10.0.4:10.3",
        },
        "g4incl": {
            "1.3": "11.4:",
            "1.2": "11.2.0:11.3",
            "1.0": "10.5:11.1",
        },
        "g4ensdfstate": {
            "3.0": "11.3:",
            "2.3": "10.7:11.2",
            "2.2": "10.4:10.6",
            "2.1": "10.3",
            "1.0": "10.0.4",
        },
        "g4channeling": {
            "2.0": "11.4:",
            "1.0": "11.3",
        },
    }

    # Optional datasets with independent variants
    _optional_datasets = {
        "g4tendl": {
            "1.4": "11.0:",
            "1.3.2": "10.4:10.7",
            "1.3": "10.3",
        },
        "g4nudexlib": {
            "1.0": "11.3:",
        },
        "g4urrpt": {
            "1.1": "11.3:",
        },
    }

    for _pkg, _vers_map in _datasets.items():
        for _dset_vers, _g4_vers in _vers_map.items():
            depends_on(f"{_pkg}@={_dset_vers}", type=("build", "run"), when=f"@{_g4_vers}")

    for _pkg, _vers_map in _optional_datasets.items():
        _variant = _pkg.replace("g4", "")
        for _dset_vers, _g4_vers in _vers_map.items():
            depends_on(
                f"{_pkg}@={_dset_vers}", type=("build", "run"), when=f"@{_g4_vers} +{_variant}"
            )

    @property
    def datadir(self):
        spec = self.spec
        return join_path(spec.prefix.share, "{0}-{1}".format(self.name, self.version.dotted))

    def install(self, spec, prefix):
        with working_dir(self.datadir, create=True):
            for s in spec.dependencies():
                if not isinstance(s.package, Geant4DataPackage):
                    if s.name.startswith("g4"):
                        raise InstallError(
                            f"Data dependency `{s.name}` must be a Geant4DataPackage"
                        )
                    continue

                d = s.package.datadir
                symlink(d, os.path.basename(d))
