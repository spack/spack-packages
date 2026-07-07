# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGeopmpy(PythonPackage):
    """The Global Extensible Open Power Manager (GEOPM) Service provides a
    user interface for accessing hardware telemetry and settings securely."""

    homepage = "https://geopm.github.io"
    git = "https://github.com/geopm/geopm.git"
    url = "https://github.com/geopm/geopm/tarball/v3.2.2"

    maintainers("bgeltz", "cmcantalupo")
    license("BSD-3-Clause")
    tags = ["e4s"]

    version("develop", branch="dev", get_full_repo=True)
    version("3.2.2", sha256="715383060187a84b0d4022a823805b158709ec9225d2f35dba94af63cd260afe")
    version(
        "3.2.1",
        sha256="9177da3af335256592c4ea8ae0dd4f8f9c8fb4caf65965af6216e7975d094b99",
        deprecated=True,
    )
    version(
        "3.2.0",
        sha256="b708233e1bfda66408c500f2ac0cbaf042140870bffdced12dd7cabbd18e0025",
        deprecated=True,
    )
    version(
        "3.1.0",
        sha256="2d890cad906fd2008dc57f4e06537695d4a027e1dc1ed92feed4d81bb1a1449e",
        deprecated=True,
    )

    variant("pytorch", default=False, description="Enable PyTorch support (for FFNet agent)")

    for ver in ["3.1.0", "3.2.0", "3.2.1", "3.2.2", "develop"]:
        depends_on(f"py-geopmdpy@{ver}", type="run", when=f"@{ver}")
        depends_on(f"libgeopm@{ver}", type=("build", "run"), when=f"@{ver}")

    depends_on("python@3.6:3", type=("build", "run"))
    depends_on("py-setuptools@53.0.0:", when="@3.1", type="build")
    depends_on("py-setuptools@59.6.0:", when="@3.2:", type="build")
    depends_on("py-setuptools-scm@6.4.2:", when="@3.1:", type="build")
    depends_on("py-build@0.9.0:", when="@3.1:", type="build")
    depends_on("py-cffi@1.14.5:", when="@3.1.0", type="run")
    depends_on("py-cffi@1.14.5:", when="@3.2:", type=("build", "run"))
    depends_on("py-natsort@8.2.0:", type="run")
    depends_on("py-numpy@1.19.5:", type="run")
    depends_on("py-numpy@1.19.5:1", when="@3.2", type="run")
    depends_on("py-pandas@1.1.5:", type="run")
    depends_on("py-tables@3.7.0:", type="run")
    depends_on("py-psutil@5.8.0:", type="run")
    depends_on("py-pyyaml@6.0:", type="run")

    # Integration test dependencies
    depends_on("py-docutils@0.18:", type="run")
    depends_on("py-dash@2.17.1:", type="run")
    depends_on("py-matplotlib", type="run")
    depends_on("py-plotly@5.18.0:", type="run")
    depends_on("py-torch@1.10.2:", when="+pytorch", type="run")
    depends_on("numactl", type="run")
    depends_on("stress-ng", type="run")

    build_directory = "geopmpy"

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if not self.spec.version.isdevelop():
            env.set("SETUPTOOLS_SCM_PRETEND_VERSION", self.version)
        if self.version >= Version("3.2.0"):  # Required for CFFI API mode builds
            env.append_path("C_INCLUDE_PATH", self.spec["libgeopm"].prefix.include)
            env.append_path("LIBRARY_PATH", self.spec["libgeopm"].prefix.lib)
