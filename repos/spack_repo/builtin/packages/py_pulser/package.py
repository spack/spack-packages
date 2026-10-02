# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPulser(PythonPackage):
    """A pulse-level composer for neutral-atom quantum devices."""

    homepage = "https://github.com/pasqal-io/Pulser"
    pypi = "pulser/pulser-1.9.0-py3-none-any.whl"

    supplier = "Organization: Pulser Development Team"

    maintainers("LydDeb")
    license("Apache-2.0", checked_by="LydDeb")

    version("1.9.0", sha256="3451003a9c62f4686cf17b7167be3f0a1e7c938b740b8775b955488aa9c44941")

    variant("torch", default=False, description="Enable torch support")

    depends_on("python@3.10:", type=("build", "run"))

    with default_args(type=("build", "run")):
        depends_on("py-pasqal-cloud@0.23.0:")
        depends_on("py-pulser-core@1.9.0")
        depends_on("py-pulser-core@1.9.0 +torch", when="+torch")
        depends_on("py-pulser-simulation@1.9.0")
