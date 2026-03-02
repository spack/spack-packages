# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)s

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyArkouda(PythonPackage):
    """This is the python client for Arkouda."""

    homepage = "https://github.com/Bears-R-Us/arkouda"

    # Updating the arkouda PyPI package is future work
    list_url = "https://github.com/Bears-R-Us/arkouda/tags"
    url = "https://github.com/Bears-R-Us/arkouda/archive/refs/tags/v2025.08.20.tar.gz"
    git = "https://github.com/Bears-R-Us/arkouda.git"

    # See https://spdx.org/licenses/ for a list.
    license("MIT")

    test_requires_compiler = True

    # A list of GitHub accounts to notify when the package is updated.
    maintainers("1RyanK", "ajpotts", "arezaii", "drculhane", "jaketrookman")

    version("main", branch="main")

    version(
        "2025.12.16", sha256="72638e9d8aa1889b6bafa76c6e8060e0c8aab0871be2693f8fb10f57cd4acbfa"
    )
    version(
        "2025.09.30", sha256="10f488a3ff3482b66f1b1e8a4235d72e91ad07acb932eca85d1e695f0f6155a2"
    )
    version(
        "2025.08.20", sha256="3e305930905397ff3a7a28a5d8cc2c9adca4194ca7f6ee51f749f427a2dea92c"
    )
    version(
        "2025.07.03", sha256="eb888fac7b0eec6b4f3bfa0bfe14e5c8f15b449286e84c45ba95c44d8cd3917a"
    )

    variant("dev", default=False, description="Include arkouda developer extras")

    depends_on("python@3.9:3.12.3", type=("build", "run"), when="@:2025.01.13")
    depends_on("python@3.9:3.13", type=("build", "run"), when="@2025.07.03:2025.08.20")
    depends_on("python@3.10:3.13", type=("build", "run"), when="@2025.09.30:")
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.25:1", when="@:2025.01.13", type=("build", "run"))
    depends_on("py-numpy@2", when="@2025.07.03:", type=("build", "run"))
    depends_on("py-pandas@2.2.3:", when="@2025.07.03:")
    depends_on("py-pandas@1.4.0:", type=("build", "run"))
    conflicts("^py-pandas@2.2.0", msg="arkouda client not compatible with pandas 2.2.0")
    depends_on("py-pyarrow", type=("build", "run"), when="@2025.12.16:")
    depends_on("py-pyarrow@:19", type=("build", "run"), when="@:2025.01.13")
    depends_on("py-pyarrow@15:19", type=("build", "run"), when="@2025.07.03:")
    depends_on("py-pyzmq@20:", type=("build", "run"))
    depends_on("py-scipy@:1.13.1", type=("build", "run"), when="@:2025.01.13")
    depends_on("py-scipy@1.14:", when="@2025.07.03:")
    depends_on("py-tables@3.8: +lzo +bzip2", type=("build", "run"))
    depends_on("py-tables@3.10: +lzo +bzip2", when="@2025.07.03:")
    depends_on("py-cloudpickle@2:", when="@2025.07.03:", type=("build", "run"))
    depends_on("py-h5py@3.7.0:", type=("build", "run"))
    depends_on("py-h5py@3.11:", when="@2025.07.03:")
    depends_on("py-matplotlib@3.9:", when="@2025.07.03:")
    depends_on("py-matplotlib@3.3.2:", type=("build", "run"))
    depends_on("py-contourpy@1.3:", when="@2025.07.03:")
    depends_on("py-versioneer", type=("build"))
    depends_on("py-pyfiglet", type=("build", "run"))
    depends_on("py-typeguard@2.10:2.12", type=("build", "run"))
    depends_on("py-tabulate", type=("build", "run"))
    depends_on("py-pytest@6.0:", type=("build", "run"), when="@2024.10.02")
