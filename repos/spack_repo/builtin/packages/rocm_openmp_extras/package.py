# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from spack_repo.builtin.build_systems.cmake import CMakeBuilder
from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

tools_url = "https://github.com/ROCm"
compute_url = "https://github.com/ROCm"

# Arrays of hashes are in order of the versions array below
# For example array[0] = 3.9.0, array[1] = 3.10.0, etc.

aomp = [
    "4f34fa02db410808c5e629f30f8804210b42c4ff7d31aa80606deaed43054c3c",
    "ed7bbf92230b6535a353ed032a39a9f16e9987397798100392fc25e40c8a1a4e",
    "1b2c0934ef16e17b2377944fae8c9b3db6dc64b7e43932ddfe2eeefdf6821410",
    "d6e13a15d5d25990d4bacbac8fabe2eb07973829f2e69abbc628e0736f95caf9",
    "832b7c48149a730619b577a2863b8d1bf1b2551eda5b815e1865a044929ab9fa",
    "62a5036a2299ed2e3053ee00b7ea1800469cd545fea486fa17266a8b3acfaf5d",
    "3de1c7a31a88c3f05a6a66ba6854ac8fdad1ce44462e561cb1e6ad59629029ce",
    "5f54d7c7c798bcf1cd47d3a7f17ceaf79991bf166cc5e47e5372a68e7cf7d520",
    "ac82e8da0c210ee14b911c833ae09a029a41541689930759737c135db52464a3",
    "ad5674b5626ed6720ca5f8772542e8ed3fb7a9150ed7a86a1adbcd70a2074e8e",
    "8c8240d948817ab1874eff0406d6053ee0518902427e0236e6b4d2cee84ff882",
    "8fefdd0d9eecd11866ddecbe039347560469eb69d974934005d480eac4432b81",
    "eeda81dafd17df7e1d2b9dbf91a23924c6dd8de29f0792725fc25a6cd1d9c5fa",
    "b43b889b5778572d6d348c6a6614dc02258212004d1f1f64f0cdc74dc3249e86",
    "b9b1537fcbb7226d99145a1c01e8c5961ab83a5834286397943ff86676d545ed",
    "1a60ee18b2b58b83f38f8cb3cdeb304689be49b47a721a185d73648c4db78427",
    "1a4b14f88a763a69e30479d27390d4bdc3307e00b5fd1cafbc645599f109f41b",
    "559704720772503a4be2ee205033614a699fae765cc6baf90b8b3c8013678b78",
    "f4931776c294354e80d562e0837881c52d2d5bfb30f7371ecb454cce6f44bbfc",
    "c028cc7ff001c7023f85056c376a393418b411ec09ff11965b78bbb433f90d3e",
    "233fcec4dc9649c93b3fa90c721e25eac33a712f0a6246b6004697425c428280",
    "89f11c149953c17b54186251eb3d3ffcd457fca1c7666c0c77c07d6d1e7efda4",
    "740cb8945ddc7d5d9d59a77cfcd2e9f24dc60f062c1a0d46377516037fd21939",
]

devlib = [
    "0f8780b9098573f1c456bdc84358de924dcf00604330770a383983e1775bf61e",
    "703de8403c0bd0d80f37c970a698f10f148daf144d34f982e4484d04f7c7bbef",
    "198df4550d4560537ba60ac7af9bde31d59779c8ec5d6309627f77a43ab6ef6f",
    "c6d88b9b46e39d5d21bd5a0c1eba887ec473a370b1ed0cebd1d2e910eedc5837",
    "6bd9912441de6caf6b26d1323e1c899ecd14ff2431874a2f5883d3bc5212db34",
    "f1a67efb49f76a9b262e9735d3f75ad21e3bd6a05338c9b15c01e6c625c4460d",
    "300e9d6a137dcd91b18d5809a316fddb615e0e7f982dc7ef1bb56876dff6e097",
    "12ce17dc920ec6dac0c5484159b3eec00276e4a5b301ab1250488db3b2852200",
    "4840f109d8f267c28597e936c869c358de56b8ad6c3ed4881387cf531846e5a7",
    "7af782bf5835fcd0928047dbf558f5000e7f0207ca39cf04570969343e789528",
    "79580508b039ca6c50dfdfd7c4f6fbcf489fe1931037ca51324818851eea0c1c",
    "e9c2481cccacdea72c1f8d3970956c447cec47e18dfb9712cbbba76a2820552c",
    "1f52e45660ea508d3fe717a9903fe27020cee96de95a3541434838e0193a4827",
    "4df9aba24e574edf23844c0d2d9dda112811db5c2b08c9428604a21b819eb23d",
    "dca1c145a23f05229d5d646241f9d1d3c5dbf1d745b338ae020eabe33beb965c",
    "460ad28677092b9eb86ffdc49bcb4d01035e32b4f05161d85f90c9fa80239f50",
    "9f42cb73d90bd4561686c0366f60f6e58cfd32ff24b094c69e8259fb5d177457",
    "7a484b621d568eef000ee8c4d2d46d589e5682b950f1f410ce7215031f1f3ad7",
    "3d479a2aa615b6bb35cd3521122fbff34188dc0cc52d8b0acda59f9f55198211",
    "fd612fa750bebd0c3be0ea642b2cae8ff5c7e00a2280b22b9ea16ee86a11d763",
    "87f5532b8b653bd18541cdf6e59923cbd340b300d8ec5046d3e4288d9e5195c0",
    "d76a16db4a56914383029e241823f7bc2a3d645f2967dd22230f11c11cfe189e",
    "e86138d2a63fbcbdf64668d55573b26ae944d0f0ae5a3f5bb59bf7bdb3124d3f",
]

