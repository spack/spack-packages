# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.python import PythonPipBuilder

from spack.package import *


class Flatbuffers(CMakePackage):
    """Memory Efficient Serialization Library"""

    homepage = "https://google.github.io/flatbuffers/"
    url = "https://github.com/google/flatbuffers/archive/v1.9.0.tar.gz"

    license("Apache-2.0")

    version(
        "25.12.19", sha256="f81c3162b1046fe8b84b9a0dbdd383e24fdbcf88583b9cb6028f90d04d90696a"
    )  # FIXME
    version("25.9.23", sha256="9102253214dea6ae10c2ac966ea1ed2155d22202390b532d1dea64935c518ada")
    version("25.2.10", sha256="b9c2df49707c57a48fc0923d52b8c73beb72d675f9d44b2211e4569be40a7421")
    version("25.1.24", sha256="0b9f8d2bb1d22d553c93cd7e3ecf3eb725469980a58a98db6e21574341b4ed63")
    version("25.1.21", sha256="7ab210001df1cd6234d0263801eeed3b941098bc9d6b41331832dd29cea4b555")
    version("24.12.23", sha256="7e2ef35f1af9e2aa0c6a7d0a09298c2cb86caf3d4f58c0658b306256e5bcab10")
    version("24.3.25", sha256="4157c5cacdb59737c5d627e47ac26b140e9ee28b1102f812b36068aab728c1ed")
    version("24.3.7", sha256="bfff9d2150fcff88f844e8c608b02b2a0e94c92aea39b04c0624783464304784")
    version("24.3.6", sha256="5d8bfbf5b1b4c47f516e7673677f0e8db0efd32f262f7a14c3fd5ff67e2bd8fc")
    version("23.5.26", sha256="1cce06b17cddd896b6d73cc047e36a254fb8df4d7ea18a46acf16c4c0cd3f3f3")
    version("23.5.9", sha256="fa0036f4a2d082f7034fd90a53a02ce0e121548b39c07c8d2a77a821da02fb01")
    version("2.0.6", sha256="e2dc24985a85b278dd06313481a9ca051d048f9474e0f199e372fea3ea4248c9")
    version("2.0.0", sha256="9ddb9031798f4f8754d00fca2f1a68ecf9d0f83dfac7239af1311e4fd9a565c4")
    version("1.12.0", sha256="62f2223fb9181d1d6338451375628975775f7522185266cd5296571ac152bc45")
    version("1.11.0", sha256="3f4a286642094f45b1b77228656fbd7ea123964f19502f9ecfd29933fd23a50b")
    version("1.10.0", sha256="3714e3db8c51e43028e10ad7adffb9a36fc4aa5b1a363c2d0c4303dd1be59a7c")
    version("1.9.0", sha256="5ca5491e4260cacae30f1a5786d109230db3f3a6e5a0eb45d0d0608293d247e3")
    version("1.8.0", sha256="c45029c0a0f1a88d416af143e34de96b3091642722aa2d8c090916c6d1498c2e")

    variant("shared", default=True, description="Build shared instead of static libraries")
    variant("python", default=False, description="Build with python support")

    depends_on("cxx", type="build")  # generated

    extends("python", when="+python")
    depends_on("python@3.6:", when="+python", type=("build", "run"))
    depends_on("py-pip", when="+python", type="build")
    depends_on("py-wheel", when="+python", type="build")
    depends_on("py-setuptools", when="+python", type="build")

    # Fixes "Class-memaccess" compilation error in test
    # https://github.com/google/flatbuffers/issues/5930
    # Possibly affects earlier releases but I haven't tried to apply it.
    patch(
        "https://raw.githubusercontent.com/Flamefire/easybuild-easyconfigs/"
        "72ba2a1a0d44fbd96ded9f279373ef804bdf3903/easybuild/easyconfigs/f/"
        "flatbuffers/flatbuffers-1.12.0_replace-usage-of-memset.patch",
        sha256="094a98b5a7debbc2c60c2b235942c79e505ec76f9281f87c95d15e9ad8a97c52",
        when="@1.12.0:1%gcc@10:",
    )
    # Silences false positive "-Wstringop-overflow" on GCC 10+
    # https://github.com/google/flatbuffers/issues/5950
    # Possibly affects earlier releases but I haven't tried to apply it.
    patch(
        "https://github.com/google/flatbuffers/commit/515a4052a750dfe6df8d143c8f23cd8aaf51f9d7.patch?full_index=1",
        sha256="f76b8777d7e719834ba0d83535b35e7c17ce474cfbc1286671d936191f784dc1",
        when="@1.12.0:1%gcc@10:",
    )

    @run_after("install")
    def python_install(self):
        if self.spec.satisfies("+python"):
            pydir = join_path(self.stage.source_path, "python")
            with working_dir(pydir):
                pip(*PythonPipBuilder.std_args(self), f"--prefix={self.prefix}", ".")

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("FLATBUFFERS_BUILD_SHAREDLIB", "shared"))
        args.append(f"-DFLATBUFFERS_BUILD_FLATLIB={'ON' if '+shared' not in self.spec else 'OFF'}")
        if "darwin" in self.spec.architecture:
            args.append("-DCMAKE_MACOSX_RPATH=ON")
        return args
