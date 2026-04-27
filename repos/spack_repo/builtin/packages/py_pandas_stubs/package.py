# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPandasStubs(PythonPackage):
    """These are public type stubs for pandas, following the convention of
    providing stubs in a separate package, as specified in PEP 561. The stubs
    cover the most typical use cases of pandas. In general, these stubs are
    narrower than what is possibly allowed by pandas, but follow a convention of
    suggesting best recommended practices for using pandas."""

    homepage = "https://pandas.pydata.org/"
    pypi = "pandas_stubs/pandas_stubs-2.0.2.230605.tar.gz"

    license("BSD-3-Clause")

    version(
        "2.3.3.251219", sha256="dc2883e6daff49d380d1b5a2e864983ab9be8cd9a661fa861e3dea37559a5af4"
    )
    version(
        "2.3.2.250926", sha256="c64b9932760ceefb96a3222b953e6a251321a9832a28548be6506df473a66406"
    )
    version(
        "2.0.2.230605", sha256="624c7bb06d38145a44b61be459ccd19b038e0bf20364a025ecaab78fea65e858"
    )

    depends_on("py-poetry-core@1:", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-numpy@1.23.5:2.3.5", when="@2.3.3")
        depends_on("py-numpy@1.23.5:", when="@2.3:")
        depends_on("py-numpy@1.24.3:", when="@2.0")
        depends_on("py-types-pytz@2022.1.1:")
