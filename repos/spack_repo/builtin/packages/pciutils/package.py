# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import os

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Pciutils(MakefilePackage):
    """This package contains the PCI Utilities."""

    homepage = "https://mj.ucw.cz/sw/pciutils/"
    url = "https://github.com/pciutils/pciutils/archive/v3.7.0.tar.gz"

    license("GPL-2.0-only")

    version("3.7.0", sha256="ea768aa0187ba349391c6c157445ecc2b42e7d671fc1ce8c53ff5ef513f1e2ab")
    version("3.6.4", sha256="551d0ac33f030868b7e95c29e58dc2b1882455dbc9c15c15adf7086e664131f1")
    version("3.6.3", sha256="7ab0fbb35cffa326eb852539260562bac14f3d27cda8c70bc2cf3211ed97c014")

    variant("shared", default=False, description="Build shared libraries instead of static ones")

    depends_on("c", type="build")  # generated

    def build(self, spec, prefix):
        args = ["PREFIX={0}".format(prefix)]
        if "+shared" in spec:
            args.append("SHARED=yes")
        make(*args)

    def install(self, spec, prefix):
        if "+shared" in spec:
            make("install-lib", "install", "PREFIX={0}".format(prefix))
            # Find the actual shared library file (libpci.so.*) and create the symlink
            lib_dir = self.prefix.lib
            so_candidates = sorted(glob.glob(os.path.join(lib_dir, "libpci.so.*")), reverse=True)
            # Exclude the symlink itself if it exists
            so_candidates = [f for f in so_candidates if os.path.basename(f) != "libpci.so"]
            if so_candidates:
                symlink_path = os.path.join(lib_dir, "libpci.so")
                # Remove existing symlink or file if present
                if os.path.islink(symlink_path) or os.path.exists(symlink_path):
                    os.remove(symlink_path)
                os.symlink(os.path.basename(so_candidates[0]), symlink_path)
                major_version = str(self.version).split(".")[0]
                libname = f"libpci.so.{major_version}"
                symlink_path = os.path.join(lib_dir, libname)
                os.symlink(os.path.basename(so_candidates[0]), symlink_path)
        else:
            make("install", "PREFIX={0}".format(prefix))

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("PATH", self.prefix.sbin)
