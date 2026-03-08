# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTroveClassifiers(PythonPackage):
    """The trove-classifiers pacakge is the canonical source for classifiers
    on PyPI. Classifiers categorize projects per PEP 301."""

    homepage = "https://github.com/pypa/trove-classifiers"
    pypi = "trove_classifiers/trove_classifiers-2024.5.17.tar.gz"

    license("Apache-2.0")

    version("2026.1.14.14", sha256="00492545a1402b09d4858605ba190ea33243d361e2b01c9c296ce06b5c3325f3")  # FIXME
    version("2026.1.12.15", sha256="832a7e89ccc43b64b89f8f9d9150c069ebcd17d2dc68279bc00bb53f2a9ae112")  # FIXME
    version("2025.12.1.14", sha256="a74f0400524fc83620a9be74a07074b5cbe7594fd4d97fd4c2bfde625fdc1633")  # FIXME
    version("2025.11.14.15", sha256="6b60f49d40bbd895bc61d8dc414fc2f2286d70eb72ed23548db8cf94f62804ca")  # FIXME
    version("2025.9.11.17", sha256="931ca9841a5e9c9408bc2ae67b50d28acf85bef56219b56860876dd1f2d024dd")  # FIXME
    version("2025.9.9.12", sha256="6a00942fc023f4f383af3254b4ed818d7fa7923a3c7c03b0e71da2ce71b538ab")  # FIXME
    version("2025.9.8.13", sha256="2de91c8f286b7fea55072061924f69e7f3bdf7a9cb63719c90090e41c6657d3a")  # FIXME
    version("2025.8.26.11", sha256="e73efff317c492a7990092f9c12676c705bf6cfe40a258a93f63f4b4c9941432")  # FIXME
    version("2025.8.6.13", sha256="5a0abad839d2ed810f213ab133d555d267124ddea29f1d8a50d6eca12a50ae6e")  # FIXME
    version(
        "2025.9.11.17", sha256="931ca9841a5e9c9408bc2ae67b50d28acf85bef56219b56860876dd1f2d024dd"
    )
    version(
        "2025.5.9.12", sha256="7ca7c8a7a76e2cd314468c677c69d12cc2357711fcab4a60f87994c1589e5cb5"
    )
    version(
        "2025.4.11.15", sha256="634728aa6698dc1ae3db161da94d9e4c7597a9a5da2c4410211b36f15fed60fc"
    )
    version("2023.8.7", sha256="c9f2a0a85d545e5362e967e4f069f56fddfd91215e22ffa48c66fb283521319a")
    version("2023.3.9", sha256="ee42f2f8c1d4bcfe35f746e472f07633570d485fab45407effc0379270a3bb03")

    depends_on("py-setuptools", type="build")
    depends_on("py-calver", type="build")

    def url_for_version(self, version):
        if version >= Version("2024.5.17"):
            sep = "_"
        else:
            sep = "-"

        return f"https://files.pythonhosted.org/packages/source/t/trove{sep}classifiers/trove{sep}classifiers-{version}.tar.gz"
