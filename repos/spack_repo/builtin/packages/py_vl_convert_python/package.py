# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyVlConvertPython(PythonPackage):
    """Convert Vega-Lite chart specifications to SVG, PNG, PDF, or Vega"""

    homepage = "https://github.com/vega/vl-convert"
    pypi = "vl_convert_python/vl_convert_python-1.4.0.tar.gz"

    version("1.9.0", sha256="bbf4eb9ac9aa9f32f6fdb689391c914dff311846365658ac70bc5b30f30d57cd")
    version("1.4.0", sha256="264d6f2338c7d3474e60c6907cca016b880b0c1c9be302bb84abc6690188a7e9")

    # TODO: This package currently requires internet access to install.
    depends_on("py-maturin@1.1:1", type="build")
    depends_on("rust", type="build")

    depends_on("cmake", type="build")  # some rust dependencies need this
    depends_on("protobuf", type="build")  # rust dependency prost need this
