# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPythonSbom(PythonPackage):
    """Software bills of materials (SBOMs) for Python distributions. python-sbom writes a CycloneDX
    SBOM into every wheel you build, where PEP 770 (a Python Enhancement Proposal) tells installers
    to keep it. The SBOM records your project, the runtime dependencies it declares, any wheels it
    bundles, and the build toolchain, and a rebuild with the same inputs reproduces it byte for
    byte."""

    homepage = "https://github.com/tox-dev/python-sbom"
    pypi = "python_sbom/python_sbom-0.3.1.tar.gz"

    maintainers("ebagrenrut")

    license("MIT")

    version("0.5.0", sha256="fc7b2c46fa40f52e587ac59cada775e83dcac231fafa90b7a71c3554527ddfb6")
    version("0.3.1", sha256="37d0fa3d0a16fddc3d88099e147e164ddb3055e8bc3424506ef41dd80f723a73")

    variant(
        "build_backend",
        default="generic",
        description="Supported build-backend integrations.",
        multi=True,
        values=("generic", "hatch", "pdm", "setuptools"),
    )

    variant(
        "validate", default=False, description="Enable use of python-sbom for SBOM validation."
    )

    with default_args(type="build"):
        depends_on("py-hatch-fancy-pypi-readme@25.1:")
        depends_on("py-hatch-vcs@0.5:")
        depends_on("py-hatchling@1.32.4:")

    with default_args(type=("build", "run")):
        depends_on("py-installer@1.1:")
        depends_on("py-packageurl-python@0.11.1:")
        depends_on("py-zipremove@0.10:")

        depends_on("python@3.11:")

    with default_args(type="run"):
        depends_on("py-packaging@26.3:")

        depends_on("py-hatchling@1.28:", when="build_backend=hatch")

        depends_on("py-pdm-backend@2.4:", when="build_backend=pdm")

        depends_on("py-setuptools@77:", when="build_backend=setuptools")

        depends_on("py-jsonschema-rs@0.60.3:", when="+validate")
        depends_on("py-license-expression@30:", when="+validate")
        depends_on("py-spdx-tools@0.8.5:", when="+validate")
