# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyToil(PythonPackage):
    """Pipeline management software for clusters."""

    homepage = "https://github.com/DataBiosphere/toil"
    pypi = "toil/toil-9.5.0.tar.gz"

    supplier = "Benedict Paten and the Toil community"

    maintainers("mr-c")
    license("Apache-2.0", checked_by="mr-c")

    version("9.5.0", sha256="dae9a12b0f277355170129be38406c831da47054758e64d6693e18d7e5b45d3f")

    depends_on("python@3.10:", type=("build", "run"))

    variant(
        "aws",
        default=False,
        description=(
            "Provides support for managing a cluster on Amazon Web "
            "Service ('AWS') using Toil's built in 'clusterUtils'. "
            "Clusters can scale up and down automatically. "
            "It also supports storing workflow state."
        ),
    )
    # variant(
    #     "google",
    #     default=False,
    #     description="Experimental. Stores workflow state in 'Google Cloud Storage'.",
    # )
    variant(
        "cwl",
        default=False,
        description=(
            "Provides support for running workflows written using the 'Common Workflow Language'."
        ),
    )
    # variant(
    #     "mesos",
    #     default=False,
    #     description=(
    #         "Provides support for running Toil on an 'Apache Mesos' cluster. "
    #         "Note that running Toil on other batch systems does not require an extra."
    #     ),
    # )  # deprecated
    # variant("htcondor", default=False, description="Support for the htcondor batch system.")
    variant(
        "encryption",
        default=False,
        description="Provides client-side encryption for files stored in the AWS job store.",
    )

    with default_args(type="build"):
        depends_on("py-setuptools@64:")
        depends_on("py-setuptools-scm@8:")

    with default_args(type=("build", "run")):
        depends_on("py-dill@0.3.2:0.4")
        depends_on("py-requests@:2.33.1")
        depends_on("py-docker@6.1")
        depends_on("py-urllib3@1.26:2")
        depends_on("py-python-dateutil")
        depends_on("py-psutil@6.1.0:7")
        depends_on("py-pypubsub@4.0.3:5")
        depends_on("py-addict@2.2.1:2.4")
        depends_on("py-enlighten@1.5.2:2")
        depends_on("py-configargparse@1.7:1")
        depends_on("py-ruamel-yaml@0.15:")
        depends_on("py-pyyaml@6:6")
        depends_on("py-typing-extensions@4.6.2:4")
        depends_on("py-coloredlogs@15:15")
        depends_on("py-prompt-toolkit@3")
        depends_on("py-cwltool@3.2.20260413085819", when="+cwl")
        depends_on("py-schema-salad@8.4.20230128170514:8", when="+cwl")
        depends_on("py-galaxy-tool-util@:27", when="+cwl")
        depends_on("py-galaxy-util@:27", when="+cwl")
        depends_on("py-ruamel-yaml@0.15:0.19.1", when="+cwl")
        depends_on("py-ruamel-yaml-clib@0.2.6:", when="+cwl")
        depends_on("py-cachecontrol+filecache", when="+cwl")
        depends_on("py-cwl-utils@0.41:", when="+cwl")
        # depends_on("py-apache-libclouds@3.6.1:4", when="+google")  ## not yet in spack
        # depends_on("py-google-cloud-storage@2:2.8", when="+google")
        # depends_on("py-google-auth@2.18.1:2", when="+google")
        depends_on("py-pynacl@1.4:1", when="+encryption")

    @property
    def import_modules(self):
        modules = [
            "toil",
            "toil.batchSystems",
            "toil.provisioners",
            "toil.lib",
            "toil.server",
            "toil.jobStores",
            "toil.utils",
            "toil.fileStores",
            "toil.wdl",
            "toil.options",
            "toil.lib.encryption",
            "toil.server.wes",
            "toil.server.api_spec",
            "toil.server.cli",
        ]
        if self.spec.satisfies("+cwl"):
            modules.append("toil.cwl")
        if self.spec.satisfies("+mesos"):
            modules.append("toil.batchSystems.mesos")
        if self.spec.satisfies("+aws"):
            modules.append("toil.provisioners.aws")
        return modules
