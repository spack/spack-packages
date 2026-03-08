# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Freeimage(MakefilePackage):
    """FreeImage is an Open Source library project for developers who would like
    to support popular graphics image formats like PNG, BMP, JPEG, TIFF and
    others as needed by today's multimedia applications"""

    homepage = "https://freeimage.sourceforge.net/"

    # FreeImage 3.18.0 is the final release (project abandoned ~2020) and is affected by:
    # - CVE-2019-12211 (CVSS 7.5 HIGH): heap buffer overflow in PluginTIFF.cpp
    # - CVE-2019-12212 (CVSS 7.5 HIGH): infinite recursion in JXRMeta.c (stack overflow)
    # - CVE-2020-21426 (CVSS 7.8 HIGH): buffer overflow in PluginEXR.cpp (code execution)
    # - CVE-2020-21428 (CVSS 7.8 HIGH): buffer overflow in PluginDDS.cpp (code execution)
    # - CVE-2023-47992 (CVSS 8.8 HIGH): integer overflow in FreeImageIO.cpp (RCE)
    # - CVE-2023-47994 (CVSS 8.8 HIGH): integer overflow in PluginBMP.cpp (code execution)
    # No upstream fix available; project is unmaintained.
    with default_args(deprecated=True):
        version("3.18.0", sha256="f41379682f9ada94ea7b34fe86bf9ee00935a3147be41b6569c9605a53e438fd")

    patch("install_fixes.patch", when="@3.18.0")

    def edit(self, spec, prefix):
        env["DESTDIR"] = prefix
        env["CXXFLAGS"] = "-std=c++14"

    def url_for_version(self, version):
        url = "https://downloads.sourceforge.net/project/freeimage/Source%20Distribution/{0}/FreeImage{1}.zip"
        return url.format(version, version.joined)
