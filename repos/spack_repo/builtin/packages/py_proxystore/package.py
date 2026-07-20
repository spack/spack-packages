# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyProxystore(PythonPackage):
    """ProxyStore facilitates efficient data flow management in
    distributed Python applications, such as dynamic task-based
    workflows or serverless and edge applications."""

    homepage = "https://docs.proxystore.dev"
    pypi = "proxystore/proxystore-0.8.3.tar.gz"
    git = "https://github.com/proxystore/proxystore.git"

    maintainers("gpauloski", "mdorier")

    license("MIT", checked_by="mdorier")

    version("main", branch="main")
    version("0.8.3", sha256="7a71de1abaefd04425f9614a32a6527de48f2c65bba999996c7c1db582ec7b48")

    variant("kafka", default=False, description="Enable Kafka connector")
    variant("redis", default=False, description="Enable Redis connector")
    variant("zmq", default=False, description="Enable ZMQ connector")
    # TODO: the "endpoints" variant in pyproject.toml requires dependencies
    # that are not in Spack yet.

    depends_on("python@3.9:")
    depends_on("python@3.10:", when="@0.8.4:")
    depends_on("py-setuptools@64.0:", type="build")
    depends_on("py-setuptools-scm", type="build")
    depends_on("py-click@:8.1.3,8.1.5:")
    depends_on("py-cloudpickle@3:")
    depends_on("py-cryptography@39.0.1:")
    depends_on("py-globus-sdk@3.46.0:3")
    depends_on("py-pydantic@2")
    depends_on("py-tomli-w")
    with when("^python@:3.10"):
        depends_on("py-tomli")
        depends_on("py-typing-extensions@4.3.0:")
    depends_on("py-confluent-kafka", when="+kafka")
    depends_on("py-redis@3.4:", when="+redis")
    depends_on("py-pyzmq", when="+zmq")
