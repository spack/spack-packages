# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os
import re

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *
from spack.util.windows_registry import RegistryError


class WinWdk(Package):
    """
    Windows Driver Kit development package
    """

    homepage = "https://learn.microsoft.com/en-us/windows-hardware/drivers/"
    has_code = False
    tags = ["windows", "windows-system"]

    # The wdk has many libraries and executables. Record one for detection purposes
    libraries = ["mmos.lib"]

    version("10.0.26100")
    version("10.0.22621")
    version("10.0.19041")
    version("10.0.18362")
    version("10.0.17763")
    version("10.0.17134")
    version("10.0.16299")
    version("10.0.15063")
    version("10.0.14393")

    variant(
        "plat", values=("x64", "x86", "arm", "arm64"), default="x64", description="Toolchain arch"
    )

    # need one to one dep on SDK per https://github.com/MicrosoftDocs/windows-driver-docs/issues/1550
    # additionally, the WDK needs to be paired with a version of the Windows SDK
    # as per https://learn.microsoft.com/en-us/windows-hardware/drivers/download-the-wdk#download-icon-step-2-install-windows-11-version-22h2-sdk
    depends_on("win-sdk@10.0.26100", when="@10.0.26100")
    depends_on("win-sdk@10.0.22621", when="@10.0.22621")
    depends_on("win-sdk@10.0.19041", when="@10.0.19041")
    depends_on("win-sdk@10.0.18362", when="@10.0.18362")
    depends_on("win-sdk@10.0.17763", when="@10.0.17763")
    depends_on("win-sdk@10.0.17134", when="@10.0.17134")
    depends_on("win-sdk@10.0.16299", when="@10.0.16299")
    depends_on("win-sdk@10.0.15063", when="@10.0.15063")
    depends_on("win-sdk@10.0.14393", when="@10.0.14393")

    for plat in ["linux", "darwin"]:
        conflicts("platform=%s" % plat)

    @classmethod
    def determine_version(cls, lib):
        """
        WDK is a set of drivers that we would like to
        be discoverable externally by Spack.
        The lib does not provide the WDK
        version so we derive from the lib path
        """
        version_match_pat = re.compile(r"[0-9][0-9].[0-9]+.[0-9][0-9][0-9][0-9][0-9]")
        ver_str = re.search(version_match_pat, lib)
        return ver_str if not ver_str else Version(ver_str.group())

    @classmethod
    def determine_variants(cls, libs, ver_str):
        """Allow for determination of toolchain arch for detected WGL"""
        variants = []
        for lib in libs:
            base, lib_name = os.path.split(lib)
            _, arch = os.path.split(base)
            variants.append("plat=%s" % arch)
        return variants

    @staticmethod
    def windows_kits_root():
        reg = WindowsRegistryView(
            "SOFTWARE\\Microsoft\\Windows Kits\\Installed Roots",
            root_key=HKEY.HKEY_LOCAL_MACHINE,
        )
        if not reg:
            return None
        try:
            value = reg.get_value("KitsRoot10")
            return value.value if value else None
        except RegistryError:
            return None

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        # This points to all core build extensions needed to build
        # drivers on Windows
        # The Kit is machine wide, so an external prefix may not be the registered Kits root
        env.set("WDKContentRoot", self.windows_kits_root() or self.prefix)

    def install(self, spec, prefix):
        raise RuntimeError(
            "This package is not installable from Spack and should be installed on the system "
            "prior to Spack use. The WDK is a component of the machine wide Windows Kits "
            "installation and cannot be relocated into a Spack prefix. Install it from "
            "https://learn.microsoft.com/en-us/windows-hardware/drivers/download-the-wdk "
            "making sure to match the version of the Windows SDK already on the system, then "
            "run `spack external find win-wdk` to make it available to Spack."
        )
