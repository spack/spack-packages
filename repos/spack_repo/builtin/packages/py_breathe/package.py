# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBreathe(PythonPackage):
    """This is an extension to reStructuredText and Sphinx to be able to read
    and render Doxygen XML output."""

    homepage = "https://github.com/breathe-doc/breathe"
    url = "https://github.com/breathe-doc/breathe/archive/refs/tags/v4.36.0.tar.gz"

    maintainers("sethrj")

    license("BSD-3-Clause")

    version("4.36.0", sha256="94fc2277e639929e898cb95559d9d2c51cf764b787eaf6fa04f848a6550c2ff5")
    version("4.35.0", sha256="55b54723752fc04b892a0f868782b1df65e69db6ca94fb32cf04be495bfd7841")
    version("4.34.0", sha256="b22e70eb4000492508d687d71f258c8f9678398e277bcee0daf34cd438a46e25")
    version("4.33.1", sha256="acda75b216b227ec09ffd74378a6c7ed8f023df4539693c6e20574d1df52e75b")
    version("4.21.0", sha256="7f97756a1b7f7998377b1153a976bf0d2879bb3ca1cb7bc846f455d37ca87ead")
    version("4.11.1", sha256="84723eefc7cc05da6895e2dd6e7c72926c5fd88a67de57edce42d99c058c7e06")
    version("4.11.0", sha256="8c9f900560529ca2f589f26759be94c2accad14fd83fee34d353cf6f446e09f6")
    version("4.10.0", sha256="10e294ca2927d40c83343674186ce6fad539acfb464ffd765fd371adc1126d4d")
    version("4.9.1", sha256="3e1e31b879dcd1fe1ebdaf4d0b11356b8e348ac5af101cafa9e54956716a7f02")
    version("4.9.0", sha256="a2b4b8cd2c4ef708ae69dd174e65731b1e18c24f8670036d2f5e608558be2613")
    version("4.8.0", sha256="edac7732ad8702ea0425773f1f0c98e7ad5028dbba5fe6483f32a1df3afe2f31")
    version("4.7.3", sha256="35e2e937fad97c6d7e287db6007184325284130ab50e1154fe126cffc09a1989")
    version("4.7.2", sha256="982d47909d22fcd71b48bad5aef3644294340b24f612b2887cde2e3be464d960")
    version("4.7.1", sha256="afb1ab0084b25d3670fa8f5cf2eeaee6fe61bfc77876e3816b140eacd4949875")
    version("4.7.0", sha256="5629c67f5adb41f39375d36c5f0d60d34b1230be268125e535205d77f69211e4")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:", when="@4.36:")
        depends_on("python@3.6:", when="@4.33:4.35")
        depends_on("python@3.5:", when="@4.21:4.32")

        depends_on("py-sphinx@7.2:", when="@4.35:")
        depends_on("py-sphinx@4,5.0.1:5", when="@4.34")
        depends_on("py-sphinx@3:4", when="@4.33")
        depends_on("py-sphinx@3:3.2", when="@4.21:4.32")
        depends_on("py-sphinx@:3", when="@:4.20")

        depends_on("py-six@1.9:", when="@4.21:4.32")
        depends_on("py-six@1.4:", when="@:4.20")

    with default_args(type="build"):
        depends_on("py-flit-core@3.7:", when="@4.36:")
        depends_on("py-setuptools", type="build", when="@:4.35")

    # Doxygen is *implicitly* required to build the XML files used by breathe,
    # but it is not called directly. It is used directly by the examples, which
    # are not hooked up to this spack recipe.
    depends_on("doxygen@1.8.4:", type="run")
