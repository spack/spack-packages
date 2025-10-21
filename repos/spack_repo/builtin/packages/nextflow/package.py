# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Nextflow(Package):
    """Data-driven computational pipelines."""

    homepage = "https://www.nextflow.io"
    url = "https://github.com/nextflow-io/nextflow/releases/download/v21.04.3/nextflow"

    maintainers("dialvarezs", "marcodelapierre")

    version(
        "25.04.6",
        sha256="a94f8bd1db9c0271ad58ec40b9c71f812d081a66f782396928b9b1f740f0be5f",
        expand=False,
    )
    version(
        "25.04.3",
        sha256="f33571f9298e930993aa4afcde84bc0d0815a59ee7168d8a153093ad08e9b263",
        expand=False,
    )
    version(
        "25.04.0",
        sha256="33d888b1e0127566950719316bac735975e15800018768cceb7d3d77ad0719eb",
        expand=False,
    )
    version(
        "24.10.9",
        sha256="9080820f9c36a08d166d509a6c6df15a1de2e3e04b969aaeef148ef2d87e3025",
        expand=False,
    )
    version(
        "24.10.5",
        sha256="a9733a736cfecdd70e504b942e823da7005f9afc288902e67afe86b43dc9bcdb",
        expand=False,
    )
    version(
        "24.10.3",
        sha256="01110949bb3256bf6cbf1d4b3ea17369491b3f693b6d86a0c9ab8171b1619ba0",
        expand=False,
    )
    version(
        "24.10.2",
        sha256="e12bf1fc1e11629f2aef22a9a6ddecc31522bcd5988d1c48d263de699b4e5289",
        expand=False,
    )
    version(
        "24.10.0",
        sha256="e848918fb9b85762822c078435d9ff71979a88cccff81ce5babd75d5eee52fe6",
        expand=False,
    )
    version(
        "24.04.6",
        sha256="77f43bc1c3d1749a68f294ae07e5cc0ffadde92f57106ea9711c4bafd68a6c64",
        expand=False,
    )
    version(
        "24.04.3",
        sha256="e258f6395a38f044eb734cba6790af98b561aa521f63e2701fe95c050986e11c",
        expand=False,
    )
    version(
        "24.04.1",
        sha256="d1199179e31d0701d86e6c38afa9ccade93f62d545e800824be7767a130510ba",
        expand=False,
    )
    version(
        "23.10.1",
        sha256="9abc54f1ffb2b834a8135d44300404552d1e27719659cbb635199898677b660a",
        expand=False,
    )
    version(
        "23.10.0",
        sha256="4b7fba61ecc6d53a6850390bb435455a54ae4d0c3108199f88b16b49e555afdd",
        expand=False,
    )
    version(
        "23.04.3",
        sha256="258714c0772db3cab567267e8441c5b72102381f6bd58fc6957c2972235be7e0",
        expand=False,
    )
    version(
        "23.04.1",
        sha256="5de3e09117ca648b2b50778d3209feb249b35de0f97cdbcf52c7d92c7a96415c",
        expand=False,
    )
    version(
        "22.10.4",
        sha256="612a085e183546688e0733ebf342fb73865f560ad1315d999354048fbca5954d",
        expand=False,
    )
    version(
        "22.10.3",
        sha256="8d67046ca3b645fab2642d90848550a425c9905fd7dfc2b4753b8bcaccaa70dd",
        expand=False,
    )
    version(
        "22.10.1",
        sha256="fa6b6faa8b213860212da413e77141a56a5e128662d21ea6603aeb9717817c4c",
        expand=False,
    )
    version(
        "22.10.0",
        sha256="6acea8bd21f7f66b1363eef900cd696d9523d2b9edb53327940f093189c1535e",
        expand=False,
    )
    version(
        "22.04.4",
        sha256="e5ebf9942af4569db9199e8528016d9a52f73010ed476049774a76b201cd4b10",
        expand=False,
    )
    version(
        "22.04.3",
        sha256="a1a79c619200b9f2719e8467cd5b8fbcb427f43adf945233ba9e03cd2f2d814e",
        expand=False,
    )
    version(
        "22.04.1",
        sha256="89ef482a53d2866a3cee84b3576053278b53507bde62db4ad05b1fcd63a9368a",
        expand=False,
    )
    version(
        "22.04.0",
        sha256="8eba475aa395438ed222ff14df8fbe93928c14ffc68727a15b8308178edf9056",
        expand=False,
    )

    depends_on("java", type="run")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(self.stage.archive_file, join_path(prefix.bin, "nextflow"))
        set_executable(join_path(prefix.bin, "nextflow"))
