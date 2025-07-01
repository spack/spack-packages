# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *

# Necessary to pin each version to libmetatensor
VERSION_MAP = {
    "0.1.14": "ee1f87bc045beadafa63cc0ccd0ebcf9c9e9fe8d619529d28775b0c22e0bbe19",
    "0.1.13": "d43dfba8c6092de3e7bbe29dcf8fa3680462abd68947ece809befc9b0f6c1d56",
}


class PyMetatensorCore(PythonPackage):
    """Python bindings for metatensor-core"""

    homepage = "https://docs.metatensor.org"
    pypi = "metatensor-core/metatensor_core-0.1.14.tar.gz"

    import_modules = ["metatensor"]

    maintainers("HaoZeke", "luthaf", "rmeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    depends_on("python@3.9:", type=("run", "build"))
    depends_on("py-numpy", type=("run", "build"))

    for ver, sha in VERSION_MAP.items():
        version(ver, sha256=sha)
        depends_on(f"libmetatensor@{ver}", when=f"@{ver}")

    # pyproject.toml
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-packaging@23:", type="build")
    depends_on("cmake@3.16", type="build")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("METATENSOR_CORE_PYTHON_USE_EXTERNAL_LIB", "ON")
