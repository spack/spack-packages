# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Libblastrampoline(MakefilePackage):
    """Using PLT trampolines to provide a BLAS and LAPACK demuxing library."""

    homepage = "https://github.com/JuliaLinearAlgebra/libblastrampoline"
    git = "https://github.com/JuliaLinearAlgebra/libblastrampoline.git"
    url = "https://github.com/JuliaLinearAlgebra/libblastrampoline/archive/refs/tags/v3.1.0.tar.gz"

    maintainers("haampie", "giordano")

    license("MIT")

    version("5.15.0", sha256="69e0be57ebf037c1997c35edf03565614cd3c6863a695d01348a21bf1f482e74")
    version("5.14.0", sha256="1036d8a34d2b6cad715da9b5f84c505517c9c65c24fcf90ba0f17d4d0003811a")
    version("5.13.1", sha256="6df0eddd846db56b885056641cf02304862411bd0e641d444acf8f4eb2e33327")
    version("5.13.0", sha256="45a73ab0e112df142d37117cd78a53c5d9b3ffd86a5f151d3103ec2274600364")
    version("5.12.0", sha256="12f9d186bc844a21dfa2a6ea1f38a039227554330c43230d72f721c330cf6018")
    version("5.11.2", sha256="eeee692ca6f28977f3aa089592b8d25bac223158f5be7a9a5f241ec837d3af51")
    version("5.11.1", sha256="65206141b81bf151f1dfcceabf280b7b7ced995da3da170b85ce3cbb5f514cc8")
    version("5.11.0", sha256="4ea6c134843bd868f78d7ee0c61bf8bdda5334f20deaa6d3cd5bc6caafc4af17")
    version("5.10.1", sha256="1185a2a85453827823c224727e7cd665b7af8f48af5d2cd0225bd45389112e81")
    version("5.9.0", sha256="fe62c48eab6000a348d6d0cc3f2ebd2c38c6cae460468b56539b8438d42dc589")
    version("5.8.0", sha256="aeceb01ebebdd1068a1147b636451c46c16d64f9e22694075abda4dddfffe13d")
    version("5.4.0", sha256="e1a2258b0ad31cc41e6e9b8ba36f5c239fd1a267f2657ef3d3f669cc5b811f6a")
    version("5.3.0", sha256="95bca73f1567e2acd1110d0dfe5bb58fc86718555cd6eab89f0a769534df3b62")
    version("5.2.0", sha256="5af9ff9cec16087f57109082a362419fc49152034fa90772ebcabd882007fd95")
    version("5.1.1", sha256="cb5515512f6653538ce74653e46ccfba58c87b7dcb79b9655f7c3655e65498f0")
    version("5.1.0", sha256="55ac0c8f9cb91b2ed2db014be8394c9dadf3b5f26bd8af6dca9d6f20ca72b8fd")
    version("5.0.2", sha256="2e96fa62957719351da3e4dff8cd0949449073708f5564dae0a224a556432356")
    version("5.0.1", sha256="1066b4d157276e41ca66ca94f0f8c2900c221b49da2df3c410e6f8bf1ce9b488")
    version("4.1.0", sha256="8b1a3a55b1e1a849e907288e3afbd10d367b25364a59cb2ccaddc88604b13266")
    version("4.0.0", sha256="8816dfba6f0c547bca5fba9d83e63062387def3089622a9514babf79e1737310")
    version("3.1.0", sha256="f6136cc2b5d090ceca67cffa55b4c8af4bcee874333d49297c867abdb0749b5f")
    version("3.0.4", sha256="3c8a54a3bd8a2737b7f74ebeb56df8e2a48083c9094dbbff80b225c228e31793")
    version("3.0.3", sha256="a9c553ee6f20fa2f92098edcb3fc4a331c653250e559f72b9317b4ee84500cd7")
    version("3.0.2", sha256="caefd708cf0cf53b01cea74a09ab763bf4dfa4aec4468892720f3921521c1f74")
    version("3.0.1", sha256="b5b8ac0d3aba1bcb9dc26d7d6bb36b352d45e7d7e2594c6122e72b9e5d75a772")
    version("3.0.0", sha256="4d0856d30e7ba0cb0de08b08b60fd34879ce98714341124acf87e587d1bbbcde")
    version("2.2.0", sha256="1fb8752891578b45e187019c67fccbaafb108756aadc69bdd876033846ad30d3")

    depends_on("c", type="build")  # generated

    build_directory = "src"

    def install(self, spec, prefix):
        with working_dir(self.build_directory):
            make("prefix={0}".format(prefix), "install")
