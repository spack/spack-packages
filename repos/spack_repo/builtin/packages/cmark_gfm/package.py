# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class CmarkGfm(CMakePackage):
    """cmark-gfm is the fork of the CommonMark reference implementation that GitHub uses.
    It adds the GitHub Flavored Markdown extensions, such as tables, strikethrough and
    autolinks, in a separate library."""

    homepage = "https://github.com/github/cmark-gfm"
    url = "https://github.com/github/cmark-gfm/archive/refs/tags/0.29.0.gfm.13.tar.gz"
    git = "https://github.com/github/cmark-gfm.git"

    maintainers("teaguesterling")

    license("BSD-2-Clause")

    version(
        "0.29.0.gfm.13", sha256="5abc61798ebd9de5660bc076443c07abad2b8d15dbc11094a3a79644b8ad243a"
    )

    # The static libraries always have POSITION_INDEPENDENT_CODE, so there is no pic variant
    variant("shared", default=True, description="Build shared libraries, else static ones")

    depends_on("c", type="build")
    # project() enables C++, though the libraries are C
    depends_on("cxx", type="build")
    depends_on("cmake@3.0:", type="build")

    def cmake_args(self):
        return [
            self.define_from_variant("CMARK_SHARED", "shared"),
            self.define("CMARK_STATIC", self.spec.satisfies("~shared")),
            self.define("CMARK_TESTS", False),
        ]

    @run_after("install")
    def install_config_files(self):
        """Adds the CMake package files that find_package(<name> CONFIG) needs.

        The project installs its exported targets as lib/cmake/cmark-gfm.cmake and
        lib/cmake-gfm-extensions/cmark-gfm-extensions.cmake, which find_package does not find.
        The vcpkg port renames those files, and adds the include directory to the targets.
        These files include the exported targets, and add the include directory.
        """
        for name, export_dir in (
            ("cmark-gfm", "cmake"),
            ("cmark-gfm-extensions", "cmake-gfm-extensions"),
        ):
            (targets,) = find(self.prefix, f"{export_dir}/{name}.cmake", recursive=True)
            config_dir = join_path(os.path.dirname(os.path.dirname(targets)), "cmake", name)
            mkdirp(config_dir)
            # Paths relative to the file, so that a move of the prefix does not break them
            targets = os.path.relpath(targets, config_dir)
            include = os.path.relpath(self.prefix.include, config_dir)
            with open(join_path(config_dir, f"{name}-config.cmake"), "w") as output:
                output.write(
                    f'include("${{CMAKE_CURRENT_LIST_DIR}}/{targets}")\n'
                    f'get_filename_component(_include "${{CMAKE_CURRENT_LIST_DIR}}/{include}"'
                    " ABSOLUTE)\n"
                    f"foreach(_target lib{name} lib{name}_static)\n"
                    "  if(TARGET ${_target})\n"
                    "    set_property(TARGET ${_target} APPEND PROPERTY\n"
                    '      INTERFACE_INCLUDE_DIRECTORIES "${_include}")\n'
                    "  endif()\n"
                    "endforeach()\n"
                )
