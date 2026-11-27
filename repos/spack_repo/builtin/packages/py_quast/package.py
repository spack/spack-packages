# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQuast(PythonPackage):
    """Quality Assessment Tool for Genome Assemblies"""

    homepage = "https://cab.spbu.ru/software/quast"
    pypi = "quast/quast-5.2.0.tar.gz"

    license("GPL-2.0-only")

    version("5.2.0", sha256="23649fbd93253c6da982c0b67d719f9262461deecdc6dffbd690b75dfd790ad7")
    version("5.0.2", sha256="cdb8f83e20cc38f218ff7172b454280fcb1c7e2dff74e1f8618cacc53d46b48e")
    version("5.0.1", sha256="b1e4443b6598b01faaefddfc0f06fb270414ed4bdaffd0ad9aa420bc0d07d8ad")
    version("5.0.0", sha256="46bba247c7f92c2ccaca8c0abeab2a8d40a257a0cbe2fa0a4ffa981ca0267526")
    version("4.6.3", sha256="f9267e5deadf20cfe67731a42e775e7ef1d0850927a2a76c4b3d49bc77b1fab5")
    version("4.6.1", sha256="7ace5bebebe9d2a70ad45e5339f998bd651c1c6b9025f7a3b51f44c87ea5bae0")
    version("4.6.0", sha256="3a7ee7a2abfeb0541b299b67f263ba95f9743f8809ddf5dfaca9c3c8f9b6a215")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    # No real boost dependency: setup.py never references boost at all
    # (confirmed by grepping the actual sdist). The upstream package.py's
    # depends_on("boost@1.56.0") is vestigial, most likely inherited by
    # copy-paste from the vendored BamTools/bedtools copies bundled
    # inside quast_libs/ -- but those vendored copies aren't what gets
    # built here, Spack's own separate bedtools2/glimmer/bwa deps below
    # are. The pin drags in an ancient (2014) boost whose own bjam
    # bootstrap hits an unrelated ICU duplicate-target bug on this
    # system; dropping the pin avoids that whole rabbit hole for a
    # dependency quast doesn't actually use.
    depends_on("perl@5.6.0:", type=("build", "run"))
    depends_on("python@2.5:,3.3:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-joblib", type=("build", "run"))
    depends_on("py-simplejson", type=("build", "run"))
    depends_on("java", type=("build", "run"))
    depends_on("perl-time-hires", type=("build", "run"))
    depends_on("gnuplot", type=("build", "run"))
    depends_on("mummer", type=("build", "run"))
    depends_on("bedtools2", type=("build", "run"))
    depends_on("bwa", type=("build", "run"))
    depends_on("glimmer", type=("build", "run"))
    depends_on("gmake", type="build")
    depends_on("zlib-api", type="build")

    def patch(self):
        # qconfig.py imports distutils.version.LooseVersion just to check
        # the running Python falls within quast's own supported-version
        # range -- distutils was removed from the stdlib in Python 3.12+.
        # packaging.version.Version is a drop-in for the comparison usage
        # here (Version(str), <, <=).
        filter_file(
            "from distutils.version import LooseVersion",
            "from packaging.version import Version as LooseVersion",
            "quast_libs/qconfig.py",
            string=True,
        )

    @run_after("install")
    def compile_bundled_minimap2(self):
        # quast bundles its own minimap2 source under quast_libs/minimap2
        # and, by design, lazily runs `make` there the first time a user
        # actually needs it (ca_utils/misc.py's get_path_to_program ->
        # compile_tool). That's fine for a normal per-user pip install,
        # but under Spack the install tree is only writable by whoever
        # ran `spack install` -- any other user running `quast.py -r`
        # (reference alignment, the single most common invocation) hits
        # a PermissionError trying to write quast_libs/minimap2/minimap2.
        # Do the one-time compile ourselves during install, while we
        # still have write access, so it's already cached for everyone.
        import glob

        minimap2_dirs = glob.glob(
            join_path(self.prefix, "lib", "python*", "site-packages", "quast_libs", "minimap2")
        )
        make = which("make")
        for d in minimap2_dirs:
            make("-C", d)
