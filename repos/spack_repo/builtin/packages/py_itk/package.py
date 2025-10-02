# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import sys

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyItk(PythonPackage):
    """ITK is an open-source toolkit for multidimensional image analysis"""

    homepage = "https://itk.org/"

    skip_version_audit = ["platform=windows"]

    if sys.platform == "darwin":
        # version 5.1.2
        version(
            "5.1.2-cp39",
            url="https://pypi.io/packages/cp39/i/itk/itk-5.1.2-cp39-cp39-macosx_10_9_x86_64.whl",
            sha256="e8dec75b4452bd2ee65beb4901b245fc3a2a2ccc46dfa008ae0b5b757718d458",
        )

        # version 5.3.0
        version(
            "5.3.0-cp39",
            url="https://pypi.io/packages/cp39/i/itk/itk-5.3.0-cp39-cp39-macosx_10_9_x86_64.whl",
            sha256="155581581929dfe834af6c6233a8c83e2ca2b1f52d6c7b2c81f04dc249aab1a5",
        )
        version(
            "5.3.0-cp310",
            url="https://pypi.io/packages/cp310/i/itk/itk-5.3.0-cp310-cp310-macosx_10_9_x86_64.whl",
            sha256="f92ec860173c82eb458764b4b5b771783b690c3aa3a01d15c6f3d008fc2bb493",
        )
        version(
            "5.3.0-cp311",
            url="https://pypi.io/packages/cp311/i/itk/itk-5.3.0-cp311-cp311-macosx_10_9_x86_64.whl",
            sha256="9dcfd9721ff6022e91eb98dc4004d437de2912dfd50d707d1ee72b89c334a3d4",
        )
    elif sys.platform.startswith("linux"):
        # version 5.1.2
        version(
            "5.1.2-cp39",
            url="https://pypi.io/packages/cp39/i/itk/itk-5.1.2-cp39-cp39-manylinux1_x86_64.whl",
            sha256="5781b74410b7189a825c89d370411595e5e3d5dbb480201907f751f26698df83",
        )

        # version 5.3.0
        version(
            "5.3.0-cp39",
            url="https://pypi.io/packages/cp39/i/itk/itk-5.3.0-cp39-cp39-manylinux_2_28_x86_64.whl",
            sha256="bcc4449f2df35224cbc26472475d2afeb8a92886a81db950b2305f911bc2a38c",
        )
        version(
            "5.3.0-cp310",
            url="https://pypi.io/packages/cp310/i/itk/itk-5.3.0-cp310-cp310-manylinux_2_28_x86_64.whl",
            sha256="272708ee5ed5d09a519b2e98ac9c130f3146630257506ea440c83501c16f9580",
        )
        version(
            "5.3.0-cp311",
            url="https://pypi.io/packages/cp311/i/itk/itk-5.3.0-cp311-cp311-manylinux_2_28_x86_64.whl",
            sha256="ba8361a8ed1c5462e690ee893f624c0babb7a1072a15609c26790eea717e3f77",
        )

    depends_on("python@3.9.0:3.9", when="@5.1.2-cp39,5.3.0-cp39", type=("build", "run"))
    depends_on("python@3.10.0:3.10", when="@5.3.0-cp310", type=("build", "run"))
    depends_on("python@3.11.0:3.11", when="@5.3.0-cp311", type=("build", "run"))
    depends_on("py-setuptools", type="run")

    requires("target=x86_64:", msg="py-itk is available for x86_64 only")
