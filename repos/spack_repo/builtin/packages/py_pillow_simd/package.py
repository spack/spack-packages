# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.py_pillow.package import PyPillowBase

from spack.package import *


class PyPillowSimd(PyPillowBase):
    """Pillow-SIMD is a SIMD-enabled fork of Pillow. It is usually 4-6x
    faster than the original Pillow in image processing benchmarks."""

    # See https://github.com/spack/spack/pull/15566
    _name = "py-pillow-simd"
    homepage = "https://github.com/uploadcare/pillow-simd"
    pypi = "Pillow-SIMD/Pillow-SIMD-7.0.0.post3.tar.gz"

    license("HPND")

    with default_args(deprecated=True):
        # https://www.cvedetails.com/cve/CVE-2024-28219/
        # https://www.cvedetails.com/cve/CVE-2023-50447/
        # https://www.cvedetails.com/cve/CVE-2023-44271/
        version(
            "9.5.0.post1",
            sha256="8c89b85c4085532752625f2cc066a28547cebb98529acf932d5d84c1a7ab2abc",
        )
        # https://www.cvedetails.com/cve/CVE-2022-45199/
        # https://www.cvedetails.com/cve/CVE-2022-45198/
        # https://www.cvedetails.com/cve/CVE-2022-24303/
        version(
            "9.0.0.post1",
            sha256="918541cfaa90ba3c0e1bae5da31ba1b1f52b09c0009bd90183b787af4e018263",
        )

    depends_on("c", type="build")  # generated

    for ver in ["9.0.0.post1", "9.5.0.post1"]:
        provides("pil@" + ver, when="@" + ver)

    conflicts("target=aarch64:")
