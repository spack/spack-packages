# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCython(PythonPackage):
    """The Cython compiler for writing C extensions for the Python language."""

    homepage = "https://github.com/cython/cython"
    pypi = "cython/cython-3.0.11.tar.gz"
    tags = ["build-tools"]

    license("Apache-2.0")

    version("3.2.3", sha256="f13832412d633376ffc08d751cc18ed0d7d00a398a4065e2871db505258748a6")
    version("3.2.2", sha256="c3add3d483acc73129a61d105389344d792c17e7c1cee24863f16416bd071634")
    version("3.2.1", sha256="2be1e4d0cbdf7f4cd4d9b8284a034e1989b59fd060f6bd4d24bf3729394d2ed8")
    version("3.2.0", sha256="41fdce8237baee2d961c292ed0386903dfe126f131e450a62de0fd7a5280d4b2")
    version("3.1.7", sha256="6f78b9053861325a44468fa4b48f11950635cd6d4715e8cd2633c73dd6a75a3d")
    version("3.1.6", sha256="ff4ccffcf98f30ab5723fc45a39c0548a3f6ab14f01d73930c5bfaea455ff01c")
    version("3.1.5", sha256="7e73c7e6da755a8dffb9e0e5c4398e364e37671778624188444f1ff0d9458112")
    version("3.1.4", sha256="9aefefe831331e2d66ab31799814eae4d0f8a2d246cbaaaa14d1be29ef777683")
    version("3.1.3", sha256="10ee785e42328924b78f75a74f66a813cb956b4a9bc91c44816d089d5934c089")
    version("3.1.2", sha256="6bbf7a953fa6762dfecdec015e3b054ba51c0121a45ad851fa130f63f5331381")
    version("3.1.1", sha256="505ccd413669d5132a53834d792c707974248088c4f60c497deb1b416e366397")
    version("3.1.0", sha256="1097dd60d43ad0fff614a57524bfd531b35c13a907d13bee2cc2ec152e6bf4a1")
    version("3.0.12", sha256="b988bb297ce76c671e28c97d017b95411010f7c77fa6623dd0bb47eed1aee1bc")
    version("3.0.11", sha256="7146dd2af8682b4ca61331851e6aebce9fe5158e75300343f80c07ca80b1faff")
    version("3.0.10", sha256="dcc96739331fb854dcf503f94607576cfe8488066c61ca50dfd55836f132de99")
    version("3.0.8", sha256="8333423d8fd5765e7cceea3a9985dd1e0a5dfeb2734629e1a2ed2d6233d39de6")
    version("3.0.7", sha256="fb299acf3a578573c190c858d49e0cf9d75f4bc49c3f24c5a63804997ef09213")
    version("3.0.6", sha256="399d185672c667b26eabbdca420c98564583798af3bc47670a8a09e9f19dd660")
    version("3.0.5", sha256="39318348db488a2f24e7c84e08bdc82f2624853c0fea8b475ea0b70b27176492")
    version("3.0.4", sha256="2e379b491ee985d31e5faaf050f79f4a8f59f482835906efe4477b33b4fbe9ff")
    version("3.0.0", sha256="350b18f9673e63101dbbfcf774ee2f57c20ac4636d255741d76ca79016b1bd82")
    version("0.29.36", sha256="41c0cfd2d754e383c9eeb95effc9aa4ab847d0c9747077ddd7c0dcb68c3bc01f")
    version("0.29.35", sha256="6e381fa0bf08b3c26ec2f616b19ae852c06f5750f4290118bf986b6f85c8c527")
    version("0.29.34", sha256="1909688f5d7b521a60c396d20bba9e47a1b2d2784bfb085401e1e1e7d29a29a8")
    version("0.29.33", sha256="5040764c4a4d2ce964a395da24f0d1ae58144995dab92c6b96f44c3f4d72286a")
    version("0.29.32", sha256="8733cf4758b79304f2a4e39ebfac5e92341bce47bcceb26c1254398b2f8c1af7")
    version("0.29.30", sha256="2235b62da8fe6fa8b99422c8e583f2fb95e143867d337b5c75e4b9a1a865f9e3")
    version("0.29.24", sha256="cdf04d07c3600860e8c2ebaad4e8f52ac3feb212453c1764a49ac08c827e8443")
    version("0.29.23", sha256="6a0d31452f0245daacb14c979c77e093eb1a546c760816b5eed0047686baad8e")
    version("0.29.22", sha256="df6b83c7a6d1d967ea89a2903e4a931377634a297459652e4551734c48195406")
    version("0.29.21", sha256="e57acb89bd55943c8d8bf813763d20b9099cc7165c0f16b707631a7654be9cad")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # Based on PyPI wheel availability
    with default_args(type=("build", "link", "run")):
        depends_on("python@:3.14")
        depends_on("python@:3.13", when="@:3.1.2")
        depends_on("python@:3.12", when="@:3.0.10")
        depends_on("python@:3.11", when="@:3.0.3")  # Cythonize still used distutils
        depends_on("python@:3.10", when="@:0.29.28")
        depends_on("python@:3.9", when="@:0.29.24")

    # https://github.com/cython/cython/issues/5751
    # https://github.com/cython/cython/commit/0000fb4c319ef8f7e8eabcc99677f99a8c503cc3
    depends_on("py-setuptools@66:", when="^python@3.12:", type="run")

    depends_on("py-setuptools", type="build")
    depends_on("gdb@7.2:", type="test")

    # Backports CYTHON_FORCE_REGEN environment variable
    patch("5307.patch", when="@0.29:0.29.33")
    patch("5712.patch", when="@0.29")

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/c/cython/{}-{}.tar.gz"
        if version >= Version("3.0.11"):
            name = "cython"
        else:
            name = "Cython"
        return url.format(name, version)

    @property
    def command(self):
        """Returns the Cython command"""
        return Executable(self.prefix.bin.cython)

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        # If cython is used as a dep, ensure it's used even when pre-generated
        # C files are distributed in the tarball. Cython is a small build dep, and
        # the time generating C-files is typically less than compiling them. So it's
        # fine. It solves an issue where distributed C-sources were generated with
        # an old, buggy Cython. In particular Cython regularly depends on cpython
        # internals, which can change even in Python patch releases. It looks like
        # the Cython folks are coming back from their recommendation to *include*
        # pre-generated C-sources in tarballs, see also
        # https://github.com/cython/cython/issues/5089

        # Support for this was backported to 0.29.34, but we patch any 0.29 release
        if self.spec.version >= Version("0.29"):
            env.set("CYTHON_FORCE_REGEN", "1")

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def build_test(self):
        # Warning: full suite of unit tests takes a very long time
        python("runtests.py", "-j", str(make_jobs))
