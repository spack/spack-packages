# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGcovr(PythonPackage):
    """Gcovr provides a utility for managing the use of the GNU gcov utility
    and generating summarized code coverage results. This command is inspired
    by the Python coverage.py package, which provides a similar utility for
    Python."""

    homepage = "https://gcovr.com/"
    pypi = "gcovr/gcovr-4.2.tar.gz"

    version("8.6", sha256="b2e7042abca9321cadbab8a06eb34d19f801b831557b28cdc30a029313de8b9e")
    version("8.5", sha256="9f0e21aab72b70fc26a4a0b6e35f25b97eefb5ce6e9c57388bf4a065726f7965")
    version("8.4", sha256="8ea0cf23176b1029f28db679d712ca6477b3807097c3755c135bdc53b51cfa72")
    version("8.3", sha256="faa371f9c4a7f78c9800da655107d4f99f04b718d1c0d9f48cafdcbef0049079")
    version("8.2", sha256="9a1dddd4585d13ec77555db5d6b6a31ee81587ea6fc604ff9fcd232cb0782df5")
    version("7.2", sha256="e3e95cb56ca88dbbe741cb5d69aa2be494eb2fc2a09ee4f651644a670ee5aeb3")
    version("5.2", sha256="217195085ec94346291a87b7b1e6d9cfdeeee562b3e0f9a32b25c9530b3bce8f")
    version("4.2", sha256="5aae34dc81e51600cfecbbbce3c3a80ce3f7548bc0aa1faa4b74ecd18f6fca3f")

    depends_on("python@3.10:", when="@8.6:", type=("build", "run"))
    depends_on("python@3.9:", when="@8.3:", type=("build", "run"))
    depends_on("python@3.8:", when="@7.2:", type=("build", "run"))
    depends_on("python@3.7:", when="@5.1:", type=("build", "run"))
    depends_on("python@3.6:", when="@5.0", type=("build", "run"))
    depends_on("python@2.7:2,3.5:", when="@:4", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"), when="@:8.2")
    depends_on("py-hatchling", when="@8.3:", type="build")
    depends_on("py-hatch-vcs", when="@8.3:", type="build")
    depends_on("py-hatch-fancy-pypi-readme", when="@8.3:", type="build")

    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-lxml", type=("build", "run"))
    depends_on("py-pygments", when="@5:", type=("build", "run"))
    depends_on("py-pygments@2.13.0:", when="@7.2:", type=("build", "run"))
    depends_on("py-colorlog", when="@7.2:", type=("build", "run"))
    depends_on("py-tomli@1.1:", when="@7.2: ^python@:3.10", type=("build", "run"))
