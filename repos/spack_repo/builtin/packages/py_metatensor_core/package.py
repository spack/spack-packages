# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *

# Necessary to pin each version to libmetatensor
VERSIONS = {
    "0.1.19": "ca7e1e73da3712a79989e856ebab4a254b7f893d01d8fb63f162b4937d81d824",
    "0.1.17": "98708f89a37652016ee508e307f824f3ca63307b85829de17ba6d2558f0b3b3b",
}


class PyMetatensorCore(PythonPackage):
    """Python bindings for metatensor-core"""

    homepage = "https://docs.metatensor.org"
    pypi = "metatensor-core/metatensor_core-0.0.0.tar.gz"

    import_modules = ["metatensor"]

    maintainers("HaoZeke", "Luthaf", "RMeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    depends_on("python@3.9:", type=("run", "build"))
    depends_on("py-numpy", type=("run", "build"))

    for ver, sha in VERSIONS.items():
        version(ver, sha256=sha)
        depends_on(f"libmetatensor@={ver}", when=f"@{ver}")

    # pyproject.toml
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-packaging@23:", type="build")
    # CMakeLists.txt
    depends_on("cmake@3.16:", type="build")
    depends_on("cmake@3.22:", type="build", when="@0.1.18:")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("METATENSOR_CORE_PYTHON_USE_EXTERNAL_LIB", "ON")
