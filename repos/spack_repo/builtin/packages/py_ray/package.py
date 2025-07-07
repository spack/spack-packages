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

    version("2.47.1", sha256="a0085b00d7204cd39658b5db60a10842a0068131129f304403e55847fc9cd69c")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("python@3.9:3.12", type=("build", "run"))
    depends_on("bazel@6.5.0", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")
    depends_on("py-cython@3.0.12:", type="build")
    depends_on("py-build", type=("build"))
    depends_on("py-wheel", type=("build"))

    variant("data", default=True, description="Install Ray Data dependencies")
    variant("tune", default=True, description="Install Ray Tune dependencies")
    variant("train", default=True, description="Install Ray Train dependencies")
    variant("serve", default=True, description="Install Ray Serve dependencies")
    variant("default", default=True, description="Support for dashboard and cluser launcher")
    variant("cpp", default=False, description="Install Ray C++ API")

    depends_on("npm", type="build", when="+default")

    with default_args(type=("run")):
        depends_on("py-click@7:")
        depends_on("py-filelock")
        depends_on("py-jsonschema")
        depends_on("py-msgpack@1:2")
        depends_on("py-packaging")
        depends_on("py-protobuf@3.15.3:")
        depends_on("py-pyyaml")

        # Used in setup.py
        depends_on("py-psutil")
        depends_on("py-colorama")
        # Removed in future versions
        depends_on("py-setproctitle@1.2.2")

        py_arrow_dep = "py-pyarrow@9.0:"
        py_pandas_dep = "py-pandas@1.3:"
        py_pydantic_dep = "py-pydantic@:1,2.5:2"

        with when("+default"):
            depends_on("py-aiohttp@3.7:")
            depends_on("py-aiohttp-cors")
            depends_on("py-colorful")
            depends_on("py-py-spy@0.4.0:")
            depends_on("py-requests")
            depends_on("py-grpcio@1.42.0:")
            depends_on("py-opencensus")
            depends_on("py-opentelemetry-sdk")
            depends_on("py-opentelemetry-exporter-prometheus")
            depends_on("py-opentelemetry-proto")
            depends_on(py_pydantic_dep)
            depends_on("py-prometheus-client")
            depends_on("py-smart-open")
            depends_on("py-virtualenv@20.0.24:")
            depends_on("py-google-api-core +grpc")
            depends_on("py-googleapis-common-protos")

        with when("+data"):
            depends_on("py-numpy@1.20:")
            depends_on(py_pandas_dep)
            depends_on(py_arrow_dep)
            depends_on("py-fsspec")

        with when("+tune"):
            depends_on(py_pandas_dep)
            depends_on(py_arrow_dep)
            depends_on("py-tensorboardx@1.9:")
            depends_on("py-requests")
            depends_on("py-fsspec")

        with when("+train"):
            depends_on(py_pydantic_dep)

        with when("+serve"):
            depends_on("py-uvicorn+standard")
            depends_on("py-requests")
            depends_on("py-starlette")
            depends_on("py-fastapi")
            depends_on("py-watchfiles")

    conflicts("~tune", when="+train")  # [train] requires [tune]
    conflicts("~default", when="+serve")  # [serve] requires [default]

    build_directory = "python"

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # Preserve PATH, otherwise build fails to find python
        env.set("BAZEL_ARGS", f"--action_env=PATH --jobs={make_jobs}")
        env.set("SKIP_THIRDPARTY_INSTALL_CONDA_FORGE", "1")

        if "+cpp" in self.spec:
            env.set("RAY_INSTALL_CPP", "1")

    # https://docs.ray.io/en/latest/ray-contribute/development.html#building-ray
    @run_before("install")
    def build_dashboard(self):
        if "+default" in self.spec:
            with working_dir(join_path("python", "ray", "dashboard", "client")):
                npm = which("npm")
                npm("ci")
                npm("run", "build")
