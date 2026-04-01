# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Podio(CMakePackage):
    """PODIO, or plain-old-data I/O, is a C++ library to support the creation
    and handling of data models in particle physics."""

    homepage = "https://github.com/AIDASoft/podio"
    url = "https://github.com/AIDASoft/podio/archive/v00-09-02.tar.gz"
    git = "https://github.com/AIDASoft/podio.git"

    maintainers("vvolkl", "drbenmorgan", "jmcarcell", "tmadlener")

    tags = ["hep", "key4hep"]

    version("master", branch="master")
    version("1.7", sha256="4a62ed2fdd9cebb5fc1799ea17237979b2d435797f1201fa8031fd99e9e47c15")
    version("1.6", sha256="4a625419bcf9d10b33b9fcf6cacbbebfd24c62e88a9980c5735b011d671397fe")
    version("1.5", sha256="3d316a86420a1e79088488f229bb8d1259244cf17752c40f817abeec2cec89a5")
    version("1.4.1", sha256="d70dad214ac683e76c6e1093804c0f1ec4e7133a704173e2f1777a1279eb1535")
    version("1.4", sha256="f8b7f5ba965ff58270d617f50f168a4683a98fbcd643b66f1852bec960e02bbd")
    version("1.3", sha256="7efdf049822f171f4da5e83a7101096c066679904e59e741f3c2833ccda5e363")
    version("1.2", sha256="bc97ba09ce908e55d4c5faa78d9739dde7daefd9337ae98351813b13708d0685")
    version("1.1", sha256="2cb5040761f3da4383e1f126da25d68e99ecd8398e0ff12e7475a3745a7030a6")
    version("1.0.1", sha256="915531a2bcf638011bb6cc19715bbc46d846ec8b985555a1afdcd6abc017e21b")
    version("1.0", sha256="491f335e148708e387e90e955a6150e1fc2e01bf6b4980b65e257ab0619559a9")
    version("0.99", sha256="c823918a6ec1365d316e0a753feb9d492e28903141dd124a1be06efac7c1877a")

    _cxxstd_values = (
        conditional("17", when="@:1.2"),
        conditional("20", when="@0.14.1:"),
        conditional("23", when="@1.3:"),
    )
    variant(
        "cxxstd",
        default="17",
        values=_cxxstd_values,
        multi=False,
        description="Use the specified C++ standard when building.",
        when="@:1.1",
    )
    variant(
        "cxxstd",
        default="20",
        values=_cxxstd_values,
        multi=False,
        description="Use the specified C++ standard when building.",
        when="@1.2:",
    )
    variant("sio", default=False, description="Build the SIO I/O backend")
    variant("rntuple", default=False, description="Build the RNTuple backend")
    variant(
        "datasource",
        default=False,
        description="Build the RDataSource for reading podio collections",
        when="@1.0.2:",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("root@6.08.06: cxxstd=17", when="cxxstd=17")
    depends_on("root@6.14:", when="+datasource")
    depends_on("root@6.28.04: +root7", when="+rntuple")
    depends_on("root@6.28:")
    depends_on("root@6.32: +root7", when="@1.3: +rntuple")
    for cxxstd in _cxxstd_values:
        depends_on(
            "root cxxstd={}".format(cxxstd[0].value), when="cxxstd={}".format(cxxstd[0].value)
        )

    depends_on("cmake@3.12:", type="build")
    depends_on("python", type=("build", "run"), when="@:1.6")
    depends_on("python", type=("build", "link", "run"), when="@1.7:")
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-jinja2@2.10.1:", type=("build", "run"))
    depends_on("sio", type=("build", "link"), when="+sio")
    depends_on("fmt@9:", type=("build", "link"), when="@1.3:")
    depends_on("catch2@3.1:", type=("test"))
    depends_on("catch2@3.4:", type=("test"), when="cxxstd=20")
    depends_on("catch2@3.3:", type=("test"), when="@1.2: cxxstd=17")
    depends_on("catch2@3.5:", type=("test"), when="@1.5:")
    depends_on("catch2@3.5:", type=("test"), when="@1.3: cxxstd=23")
    depends_on("py-graphviz", type=("run"))
    depends_on("py-tabulate", type=("run", "test"))

    conflicts("+rntuple ^root@6.32:", when="@:0.99", msg="rntuple API change requires podio@1:")
    conflicts("+rntuple ^root@6.34:", when="@:1.1", msg="rntuple API change requires podio@1.2:")
    conflicts(
        "^python +freethreading", when="@:1.6", msg="python free-threading requires podio@1.7:"
    )

    # See https://github.com/AIDASoft/podio/pull/600
    patch(
        "https://github.com/AIDASoft/podio/commit/0222a077aaff817b21a46a590af0f8329dd27d67.patch?full_index=1",
        when="@0.17:0.99",
        sha256="9e42e0995634f2afdd358cd19383e882dc9143cce1b6afb0d2c4a1ec9add6e15",
    )

    # See https://github.com/AIDASoft/podio/pull/599 that landed after 0.99
    extends("python", when="@1.0:")

    def cmake_args(self):
        args = [
            self.define_from_variant("ENABLE_SIO", "sio"),
            self.define_from_variant("ENABLE_RNTUPLE", "rntuple"),
            self.define_from_variant("ENABLE_DATASOURCE", "datasource"),
            self.define("PODIO_SET_RPATH", True),
            self.define("CMAKE_CXX_STANDARD", self.spec.variants["cxxstd"].value),
            self.define("BUILD_TESTING", self.run_tests),
        ]
        return args

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("@:0.99"):
            # After 0.99 podio installs its python bindings into a more standard place
            env.prepend_path("PYTHONPATH", self.prefix.python)

        env.prepend_path("LD_LIBRARY_PATH", self.spec["podio"].libs.directories[0])
        if "+sio" in self.spec:
            # sio needs to be on LD_LIBRARY_PATH for ROOT to be able to
            # dynamicaly load the python bindings library
            env.prepend_path("LD_LIBRARY_PATH", self.spec["sio"].libs.directories[0])

        # Frame header needs to be available for python bindings
        env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)

        # Pythonizations require Python.h accessible for ACLiC
        if self.spec.satisfies("@1.5:"):
            env.prepend_path("ROOT_INCLUDE_PATH", self.spec["python"].headers.directories[0])

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        if self.spec.satisfies("@:0.99"):
            env.prepend_path("PYTHONPATH", self.prefix.python)

        env.prepend_path("LD_LIBRARY_PATH", self.spec["podio"].libs.directories[0])
        env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        if self.spec.satisfies("+sio"):
            # sio needs to be on LD_LIBRARY_PATH for ROOT to be able to
            # dynamicaly load the python libraries also in dependent build
            # environments since the import structure has changed with
            # podio@0.17
            env.prepend_path("LD_LIBRARY_PATH", self.spec["sio"].libs.directories[0])

    def url_for_version(self, version):
        """Translate version numbers to ilcsoft conventions.
        in spack, the convention is: 0.1 (or 0.1.0) 0.1.1, 0.2, 0.2.1 ...
        in ilcsoft, releases are dashed and padded with a leading zero
        the patch version is omitted when 0
        so for example v01-12-01, v01-12 ...
        :param self: spack package class that has a url
        :type self: class: `spack.PackageBase`
        :param version: version
        :type param: str
        """
        base_url = self.url.rsplit("/", 1)[0]

        if len(version) == 1:
            major = version[0]
            minor, patch = 0, 0
        elif len(version) == 2:
            major, minor = version
            patch = 0
        else:
            major, minor, patch = version

        # By now the data is normalized enough to handle it easily depending
        # on the value of the patch version
        if patch == 0:
            version_str = "v%02d-%02d.tar.gz" % (major, minor)
        else:
            version_str = "v%02d-%02d-%02d.tar.gz" % (major, minor, patch)

        return base_url + "/" + version_str
