# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class RoctracerDevApi(Package):
    """ROC-tracer API. Installs the API header files of the roctracer-dev
    package, mainly to avoid circular dependencies in the ROCm ecosystem.
    For the ROC-tracer library, please check out roctracer-dev."""

    homepage = "https://github.com/ROCm/roctracer"
    git = "https://github.com/ROCm/rocm-systems.git"
    url = "https://github.com/ROCm/roctracer/archive/refs/tags/rocm-6.4.3.tar.gz"

    tags = ["rocm"]
    maintainers("srekolam", "renjithravindrankannath", "afzpatel")
    license("MIT")

    def url_for_version(self, version):
        if version <= Version("7.1.1"):
            url = "https://github.com/ROCm/roctracer/archive/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/rocm-systems/archive/rocm-{0}.tar.gz"
        return url.format(version)

    version("7.2.1", sha256="201f19174eafbace2f7abf0d1178ebb17db878191276aba6d23f0e1758b0e10f")
    version("7.2.0", sha256="728ea7e9bf16e6ed217a0fd1a8c9afaba2dae2e7908fa4e27201e67c803c5638")
    version("7.1.1", sha256="dec80803c6d2d684759172145177849efda65672645b95a2f2ad1a84335043bb")
    version("7.1.0", sha256="a90077e2080531803dac154e64d6d481289a5839493ce131c4edc8b5ac1bc294")
    version("7.0.2", sha256="c9dc54fc8b68a7598b3e9453f7962a87cb02e86d64e5681452ebafd62fb85e96")
    version("7.0.0", sha256="c1f435b8040c6d34720eeadf837bc888b1c5aaccbfd7efaff4d602f1957f812f")
    version("6.4.3", sha256="a4378652b3b7141ca3b2743eedada03757383bff88932db8e28d0afd5869b882")
    version("6.4.2", sha256="c9bc3390fe4c406cc2b2bdb5a7e9f088e0107825624c9cd7b2a6ec120bc73ef8")
    version("6.4.1", sha256="57d61441d95b05b12cd05210a80d81cd1d7a21dab7487680897427dfbdafddca")
    version("6.4.0", sha256="e5c6e3b20ed3c0d2dca61ad472f9878107c9ce09a2108ff6583ae32031298022")
    version("6.3.3", sha256="0d03ebd058291d584be6bf8b114292c666a799b0fd23c697e1c6cb2b6d43f990")
    version("6.3.2", sha256="ca8e93fc37f4671db28df5cb7a24b48f3d4879a188e4780e45961bba3725bb8a")
    version("6.3.1", sha256="89e4ab249f527131f684714c9135c69eaad1a63b7e74bae718b1617543b94426")
    version("6.3.0", sha256="6eb09e3b3b45ed68b2ac7ed6848521e645569bcd4a1f3a336cf2473a801308a2")
    version("6.2.4", sha256="b94c7db8ac57a4a1d7f8115020c36551220c20f33289fd06830495b4914a7d7b")
    version("6.2.1", sha256="9e69c90b9dc650e0d8642ec675082c9566e576285a725c3a5d07a37cebb18810")
    version("6.2.0", sha256="2fc39f47161f41cc041cd5ee4b1bb0e9832508650e832434056423fec3739735")
    version("6.1.2", sha256="073e67e728d5eda16d7944f3abd96348b3f278e9f36cab3ac22773ebaad0d2d6")
    version("6.1.1", sha256="9cb77fd700a0d615056f0db1e9500b73bd0352214f33bdac520e25b9125a926a")
    version("6.1.0", sha256="3f8e296c4d04123a7177d815ca166e978b085ad7c816ac298e6bb47a299fa187")
    version("6.0.2", sha256="1e0105b32fdd9c010aab304bb2ca1a5a38ba323cea610afe1135657edda8f26e")
    version("6.0.0", sha256="941166a0363c5689bfec118d54e986c43fb1ec8cbf18d95721d9a824bd52c0f8")
    version("5.7.1", sha256="ec0453adac7e62b142eb0df1e1e2506863aac4c3f2ce9d117c3184c08c0c6b48")
    version("5.7.0", sha256="40bb757920488466e29df90bb80a975cc340bf7f8771fb1d754dfbb6b688d78e")

    depends_on("cxx", type="build")  # generated

    def install(self, spec, prefix):
        if self.spec.satisfies("@7.2:"):
            source_directory = f"{self.stage.source_path}/projects/roctracer"
        else:
            source_directory = self.stage.source_path
        include = join_path(source_directory, "inc")

        def only_headers(p):
            return p.endswith("CMakeLists.txt") or p.endswith("RPM") or p.endswith("DEBIAN")

        mkdirp(prefix.roctracer.include)
        install_tree(include, prefix.roctracer.include, ignore=only_headers)
