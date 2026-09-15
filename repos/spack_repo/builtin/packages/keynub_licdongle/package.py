# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class KeynubLicdongle(Package):
    """KeyNub USB-C license dongle SDK: the C API, a header-only C++11 wrapper and
    the flat companion API over the prebuilt keynub_licdongle shared library.
    The library ships prebuilt for Windows, Linux and macOS on x86_64 and arm64;
    nothing is compiled here."""

    homepage = "https://www.keynub.com/developers/c-cpp/"
    url = "https://github.com/AB-KeyNub/KeyNub-SDK/archive/refs/tags/v1.1.1.tar.gz"
    git = "https://github.com/AB-KeyNub/KeyNub-SDK.git"

    maintainers("ab-tools")

    license("Apache-2.0", checked_by="ab-tools")

    version("1.1.1", sha256="3a8242fc9a19cd6c04f1abc9e23c17374ba48712089f49c4d9f6e1830321513a")

    requires(
        "target=x86_64:",
        "target=aarch64:",
        policy="one_of",
        msg="prebuilt for x86_64 and arm64 only",
    )
    requires(
        "platform=linux",
        "platform=darwin",
        "platform=windows",
        policy="one_of",
        msg="prebuilt for Linux, macOS and Windows only",
    )

    @property
    def _natives(self):
        os_name = {"linux": "linux", "darwin": "osx", "windows": "win"}[str(self.spec.platform)]
        arch_name = {"x86_64": "x64", "aarch64": "arm64"}[str(self.spec.target.family)]
        return join_path("natives", f"{os_name}-{arch_name}")

    def install(self, spec, prefix):
        mkdirp(prefix.include)
        install("include/licdongle.h", prefix.include)
        install("bindings/cpp/licdongle.hpp", prefix.include)
        install("bindings/flat/licd_flat.h", prefix.include)
        install("bindings/labview/licd_labview.h", prefix.include)

        natives = self._natives
        mkdirp(prefix.lib)
        if spec.satisfies("platform=windows"):
            mkdirp(prefix.bin)
            for name in ("keynub_licdongle", "keynub_licdongle_flat"):
                install(join_path(natives, name + ".dll"), prefix.bin)
                install(join_path(natives, name + ".lib"), prefix.lib)
            install(join_path(natives, "keynub_licdongle_static.lib"), prefix.lib)
        else:
            for lib in find(natives, "libkeynub_licdongle*", recursive=False):
                install(lib, prefix.lib)

        for name in ("LICENSE", "BINARY-LICENSE.txt", "NOTICE", "THIRD-PARTY-NOTICES.txt"):
            install(name, prefix)
