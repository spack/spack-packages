# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.packages.qt_base.package import QtBase, QtPackage

from spack.package import *


class QtTools(QtPackage):
    """Qt Tools contains tools like Qt Designer."""

    url = QtPackage.get_url(__qualname__)
    git = QtPackage.get_git(__qualname__)
    list_url = QtPackage.get_list_url(__qualname__)

    maintainers("wdconinc")

    license("BSD-3-Clause")

    # src/assistant/qlitehtml is a submodule that is not in the git archive
    version("6.11.1", commit="947c5f152f4abc06f9e135b411c06a6fbe608aed", submodules=True)
    version("6.10.2", commit="171ae9df0d84ee5133193cd3e27848fd73601c53", submodules=True)
    version("6.10.1", commit="9e0030f889168f7a0ec1bb47a7d7138a497b3c96", submodules=True)
    version("6.10.0", commit="f33c4bb1dee569eec4ffe1333584cb4b75af6c59", submodules=True)
    version("6.9.3", commit="89031fa54058af5e4d92ee08d31642ca338e9c0c", submodules=True)
    version("6.9.2", commit="f117f860edcbe49a38275bfe35d3573614be6107", submodules=True)
    version("6.9.1", commit="9e8f157b49c78c05abf8fa87da21e04cdf09780c", submodules=True)
    version("6.9.0", commit="087e300bf286aaee92682d828ee0bd622e00d52a", submodules=True)
    version("6.8.3", commit="2649ea1aa5cc1c23bd920ae94dd50071315ea30f", submodules=True)
    version("6.8.2", commit="8aa2456d4461516f54c98916fcd699557afb41ad", submodules=True)
    version("6.8.1", commit="b0d66c51cbda17b213bed73d379f0900c77f457c", submodules=True)
    version("6.8.0", commit="3dd2b6ad0dd1a0480628b4cc74cb7b89a89e4a61", submodules=True)
    version("6.7.3", commit="ec4747e62a837a0262212a5f4fb03734660c7360", submodules=True)
    version("6.7.2", commit="46ffaed90df8c14d67b4b16fdf5e0b87ab227c88", submodules=True)

    variant(
        "assistant",
        default=False,
        description="Qt Assistant for viewing on-line documentation in Qt help file format.",
    )
    variant(
        "designer",
        default=False,
        description="Qt Widgets Designer for designing and building GUIs with Qt Widgets.",
    )
    variant(
        "qdoc",
        default=False,
        description="QDoc is Qt's documentation generator for C++ and QML projects.",
    )
    variant(
        "linguist",
        default=False,
        description="Qt Linguist can be used by translator to translate text in Qt applications.",
    )

    # use of relative path in https://github.com/qt/qttools/blob/6.8.2/.gitmodules
    conflicts("+assistant", when="@6.8.2", msg="Incorrect git submodule prevents +assistant")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("llvm +clang", when="+qdoc")

    depends_on("qt-base +network")
    depends_on("qt-base +widgets", when="+designer")

    depends_on("zstd@1.3:", when="+designer")

    for _v in QtBase.versions:
        v = str(_v)
        depends_on("qt-base@" + v, when="@" + v)

    def cmake_args(self):
        return super().cmake_args() + [
            self.define_qt_feature("fullqthelp", True),
            self.define_qt_feature_from_variant("qdoc"),
            self.define_qt_feature_from_variant("clang", "qdoc"),
            self.define_qt_feature_from_variant("assistant"),
            self.define_qt_feature_from_variant("designer"),
            self.define_qt_feature_from_variant("zstd", "designer"),
            self.define_qt_feature_from_variant("linguist"),
        ]
