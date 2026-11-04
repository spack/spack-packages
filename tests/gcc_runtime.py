# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import pathlib

import pytest
from spack_repo.builtin.packages.gcc_runtime.package import get_elf_libraries


@pytest.mark.regression
@pytest.mark.parametrize(
    "name,script,soname",
    [
        # RHEL gcc-toolset
        ("stdc++", "INPUT ( /usr/lib64/libstdc++.so.6 -lstdc++_nonshared )", "libstdc++.so.6"),
        ("gcc_s", "GROUP ( libgcc_s.so.1 -lgcc )", "libgcc_s.so.1"),
    ],
)
def test_get_elf_libraries_linker_script(tmp_path: pathlib.Path, name, script, soname):
    (tmp_path / f"lib{name}.so").write_text(f"/* GNU ld script */\n{script}\n")
    (tmp_path / soname).write_text("")
    cc = tmp_path / "cc"
    cc.write_text(f'#!/bin/sh\necho "{tmp_path}/${{1#-print-file-name=}}"\n')
    cc.chmod(0o755)

    class Compiler:
        pass

    compiler = Compiler()
    compiler.cc = str(cc)
    assert get_elf_libraries(compiler, [name]) == [(str(tmp_path / soname), soname)]
