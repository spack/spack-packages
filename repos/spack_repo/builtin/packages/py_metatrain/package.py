# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMetatrain(PythonPackage):
    """Train, fine-tune, and manipulate machine learning models for atomistic systems"""

    homepage = "https://docs.metatensor.org/metatrain/latest/index.html"
    pypi = "metatrain/metatrain-2025.11.tar.gz"

    maintainers("RMeli", "Luthaf", "HaoZeke")

    license("BSD-3-Clause", checked_by="RMeli")

    version("2025.12", sha256="d0634934cc33d23189a9ef99f8c27e2e81cdfc248cf110d8df6c48255cb78765")
    version("2025.11", sha256="4c1a78feb359885f29d659f97ccf0e0676892ba1aa120cf58d0c7a0442161255")

    variant("soap_bpnn", default=False, description="Enable SOAP-BPNN architecture")

    # pyproject.toml [build-system]
    with default_args(type="build"):
        depends_on("py-setuptools@77:")
        depends_on("py-setuptools-scm@8:")

    # pyproject.toml [project] dependencies
    with default_args(type=("build", "run")):
        depends_on("py-ase")
        depends_on("py-huggingface-hub")
        depends_on("py-numpy", when="@2025.12:")
        depends_on("py-metatensor-learn@0.3.2:0.3", when="@2025.11")
        depends_on("py-metatensor-learn@0.4.0:0.4", when="@2025.12:")
        depends_on("py-metatensor-operations@0.3.4:0.3", when="@2025.11")
        depends_on("py-metatensor-operations@0.4.0:0.4", when="@2025.12:")
        depends_on("py-metatensor-torch@0.8.1:0.8", when="@2025.11")
        depends_on("py-metatensor-torch@0.8.2:0.8", when="@2025.12:")
        depends_on("py-metatomic-torch@0.1.5:0.1", when="@2025.11")
        depends_on("py-metatomic-torch@0.1.6:0.1", when="@2025.12:")
        depends_on("py-jsonschema")
        depends_on("py-pydantic@2.12:", when="@2025.12:")
        depends_on("py-typing-extensions", when="@2025.12:")
        depends_on("py-omegaconf@2.3.0:")
        depends_on("py-python-hostlist")
        depends_on("py-tqdm")
        depends_on("py-vesin")

    # soap-bpnn
    # pyproject.toml [project.optional-dependencies] soap-bpnn
    with default_args(type=("build", "run"), when="+soap_bpnn"):
        depends_on("py-wigners")
        depends_on("py-torch-spex")
