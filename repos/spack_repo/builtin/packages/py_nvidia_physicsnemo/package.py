# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNvidiaPhysicsnemo(PythonPackage):
    """A deep learning framework for AI-driven multi-physics systems"""

    homepage = "https://github.com/NVIDIA/physicsnemo"
    pypi = "nvidia-physicsnemo/nvidia_physicsnemo-1.3.0-py3-none-any.whl"
    # Work-around URL until the CI version check can rely on the URL related to a PyPi wheel.
    # ref. https://github.com/spack/spack-packages/pull/2400/changes/a3e13de4f218e3fb6951e8b89dfa914be704313f
    url = "https://pypi.io/packages/py3/n/nvidia-physicsnemo/nvidia_physicsnemo-1.3.0-py3-none-any.whl"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("1.3.0", sha256="404b5a17cdc00bcc8a2b003304695e4cbd8fff7fc7cca7f140988569c690f6b9")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@77.0.3:", type=("build"))
    depends_on("py-certifi@2023.7.22:", type=("build", "run"))
    depends_on("py-einops@0.8.0:", type=("build", "run"))
    depends_on("py-fsspec@2023.1.0:", type=("build", "run"))
    depends_on("py-numpy@1.22.4:", type=("build", "run"))
    depends_on("py-onnx@1.14.0:", type=("build", "run"))
    depends_on("py-packaging@24.2:", type=("build", "run"))
    depends_on("py-requests@2.32.2:", type=("build", "run"))
    depends_on("py-s3fs@2023.5.0:", type=("build", "run"))
    depends_on("py-timm@1.0.0:", type=("build", "run"))
    depends_on("py-torch@2.4.0:", type=("build", "run"))
    depends_on("py-tqdm@4.60.0:", type=("build", "run"))
    depends_on("py-treelib@1.2.5:", type=("build", "run"))
    depends_on("py-xarray@2023.1.0:", type=("build", "run"))
    depends_on("py-zarr@2.14.2:", type=("build", "run"))
