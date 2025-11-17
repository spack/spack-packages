# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMetatrain(PythonPackage):
    """Train, fine-tune, and manipulate machine learning models for atomistic systems"""

    homepage = "https://docs.metatensor.org/metatrain/latest/index.html#"
    pypi = "metatrain/metatrain-2025.11.tar.gz"

    maintainers("RMeli", "luthaf", "HaoZeke")

    license("BSD-3-Clause", checked_by="RMeli")

    version("2025.11", sha256="4c1a78feb359885f29d659f97ccf0e0676892ba1aa120cf58d0c7a0442161255")

    variant("soap_bpnn", default=False, description="Enable SOAP-BPNN architecture")

    # pyproject.toml [build-system]
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-setuptools-scm@8:", type="build")

    # pyproject.toml [project] dependencies
    depends_on("py-ase", type=("build", "run"))
    depends_on("py-huggingface-hub", type=("build", "run"))
    depends_on("py-metatensor-learn@0.3.2:0.3", type=("build", "run"))
    depends_on("py-metatensor-operations@0.3.4:0.3", type=("build", "run"))
    depends_on("py-metatensor-torch@0.8.1:0.8", type=("build", "run"))
    depends_on("py-metatomic-torch@0.1.5:0.1", type=("build", "run"))
    depends_on("py-jsonschema", type=("build", "run"))
    depends_on("py-omegaconf@2.3.0:", type=("build", "run"))
    depends_on("py-python-hostlist", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-vesin", type=("build", "run"))

    # soap-bpnn
    # pyproject.toml [project.optional-dependencies] soap-bpnn
    depends_on("py-wigners", type=("build", "run"), when="+soap_bpnn")
    depends_on("py-torch-spex", type=("build", "run"), when="+soap_bpnn")
