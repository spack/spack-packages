# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDramBio(PythonPackage):
    """Distilled and Refined Annotation of Metabolism: A tool for the annotation and
    curation of function for microbial and viral genomes."""

    homepage = "https://github.com/WrightonLabCSU/DRAM"
    pypi = "DRAM-bio/DRAM-bio-1.5.0.tar.gz"

    license("GPL-3.0")

    version("1.5.0", sha256="2d4a503fa806e33b580afb6d21879b2399178e48ba3b05ada882449fee571889")

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-scikit-bio", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-altair", type=("build", "run"))
    depends_on("py-sqlalchemy", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-openpyxl", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))

    # https://github.com/WrightonLabCSU/DRAM/commit/9ff00c9933723e6d628362b35d486f6dc68709f9
    patch(
        "https://github.com/WrightonLabCSU/DRAM/commit/9ff00c9933723e6d628362b35d486f6dc68709f9.patch?full_index=1",
        sha256="a67c933c7e0a78eca00ae48670d3b02724484ec26493a69ecb104d48d5e65211",
    )
