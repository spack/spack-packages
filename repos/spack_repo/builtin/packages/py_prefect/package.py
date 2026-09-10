# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPrefect(PythonPackage):
    """Prefect is a workflow orchestration framework for building resilient
    data pipelines in Python."""

    homepage = "https://www.prefect.io/"
    pypi = "prefect/prefect-3.6.10.tar.gz"

    license("Apache-2.0")

    version("3.6.10", sha256="b300aecdb26fde32f34c6689d29a2f9782fdcbe54107460470ba6097201e3179")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-versioningit", type="build")

    depends_on("py-aiosqlite@0.17:0", type=("build", "run"))
    depends_on("py-alembic@1.7.5:1", type=("build", "run"))
    depends_on("py-apprise@1.1:1", type=("build", "run"))
    depends_on("py-asyncpg@0.23:0", type=("build", "run"))
    depends_on("py-click@8", type=("build", "run"))
    depends_on("py-cryptography@36.0.1:", type=("build", "run"))
    depends_on("py-dateparser@1.1.1:1", type=("build", "run"))
    depends_on("py-docker@4:7", type=("build", "run"))
    depends_on("py-jinja2@3.1.6:3", type=("build", "run"))
    depends_on("py-jinja2-humanize-extension@0.4:", type=("build", "run"))
    depends_on("py-pytz@2021.1:2025", type=("build", "run"))
    depends_on("py-readchar@4", type=("build", "run"))
    depends_on("py-sqlalchemy@2 +asyncio", type=("build", "run"))
    depends_on("py-typer@0.16:0.20", type=("build", "run"))

    depends_on("py-anyio@4.4:4", type=("build", "run"))
    depends_on("py-asgi-lifespan@1:2", type=("build", "run"))
    depends_on("py-cachetools@5.3:6", type=("build", "run"))
    depends_on("py-cloudpickle@2:3", type=("build", "run"))
    depends_on("py-coolname@1.0.4:2", type=("build", "run"))
    depends_on("py-exceptiongroup@1:", type=("build", "run"))
    depends_on("py-fastapi@0.111:0", type=("build", "run"))
    depends_on("py-fsspec@2022.5:", type=("build", "run"))
    depends_on("py-graphviz@0.20.1:", type=("build", "run"))
    depends_on("py-griffe@0.49:1", type=("build", "run"))
    depends_on("py-httpcore@1.0.5:1", type=("build", "run"))
    depends_on("py-httpx@0.23: +http2", type=("build", "run"))
    depends_on("py-humanize@4.9:4", type=("build", "run"))
    depends_on("py-jsonpatch@1.32:1", type=("build", "run"))
    depends_on("py-jsonschema@4.18:4", type=("build", "run"))
    depends_on("py-opentelemetry-api@1.27:1", type=("build", "run"))
    depends_on("py-orjson@3.7:3", type=("build", "run"))
    depends_on("py-packaging@21.3:25.0", type=("build", "run"))
    depends_on("py-pathspec@0.8:", type=("build", "run"))
    depends_on("py-pendulum@3", when="^python@:3.12", type=("build", "run"))
    depends_on("py-prometheus-client@0.20:", type=("build", "run"))
    depends_on("py-pydantic@2.10.1:2", type=("build", "run"))
    depends_on("py-pydantic-core@2.12:2", type=("build", "run"))
    depends_on("py-pydantic-extra-types@2.8.2:2", type=("build", "run"))
    depends_on("py-pydantic-settings@2.2.1:2", type=("build", "run"))
    depends_on("py-python-dateutil@2.8.2:2", type=("build", "run"))
    depends_on("py-python-slugify@5:8", type=("build", "run"))
    depends_on("py-pyyaml@5.4.1:6", type=("build", "run"))
    depends_on("py-rfc3339-validator@0.1.4:0.1", type=("build", "run"))
    depends_on("py-rich@11:14", type=("build", "run"))
    depends_on("py-ruamel-yaml@0.17:", type=("build", "run"))
    depends_on("py-ruamel-yaml-clib@0.2.8:", type=("build", "run"))
    depends_on("py-sniffio@1.3:1", type=("build", "run"))
    depends_on("py-toml@0.10:", type=("build", "run"))
    depends_on("py-typing-extensions@4.10:4", type=("build", "run"))
    depends_on("py-uvicorn@0.14:", type=("build", "run"))
    depends_on("py-websockets@15.0.1:15", type=("build", "run"))
    depends_on("py-whenever@0.7.3:0.9", when="^python@3.13:", type=("build", "run"))
    depends_on("py-semver@3.0.4:", type=("build", "run"))
    depends_on("py-pluggy@1.6:", type=("build", "run"))
    depends_on("py-docket@0.16.2:", type=("build", "run"))

    conflicts("^py-httpx@0.23.2")
    conflicts("^py-pydantic@2.11.0:2.11.4")
    conflicts("^py-pydantic-settings@2.9.0")
    conflicts("^py-uvicorn@0.29.0")
