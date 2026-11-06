# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyExqalibur(PythonPackage):
    """Cutting-edge optimization for Perceval"""

    homepage = "https://perceval.quandela.net"

    license("CC-BY-NC-ND-4.0", checked_by="LydDeb")

    supplier = "Organization: QuandelaOSS"

    maintainers("LydDeb")

    machine = platform.machine().lower()
    system = platform.system().lower()
    if system == "linux":
        if "x86_64" == machine:
            platform_tag = "manylinux_2_27_x86_64.manylinux_2_28_x86_64"
        if "aarch64" == machine:
            platform_tag = "manylinux_2_26_aarch64.manylinux_2_28_aarch64"
    elif system == "darwin":
        if "x86_64" == machine:
            platform_tag = "macosx_10_15_x86_64"
        if "aarch64" == machine:
            platform_tag = "macosx_11_0_arm64"
    elif system == "windows":
        platform_tag = "win_amd64"

    if "macosx_10_15_x86_64" == platform_tag:
        version(
            "1.4.1-cp310",
            sha256="42ed0af29b3469e4718b7419961d134313df486c373e9b7bc2f3af2f41ffaa6c",
        )
        version(
            "1.4.1-cp311",
            sha256="7ac2df08560417f17a34ff7749d35bc81196e6e9b2e576d68a87a7d34324a1e3",
        )
        version(
            "1.4.1-cp312",
            sha256="6f7418486705a0370d6dce068a225d90d5cad7c27146d0586c566deeb4ac9791",
        )
        version(
            "1.4.1-cp313",
            sha256="0f4b0f297e3e3f32f0852c1b05b9be1788c4913a5aed37c18d2d21cba3eade59",
        )
        version(
            "1.4.1-cp314",
            sha256="c2f501feac8dd2c6e90de7b34d9c1b527eb3d605b2406b7cd839f03d2a1ea4fb",
        )
    elif "macosx_11_0_arm64" == platform_tag:
        version(
            "1.4.1-cp310",
            sha256="83a56bb171cd445cbee914ac2e9dba647aa6cd177f0fe6ae00b4c621a07ccb95",
        )
        version(
            "1.4.1-cp311",
            sha256="0df9838ce27429a17360d415506b89cd795abd840802e6b7846f135e2485d67c",
        )
        version(
            "1.4.1-cp312",
            sha256="97b39fe42d2c1b74a82ee6fa8f70cf21c7cc4f8dd77230bd8874496f54e45413",
        )
        version(
            "1.4.1-cp313",
            sha256="5086ec7656f02bccc4227db7acfd94984d139cccaa55846b328524d43f770f7b",
        )
        version(
            "1.4.1-cp314",
            sha256="5c9153b95202f2be0e9e6623b6619f553f1f4ff0a0e0fa8c9e16571e0ffe3c0a",
        )
    elif "manylinux_2_26_aarch64.manylinux_2_28_aarch64" == platform_tag:
        version(
            "1.4.1-cp310",
            sha256="8d5ba4a2e908bd21f7a7414b4e28941f42746531f38d5194de8538985727db9f",
        )
        version(
            "1.4.1-cp311",
            sha256="a9818a17f0381409edeb87c2db1b266d810924864d0f9b13b7a26db7280f718c",
        )
        version(
            "1.4.1-cp312",
            sha256="0f94ec3f9d96d48c9e49e6b12a96ca5deb5299252f7737eea10162549a9dba32",
        )
        version(
            "1.4.1-cp313",
            sha256="66551e68c6b937b94d193dbb46234fd34efbb14e28361b46ac843c99588be941",
        )
        version(
            "1.4.1-cp314",
            sha256="7f820bcbc0145470e9b2fe48d3bb5dd081330ae20d051c9ffd5c3d1da1fa3c52",
        )
    elif "manylinux_2_27_x86_64.manylinux_2_28_x86_64" == platform_tag:
        version(
            "1.4.1-cp310",
            sha256="ae57378ba295e735f61e02dd2f1585489a6c8d5c3c2df03ca21c00d346918cfe",
        )
        version(
            "1.4.1-cp311",
            sha256="dbdcd725868a9e60703f978b0f62e2f2744bca034933e25cdfdf2ca8ec2b8188",
        )
        version(
            "1.4.1-cp312",
            sha256="4de59a2d5c1077b798a0e7f9181eeb0f9d750db8e97e12d3576883f60d271627",
        )
        version(
            "1.4.1-cp313",
            sha256="331cb65cf07f96a543b6403f77618dc84dc1e7e0901c0c0e3d227d45122e5ed3",
        )
        version(
            "1.4.1-cp314",
            sha256="4a1ffc5950ed78d4e835e14bded35c56079d8e177044cedf333072a4d0411626",
        )
    elif "win_amd64" == platform_tag:
        version(
            "1.4.1-cp310",
            sha256="26d8d7c69d3813ba491006a96aae5340ecb8e43eb81acb0227dee7e97fee3c61",
        )
        version(
            "1.4.1-cp311",
            sha256="c3f3f5e3eaabe4d0928c2feabce399501d39a3bd47b01f758d395942aa98503d",
        )
        version(
            "1.4.1-cp312",
            sha256="a7d6399110abd648f38dc1b8306f3f99344ac826c84119463ef4e84af715074f",
        )
        version(
            "1.4.1-cp313",
            sha256="2786e61506cd9160e474d34a36e27a9d516459bc4f970b9a9e93d5433ffdd586",
        )
        version(
            "1.4.1-cp314",
            sha256="9d041bcf827e6918c06c1e258471edeac545058c2c01faeb146b0803c48180d4",
        )

    depends_on("python@3.14", type=("build", "run"), when="@1.4.1-cp314")
    depends_on("python@3.13", type=("build", "run"), when="@1.4.1-cp313")
    depends_on("python@3.12", type=("build", "run"), when="@1.4.1-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@1.4.1-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@1.4.1-cp310")

    with default_args(type="run"):
        depends_on("py-protobuf")

    def url_for_version(self, version):
        name = self.name.split("-")[1]
        first_letter = name[0]
        url = "https://files.pythonhosted.org/packages/{1}/{3}/{4}/{4}-{0}-{1}-{1}-{2}.whl"
        pkg_ver = version.up_to_3
        cp_ver = version.string.split("-")[1]
        return url.format(pkg_ver, cp_ver, self.platform_tag, first_letter, name)
