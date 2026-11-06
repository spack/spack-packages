# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class ModelAngelo(PythonPackage):
    """ModelAngelo is an automatic atomic model building program for cryo-EM maps."""

    homepage = "https://github.com/3dem/model-angelo"

    url = "https://github.com/3dem/model-angelo"
    git = "https://github.com/3dem/model-angelo.git"

    license("MIT", checked_by="snehring")

    version("20250218", commit="ddd969038045c28c5f281353dd62e98afb57859c")

    depends_on("py-setuptools", type="build")

    # model-angelo imports torch directly (41 files). No ceiling: only verified up to 2.13.0,
    # no specific break known beyond it.
    depends_on("py-torch@2.7.1:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-biopython@1.81:", type=("build", "run"))
    depends_on("py-einops", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-mrcfile", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    # model-angelo only uses esm.pretrained.* for checkpoint loading, never ESMFold structure
    # prediction, so the optional deepspeed/pytorch-lightning/... stack isn't needed.
    depends_on("py-fair-esm@1.0.3~esmfold", type=("build", "run"))
    # pyhmmer<0.11 has no cp313 wheel and fails to build from source on python@3.13 (removed
    # CPython C-API symbols). 0.11.0 is the lowest version with a cp313 wheel.
    depends_on("py-pyhmmer@0.11.0", type=("build", "run"))
    depends_on("py-loguru", type=("build", "run"))
    # numpy<2.0 doesn't support python@3.13. No ceiling beyond that - not aware of a specific
    # break past 2.2.6.
    depends_on("py-numpy@1.24.4:", type=("build", "run"))
