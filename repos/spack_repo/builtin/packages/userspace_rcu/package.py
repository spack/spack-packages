# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class UserspaceRcu(AutotoolsPackage):
    """liburcu is a LGPLv2.1 userspace RCU (read-copy-update) library. This
    data synchronization library provides read-side access which scales
    linearly with the number of cores."""

    homepage = "https://liburcu.org/"
    url = "https://github.com/urcu/userspace-rcu/archive/v0.11.1.tar.gz"

    license("LGPL-2.1-or-later")

    version("0.15.7", sha256="a5d37ac56d984b36f8a1ec0831fd5137aa73dfe16be6d716f76ae16125024ac9")
    version("0.15.6", sha256="15c341ce8b93d3b70bec120c1df90b2b02a219d65593cddeb4b52521a950e45e")
    version("0.15.5", sha256="46d276662de37c2be46675be7b5ab418b0a7ef308fe92ec7fbc0cc4436ee8c38")
    version("0.15.4", sha256="530e10617a09cce5cd8ac1f3351b8caba5244247bdafb3baed61f1f7980592db")
    version("0.15.3", sha256="b9b3516b4a403e96fe6be471a52df672dfd89249b8b27b19bc9ef4cc7cb40275")
    version("0.15.2", sha256="83aea81e4b8f7ea9087d655afb40a7d6228daae8cdde0c70c8b84f9dee657159")
    version("0.15.1", sha256="5dc719a6cd59ea90543c731da1c31ebc8172cabee1c8bee0e7a7ab236eb0ef8f")
    version("0.15.0", sha256="e3e1b2c1828d7dbeeb9291c9a9cfdaad8f1fda436d24fc08f654ad2c01b01f92")
    version("0.14.3", sha256="e0e52c687fc3c0e832e1b52ca81d9af818df1a0bc8b2610895300012f4b3dac5")
    version("0.14.2", sha256="be1e6db564b4f8a889526f5bb632883cd0f7bc87a9f0df28455ca13e0f845898")
    version("0.14.1", sha256="d8f883c774e1be4fecb216e0ed594fb595ecb04a15720db876ae29a41e198437")
    version("0.14.0", sha256="42fb5129a3fffe5a4b790dfe1ea3a734c69ee095fefbf649326269bba94c262d")
    version("0.13.3", sha256="2752d58f05859e8d1c458c6d162f03625dcd51c28e65c54fb419f4074bb07a65")
    version("0.13.2", sha256="312d95376e76068b8cc70347676f1570f4f20b3014862f729dc538a316593824")
    version("0.13.1", sha256="b810481f0c859a5859d82e23eddd2856b410802009f94663d64c330dc2f4403e")
    version("0.13.0", sha256="c457d17ec9dff7db0e90b103ef1a03737efdeaec13098af82f83a03091c835b5")
    version("0.12.3", sha256="a61b5aca001f70cb576505cc4869bd74a758484343466cc49cb1342c67028a54")
    version("0.12.2", sha256="d282169cdfa9fcc4cfbacab3757bb739debf4559a7f9ad537bb8b2061e98351a")
    version("0.12.1", sha256="19f31563db5078f47cabbb06bd7a3935a0964e31449efedd267f311ae79443c6")
    version("0.12.0", sha256="6b0cdee07a651c56daea8d03285f379afab898ebc83c785a23927320e45a3012")
    version("0.11.4", sha256="d995598482221587ff6753d2a8da6ac74ff0fa79fbea29ccee196f295834531d")
    version("0.11.3", sha256="fa7a3be0fe1bb000be0a5b28c5b33fdbc13d7cf5a4816b9bcbc60e2adf8ec8d5")
    version("0.11.2", sha256="072da1b9cf864a4cb9f7b9bb6c208979682ce018cbd1ead0ee84e294e3035cbd")
    version("0.11.1", sha256="a0ed8995edfbeac5f5eb2f152a8f3654040ecfc99a746bfe3da3bccf435b7d5d")
    version("0.11.0", sha256="7834e4692565b491b9d2d258095d6c05089c9bae8a1bef280c338d15ba02e9ac")
    version("0.10.2", sha256="e117c416fced894e24720cc1b38247074a13020f19d6704b38e554cbcb993d06")
    version("0.9.6", sha256="4d9e4ca40c079e0b0e9f912a9092589b97fbaf80eb6537e9ae70d48c09472efa")

    depends_on("c", type="build")  # generated

    depends_on("m4", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")

    patch(
        "examples.patch", sha256="49aa8fa99d3a1315c639d2a90014079c34a7d0a6dde110b6cbb7b02f87324742"
    )

    def autoreconf(self, spec, prefix):
        bash = which("bash", required=True)
        bash("./bootstrap")
