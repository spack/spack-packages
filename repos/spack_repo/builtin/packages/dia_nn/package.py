# Copyright Spack Project Developers. See COPYRIGHT file for details.
import os

from spack.package import (
    Package,
    depends_on,
    install_tree,
    join_path,
    license,
    mkdirp,
    set_executable,
    symlink,
    version,
    which,
    working_dir,
)


class DiaNn(Package):
    """DIA-NN: automated software suite for DIA proteomics data processing."""

    homepage = "https://github.com/vdemichev/DiaNN"
    url = (
        "https://github.com/vdemichev/DiaNN/releases/download/2.0/DIA-NN-2.3.2-Academia-Linux.zip"
    )

    maintainers = ["rfsilvaesib-beep"]

    license("MIT", checked_by="rfsilvaesib-beep")

    version(
        "2.3.2-Academia", sha256="dab4a5267a39d2c3f4e36430389f6f6f893c9b9cfd05571cc94c5941aad7b446"
    )
    version(
        "2.2.0-Academia", sha256="61317acf1552753d300d5e10642f05acae2befa649a5d49a6b10501c8bed9832"
    )
    version(
        "2.1.0-Academia", sha256="ec3759ef164d008b2bc8480f44ea7ff407f4dc4a7c30d3a66b1364e3e632e282"
    )
    version(
        "2.0.2-Academia", sha256="a2dc6ffe83ca6df0796c0fa17aa142527ce55fd583fbcaa090d4f3a383c87ddf"
    )
    version(
        "2.0.1-Academia", sha256="4b99f1a365886a029feda3d2146306f33b0e4e41cd607dfd690419942864a235"
    )
    version(
        "2.0-Academia", sha256="22bf20c5b31eefb11710745a246bfc05b3faadb99eaf89a4e56c5a4fb614f791"
    )

    depends_on("zlib")
    depends_on("boost")
    depends_on("eigen")
    depends_on("patchelf", type="build")
    depends_on("gcc-runtime@12:", type="run")

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin)
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.bin)
        env.set("DIANN_MODELS", join_path(self.prefix.bin, "models"))

        if "gcc-runtime" in self.spec:
            rt_prefix = self.spec["gcc-runtime"].prefix
            lib_dir = "lib64" if os.path.isdir(join_path(rt_prefix, "lib64")) else "lib"
            env.prepend_path("LD_LIBRARY_PATH", join_path(rt_prefix, lib_dir))

    def install(self, spec, prefix):
        mkdirp(prefix.bin)

        v_num = str(self.version).split("-")[0]
        src_dir = "diann-{0}".format(v_num)
        install_tree(src_dir, prefix.bin)

        binary = join_path(prefix.bin, "diann-linux")

        rt_prefix = spec["gcc-runtime"].prefix
        lib_dir = "lib64" if os.path.isdir(join_path(rt_prefix, "lib64")) else "lib"
        gcc_lib = join_path(rt_prefix, lib_dir)

        rpath = "{0}:{1}".format(prefix.bin, gcc_lib)
        patchelf = which("patchelf")
        patchelf("--set-rpath", rpath, binary)

        with working_dir(prefix.bin):
            if os.path.exists("dia-nn"):
                os.remove("dia-nn")
            symlink("diann-linux", "dia-nn")

        set_executable(binary)
        set_executable(join_path(prefix.bin, "dia-nn"))
