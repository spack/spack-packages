# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMultiqc(PythonPackage):
    """MultiQC is a tool to aggregate bioinformatics results across many
    samples into a single report. It is written in Python and contains modules
    for a large number of common bioinformatics tools."""

    homepage = "https://multiqc.info"
    pypi = "multiqc/multiqc-1.0.tar.gz"

    license("GPL-3.0-only", checked_by="A_N_Other")
    maintainers("ewels", "vladsavelyev")

    version("1.34", sha256="859a54f8d1cf6b55c367d885860ad3c2b423e63b8804485ef065b77f4ffee58e")
    version("1.33", sha256="06e2b82fd9bfa458a79d8da869cb7d88260f624c03297120a70446a49ce852ed")
    version("1.32", sha256="753908c16256bda6371e094d6a7dd5e9d15a43648e7ffa9a38a34a8bc29a127f")
    version("1.31", sha256="3e2e4202ed335cd0651733018f6fe1dc8faf982cc335e837cf2a54bbd7646152")
    version("1.30", sha256="4e5e4af10c965b9139c97620bb2174e558143aa4116a7aa969f6065b848183d8")
    version("1.29", sha256="14e61bcb710caee59a7f6037d6a255f3062f6032e760734a351d9dd8a8be2609")
    version("1.28", sha256="3cb65ac9ca07b6146fb239e0bc42f5337808973cb37e1d9a8bd753eaf70ac7e7")
    version("1.23", sha256="4e84664000fec69a0952a0457a8d780dcc1ce9e36d14680dbdba5610b9766265")

    depends_on("py-setuptools", type="build")

    depends_on("py-click", type=("build", "run"))
    depends_on("py-humanize", type=("build", "run"))
    depends_on("py-importlib-metadata", type=("build", "run"))
    depends_on("py-jinja2@3.0.0:", type=("build", "run"))
    depends_on("py-jsonschema", type=("build", "run"))
    depends_on("py-kaleido@0.2.1", type=("build", "run"))
    depends_on("py-markdown", type=("build", "run"))
    depends_on("py-natsort", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-pillow@10:", type=("build", "run"))
    depends_on("py-plotly@5.18:", type=("build", "run"))
    depends_on("py-pyyaml@4:", type=("build", "run"))
    depends_on("py-pyaml-env", type=("build", "run"))
    depends_on("py-pydantic@2.7.1:", type=("build", "run"))
    depends_on("py-python-dotenv", type=("build", "run"))
    depends_on("py-rich@10:", type=("build", "run"))
    depends_on("py-rich-click", type=("build", "run"))
    depends_on("py-coloredlogs", type=("build", "run"))
    depends_on("py-spectra@0.0.10:", type=("build", "run"))
    depends_on("py-tiktoken", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-typeguard", type=("build", "run"))
    depends_on("py-boto3", type=("build", "run"), when="@1.29:")
    depends_on("py-pyarrow", type=("build", "run"), when="@1.29:")
    # 1.30+ declare polars-lts-cpu, PyPI's build of polars for CPUs without AVX2
    depends_on("py-polars", type=("build", "run"), when="@1.29:")
    # 1.31's new xenium module imported scanpy and scipy; 1.32 reworked it without them
    depends_on("py-scanpy", type=("build", "run"), when="@1.31")
    depends_on("py-scipy", type=("build", "run"), when="@1.31")
