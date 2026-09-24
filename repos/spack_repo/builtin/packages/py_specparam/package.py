# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySpecparam(PythonPackage):
    """Parameterize neural power spectra into periodic and aperiodic components."""

    homepage = "https://specparam-tools.github.io/"
    pypi = "specparam/specparam-2.0.0rc6.tar.gz"

    license("Apache-2.0")

    version("2.0.0rc7", sha256="00744b009c1822ef69478df7b7b5399e1d14fb061747d4606e9fc76772bbcc95")
    version("2.0.0rc6", sha256="1f96a16132d999108c228b723e856a99a736f477d7f567e6226f17ce65852c87")
    version("2.0.0rc5", sha256="94a690169d7561f0eef52626ec1927038788a4ebe45daa804c5874b5b505140d")
    version("2.0.0rc4", sha256="0dfe3a3ca2c0db2729ac3ba971631947586fe4e5a3344363b479ec612322bad1")
    version("2.0.0rc3", sha256="11e454388e3df49f3b619a441f76402dd98aa3b793d3b4158b91b3a4b3fb65cd")
    version("2.0.0rc2", sha256="ea9a38ad8b698ebf076433b0955996b4295aa7354df83925507c00431654d619")
    version("2.0.0rc1", sha256="a5a636693dd55520bad36b3dfdaecdcd3d7221d055d281e5e13576a4fc491c3a")
    version("2.0.0rc0", sha256="e4dfd489c2c9cc836b60325a79bab4b82a0d0c743ec85757ab0ab7e5c2864e5b")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-numpy")
        depends_on("py-scipy@0.19:")
