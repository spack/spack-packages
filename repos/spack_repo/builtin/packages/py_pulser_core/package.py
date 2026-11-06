# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPulserCore(PythonPackage):
    """A pulse-level composer for neutral-atom quantum devices."""

    homepage = "https://github.com/pasqal-io/Pulser"
    pypi = "pulser-core/pulser_core-1.9.0-py3-none-any.whl"

    supplier = "Organization: Pulser Development Team"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("1.9.0", sha256="20c8785556ac0de8e8de36e8eace1407f7ea8c145414f487937f8ac9ec15a4ea")

    variant("torch", default=False, description="Enable torch support")

    with default_args(type=("build", "run")):
        depends_on("py-jsonschema@4.17.3:4")
        depends_on("py-referencing")
        depends_on("py-matplotlib@3.10.5:3")
        depends_on("py-packaging")
        depends_on("py-numpy@1.20:1.23,1.24.1:")
        depends_on("py-numpy@2:", when="^python@3.13:")
        depends_on("py-scipy@:1")
        depends_on("py-torch@2.6:2", when="+torch")

    # The CI fetches the wrong URL
    # https://files.pythonhosted.org/packages/source/p/pulser-core/pulser_core-1.9.0-py3-none-any.whl
    # The wheel is here:
    # https://files.pythonhosted.org/packages/py3/p/pulser-core/pulser_core-1.9.0-py3-none-any.whl
    def url_for_version(self, version):
        split_name = self.name.split("-")[1:]
        dash_name = "-".join(split_name)
        underscored_name = "_".join(split_name)
        first_letter = dash_name[0]
        url = "https://files.pythonhosted.org/packages/{1}/{3}/{4}/{5}-{0}-{1}-{2}.whl"
        pkg_ver = version.up_to_3
        cp_ver = "py3"
        platform_tag = "none-any"
        return url.format(pkg_ver, cp_ver, platform_tag, first_letter, dash_name, underscored_name)
