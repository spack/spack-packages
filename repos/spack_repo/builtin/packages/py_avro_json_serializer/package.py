# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAvroJsonSerializer(PythonPackage):
    """Serializes data into a JSON format using AVRO schema."""

    homepage = "https://github.com/linkedin/python-avro-json-serializer"
    pypi = "avro_json_serializer/avro_json_serializer-0.4.tar.gz"

    license("Apache-2.0")

    version("1.0.4", sha256="7453a3239b9aa8277321c668b27e49895b4c532a6c2f7b2884e10cdda7b9d381")
    version("0.4", sha256="f9dac2dac92036c5dd5aba8c716545fc0a0630cc365a51ab15bc2ac47eac28f1")

    depends_on("py-setuptools", type="build")
    depends_on("py-simplejson", type=("build", "run"))
    depends_on("py-avro", type=("build", "run"))
