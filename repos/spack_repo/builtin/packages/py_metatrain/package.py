# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMetatrain(PythonPackage):
    """Train, fine-tune, and manipulate machine learning models for atomistic systems"""

    homepage = "https://docs.metatensor.org/metatrain/latest/index.html#"
    pypi = "metatrain/metatrain-2025.10.tar.gz"

    maintainers("RMeli", "luthaf", "HaoZeke")

    license("BSD-3-Clause", checked_by="RMeli")

    version("2025.10", sha256="70ca3d422dbaf8eca14f05f81299497faf52134bcf478b29484e891ba0881549")

    variant("soap_bpnn", default=False, description="Enable SOAP-BPNN architecture")

    depends_on("py-setuptools@77:", type="build")
    depends_on("py-setuptools-scm@8:", type="build")

    depends_on("py-ase", type=("build", "run"))
    depends_on("py-huggingface-hub", type=("build", "run"))
    depends_on("py-metatensor-learn@0.3.2:0.3", type=("build", "run"))
    depends_on("py-metatensor-operations@0.3.4:0.3", type=("build", "run"))
    depends_on("py-metatensor-torch@0.7.6:0.7", type=("build", "run"))
    depends_on("py-metatomic-torch@0.1.2:0.1", type=("build", "run"))
    depends_on("py-jsonschema", type=("build", "run"))
    depends_on("py-omegaconf@2.3.0:", type=("build", "run"))
    depends_on("py-python-hostlist", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-vesin", type=("build", "run"))

    # soap-bpnn
    depends_on("py-wigners", type=("build", "run"), when="+soap_bpnn")
    depends_on("py-torch-spex", type=("build", "run"), when="+soap_bpnn")
