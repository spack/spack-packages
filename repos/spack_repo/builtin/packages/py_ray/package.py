# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRay(PythonPackage):
    """Ray provides a simple, universal API for building distributed applications."""

    homepage = "https://github.com/ray-project/ray"
    url = "https://github.com/ray-project/ray/archive/ray-0.8.7.tar.gz"

    license("Apache-2.0")

    version("2.53.0", sha256="bb2e1393e0617b2edbdbc793718a5dbe98d5024e9f2ab06b33ecc524b02c9e0e")
    version("2.0.1", sha256="b8b2f0a99d2ac4c001ff11c78b4521b217e2a02df95fb6270fd621412143f28b")

    variant("default", default=False, description="Install default extras")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("npm", type="build")
    depends_on("py-setuptools", type="build")

    depends_on("bazel@6.5.0", when="@2.53.0", type="build")  # exact version
    depends_on("python@3.9:3.13", when="@2.53.0:", type=("build", "run"))
    depends_on("py-packaging", when="@2.53.0:", type=("build", "run"))
    depends_on("py-cython@3.0.12:", when="@2.53.0:", type="build")
    depends_on("py-click@7:", when="@2.53.0:", type=("build", "run"))
    depends_on("py-protobuf@3.20.3:", when="@2.53.0:", type=("build", "run"))
    depends_on("py-pyarrow@9:", when="@2.53.0:", type=("build", "run"))
    depends_on("py-watchfiles", when="@2.53.0:", type=("build", "run"))

    depends_on("py-filelock", type=("build", "run"))
    depends_on("py-jsonschema", type=("build", "run"))
    depends_on("py-msgpack@1", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))

    with when("+default"):
        depends_on("py-aiohttp@3.7:", type=("build", "run"))
        depends_on("py-aiohttp-cors", type=("build", "run"))
        depends_on("py-colorful", type=("build", "run"))
        depends_on("py-py-spy@0.4:", when="@2.53.0: ^python@3.12:", type=("build", "run"))
        depends_on("py-py-spy@0.2:", type=("build", "run"))
        depends_on("py-grpcio@1.42:", when="@2.53.0: ^python@3.10:", type=("build", "run"))
        depends_on("py-grpcio@1.32:", when="@2.53.0: ^python@:3.9", type=("build", "run"))
        depends_on("py-opencensus", type=("build", "run"))
        depends_on("py-pydantic@1,2.12:2", type=("build", "run"))
        depends_on("py-prometheus-client@0.7.1:", when="@2.53.0:", type=("build", "run"))
        depends_on("py-smart-open", type=("build", "run"))
        depends_on("py-virtualenv@20.0.24:", when="@2.53.0:", type=("build", "run"))
        conflicts("py-virtualenv@20.21.1")

    # Old version
    with when("@2.0.1"):
        depends_on("python@3.6:3.10", type=("build", "run"))
        depends_on("bazel@4.2.2", type="build")
        depends_on("py-cython@0.29.26:", type="build")
        depends_on("py-attrs", type=("build", "run"))
        depends_on("py-click@7:8.0.4", type=("build", "run"))
        depends_on("py-grpcio@1.32:1.43.0", when="^python@:3.9", type=("build", "run"))
        depends_on("py-grpcio@1.42:1.43.0", when="^python@3.10:", type=("build", "run"))
        depends_on("py-numpy@1.19.3:", when="^python@3.9:", type=("build", "run"))
        depends_on("py-numpy@1.16:", when="^python@:3.8", type=("build", "run"))
        depends_on("py-protobuf@3.15.3:3", type=("build", "run"))
        depends_on("py-aiosignal", type=("build", "run"))
        depends_on("py-frozenlist", type=("build", "run"))
        depends_on("py-typing-extensions", when="^python@:3.7", type=("build", "run"))
        depends_on("py-virtualenv", type=("build", "run"))

        with when("+default"):
            depends_on("py-gpustat@1:", type=("build", "run"))
            depends_on("py-prometheus-client@0.7.1:0.13", type=("build", "run"))

    build_directory = "python"

    def patch(self):
        filter_file(
            'bazel_flags = ["--verbose_failures"]',
            f'bazel_flags = ["--verbose_failures", "--jobs={make_jobs}"]',
            join_path("python", "setup.py"),
            string=True,
        )

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("SKIP_THIRDPARTY_INSTALL", "1")

    # Compile the dashboard npm modules included in the project
    @run_before("install")
    def build_dashboard(self):
        with working_dir(join_path("python", "ray", "dashboard", "client")):
            npm = which("npm")
            npm("ci")
            npm("run", "build")
