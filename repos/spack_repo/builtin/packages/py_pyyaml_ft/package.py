# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyyamlFt(PythonPackage):
    """
    YAML processing framework for Python with support for free-threading.

    This recipe is almost identical to py-pyyaml due to py-pyyaml-ft being a fork of py-pyyaml.
    """

    homepage = "https://github.com/Quansight-Labs/pyyaml-ft"
    pypi = "pyyaml_ft/pyyaml_ft-8.0.0.tar.gz"

    license("MIT")

    version("8.0.0", sha256="0c947dce03954c7b5d38869ed4878b2e6ff1d44b08a0d84dc83fdad205ae39ab")

    variant("libyaml", default=True, description="Use libYAML bindings")

    depends_on("python@3.13:", type=("build", "run"))

    depends_on("libyaml", when="+libyaml", type="link")

    with default_args(type="build"):
        depends_on("py-setuptools")
        depends_on("py-packaging")
        depends_on("py-cython@3.1:")

    @property
    def import_modules(self):
        modules = ["yaml"]

        if "+libyaml" in self.spec:
            modules.append("yaml.cyaml")

        return modules

    @when("^py-pip@23.1: ^py-setuptools@64:")
    def config_settings(self, spec, prefix):
        if "+libyaml" in self.spec:
            return {"--global-option": "--with-libyaml"}
        else:
            return {"--global-option": "--without-libyaml"}

    @when("^py-pip@:23.0")
    def global_options(self, spec, prefix):
        args = []

        if "+libyaml" in self.spec:
            args.append("--with-libyaml")
        else:
            args.append("--without-libyaml")

        return args

    def setup_build_environment(self, env):
        if "+libyaml" in self.spec:
            env.append_flags("LDFLAGS", f"-L{self.spec['libyaml'].prefix.lib}")
            env.append_flags("LDFLAGS", f"-Wl,-rpath,{self.spec['libyaml'].prefix.lib}")
            env.append_flags("CFLAGS", f"-I{self.spec['libyaml'].prefix.include}")
