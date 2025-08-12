# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class EtcdCppApiv3(CMakePackage):
    """The etcd-cpp-apiv3 is a C++ library for etcd's v3 client APIs, i.e., ETCDCTL_API=3."""

    homepage = "https://github.com/etcd-cpp-apiv3/etcd-cpp-apiv3"
    url = "https://github.com/etcd-cpp-apiv3/etcd-cpp-apiv3/archive/refs/tags/v0.15.4.tar.gz"
    git = homepage + ".git"

    license("BSD-3-Clause")

    version("master", branch="master")
    version("0.15.4", sha256="4516ecfa420826088c187efd42dad249367ca94ea6cdfc24e3030c3cf47af7b4")

    depends_on("boost")
    depends_on("openssl")
    depends_on("grpc")
    depends_on("protobuf")
    depends_on("cpprestsdk")

    patch(  # Latest GRPC >= 2.66 has dropped GRPC_ASSERT macro
        "https://github.com/etcd-cpp-apiv3/etcd-cpp-apiv3/commit/216b86f8d763acf88e4ed7265f983b57c12da2df.patch?full_index=1",
        sha256="4d16ab69a5dd6af4c0eb99c777dae6ffb913116b074882381cea69889789308e",
    )