llvm = [
    "4abdf00b297a77c5886cedb37e63acda2ba11cb9f4c0a64e133b05800aadfcf0",
    "6b54c422e45ad19c9bf5ab090ec21753e7f7d854ca78132c30eb146657b168eb",
    "c673708d413d60ca8606ee75c77e9871b6953c59029c987b92f2f6e85f683626",
    "7d35acc84de1adee65406f92a369a30364703f84279241c444cd93a48c7eeb76",
    "6bd9912441de6caf6b26d1323e1c899ecd14ff2431874a2f5883d3bc5212db34",
    "f1a67efb49f76a9b262e9735d3f75ad21e3bd6a05338c9b15c01e6c625c4460d",
    "300e9d6a137dcd91b18d5809a316fddb615e0e7f982dc7ef1bb56876dff6e097",
    "12ce17dc920ec6dac0c5484159b3eec00276e4a5b301ab1250488db3b2852200",
    "4840f109d8f267c28597e936c869c358de56b8ad6c3ed4881387cf531846e5a7",
    "7af782bf5835fcd0928047dbf558f5000e7f0207ca39cf04570969343e789528",
    "79580508b039ca6c50dfdfd7c4f6fbcf489fe1931037ca51324818851eea0c1c",
    "e9c2481cccacdea72c1f8d3970956c447cec47e18dfb9712cbbba76a2820552c",
    "1f52e45660ea508d3fe717a9903fe27020cee96de95a3541434838e0193a4827",
    "4df9aba24e574edf23844c0d2d9dda112811db5c2b08c9428604a21b819eb23d",
    "dca1c145a23f05229d5d646241f9d1d3c5dbf1d745b338ae020eabe33beb965c",
    "460ad28677092b9eb86ffdc49bcb4d01035e32b4f05161d85f90c9fa80239f50",
    "9f42cb73d90bd4561686c0366f60f6e58cfd32ff24b094c69e8259fb5d177457",
    "7a484b621d568eef000ee8c4d2d46d589e5682b950f1f410ce7215031f1f3ad7",
    "3d479a2aa615b6bb35cd3521122fbff34188dc0cc52d8b0acda59f9f55198211",
    "fd612fa750bebd0c3be0ea642b2cae8ff5c7e00a2280b22b9ea16ee86a11d763",
    "87f5532b8b653bd18541cdf6e59923cbd340b300d8ec5046d3e4288d9e5195c0",
    "d76a16db4a56914383029e241823f7bc2a3d645f2967dd22230f11c11cfe189e",
    "e86138d2a63fbcbdf64668d55573b26ae944d0f0ae5a3f5bb59bf7bdb3124d3f",
]

flang = [
    "cc4f1973b1b8e7bcc4f09e3381bae4e1a2e51ea4e2598fc1b520ccb8bf24d28c",
    "8fd618d81af092416b267c4d00c801731f7a00c0f8d4aedb795e52a4ec1bf183",
    "fcb319ddb2aa3004a6ae60370ab4425f529336b1cee50f29200e697e61b53586",
    "8e6469415880bb068d788596b3ed713a24495eb42788f98cca92e73a2998f703",
    "51ecd2c154568c971f5b46ff0e1e1b57063afe28d128fc88c503de88f7240267",
    "1bcaa73e73a688cb092f01987cf3ec9ace4aa1fcaab2b812888c610722c4501d",
    "12418ea61cca58811b7e75fd9df48be568b406f84a489a41ba5a1fd70c47f7ba",
    "6af7785b1776aeb9229ce4e5083dcfd451e8450f6e5ebe34214560b13f679d96",
    "409ee98bf15e51ac68b7ed351f4582930dfa0288de042006e17eea6b64df5ad6",
    "51c1308f324101e4b637e78cd2eb652e22f68f6d820991a76189c15131f971dc",
    "43f10662706dbf22b0090839fd590d9fc633e7339b19aaee7578322ea6809275",
    "2e38ba138312d18b2677347839a960802bb04090bb92b5e6a15ac06ed789dbc0",
    "4b4d8025a215c52e62dd6317cafce224d95f91040e90942c9a93ade568a8dd48",
    "e0f650fc633ab4a8eab30b0c1ba0efb46ec596b540c3a4c13ca24d92c512d255",
    "a51fbdda9d5d968fe6d23eaeabbe04a0db810a88a7a609ae924e3caaed4539f1",
    "84b8a9501bece0a56d038c4f0210b0a2537ae6c1b5005c89eec026af07d52bc6",
    "4bab6319c378629df868503be1f9e86effa5148924966a780d2ee1d7b6dd6747",
    "fcc8b30fc7772ccb36c28af2deb5d1efe6ecf4da3fc2e457a2b7b299b693a290",
    "4b03e7932d3291f1d285dc68e2cde6f2e1f1bbf66a2c5da77b329bf902d4b14e",
    "dc61c10a5c6853fcf655d45293dc075764b0c0f8ffc63f8d38dcde3139b8f495",
    "06c3cee1e3426e4d6b14f80f7e1938991b403cacea36e406491a0fd13dfbaa72",
    "a2e27a8da910facea710f56f5d83319dd192746f5ba755493ba1da223228ae8a",
    "c4c7caa29c1ad4363288853229a7ef78abb397bb51e3b617d0dc4e8b7d0b08ad",
]

