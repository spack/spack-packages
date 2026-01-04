# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Igv(Package):
    """The Integrative Genomics Viewer (IGV) is a high-performance visualization
    tool for interactive exploration of large, integrated genomic datasets.
    It supports a wide variety of data types, including array-based and
    next-generation sequence data, and genomic annotations."""

    homepage = "https://software.broadinstitute.org/software/igv/home"
    url = "https://data.broadinstitute.org/igv/projects/downloads/2.8/IGV_2.8.0.zip"

    maintainers("snehring")

    version("2.19.7", sha256="692ae6c3037a6633c33afdbbe960a715f537173f26a16f56a58cb9ccbe163e9f")
    version("2.18.4", sha256="d60870e27db0ba22278df3bcfb6113c1adc86b940f02d754983c91688d3a0fae")
    version("2.17.4", sha256="6a36ae64fa3b74182db654a93f6254256305a8afa6b878f381b5d04fc1e8eaa5")
    version("2.16.2", sha256="489d34ed4e807a3d32a3720f11248d2ddf1e21d264b06bea44fbe1ccb74b3aa2")
    version("2.12.3", sha256="c87a109deb35994e1b28dee80b5acfd623ec3257f031fcd9cfce008cd32a4cf2")
    version("2.8.0", sha256="33f3ac57017907b931f90c35b63b2de2e4f8d2452f0fbb5be39d30288fc9b2c6")

    depends_on("java@21:", when="@2.19:", type="run")
    depends_on("java@17:", when="@2.17:2.18", type="run")
    depends_on("java@11:", when="@:2.16", type="run")

    variant("igvtools", default=False, description="Include igvtools")

    def url_for_version(self, version):
        url = "https://data.broadinstitute.org/igv/projects/downloads/{0}/IGV_{1}.zip"
        return url.format(version.up_to(2), version)

    def install(self, spec, prefix):
        install_tree("lib", prefix.lib)
        mkdirp(prefix.bin)
        install("igv.args", prefix)
        files = ["igv.sh", "igv_hidpi.sh"]
        if spec.satisfies("+igvtools"):
            files.extend(["igvtools", "igvtools_gui", "igvtools_gui_hidpi"])
        for f in files:
            filter_file("^prefix=.*$", "prefix=" + prefix, f)
            filter_file(" java ", " {0} ".format(spec["java"].prefix.bin.java), f)
            set_executable(f)
            install(f, prefix.bin)
