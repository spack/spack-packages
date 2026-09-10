# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAudioread(PythonPackage):
    """cross-library (GStreamer + Core Audio + MAD + FFmpeg) audio decoding for
    Python."""

    homepage = "https://github.com/beetbox/audioread"
    pypi = "audioread/audioread-2.1.8.tar.gz"

    license("MIT")

    version("3.1.0", sha256="1c4ab2f2972764c896a8ac61ac53e261c8d29f0c6ccd652f84e18f08a4cab190")
    version("2.1.8", sha256="073904fabc842881e07bd3e4a5776623535562f70b1655b635d22886168dd168")

    depends_on("py-setuptools", type="build")
    depends_on("py-poetry-core", type="build")
    # the following does not seem to be used for building but is listed in
    # setup.py
    depends_on("py-pytest-runner", type="build")

    conflicts(
        "^python@3.12:",
        when="@:3.0.0",
        msg="python@3.12 dropped imp, use py-audioread >= 3.0.1 for 3.12 support",
    )

    conflicts(
        "^python@:3.8",
        when="@3.1:",
        msg="py-audioread >= 3.1 requires python@3.9 or later",
    )

    # This can be replaced with dependencies on py-standard-aifc, py-standard-sunau once
    # these packages are available in spack
    conflicts(
        "^python@3.13:",
        when="@3.1:",
        msg="py-audioread requires py-standard-aifc, py-standard-sunau packages with python@3.13:",
    )
