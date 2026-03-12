# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import json
import platform
from pathlib import Path

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *

_dirname = Path(__file__).resolve().parent
_versions = json.load(open(join_path(_dirname, "versions.json"), "r"))


class PyOvito(PythonPackage):
    """A scientific data visualization and analysis software for particle-based simulations"""

    homepage = "https://www.ovito.org"

    for _version, packages in _versions.items():
        key = "{0}-{1}".format(platform.system(), platform.machine())
        pkg = packages.get(key)
        if pkg:
            for cp_version, sha_url in pkg.items():
                if "-abi3-" in sha_url["url"]:
                    version(
                        f"{_version}", sha256=sha_url["sha256"], url=sha_url["url"], expand=False
                    )
                    python_version = (
                        f"{cp_version.split('cp')[1][0]}.{cp_version.split('cp')[1][1:]}"
                    )
                    depends_on(
                        f"python@{python_version}:", type=("build", "run"), when=f"@{_version}"
                    )
                else:
                    version(
                        f"{_version}-{cp_version}",
                        sha256=sha_url["sha256"],
                        url=sha_url["url"],
                        expand=False,
                    )
                    python_version = (
                        f"{cp_version.split('cp')[1][0]}.{cp_version.split('cp')[1][1:]}"
                    )
                    depends_on(
                        f"python@{python_version}",
                        type=("build", "run"),
                        when=f"@{_version}-{cp_version}",
                    )

    depends_on("py-wheel", type="build")
    depends_on("py-numpy@1.23:", type=("build", "run"), when="@3.13.0")
    depends_on("py-traits@6.3:", type=("build", "run"), when="@3.13.0")
    depends_on("py-pyside6@6.8.3:", type=("build", "run"), when="@3.13.0")
