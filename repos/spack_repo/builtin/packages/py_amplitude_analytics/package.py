# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAmplitudeAnalytics(PythonPackage):
    """The official Amplitude backend Python SDK for server-side instrumentation."""

    homepage = "https://github.com/amplitude/Amplitude-Python"
    pypi = "amplitude_analytics/amplitude_analytics-1.2.3.tar.gz"

    version("1.2.3", sha256="4c9525847c391c19675d6e026f4601c27204ffeec71cb92252770d84d4538404")

    depends_on("py-setuptools", type="build")