extras = [
    "be59433dd85d4b8f0eaff87e0cc424a814152c67f3a682d1343c4bd61dd49a0f",
    "8060c6879708faf5f7d417b19a479dec9b7b9583a1b885f12d247faf831f7f0b",
    "f37e1107e4da5b083e794244f3d0c9fd073ccb6fd6015e635349d8f0d679c4b8",
    "b2e117d703cefdc2858adaeee5bad95e9b6dab6263a9c13891a79a7b1e2defb6",
    "57d6d9d26c0cb6ea7f8373996c41165f463ae7936d32e5793822cfae03900f8f",
    "3dc837fbfcac64e000e1b5518e4f8a6b260eaf1a3e74152d8b8c22f128f575b7",
    "2b9351fdb1cba229669233919464ae906ca8f70910c6fa508a2812b7c3bed123",
    "7cef51c980f29d8b46d8d4b110e4f2f75d93544cf7d63c5e5d158cf531aeec7d",
    "4b0d250b5ebd997ed6d5d057689c3f67dfb4d82f09f582ebb439ca9134fae48d",
    "34c3506b0f6aefbf0bc7981ff2901b7a2df975a5b40c5eb078522499d81057f0",
    "22cdd87b1d66e7e7f9e30fd9031fcbf01ce0b631551959144bb42e7f1dba28cb",
    "4050c60cbbf582122cc0a30b4a99200341c426f2fa3d81ac8dc61f5a0890ed15",
    "70b49c1198bf176498ec4a94584b8ed8a07f623ebfa567e4fcf1a6545b635185",
    "9615235b4d5ae78e43ca4854f316b83e75f7d9ed3fc187ed1869b7d8d7e26341",
    "105dd0ccae2864275de5a6370010d923d25307e6a8c35af3befdd0064ea743bc",
    "cf20b02b1f99f506c198866ef03f2265dc355627760f82cda3878d5bc6486afc",
    "5c005fdd3ec1bcd8588628d87298cb59e2ee276a02046b9f2592ab90d39e1f52",
    "e13112f5ce118a25decf9626460ca5f1e2333976e23879cb0a4a6a5343db858f",
    "5a8172d80162f46c84e9fabd06c25d044767855746a059c859a0180ac4424791",
    "ba16f796f47b4a0a152b0e87db72cfe222d186334a0cbf6d8708083ebc1817d8",
    "7736fad25566d09702a6e45211495977bef1ba1f8b032d224fc26ffacc6aca60",
    "4b0068986e62bb2ba1e26197f8b1350aec65132396f225e3c66530c2ef78f801",
    "8b56639b4ba9f791b873da20dbc552e4678acd69f9b256177e9a1d44c8361fdd",
]

versions = [
    "5.7.0",
    "5.7.1",
    "6.0.0",
    "6.0.2",
    "6.1.0",
    "6.1.1",
    "6.1.2",
    "6.2.0",
    "6.2.1",
    "6.2.4",
    "6.3.0",
    "6.3.1",
    "6.3.2",
    "6.3.3",
    "6.4.0",
    "6.4.1",
    "6.4.2",
    "6.4.3",
    "7.0.0",
    "7.0.2",
    "7.1.0",
    "7.1.1",
    "7.2.0",
]
versions_dict = dict()  # type: Dict[str,Dict[str,str]]
components = ["aomp", "devlib", "llvm", "flang", "extras"]
component_hashes = [aomp, devlib, llvm, flang, extras]

# Loop through versions and create necessary dictionaries of components
for outer_index, item in enumerate(versions):
    for inner_index, component in enumerate(component_hashes):
        versions_dict.setdefault(item, {})[components[inner_index]] = component_hashes[
            inner_index
        ][outer_index]


