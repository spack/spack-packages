# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.gnu import GNUMirrorPackage

from spack.package import *


class Parallel(AutotoolsPackage, GNUMirrorPackage):
    """GNU parallel is a shell tool for executing jobs in parallel using
    one or more computers. A job can be a single command or a small
    script that has to be run for each of the lines in the input.
    """

    homepage = "https://www.gnu.org/software/parallel/"
    gnu_mirror_path = "parallel/parallel-20220522.tar.bz2"

    license("GPL-3.0-or-later", checked_by="wdconinc")

    version("20260122", sha256="831f78e01f3f28ac2441e66b10171562c71a0300353893aa05bbc277f13cc596")
    version("20251222", sha256="b56b5388da0f2cadff6f70c6e9e69f8af9516eb2665ada24d3472d596592c275")
    version("20251122", sha256="368d1982cfd9dbebb8cd0e444de6199559df94ac2dd1edf95f74350f0af1e84d")
    version("20251022", sha256="474326d59688d2fc078cf89a7b0b4a11cc9684229b3fa0158fe8bc03f1b69ee1")
    version("20250922", sha256="ee3ddc3125ef7ddcd97dde5ba64ab7f71874faa2f5d7720acdd3e4bf5265a32b")
    version("20250822", sha256="019d328722867cffe918c449364308c0df048456c69299b91451a3e6fac9167a")
    version("20250722", sha256="91a81ff4129cdf5ad3c3c45ec033e75f2bbea5447f4b6813a0d8cfe8e5c7843b")
    version("20250622", sha256="69f578cf11f1b124ba3c2b673a16641debe63aeb3d2ac4cec5ad65f8a53d489b")
    version("20250522", sha256="b4b28f475f8cff8bb6ed4b03cc5a67041f18fc73fa256923b23181b56afdb2cb")
    version("20250422", sha256="10f0a7b7fbed87edcbd63a403fdc0ee1a1f86c241a3605f33162b4b9aff248dd")
    version("20250322", sha256="c82896e779b18c2a157527f32f35de9a6d984f8b8ebad2b41dbc78c33adbaabe")
    version("20250222", sha256="d05ab27e0dd14e3bf253dbae18e7894717ce834193336c9a8eb26081305dbbf7")
    version("20250122", sha256="03c79e5b346e330cf9e5381c8e5a435fcbcdd08448964676b42f04e199bc8db3")
    version("20241222", sha256="7a1b038cb198604107f9601b7c2a176e78d845858121708fa8690671cb301a79")
    version("20241122", sha256="1a9e752f42c17ca10bc07d0a63a2ca6edcee532282e55d2b34bd9dd14c978a58")
    version("20241022", sha256="6de22bf1c67f7f316670d21ed1a2a32f1214dfbd3e420939ba937925c0a57a12")
    version("20240922", sha256="63210715e8b7c5e129e098f333cd7cdd5fc7a2f325e8e0fb9ed6edba9f1acbc4")
    version("20240822", sha256="d7bbd95b7631980b172be04cbd2138d5f7d8c063d6da5ad8f9f70dfd88c8309d")
    version("20220522", sha256="bb6395f8d964e68f3bdb26a764d3c48b69bc5b759a92ac3ab2bd1895c7fa8c1f")
    version("20220422", sha256="96e4b73fff1302fc141a889ae43ab2e93f6c9e86ac60ef62ced02dbe70b73ca7")
    version("20220322", sha256="df93ccf6a9f529ad2126b7042aef0486603e938c77b405939c41702d38a4e6d8")
    version("20220222", sha256="f81682b863ead7fb9a114754001e9286f954550a57a3cf36c9003a8047a6a445")
    version("20220122", sha256="b8221a21412bca572ad8445b7981dfd625a3c6d48772cda468dfb5b886337e00")
    version("20210922", sha256="dedca94fc41f2054dbadd9b8361e56015fc8af5d1961c1b982b63e6d86494d66")
    version("20200822", sha256="9654226a808392c365b1e7b8dea91bf4870bc4f306228d853eb700679e21be09")
    version("20190222", sha256="86b1badc56ee2de1483107c2adf634604fd72789c91f65e40138d21425906b1c")
    version("20170322", sha256="f8f810040088bf3c52897a2ee0c0c71bd8d097e755312364b946f107ae3553f6")
    version("20170122", sha256="417e83d9de2fe518a976fcff5a96bffe41421c2a57713cd5272cc89d1072aaa6")
    version("20160422", sha256="065a8f471266361218a9eb45c5f8ab995d73b181cc1180600ee08cc768c9ac42")
    version("20160322", sha256="6430f649ec07243645c955e8d6bee6da1df2e699b1e49b185946d1ab38731b08")

    def check(self):
        # The Makefile has a 'test' target, but it does not work
        make("check")

    depends_on("perl", type=("build", "run"))

    @run_before("install")
    def filter_sbang(self):
        """Run before install so that the standard Spack sbang install hook
        can fix up the path to the perl binary.
        """
        perl = self.spec["perl"].command
        kwargs = {"ignore_absent": False, "backup": False, "string": False}

        with working_dir("src"):
            match = "^#!/usr/bin/env perl|^#!/usr/bin/perl.*"
            substitute = f"#!{perl}"
            files = ["parallel", "niceload", "parcat", "sql"]
            filter_file(match, substitute, *files, **kwargs)
            # Since scripts are run during installation, we need to add sbang
            for file in files:
                filter_shebang(file)
