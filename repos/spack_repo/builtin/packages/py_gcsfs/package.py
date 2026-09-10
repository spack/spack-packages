# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGcsfs(PythonPackage):
    """Pythonic file-system for Google Cloud Storage."""

    homepage = "https://github.com/fsspec/gcsfs"
    pypi = "gcsfs/gcsfs-2023.1.0.tar.gz"

    license("BSD-3-Clause")

    version("2025.9.0", sha256="36b8c379d9789d5332a45a3aa2840ec518ff73c6d21c1e962f53318d1cd65db9")
    version("2024.2.0", sha256="f7cffd7cae2fb50c56ef883f8aef9792be045b5059f06c1902c3a6151509f506")
    version("2023.1.0", sha256="0a7b7ca8c1affa126a14ba35d7b7dff81c49e2aaceedda9732c7f159a4837a26")

    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-aiohttp")
        depends_on("py-decorator@4.1.3:")
        for v in ["2025.9.0", "2024.2.0", "2023.1.0"]:
            depends_on(f"py-fsspec@{v}", when=f"@{v}")
        depends_on("py-google-auth@1.2:")
        depends_on("py-google-auth-oauthlib")
        depends_on("py-google-cloud-storage")
        depends_on("py-requests")
