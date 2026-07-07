# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTorchSpex(PythonPackage):
    """Spherical expansions of atomic neighbourhoods"""

    homepage = "https://github.com/lab-cosmo/torch-spex"
    pypi = "torch_spex/torch_spex-0.0.0.tar.gz"

    maintainers("RMeli", "luthaf", "HaoZeke")

    # pyproject.toml
    license("MIT", checked_by="RMeli")

    version("0.1.0", sha256="82722780bf49638c439b8e7ca98ab31b956941aacef72382a9650ff1f1c5eed0")

    depends_on("py-flit-core@3.4:3", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-numpy")
        depends_on("py-pyyaml")
        depends_on("py-scipy")
        depends_on("py-sphericart-torch")