class RocmOpenmpExtras(Package):
    """OpenMP support for ROCm LLVM."""

    homepage = tools_url + "/aomp"
    url = tools_url + "/aomp/archive/rocm-7.0.2.tar.gz"
    tags = ["rocm"]

    license("Apache-2.0")

    maintainers("srekolam", "renjithravindrankannath", "estewart08", "afzpatel")
    version("7.2.0", sha256=versions_dict["7.2.0"]["aomp"])
    version("7.1.1", sha256=versions_dict["7.1.1"]["aomp"])
    version("7.1.0", sha256=versions_dict["7.1.0"]["aomp"])
    version("7.0.2", sha256=versions_dict["7.0.2"]["aomp"])
    version("7.0.0", sha256=versions_dict["7.0.0"]["aomp"])
    version("6.4.3", sha256=versions_dict["6.4.3"]["aomp"])
    version("6.4.2", sha256=versions_dict["6.4.2"]["aomp"])
    version("6.4.1", sha256=versions_dict["6.4.1"]["aomp"])
    version("6.4.0", sha256=versions_dict["6.4.0"]["aomp"])
    version("6.3.3", sha256=versions_dict["6.3.3"]["aomp"])
    version("6.3.2", sha256=versions_dict["6.3.2"]["aomp"])
    version("6.3.1", sha256=versions_dict["6.3.1"]["aomp"])
    version("6.3.0", sha256=versions_dict["6.3.0"]["aomp"])
    version("6.2.4", sha256=versions_dict["6.2.4"]["aomp"])
    version("6.2.1", sha256=versions_dict["6.2.1"]["aomp"])
    version("6.2.0", sha256=versions_dict["6.2.0"]["aomp"])
    version("6.1.2", sha256=versions_dict["6.1.2"]["aomp"])
    version("6.1.1", sha256=versions_dict["6.1.1"]["aomp"])
    version("6.1.0", sha256=versions_dict["6.1.0"]["aomp"])
    version("6.0.2", sha256=versions_dict["6.0.2"]["aomp"])
    version("6.0.0", sha256=versions_dict["6.0.0"]["aomp"])
    version("5.7.1", sha256=versions_dict["5.7.1"]["aomp"])
    version("5.7.0", sha256=versions_dict["5.7.0"]["aomp"])

    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")
    variant("flang-legacy", default=False, description="Build flang-legacy")

    conflicts("~flang-legacy", when="@:6")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("gmake", type="build")

    depends_on("cmake@3:", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("python@3:", type="build")
    depends_on("perl-data-dumper", type="build")
    depends_on("awk", type="build")
    depends_on("elfutils", type=("build", "link"))
    depends_on("libffi", type=("build", "link"))
    depends_on("libdrm", when="@5.7:6.0")
    depends_on("numactl", when="@5.7:6.0")
    depends_on("zlib", when="@6.2:")

    for ver in [
        "5.7.0",
        "5.7.1",
        "6.0.0",
        "6.0.2",
        "6.1.0",
        "6.1.1",
        "6.1.2",
        "6.2.0",
        "6.2.1",
        "6.2.4",
        "6.3.0",
        "6.3.1",
        "6.3.2",
        "6.3.3",
        "6.4.0",
        "6.4.1",
        "6.4.2",
        "6.4.3",
        "7.0.0",
        "7.0.2",
        "7.1.0",
        "7.1.1",
        "7.2.0",
    ]:
        depends_on(f"rocm-core@{ver}", when=f"@{ver}")

    for ver in ["5.7.0", "5.7.1", "6.0.0", "6.0.2"]:
        depends_on(f"hsakmt-roct@{ver}", when=f"@{ver}")
        depends_on(f"comgr@{ver}", when=f"@{ver}")
        depends_on(f"hsa-rocr-dev@{ver}", when=f"@{ver}")
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")

        resource(
            name="rocm-device-libs",
            url=f"{compute_url}/ROCm-Device-Libs/archive/rocm-{ver}.tar.gz",
            sha256=versions_dict[ver]["devlib"],
            expand=True,
            destination="rocm-openmp-extras",
            placement="rocm-device-libs",
            when=f"@{ver}",
        )
        resource(
            name="flang",
            url=f"{tools_url}/flang/archive/rocm-{ver}.tar.gz",
            sha256=versions_dict[ver]["flang"],
            expand=True,
            destination="rocm-openmp-extras",
            placement="flang",
            when=f"@{ver}",
        )

        resource(
            name="aomp-extras",
            url=f"{tools_url}/aomp-extras/archive/rocm-{ver}.tar.gz",
            sha256=versions_dict[ver]["extras"],
            expand=True,
            destination="rocm-openmp-extras",
            placement="aomp-extras",
            when=f"@{ver}",
        )

        resource(
            name="llvm-project",
            url=f"{compute_url}/llvm-project/archive/rocm-{ver}.tar.gz",
            sha256=versions_dict[ver]["llvm"],
            expand=True,
            destination="rocm-openmp-extras",
            placement="llvm-project",
            when=f"@{ver}",
        )
    for ver in ["6.1.0", "6.1.1", "6.1.2", "6.2.0", "6.2.1", "6.2.4"]:
        depends_on(f"hsakmt-roct@{ver}", when=f"@{ver}")

    for ver in [
        "6.1.0",
        "6.1.1",
        "6.1.2",
        "6.2.0",
        "6.2.1",
        "6.2.4",
        "6.3.0",
        "6.3.1",
        "6.3.2",
        "6.3.3",
        "6.4.0",
        "6.4.1",
        "6.4.2",
        "6.4.3",
        "7.0.0",
        "7.0.2",
        "7.1.0",
        "7.1.1",
        "7.2.0",
    ]:
        depends_on(f"comgr@{ver}", when=f"@{ver}")
        depends_on(f"hsa-rocr-dev@{ver}", when=f"@{ver}")
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")

        resource(
            name="flang",
            url=f"{tools_url}/flang/archive/rocm-{ver}.tar.gz",
            sha256=versions_dict[ver]["flang"],
            expand=True,
            destination="rocm-openmp-extras",
            placement="flang",
            when=f"@{ver} +flang-legacy",
        )

        resource(
            name="aomp-extras",
            url=f"{tools_url}/aomp-extras/archive/rocm-{ver}.tar.gz",
            sha256=versions_dict[ver]["extras"],
            expand=True,
            destination="rocm-openmp-extras",
            placement="aomp-extras",
            when=f"@{ver}",
        )

        resource(
            name="llvm-project",
            url=f"{compute_url}/llvm-project/archive/rocm-{ver}.tar.gz",
            sha256=versions_dict[ver]["llvm"],
            expand=True,
            destination="rocm-openmp-extras",
            placement="llvm-project",
            when=f"@{ver}",
        )
    patch("0001-Linking-hsakmt-libdrm-and-numactl-libraries.patch", when="@5.7:6.0")
    patch(
        "0001-Linking-hsakmt-libdrm-and-numactl-libraries-6.1.patch",
        working_dir="rocm-openmp-extras/llvm-project/openmp/libomptarget",
        when="@6.1",
    )
    patch("0001-Avoid-duplicate-registration-on-cuda-env.patch", when="@6.1")
    patch("0001-Avoid-duplicate-registration-on-cuda-env-6.2.patch", when="@6.2:6.3")
    patch("0001-Avoid-duplicate-registration-on-cuda-env-6.4.patch", when="@6.4:")
    patch("0002-add-include-dir-omp.patch", when="@6.4:7.1")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.external:
            devlibs_prefix = self.prefix
            llvm_prefix = self.prefix
            # prefix is set to either <rocm_path>/llvm or <rocm_path>/lib/llvm
            path_parts = self.prefix.rstrip("llvm").rstrip("lib/")
            hsa_prefix = os.path.dirname(path_parts)
        else:
            devlibs_prefix = self.spec["llvm-amdgpu"].prefix
            llvm_prefix = self.spec["llvm-amdgpu"].prefix
            hsa_prefix = self.spec["hsa-rocr-dev"].prefix
        env.set("AOMP", f"{llvm_prefix}")
        env.set("HIP_DEVICE_LIB_PATH", f"{devlibs_prefix}/amdgcn/bitcode")
        env.prepend_path("CPATH", f"{self.prefix}/include")
        env.prepend_path("LIBRARY_PATH", f"{self.prefix}/lib")
        env.prepend_path("LD_LIBRARY_PATH", f"{self.prefix}/lib")
        env.prepend_path("LD_LIBRARY_PATH", f"{hsa_prefix}/lib")
        env.set("AOMP_GPU", f"`{self.prefix}/bin/mygpu`")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        llvm_prefix = self.spec["llvm-amdgpu"].prefix
        env.set("AOMP", f"{llvm_prefix}")
        env.set("FC", f"{self.prefix}/bin/flang")
        if self.spec.satisfies("@6.1:"):
            env.prepend_path("LD_LIBRARY_PATH", self.spec["hsa-rocr-dev"].prefix.lib)
        gfx_list = "gfx700 gfx701 gfx801 gfx803 gfx900 gfx902 gfx906 gfx908"

        if self.spec.version >= Version("4.3.1"):
            gfx_list = gfx_list + " gfx90a gfx1030 gfx1031 gfx942"
        env.set("GFXLIST", gfx_list)
        if self.spec.satisfies("%cxx=gcc"):
            env.prepend_path("LD_LIBRARY_PATH", self.spec["gcc-runtime"].prefix.lib)

    def patch(self):
        src = self.stage.source_path
        if self.spec.satisfies("@6.4:"):
            libomptarget = "{0}/rocm-openmp-extras/llvm-project/offload"
        else:
            libomptarget = "{0}/rocm-openmp-extras/llvm-project/openmp/libomptarget"
        flang = "{0}/rocm-openmp-extras/flang/"

        plugin = "/plugins/amdgpu/CMakeLists.txt"

        if self.spec.satisfies("@6.1"):
            filter_file(
                r"${HSAKMT_LIB_PATH}",
                "${HSAKMT_LIB_PATH} ${HSAKMT_LIB64}"
                + "${HSAKMT_LIB} ${LIBDRM_LIB} ${NUMACTL_DIR}/lib",
                libomptarget.format(src) + "/CMakeLists.txt",
            )
            filter_file(
                r"${LIBOMPTARGET_LLVM_INCLUDE_DIRS}",
                "${LIBOMPTARGET_LLVM_INCLUDE_DIRS} ${HSAKMT_INC_PATH}",
                libomptarget.format(src) + "/../CMakeLists.txt",
            )
            filter_file(
                r"${LIBOMPTARGET_LLVM_INCLUDE_DIRS}",
                "${LIBOMPTARGET_LLVM_INCLUDE_DIRS} ${HSAKMT_INC_PATH}",
                libomptarget.format(src) + "/CMakeLists.txt",
            )

        # Openmp adjustments
        # Fix relocation error with libffi by not using static lib.
        filter_file(
            "libffi.a",
            "",
            libomptarget.format(src) + "/cmake/Modules/LibomptargetGetDependencies.cmake",
        )
        if self.spec.satisfies("@:6.1"):
            filter_file(
                r"{OPENMP_INSTALL_LIBDIR}",
                "{OPENMP_INSTALL_LIBDIR}/libdevice",
                libomptarget.format(src) + "/deviceRTLs/amdgcn/CMakeLists.txt",
            )
            filter_file(
                "-nogpulib",
                "-nogpulib -nogpuinc",
                libomptarget.format(src) + "/deviceRTLs/amdgcn/CMakeLists.txt",
            )
            filter_file(
                "-x hip",
                "-x hip -nogpulib -nogpuinc",
                libomptarget.format(src) + "/deviceRTLs/amdgcn/CMakeLists.txt",
            )
            filter_file(
                "-c ",
                "-c -nogpulib -nogpuinc -I{LIMIT}",
                libomptarget.format(src) + "/hostrpc/CMakeLists.txt",
            )
            filter_file(
                r"${ROCM_DIR}/hsa/include ${ROCM_DIR}/hsa/include/hsa",
                "${HSA_INCLUDE}/hsa/include ${HSA_INCLUDE}/hsa/include/hsa",
                libomptarget.format(src) + plugin,
                string=True,
            )

            filter_file("{ROCM_DIR}/hsa/lib", "{HSA_LIB}", libomptarget.format(src) + plugin)

            filter_file(
                r"{ROCM_DIR}/lib\)",
                "{HSAKMT_LIB})\nset(HSAKMT_LIB64 ${HSAKMT_LIB64})",
                libomptarget.format(src) + plugin,
            )

            filter_file(
                r"-L${LIBOMPTARGET_DEP_LIBHSAKMT_LIBRARIES_DIRS}",
                "-L${LIBOMPTARGET_DEP_LIBHSAKMT_LIBRARIES_DIRS} -L${HSAKMT_LIB64}",
                libomptarget.format(src) + plugin,
                string=True,
            )

            filter_file(
                r"-rpath,${LIBOMPTARGET_DEP_LIBHSAKMT_LIBRARIES_DIRS}",
                "-rpath,${LIBOMPTARGET_DEP_LIBHSAKMT_LIBRARIES_DIRS}" + ",-rpath,${HSAKMT_LIB64}",
                libomptarget.format(src) + plugin,
                string=True,
            )

            filter_file("{ROCM_DIR}/include", "{COMGR_INCLUDE}", libomptarget.format(src) + plugin)

            filter_file(
                r"-L${LLVM_LIBDIR}${OPENMP_LIBDIR_SUFFIX}",
                "-L${LLVM_LIBDIR}${OPENMP_LIBDIR_SUFFIX} -L${COMGR_LIB}",
                libomptarget.format(src) + plugin,
                string=True,
            )

            filter_file(
                r"rpath,${LLVM_LIBDIR}${OPENMP_LIBDIR_SUFFIX}",
                "rpath,${LLVM_LIBDIR}${OPENMP_LIBDIR_SUFFIX}" + "-Wl,-rpath,${COMGR_LIB}",
                libomptarget.format(src) + plugin,
                string=True,
            )
        if self.spec.satisfies("@:6"):
            filter_file(
                "ADDITIONAL_VERSIONS 2.7",
                "ADDITIONAL_VERSIONS 3",
                flang.format(src) + "CMakeLists.txt",
            )
        if self.spec.satisfies("@:7.1"):
            filter_file(
                "if (LIBOMPTARGET_DEP_CUDA_FOUND)",
                "if (LIBOMPTARGET_DEP_CUDA_FOUND AND NOT LIBOMPTARGET_AMDGPU_ARCH)",
                libomptarget.format(src) + "/hostexec/CMakeLists.txt",
                string=True,
            )

    def install(self, spec, prefix):
        src = self.stage.source_path
        gfx_list = os.environ["GFXLIST"]
        gfx_list = gfx_list.replace(" ", ";")
        devlibs_prefix = self.spec["llvm-amdgpu"].prefix
        if self.spec.satisfies("@6.1:"):
            devlibs_src = f"{src}/rocm-openmp-extras/llvm-project/amd/device-libs"
        else:
            devlibs_src = f"{src}/rocm-openmp-extras/rocm-device-libs"
        hsa_prefix = self.spec["hsa-rocr-dev"].prefix
        if self.spec.satisfies("@:6.2"):
            hsakmt_prefix = self.spec["hsakmt-roct"].prefix
        if self.spec.satisfies("@5.7:6.1"):
            libdrm_prefix = self.spec["libdrm"].prefix
            numactl_prefix = self.spec["numactl"].prefix
        comgr_prefix = self.spec["comgr"].prefix
        llvm_inc = "/rocm-openmp-extras/llvm-project/llvm/include"
        llvm_prefix = self.spec["llvm-amdgpu"].prefix
        omp_bin_dir = f"{self.prefix}/bin"
        omp_lib_dir = f"{self.prefix}/lib"
        bin_dir = f"{llvm_prefix}/bin"
        lib_dir = f"{llvm_prefix}/lib"
        flang_warning = "-Wno-incompatible-pointer-types-discards-qualifiers"
        libpgmath = "/rocm-openmp-extras/flang/runtime/libpgmath/lib/common"
        elfutils_inc = spec["elfutils"].prefix.include
        ffi_inc = spec["libffi"].prefix.include
        if self.spec.satisfies("@6.2:"):
            ncurses_lib_dir = self.spec["ncurses"].prefix.lib
            zlib_lib_dir = self.spec["zlib"].prefix.lib

        legacy_or_classic = "classic" if self.spec.satisfies("@7.0:") else "legacy"

        # flang1 and flang2 symlink needed for build of flang-runtime
        # libdevice symlink to rocm-openmp-extras for runtime
        # libdebug symlink to rocm-openmp-extras for runtime
        if self.spec.satisfies("+flang-legacy"):
            if os.path.islink((os.path.join(bin_dir, "flang1"))):
                os.unlink(os.path.join(bin_dir, "flang1"))
            if os.path.islink((os.path.join(bin_dir, "flang2"))):
                os.unlink(os.path.join(bin_dir, "flang2"))
            if self.spec.version >= Version("6.1.0"):
                if os.path.islink((os.path.join(bin_dir, f"flang-{legacy_or_classic}"))):
                    os.unlink(os.path.join(bin_dir, f"flang-{legacy_or_classic}"))
            if not os.path.exists(os.path.join(bin_dir, "flang1")):
                symlink(os.path.join(omp_bin_dir, "flang1"), os.path.join(bin_dir, "flang1"))
            if not os.path.exists(os.path.join(bin_dir, "flang2")):
                symlink(os.path.join(omp_bin_dir, "flang2"), os.path.join(bin_dir, "flang2"))

            if self.spec.version >= Version("6.1.0"):
                symlink(
                    os.path.join(omp_bin_dir, f"flang-{legacy_or_classic}"),
                    os.path.join(bin_dir, f"flang-{legacy_or_classic}"),
                )

        if self.spec.satisfies("@:7"):
            if os.path.islink((os.path.join(lib_dir, "libdevice"))):
                os.unlink(os.path.join(lib_dir, "libdevice"))
            if os.path.islink((os.path.join(llvm_prefix, "lib-debug"))):
                os.unlink(os.path.join(llvm_prefix, "lib-debug"))
            symlink(os.path.join(omp_lib_dir, "libdevice"), os.path.join(lib_dir, "libdevice"))
            symlink(os.path.join(self.prefix, "lib-debug"), os.path.join(llvm_prefix, "lib-debug"))

        # Set cmake args
        components = dict()

        components["aomp-extras"] = [
            "../rocm-openmp-extras/aomp-extras",
            f"-DLLVM_DIR={llvm_prefix}",
            f"-DDEVICE_LIBS_DIR={devlibs_prefix}/amdgcn/bitcode",
            "-DAOMP_STANDALONE_BUILD=0",
            f"-DDEVICELIBS_ROOT={devlibs_src}",
            "-DNEW_BC_PATH=1",
            f"-DAOMP={llvm_prefix}",
        ]
        if not self.spec.satisfies("%cxx=rocmcc"):
            components["aomp-extras"] += [
                f"-DCMAKE_C_COMPILER={bin_dir}/clang",
                f"-DCMAKE_CXX_COMPILER={bin_dir}/clang++",
            ]

        # Shared cmake configuration for openmp, openmp-debug
        # Due to hsa-rocr-dev using libelf instead of elfutils
        # the build of openmp fails because the include path
        # for libelf is placed before elfutils in SPACK_INCLUDE_DIRS.
        # Passing the elfutils include path via cmake options is a
        # workaround until hsa-rocr-dev switches to elfutils.
        openmp_common_args = [
            f"-DROCM_DIR={hsa_prefix}",
            f"-DDEVICE_LIBS_DIR={devlibs_prefix}/amdgcn/bitcode",
            "-DAOMP_STANDALONE_BUILD=0",
            f"-DDEVICELIBS_ROOT={devlibs_src}",
            f"-DOPENMP_TEST_C_COMPILER={bin_dir}/clang",
            f"-DOPENMP_TEST_CXX_COMPILER={bin_dir}/clang++",
            f"-DLIBOMPTARGET_AMDGCN_GFXLIST={gfx_list}",
            "-DLIBOMP_COPY_EXPORTS=OFF",
            f"-DHSA_LIB={hsa_prefix}/lib",
            f"-DCOMGR_INCLUDE={comgr_prefix}/include",
            f"-DCOMGR_LIB={comgr_prefix}/lib",
            "-DOPENMP_ENABLE_LIBOMPTARGET=1",
            "-DOPENMP_ENABLE_LIBOMPTARGET_HSA=1",
            f"-DLLVM_MAIN_INCLUDE_DIR={src}{llvm_inc}",
            f"-DLLVM_INSTALL_PREFIX={llvm_prefix}",
            f"-DCMAKE_C_FLAGS=-isystem{elfutils_inc} -I{ffi_inc}",
            f"-DCMAKE_CXX_FLAGS=-isystem{elfutils_inc} -I{ffi_inc}",
            "-DNEW_BC_PATH=1",
            f"-DHSA_INCLUDE={hsa_prefix}/include/hsa",
            "-DLIBOMPTARGET_ENABLE_DEBUG=ON",
        ]
        if self.spec.satisfies("@5.7:6.1"):
            openmp_common_args += [
                f"-DLIBDRM_LIB={libdrm_prefix}/lib",
                f"-DHSAKMT_INC_PATH={hsakmt_prefix}/include",
                f"-DNUMACTL_DIR={numactl_prefix}",
            ]
        if self.spec.satisfies("@:6.2"):
            openmp_common_args += [
                f"-DHSAKMT_LIB={hsakmt_prefix}/lib",
                f"-DHSAKMT_LIB64={hsakmt_prefix}/lib64",
            ]
        if self.spec.satisfies("+asan"):
            openmp_common_args += [
                "-DASAN_OPTIONS=detect_leaks=0",
                "-DCMAKE_C_FLAGS=-fsanitize=address -shared-libasan",
                "-DCMAKE_CXX_FLAGS=-fsanitize=address -shared-libasan",
                "-DCMAKE_LD_FLAGS=-fuse-ld=lld",
            ]
        if not self.spec.satisfies("%cxx=rocmcc"):
            openmp_common_args += [
                f"-DCMAKE_C_COMPILER={bin_dir}/clang",
                f"-DCMAKE_CXX_COMPILER={bin_dir}/clang++",
            ]

        components["openmp"] = ["../rocm-openmp-extras/llvm-project/openmp"]
        components["openmp"] += openmp_common_args

        components["openmp-debug"] = [
            "../rocm-openmp-extras/llvm-project/openmp",
            "-DLIBOMPTARGET_NVPTX_DEBUG=ON",
            "-DCMAKE_CXX_FLAGS=-g",
            "-DCMAKE_C_FLAGS=-g",
        ]

        components["openmp-debug"] += openmp_common_args

        flang_bin = "flang-classic" if self.spec.satisfies("@7.0:") else "flang"

        # Shared cmake configuration for pgmath, flang, flang-runtime
        flang_common_args = [
            "-DLLVM_ENABLE_ASSERTIONS=ON",
            f"-DLLVM_CONFIG={bin_dir}/llvm-config",
            f"-DCMAKE_CXX_COMPILER={bin_dir}/clang++",
            f"-DCMAKE_C_COMPILER={bin_dir}/clang",
            f"-DCMAKE_Fortran_COMPILER={bin_dir}/{flang_bin}",
            "-DLLVM_TARGETS_TO_BUILD=AMDGPU;x86",
            # Spack thinks some warnings from the flang build are errors.
            # Disable those warnings in C and CXX flags.
            f"-DCMAKE_CXX_FLAGS={flang_warning} -I{src}{libpgmath}",
            f"-DCMAKE_C_FLAGS={flang_warning} -I{src}{libpgmath}",
        ]

        if not self.spec.satisfies("%cxx=rocmcc"):
            flang_common_args += [
                f"-DCMAKE_C_COMPILER={bin_dir}/clang",
                f"-DCMAKE_CXX_COMPILER={bin_dir}/clang++",
            ]

        components["pgmath"] = ["../rocm-openmp-extras/flang/runtime/libpgmath"]

        components["pgmath"] += flang_common_args
        components["offload"] = ["../rocm-openmp-extras/llvm-project/offload"]
        if self.spec.satisfies("@7.0:"):
            components["offload"] += [f"-DLLVM_DIR={llvm_prefix}/lib/cmake/llvm"]
        components["offload"] += openmp_common_args

        flang_legacy_version = "17.0-4"

        components["flang-legacy-llvm"] = [
            "-DLLVM_ENABLE_PROJECTS=clang",
            "-DCMAKE_BUILD_TYPE=Release",
            "-DLLVM_ENABLE_ASSERTIONS=ON",
            "-DLLVM_TARGETS_TO_BUILD=AMDGPU;X86",
            "-DCLANG_DEFAULT_LINKER=lld",
            "-DLLVM_INCLUDE_BENCHMARKS=0",
            "-DLLVM_INCLUDE_RUNTIMES=0",
            "-DLLVM_INCLUDE_EXAMPLES=0",
            "-DLLVM_INCLUDE_TESTS=0",
            "-DLLVM_INCLUDE_DOCS=0",
            "-DLLVM_INCLUDE_UTILS=0",
            "-DCLANG_DEFAULT_PIE_ON_LINUX=0",
            f"../../rocm-openmp-extras/flang/flang-{legacy_or_classic}/"
            f"{flang_legacy_version}/llvm-{legacy_or_classic}/llvm",
        ]

        components["flang-legacy"] = [
            f"../rocm-openmp-extras/flang/flang-{legacy_or_classic}/{flang_legacy_version}"
        ]

        if not self.spec.satisfies("%cxx=rocmcc"):
            components["flang-legacy"] += [
                f"-DCMAKE_C_COMPILER={bin_dir}/clang",
                f"-DCMAKE_CXX_COMPILER={bin_dir}/clang++",
            ]

        flang_legacy_flags = []
        if (
            self.compiler.name == "gcc"
            and self.compiler.version >= Version("7.0.0")
            and self.compiler.version < Version("9.0.0")
        ):
            flang_legacy_flags.append("-D_GLIBCXX_USE_CXX11_ABI=0")
        if self.spec.satisfies("@6.2:"):
            flang_legacy_flags.append(f"-L{ncurses_lib_dir}")
            flang_legacy_flags.append(f"-L{zlib_lib_dir}")
        components["flang-legacy-llvm"] += [f"-DCMAKE_CXX_FLAGS={' '.join(flang_legacy_flags)}"]
        components["flang-legacy"] += [f"-DCMAKE_CXX_FLAGS={' '.join(flang_legacy_flags)}"]

        components["flang"] = [
            "../rocm-openmp-extras/flang",
            "-DFLANG_OPENMP_GPU_AMD=ON",
            "-DFLANG_OPENMP_GPU_NVIDIA=ON",
        ]

        components["flang"] += flang_common_args

        components["flang-runtime"] = [
            "../rocm-openmp-extras/flang",
            "-DLLVM_INSTALL_RUNTIME=ON",
            "-DFLANG_BUILD_RUNTIME=ON",
            f"-DOPENMP_BUILD_DIR={src}/spack-build-openmp/runtime/src",
        ]
        components["flang-runtime"] += flang_common_args

        build_order = ["aomp-extras", "openmp"]
        if self.spec.version >= Version("6.4.0"):
            build_order += ["offload"]

        if self.spec.satisfies("+flang-legacy"):
            if self.spec.version >= Version("6.1.0"):
                build_order += ["flang-legacy-llvm", "flang-legacy"]
            build_order += ["pgmath", "flang", "flang-runtime"]
        # Override standard CMAKE_BUILD_TYPE
        std_cmake_args = CMakeBuilder.std_args(self, generator="Unix Makefiles")
        for arg in std_cmake_args:
            found = re.search("CMAKE_BUILD_TYPE", arg)
            if found:
                std_cmake_args.remove(arg)
        for component in build_order:
            cmake_args = components[component]
            cmake_args.extend(std_cmake_args)
            if component == "flang-legacy-llvm":
                with working_dir(f"spack-build-{component}/llvm-{legacy_or_classic}", create=True):
                    cmake_args.append("-DCMAKE_BUILD_TYPE=Release")
                    cmake(*cmake_args)
                    make()
            elif component == "flang-legacy":
                with working_dir("spack-build-flang-legacy-llvm"):
                    cmake_args.append("-DCMAKE_BUILD_TYPE=Release")
                    cmake(*cmake_args)
                    make()
                    make("install")
                    symlink(os.path.join(bin_dir, "clang"), os.path.join(omp_bin_dir, "clang"))
            else:
                with working_dir(f"spack-build-{component}", create=True):
                    # OpenMP build needs to be run twice(Release, Debug)
                    if component == "openmp-debug":
                        cmake_args.append("-DCMAKE_BUILD_TYPE=Debug")
                    else:
                        cmake_args.append("-DCMAKE_BUILD_TYPE=Release")
                    cmake(*cmake_args)
                    make()
                    make("install")
