# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyS3transfer(PythonPackage):
    """S3transfer is a Python library for managing Amazon S3 transfers."""

    homepage = "https://github.com/boto/s3transfer"
    pypi = "s3transfer/s3transfer-0.2.1.tar.gz"

    license("Apache-2.0")

    version("0.16.0", sha256="8e990f13268025792229cd52fa10cb7163744bf56e719e0b9cb925ab79abf920")
    version("0.15.0", sha256="d36fac8d0e3603eff9b5bfa4282c7ce6feb0301a633566153cbd0b93d11d8379")
    version("0.14.0", sha256="eff12264e7c8b4985074ccce27a3b38a485bb7f7422cc8046fee9be4983e4125")
    version("0.13.1", sha256="c3fdba22ba1bd367922f27ec8032d6a1cf5f10c934fb5d68cf60fd5a23d936cf")
    version("0.13.0", sha256="f5e6db74eb7776a37208001113ea7aa97695368242b364d73e91c981ac522177")
    version("0.12.0", sha256="8ac58bc1989a3fdb7c7f3ee0918a66b160d038a147c7b5db1500930a607e9a1c")
    version("0.11.5", sha256="8c8aad92784779ab8688a61aefff3e28e9ebdce43142808eaa3f0b0f402f68b7")
    version("0.11.4", sha256="559f161658e1cf0a911f45940552c696735f5c74e64362e515f333ebed87d679")
    version("0.11.3", sha256="edae4977e3a122445660c7c114bba949f9d191bae3b34a096f18a1c8c354527a")
    version("0.11.2", sha256="3b39185cb72f5acc77db1a58b6e25b977f28d20496b6e58d6813d75f464d632f")
    version("0.11.1", sha256="3f25c900a367c8b7f7d8f9c34edc87e300bde424f779dc9f0a8ae4f9df9264f6")
    version("0.11.0", sha256="6563eda054c33bdebef7cbf309488634651c47270d828e594d151cd289fb7cf7")
    version("0.10.4", sha256="29edc09801743c21eb5ecbc617a152df41d3c287f67b615f73e5f750583666a7")
    version("0.10.3", sha256="4f50ed74ab84d474ce614475e0b8d5047ff080810aac5d01ea25231cfc944b0c")
    version("0.10.2", sha256="0711534e9356d3cc692fdde846b4a1e4b0cb6519971860796e6bc4c7aea00ef6")
    version("0.10.1", sha256="5683916b4c724f799e600f41dd9e10a9ff19871bf87623cc8f491cb4f5fa0a19")
    version("0.10.0", sha256="d0c8bbf672d5eebbe4e57945e23b972d963f07d82f661cabf678a5c88831595b")
    version("0.9.0", sha256="9e1b186ec8bb5907a1e82b51237091889a9973a2bb799a924bcd9f301ff79d3d")
    version("0.8.2", sha256="368ac6876a9e9ed91f6bc86581e319be08188dc60d50e0d56308ed5765446283")
    version("0.7.0", sha256="fd3889a66f5fe17299fe75b82eae6cf722554edca744ca5d5fe308b104883d2e")
    version("0.6.2", sha256="cab66d3380cca3e70939ef2255d01cd8aece6a4907a9528740f668c4b0611861")
    version("0.6.0", sha256="2ed07d3866f523cc561bf4a00fc5535827981b117dd7876f036b0c1aca42c947")
    version("0.5.0", sha256="50ed823e1dc5868ad40c8dc92072f757aa0e653a192845c94a3b676f4a62da4c")
    version("0.4.2", sha256="cb022f4b16551edebbb31a377d3f09600dbada7363d8c5db7976e7f47732e1b2")
    version("0.3.4", sha256="7fdddb4f22275cf1d32129e21f056337fd2a80b6ccef1664528145b72c49e6d2")
    version("0.2.1", sha256="6efc926738a3cd576c2a79725fed9afde92378aa5c6a957e3af010cb019fac9d")

    depends_on("py-setuptools", type="build")

    depends_on("py-botocore@1.37.4:1", type=("build", "run"), when="@0.11.4:")
    depends_on("py-botocore@1.33.2:1", type=("build", "run"), when="@0.8.1:")
    depends_on("py-botocore@1.32.7:1", type=("build", "run"), when="@0.8.0:")
    depends_on("py-botocore@1.12.36:1", type=("build", "run"))
