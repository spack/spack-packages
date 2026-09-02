# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import os

from spack_repo.builtin.build_systems.maven import MavenPackage

from spack.package import *


class Hpcserver(MavenPackage):
    """
    remote performance analysis. It runs on remote hosts holding HPCToolkit
    measurement databases, performing server-side parsing, indexing, and
    serving of performance data to GUI tools like hpcviewer, avoiding the need
    to download large profile directories locally
    """

    homepage = "https://gitlab.com/hpctoolkit/database"
    git = "https://gitlab.com/hpctoolkit/database.git"
    url = "https://gitlab.com/hpctoolkit/database/-/archive/1.4.0/database-1.4.0.tar.gz"

    maintainers("laksono")

    license("Apache-2.0")

    version("develop", branch="main")
    version("1.4.0", sha256="661806f9d2e2a4ebcc99f54853cb8d5188fc6a3ce0287af2c5ca93631461a373")
    version("1.3.1", sha256="beafbadd409720456833dcf9044f1ca34df41ac9c0be62c3432fa476344581ab")
    version("1.3.0", sha256="5658c4e043482ac01b8015a7aeac20e5fe54b170567a12f05a5ba71a532617f0")

    # -----------------------------------------------------------------------
    # Dependencies
    # -----------------------------------------------------------------------
    # Java is needed both to build (Maven runs on the JVM) and at runtime
    # (the server is a Java application).
    depends_on("java@17:25", type=("build", "run"))

    # -----------------------------------------------------------------------
    def install(self, spec, prefix):
        """Unpack the assembled tarball and bind the Spack JRE into the launcher."""

        # Locate the produced binary tarball.  Maven puts it under
        # server/target/ with the naming convention:
        #   org.hpctoolkit.db.server-<VERSION>-bin.tar.gz
        pattern = join_path(
            "server",
            "target",
            "org.hpctoolkit.db.server-*-bin.tar.gz",
        )
        tarballs = glob.glob(pattern)
        if not tarballs:
            raise InstallError(
                "Could not find the hpcserver binary tarball matching:\n"
                f"  {pattern}\n"
                "Check that 'mvn clean package' completed successfully."
            )
        # Take the most-recently modified match (there should be exactly one).
        tarball = max(tarballs, key=os.path.getmtime)

        # The tarball unpacks into a directory named
        # org.hpctoolkit.db.server-<VERSION>/  (no '-bin' suffix after extraction).
        # We install that directory tree directly into prefix.
        mkdirp(prefix)
        tar = which("tar")
        tar("xf", tarball, "-C", prefix, "--strip-components=1")

        # Bind the Spack-provided JRE so the launcher script uses the correct
        # Java regardless of what is in the user's PATH at runtime.
        bind_java = join_path(prefix, "share", "hpcserver", "bind-java.sh")
        if not os.path.isfile(bind_java):
            raise InstallError(
                f"bind-java.sh not found at expected location:\n  {bind_java}\n"
                "Check the tarball layout – the install prefix structure may have changed."
            )

        # bind-java.sh must be run from inside the installation directory.
        with working_dir(prefix):
            bash = which("bash")
            bash(bind_java)

    # -----------------------------------------------------------------------
    sanity_check_is_file = ["bin/hpcserver"]
