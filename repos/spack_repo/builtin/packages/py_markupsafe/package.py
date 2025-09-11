# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMarkupsafe(PythonPackage):
    """MarkupSafe is a library for Python that implements a unicode
    string that is aware of HTML escaping rules and can be used to
    implement automatic string escaping. It is used by Jinja 2, the
    Mako templating engine, the Pylons web framework and many more."""

    homepage = "https://palletsprojects.com/p/markupsafe"
    pypi = "MarkupSafe/markupsafe-3.0.2.tar.gz"
    git = "https://github.com/pallets/markupsafe.git"

    license("BSD-3-Clause")

    version("3.0.2", sha256="ee55d3edf80167e48ea11a923c7386f4669df67d7994554387f84e7d8b0a2bf0")
    version("2.1.5", sha256="d283d37a890ba4c1ae73ffadf8046435c76e7bc2247bbb63c00bd1a709c6544b")
    version("2.1.3", sha256="af598ed32d6ae86f1b747b82783958b1a4ab8f617b06fe68795c7f026abbdcad")
    version("2.1.1", sha256="7f91197cc9e48f989d12e4e6fbc46495c446636dfc81b9ccf50bb0ec74b91d4b")
    version("2.0.1", sha256="594c67807fb16238b30c44bdf74f36c02cdf22d1c8cda91ef8a0ed8dabf5620a")
    version("1.1.1", sha256="29872e92839765e546828bb7754a68c418d927cd064fd4708fab9fe9c8bb116b")
    version("1.0", sha256="a6be69091dac236ea9c6bc7d012beab42010fa914c459791d627dad4910eb665")
    version("0.23", sha256="a4ec1aff59b95a14b45eb2e23761a0179e98319da5a7eb76b56ea8cdc7b871c3")
    version("0.22", sha256="7642852b6d1e55c9e12e00a552c0b8943880f2172e55141ccb41eb5f8675dfa5")
    version("0.21", sha256="c6465cd6ed2b96509ef0100e7fff8718ed52c2affab1860ed5a9b67f604dd59a")
    version("0.20", sha256="f6cf3bd233f9ea6147b21c7c02cac24e5363570ce4fd6be11dab9f499ed6a7d8")
    version("0.19", sha256="62fcc5d641df8b5ad271ebbd6b77a19cd92eceba1e1a990de4e96c867789f037")

    depends_on("c", type="build")  # generated

    depends_on("python@3.9:", type=("build", "run"), when="@3:")
    depends_on("python@3.7:", type=("build", "run"), when="@2:")
    depends_on("py-setuptools@70.1:", type="build", when="@3:")
    depends_on("py-setuptools", type="build")

    def url_for_version(self, version):
        if version >= Version("3.0.0"):
            name = "markupsafe"
        else:
            name = "MarkupSafe"
        return (
            f"https://files.pythonhosted.org/packages/source/M/MarkupSafe/{name}-{version}.tar.gz"
        )
