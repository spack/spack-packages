# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyJaxTqdm(PythonPackage):
    """Tqdm progress bar for JAX scans and loops."""

    homepage = "https://github.com/jeremiecoullon/jax-tqdm"
    pypi = "jax_tqdm/jax_tqdm-0.4.0.tar.gz"

    maintainers("tpadioleau")

    license("MIT", checked_by="tpadioleau")

    version("0.4.0", sha256="d76a7ab07286ed8024fa019add2668b4d1d6ddf3bcaa166f2e1466d9e51b99a0")

    depends_on("py-poetry-core@1.2:1", type="build")

    depends_on("python@3.10:3", type=("build", "run"))
    depends_on("py-tqdm@4.64.1:4", type=("build", "run"))
    depends_on("py-jax@0.4.12:0", type=("build", "run"))
    depends_on("py-chex@0.1.87:0.1", type=("build", "run"))
