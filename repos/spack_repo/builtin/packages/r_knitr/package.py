# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RKnitr(RPackage):
    """A General-Purpose Package for Dynamic Report Generation in R.

    Provides a general-purpose tool for dynamic report generation in R using
    Literate Programming techniques."""

    cran = "knitr"

    license("GPL-2.0-or-later")

    version("1.51", sha256="bcfa3081677ff5c3881c7cef35f3305bbf6714b01320c81a523772663741ca11")
    version("1.48", sha256="501b5926da7da1e8df61958639537e4c30110a0a8de07381afd92b31b9bff197")
    version("1.42", sha256="9344f1a0089e4da101def54aee38d7cfe3b2022d75c560141d8cc22ac65130f3")
    version("1.40", sha256="9b8f95ff367a0e52f024bda30315ec7cdd6a5b82371a1aaed95ab4eea78535bc")
    version("1.39", sha256="c91a65edebdca779af7f7480fa6636667497c9291ad55d6efd982db0bb91ac72")
    version("1.37", sha256="39cd2a4848baebbe7fa0c0ab8200179690fb5b9190f0c1688d987c38363ad763")
    version("1.33", sha256="2f83332b0a880de6eae522271bda7f862c97693fba45c23ab1f772028f6c0909")
    version("1.30", sha256="3aabb13566a234131ba18b78d690104f9468a982dc711f81344a985318c7c93e")
    version("1.28", sha256="05ee01da31d715bf24793efb3e4ef3bb3101ef1e1ab2d760c645fc5b9d40232a")
    version("1.24", sha256="e80c2043b445a7e576b62ae8510cce89322660fe388881d799a706d35cd27b89")
    version("1.23", sha256="063bfb3300fc9f3e7d223c346e19b93beced0e6784470b9bef2524868a206a99")
    version("1.17", sha256="9484a2b2c7b0c2aae24ab7f4eec6db48affbceb0e42bd3d69e34d953fe92f401")
    version("1.14", sha256="ba6d301482d020a911390d5eff181e1771f0e02ac3f3d9853a9724b1ec041aec")

    with default_args(type=("build", "run")):
        depends_on("r@3.6.0:", when="@1.49:")
        depends_on("r@3.3.0:", when="@1.39:")
        depends_on("r@3.2.3:", when="@1.23:")
        depends_on("r@3.1.0:", when="@1.15:1.22")
        depends_on("r@3.0.2:", when="@1.10:1.14")
        depends_on("r@2.14.1:", when="@:1.9")

        depends_on("r-evaluate@0.15:", when="@1.39:")
        depends_on("r-evaluate@0.10:")

        depends_on("r-highr@0.11:", when="@1.47:")
        depends_on("r-highr")

        depends_on("r-xfun@0.52:", when="@1.51:")
        depends_on("r-xfun@0.44:", when="@1.47:")
        depends_on("r-xfun@0.43:", when="@1.46:")
        depends_on("r-xfun@0.39:", when="@1.43:")
        depends_on("r-xfun@0.34:", when="@1.42:")
        depends_on("r-xfun@0.29:", when="@1.39:")
        depends_on("r-xfun@0.27:", when="@1.37:")
        depends_on("r-xfun@0.21:", when="@1.32:")
        depends_on("r-xfun@0.19:", when="@1.31")
        depends_on("r-xfun@0.15:", when="@1.30")
        depends_on("r-xfun", when="@1.23:")

        depends_on("r-yaml@2.1.19:")

        depends_on("py-rst2pdf")
        depends_on("pandoc")

        # Historical dependencies
        depends_on("r-digest", when="@:1.17")
        depends_on("r-formatr", when="@:1.14")
        depends_on("r-markdown", when="@:1.33")
        depends_on("r-stringr@0.6:", when="@:1.40")
