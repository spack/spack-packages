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

    version("2.1.9", sha256="a3480e42056c8e80a8192a54f6729a280ef66d27782ee11cbd63e9d4d1523089")
    version("2.1.8", sha256="073904fabc842881e07bd3e4a5776623535562f70b1655b635d22886168dd168")

    depends_on("py-setuptools", type="build")
    # the following does not seem to be used for building but is listed in
    # setup.py
    depends_on("py-pytest-runner", type="build")
