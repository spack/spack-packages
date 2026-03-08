# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRucioClients(PythonPackage):
    """Rucio Client Lite Package"""

    homepage = "https://rucio.cern.ch/"
    pypi = "rucio_clients/rucio_clients-35.4.0.tar.gz"

    maintainers("wdconinc")

    license("Apache-2.0", checked_by="wdconinc")

    version("39.3.0", sha256="e6890df6b25785a3ff2006774fceeafd9541e6b710b288efaf72ff1f598213eb")
    version("39.2.0", sha256="830d232928b10aad2aa471ec2ea71023b930a3b73d4c7e895f79f1cba101af27")
    version("39.1.0", sha256="5c83a6c0b1c0823e7b95f6569c6478698c433db1901d8398d3844f48a2728aca")
    version("39.0.0", sha256="a83632897cfc2cc9052848b1b795fb71b2cf8d0a7920a6cff1f7367874bac72a")
    version("38.5.3", sha256="7457d8d91e4b33bc760495974bc160b2e823f217f5cfaa98034e9bd644d8950b")
    version("38.5.2", sha256="d3ef7f2a834df762aa28c6535ace4ee575b8096952f9d446f2d15da43a294507")
    version("38.5.1", sha256="3cfe97c5e5996cfc5861b259ff0bed3369e7379bcaa826b6d181ee5b939ac401")
    version("38.5.0", sha256="f0379a3efc9ba948ecbc8bf96d6c325aa79156b344a95b7f2358b43371792e9f")
    version("38.4.0", sha256="bf4bbb21f514156f6ca975f981583a1f8f8af9ca7e41b77ae20c10147fc5d3fb")
    version("38.3.0", sha256="49f8809b5378d1c9e9edc5f1a74fbf7eebe45db27084945f748b2c73a841efed")
    version("38.2.0", sha256="7495d7274e17e4099f9ccd2672667236e17f806292954387145e99c7c688414a")
    version("38.1.0", sha256="69a4197fdad548671a3ab8322f181f62b13d8aaa3e2e96ebdbc6d3a434fd0062")
    version("38.0.0", sha256="d49f912f2f98870cab2227e0464129ba0954e99b975d0225126cca1b9d9c983c")
    version("37.3.0", sha256="b4bca8d451bc34528797ca188884a0c8b5ddfef2d32803765e6333455879f819")
    version(
        "36.0.0.post2", sha256="48ac2e3217aac9aaa70133cbfff991560bbeb162165bcf3dd3425967c8a2f816"
    )
    version(
        "36.0.0.post1", sha256="141aafdde66080d36708dedc9f06a72c55918ee1d138b8cd2f5d2fe43cbc504f"
    )
    version("36.0.0", sha256="80fbf3b2ec63c13ac1ce430d769fcc526a5f742ba3960ecc64560e0d4cd465b5")
    version("35.6.0", sha256="3c77dea0ce95b7649211da08cee7e93fa9ecb1a6c91bbe750b76b4c576a8b0dd")
    version("35.5.0", sha256="bc79602193e271f66c3fdb43e7abda7903026795d6f3c5d71afb5e52250f8d92")
    version("35.4.1", sha256="d87405785776d7522100cda2ebc16892f94cda94d3c257896ee4817c4e03c06b")
    version("35.4.0", sha256="f8771ee39d0d496109586ddbb4000ce006a193fd33cdac8a654661ae0b7346c0")

    variant("ssh", default=False, description="Enable SSH2 protocol library")
    variant("kerberos", default=False, description="Enable kerberos authentication")
    variant("swift", default=False, description="Enable support for swift service")
    variant("argcomplete", default=False, description="Enable bash tab completion for argparse")
    variant("dumper", default=False, description="Enable file type identification using libmagic")

    # requirements/requirements.client.txt
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-requests@2.32.2:", type=("build", "run"), when="@:36")
    depends_on("py-urllib3@1.26.18:", type=("build", "run"), when="@:36")
    depends_on("py-requests@2.32.3:", type=("build", "run"), when="@37:")
    depends_on("py-urllib3@2.3.0:", type=("build", "run"), when="@37:")
    depends_on("py-dogpile-cache@1.2.2:", type=("build", "run"))
    depends_on("py-tabulate@0.9.0:", type=("build", "run"))
    depends_on("py-jsonschema@4.20.0:", type=("build", "run"), when="@:36")
    depends_on("py-jsonschema@4.23.0:", type=("build", "run"), when="@37:")
    depends_on("py-packaging@24.1:", type=("build", "run"), when="@36:")
    depends_on("py-packaging@24.2:", type=("build", "run"), when="@37:")
    depends_on("py-rich@13.7.1:", type=("build", "run"), when="@36:")
    depends_on("py-rich@13.9.4:", type=("build", "run"), when="@37:")
    depends_on("py-typing-extensions@4.12.2:", type=("build", "run"))
    depends_on("py-typing-extensions@4.14.0:", type=("build", "run"), when="@38:")
    depends_on("py-click@8.1.7:", type=("build", "run"), when="@37:")

    with when("+ssh"):
        depends_on("py-paramiko@3.4.0:", when="@:36")
        depends_on("py-paramiko@3.5.1:", when="@37:")

    with when("+kerberos"):
        depends_on("py-kerberos@1.3.1:")
        depends_on("py-pykerberos@1.2.4:")
        depends_on("py-requests-kerberos@0.14.0:", when="@:36")
        depends_on("py-requests-kerberos@0.15.0:", when="@37:")

    with when("+swift"):
        depends_on("py-python-swiftclient@4.4.0:", when="@:36")
        depends_on("py-python-swiftclient@4.7.0:", when="@37:")

    with when("+argcomplete"):
        depends_on("py-argcomplete@3.1.6:", when="@:36")
        depends_on("py-argcomplete@3.5.3:", when="@37:")

    with when("+dumper"):
        depends_on("py-python-magic@0.4.27:")
