# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGeopmdpy(PythonPackage):
    """The Global Extensible Open Power Manager (GEOPM) Service provides a
    user interface for accessing hardware telemetry and settings securely."""

    homepage = "https://geopm.github.io"
    git = "https://github.com/geopm/geopm.git"
    url = "https://github.com/geopm/geopm/tarball/v3.2.0"

    maintainers("bgeltz", "cmcantalupo")
    license("BSD-3-Clause")
    tags = ["e4s"]

    variant("grpc", default=False, when="@3.2:", description="Enable gRPC support")
    variant(
        "stats",
        default=False,
        when="@3.2:",
        description="Enable additional packages for data analysis and post-processing",
    )

    version("develop", branch="dev", get_full_repo=True)
    version("3.2.0", sha256="b708233e1bfda66408c500f2ac0cbaf042140870bffdced12dd7cabbd18e0025")
    version("3.1.0", sha256="2d890cad906fd2008dc57f4e06537695d4a027e1dc1ed92feed4d81bb1a1449e")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    for ver in ["3.1.0", "3.2.0", "develop"]:
        depends_on(f"geopm-service@{ver}", type=("build", "test", "run"), when=f"@{ver}")
    depends_on("py-dasbus@1.6.0:", type=("build", "run"))
    depends_on("py-cffi@1.14.5:", when="@3.1", type="run")
    depends_on("py-cffi@1.14.5:", when="@3.2:", type=("build", "run"))
    depends_on("py-psutil@5.8.0:", when="@3.1", type="run")
    depends_on("py-psutil@5.8.0:", when="@3.2:", type=("test", "run"))
    depends_on("py-jsonschema@3.2.0:", when="@3.1", type="run")
    depends_on("py-jsonschema@3.2.0:", when="@3.2:", type=("test", "run"))
    depends_on("py-pyyaml@6.0:", when="+stats", type="run")
    depends_on("py-seaborn@0.11.2:", when="+stats", type="run")
    depends_on("py-setuptools@59.6.0:", when="@3.2:", type="build")
    depends_on("py-setuptools-scm@6.4.2:", type="build")
    depends_on("py-build@0.9.0:", type="build")
    depends_on("py-defusedxml@0.7.1:", when="@3.2:", type="test")
    depends_on("py-grpcio@1.30.2:", when="+grpc", type=("build", "run"))
    depends_on("py-protobuf@3.12.4:", when="+grpc", type=("build", "run"))

    build_directory = "geopmdpy"

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if not self.spec.version.isdevelop():
            env.set("SETUPTOOLS_SCM_PRETEND_VERSION", self.version)
        if self.version >= Version("3.2.0"):  # Required for CFFI API mode builds
            env.append_path("C_INCLUDE_PATH", self.spec["geopm-service"].prefix.include)
            env.append_path("LIBRARY_PATH", self.spec["geopm-service"].prefix.lib)
