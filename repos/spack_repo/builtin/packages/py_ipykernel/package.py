# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyIpykernel(PythonPackage):
    """IPython Kernel for Jupyter"""

    homepage = "https://github.com/ipython/ipykernel"
    pypi = "ipykernel/ipykernel-5.3.4.tar.gz"

    maintainers("ChristopherChristofi")

    license("BSD-3-Clause")

    version("6.30.1", sha256="6abb270161896402e76b91394fcdce5d1be5d45f456671e5080572f8505be39b")
    version("6.29.5", sha256="f093a22c4a40f8828f8e330a9c297cb93dcab13bd9678ded6de8e5cf81c56215")
    version("6.29.4", sha256="3d44070060f9475ac2092b760123fadf105d2e2493c24848b6691a7c4f42af5c")
    version("6.28.0", sha256="69c11403d26de69df02225916f916b37ea4b9af417da0a8c827f84328d88e5f3")
    version("6.27.1", sha256="7d5d594b6690654b4d299edba5e872dc17bb7396a8d0609c97cb7b8a1c605de6")
    version("6.26.0", sha256="553856658eb8430bbe9653ea041a41bff63e9606fc4628873fc92a6cf3abd404")
    version("6.25.2", sha256="f468ddd1f17acb48c8ce67fcfa49ba6d46d4f9ac0438c1f441be7c3d1372230b")
    version("6.24.0", sha256="29cea0a716b1176d002a61d0b0c851f34536495bc4ef7dd0222c88b41b816123")
    version("6.23.3", sha256="dd4e18116357f36a1e459b3768412371bee764c51844cbf25c4ed1eb9cae4a54")
    version("6.23.1", sha256="1aba0ae8453e15e9bc6b24e497ef6840114afcdb832ae597f32137fa19d42a6f")
    version("6.22.0", sha256="302558b81f1bc22dc259fb2a0c5c7cf2f4c0bdb21b50484348f7bafe7fb71421")
    version("6.16.0", sha256="7fe42c0d58435e971dc15fd42189f20d66bf35f3056bda4f6554271bc1fa3d0d")
    version("6.15.2", sha256="e7481083b438609c9c8a22d6362e8e1bc6ec94ba0741b666941e634f2d61bdf3")
    version("6.9.1", sha256="f95070a2dfd3147f8ab19f18ee46733310813758593745e07ec18fb08b409f1d")
    version("6.4.1", sha256="df3355e5eec23126bc89767a676c5f0abfc7f4c3497d118c592b83b316e8c0cd")
    version("6.2.0", sha256="4439459f171d77f35b7f7e72dace5d7c2dd10a5c9e2c22b173ad9048fbfe7656")
    version("6.0.2", sha256="7fb3e370dbb481b012b74bed4e794d2d16eb2a83930b31e6d8d030b9fdb4d5b4")
    version("5.5.6", sha256="4ea44b90ae1f7c38987ad58ea0809562a17c2695a0499644326f334aecd369ec")
    version("5.5.5", sha256="e976751336b51082a89fc2099fb7f96ef20f535837c398df6eab1283c2070884")

    depends_on("py-hatchling@1.4:", when="@6.13.1:", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:", when="@6.30:")
        depends_on("python@3.8:", when="@6.11:")
        depends_on("python@3.8:3.11", when="@6:6.10")
        depends_on("python@3.6:3.9", when="@5.5:5")

        with when("@6:"):
            depends_on("py-debugpy@1.6.5:", when="@6.22:")
            depends_on("py-debugpy@1:")
            depends_on("py-debugpy@:1", when="@:6.10")

            depends_on("py-matplotlib-inline@0.1:")
            depends_on("py-matplotlib-inline@:0.1", when="@:6.10")

        depends_on("py-ipython@7.23.1:", when="@6.5.1:")
        depends_on("py-ipython@7.23.1:7", when="@6:6.5.0")
        depends_on("py-ipython@5:", when="@5:")
        depends_on("py-ipython@:7", when="@:6.5")

        depends_on("py-comm@0.1.1:", when="@6.22:")

        depends_on("py-traitlets@5.4:", when="@6.22:")
        depends_on("py-traitlets@5.1:", when="@6.5:")
        depends_on("py-traitlets@4.1.0:")
        depends_on("py-traitlets@:5", when="@:6.10")

        depends_on("py-jupyter-client@8:", when="@6.30:")
        depends_on("py-jupyter-client@6.1.12:", when="@6.11:")
        depends_on("py-jupyter-client")
        depends_on("py-jupyter-client@:7", when="@:6.10")
        depends_on("py-jupyter-client@:6", when="@:6.1")

        depends_on("py-jupyter-core@4.12:", when="@6.22:")

        depends_on("py-nest-asyncio@1.4:", when="@6.30:")
        depends_on("py-nest-asyncio", when="@6.6.1:")

        depends_on("py-tornado@6.2:", when="@6.30:")
        depends_on("py-tornado@6.1:", when="@6.11:")
        depends_on("py-tornado@5:", when="@6.10:")
        depends_on("py-tornado@4.2:", when="@5:")
        depends_on("py-tornado@:6", when="@:6.10")

        depends_on("py-appnope@0.1.2:", when="@6.30: platform=darwin")
        depends_on("py-appnope", when="@5.1.3: platform=darwin")

        depends_on("py-pyzmq@25:", when="@6.30:")
        depends_on("py-pyzmq@24:", when="@6.28:")
        depends_on("py-pyzmq@20:", when="@6.22:")
        depends_on("py-pyzmq@17:", when="@6.15:")

        depends_on("py-psutil@5.7:", when="@6.30:")
        depends_on("py-psutil", when="@6.9.2:")

        depends_on("py-packaging@22:", when="@6.30:")
        depends_on("py-packaging", when="@6.12:")

    conflicts("^py-jupyter-core@5.0")

    # Historical dependencies
    depends_on("py-setuptools", when="@5:6.13.0", type="build")
    depends_on("py-jupyter-core@4.2:", when="@5:6.13.0", type="build")
    depends_on("py-ipython-genutils", when="@6.3.1:6.4", type=("build", "run"))
    depends_on("py-ipython-genutils", when="@5.5.6", type=("build", "run"))
    depends_on("py-importlib-metadata@:4", when="@6.1:6.6 ^python@:3.7", type=("build", "run"))
    depends_on("py-importlib-metadata@:3", when="@6.0.0:6.0 ^python@:3.7", type=("build", "run"))
    depends_on("py-argcomplete@1.12.3:", when="@6.1:6.6 ^python@:3.7", type=("build", "run"))

    @run_after("install")
    def install_data(self):
        """install the Jupyter kernel spec"""
        python("-m", "ipykernel", "install", "--prefix=" + self.prefix)
