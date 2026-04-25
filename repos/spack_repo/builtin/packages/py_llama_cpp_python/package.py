# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLlamaCppPython(PythonPackage):
    """Python bindings for llama.cpp"""

    homepage = "https://github.com/abetlen/llama-cpp-python"
    pypi = "llama-cpp-python/llama_cpp_python-0.3.16.tar.gz"
    git = "https://github.com/abetlen/llama-cpp-python.git"

    maintainers("rbberger")

    license("MIT")

    version("main", branch="main")
    version("0.3.16", sha256="34ed0f9bd9431af045bb63d9324ae620ad0536653740e9bb163a2e1fcb973be6")

    depends_on("py-scikit-build-core@0.9.2: +pyproject", type="build")
    depends_on("py-typing-extensions@4.5.0:")
    depends_on("py-diskcache@5.6.1:")
    depends_on("py-numpy@1.20.0:")
    depends_on("py-jinja2@2.11.3:")

    depends_on("llama-cpp")

    def config_settings(self, spec, prefix):
        return {"wheel.cmake": "false"}
