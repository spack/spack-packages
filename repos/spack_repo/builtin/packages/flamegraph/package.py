# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Flamegraph(Package):
    """FlameGraph is a stack trace visualizer that produces interactive
    SVG flame graphs from profiling data collected by Linux perf,
    DTrace, SystemTap, and other profilers. Developed by Brendan Gregg."""

    homepage = "https://www.brendangregg.com/flamegraphs.html"
    url = "https://github.com/brendangregg/FlameGraph/archive/refs/tags/v1.0.tar.gz"
    git = "https://github.com/brendangregg/FlameGraph.git"

    maintainers("CodingYayaToure")

    license("CDDL-1.0")

    version("1.0", sha256="c5ba824228a4f7781336477015cb3b2d8178ffd86bccd5f51864ed52a5ad6675")

    depends_on("perl", type="run")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        scripts = [
            "flamegraph.pl",
            "stackcollapse-perf.pl",
            "stackcollapse.pl",
            "stackcollapse-recursive.pl",
            "difffolded.pl",
            "flamechart.pl",
        ]
        for script in scripts:
            if os.path.exists(script):
                install(script, prefix.bin)
                os.chmod(join_path(prefix.bin, script), 0o755)
