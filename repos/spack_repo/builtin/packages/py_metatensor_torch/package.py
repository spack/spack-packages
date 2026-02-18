# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *

VERSIONS = {
    "0.8.4": "0b2e158e8b31f12735bf2db391257296a5ef0b802512f2d2db8e0c5ee028a192",
    "0.8.3": "9b0907f0969bd2139a6ab3614d81faebc7abca102df4127cba9f0521e2e1437d",
    "0.8.2": "60a81ccb5bda11ee173abfecd02a5d126d2788732b2ebb4d701ba0c82c7331a1",
    "0.8.1": "11986d4c2964054baae9fe10ffc36c6a6ba70a78d97b406cb6c2e14e72a0cf72",
    "0.8.0": "240ea8c37328f6bb61ec9f3e482131f0875c73166a0e349a8dd8b85204c58bd7",
    "0.7.6": "bcc23b535e5b86c0d49096cbf73de67141896f4f14c114515d97b936a78353a1",
}


class PyMetatensorTorch(PythonPackage):
    """Torchscript bindings for metatensor"""

    homepage = "https://docs.metatensor.org"
    pypi = "metatensor-torch/metatensor_torch-0.0.0.tar.gz"

    import_modules = ["metatensor.torch"]

    maintainers("HaoZeke", "Luthaf", "RMeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    # setup.py
    for ver, sha256 in VERSIONS.items():
        version(ver, sha256=sha256)
        depends_on(f"libmetatensor-torch@={ver}", when=f"@{ver}")

    # setup.py
    depends_on("py-torch@2.1:", type=("build", "run"))
    depends_on("py-metatensor-core@0.1.13:0.1", type=("build", "run"), when="@0.7.6")
    depends_on("py-metatensor-core@0.1.15:0.1", type=("build", "run"), when="@0.8.0:")

    # pyproject.toml
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("python@3.10:", type=("build", "run"), when="@0.8.1:")
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-packaging@23:", type="build")
    # metatensor/python/CMakeLists.txt
    depends_on("cmake@3.16:", type="build")
    depends_on("cmake@3.22:", type="build", when="@0.8.2:")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("METATENSOR_TORCH_PYTHON_USE_EXTERNAL_LIB", "ON")

    @run_after("install")
    def workaround(self):
        """
        Workaround for the incorrect usage of namespace packages.

        See https://github.com/metatensor/metatensor/issues/976
        """
        python = self.spec["python"]
        python_version = python.version.up_to(2)

        metatensor_core = os.path.join(
            self.spec["py-metatensor-core"].prefix.lib,
            f"python{python_version}",
            "site-packages",
            "metatensor",
        )
        metatensor_torch = os.path.join(
            self.prefix.lib, f"python{python_version}", "site-packages", "metatensor", "torch"
        )

        dest = os.path.join(metatensor_core, "torch")

        if os.path.lexists(dest):
            os.remove(dest)

        symlink(metatensor_torch, dest)
