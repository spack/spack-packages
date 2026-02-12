# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Git(AutotoolsPackage):
    """Git is a free and open source distributed version control
    system designed to handle everything from small to very large
    projects with speed and efficiency.
    """

    homepage = "https://git-scm.com"
    url = "https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.12.0.tar.gz"
    maintainers("jennfshr")

    tags = ["build-tools"]

    executables = ["^git$"]

    license("GPL-2.0-only")

    # Every new git release comes with a corresponding manpage resource:
    # https://www.kernel.org/pub/software/scm/git/git-manpages-{version}.tar.gz
    # https://mirrors.edge.kernel.org/pub/software/scm/git/sha256sums.asc
    version("2.52.0", sha256="6880cb1e737e26f81cf7db9957ab2b5bb2aa1490d87619480b860816e0c10c32")
    version("2.51.2", sha256="9b44c2b337ec838e10aad42439d390963904449710d30c9e7e4ba449f45da98f")
    version("2.51.1", sha256="b049d79e6a6cb3d81334bf689af6301f4d4c884191dfae65d2bb314a90384831")
    version("2.51.0", sha256="3d531799d2cf2cac8e294ec6e3229e07bfca60dc6c783fe69e7712738bef7283")
    version("2.50.1", sha256="522d1635f8b62b484b0ce24993818aad3cab8e11ebb57e196bda38a3140ea915")
    version("2.50.0", sha256="920f8ca563d16a7d4fdecb44349cbffbc5cb814a8b36c96028463478197050da")
    version("2.49.1", sha256="84a8383ffc77146133bc128a544450cf8ce5166cbea5056c98033d2f0c454794")
    version("2.49.0", sha256="f8047f572f665bebeb637fd5f14678f31b3ca5d2ff9a18f20bd925bd48f75d3c")
    version("2.48.2", sha256="e7f32466e7316431d472b014c344a80e68d92ba6b3aa069f64499bbe605e2383")
    version("2.48.1", sha256="51b4d03b1e311ba673591210f94f24a4c5781453e1eb188822e3d9cdc04c2212")
    version("2.47.2", sha256="a5d26bf7b01b2f0571b5a99300c256e556bd89b2a03088accf7b81bfa4f8f2fd")
    version("2.46.3", sha256="f7ae38b1d2c4724cd9088575da470229b3360903a17b531f2e86967d856ed7ed")
    version("2.45.3", sha256="40a2c40323d5077eda1e0353806b102813a23a174d24ff4b5aa7b87ffd3fcb03")
    version("2.44.3", sha256="4237c37cdf7b3d38102117b22993b2f761a4c02758dfbe33f7b7423c0b096ca9")
    version("2.43.6", sha256="f11f89bb48ecb3e18a2ecfb2a2db5a96fd6115d7e617be04e40020a50b03a038")
    version("2.42.4", sha256="886898866d624fce14f470773bc19c671c1c858091afdf5815bf569ae14356b6")
    version("2.41.3", sha256="2bf6589869f59b9c06e7b71ff8da3d7bb67b75549ca42c6f0ec81ab5e4570aa8")
    version("2.40.4", sha256="796993ef502481acbeb7caa22ffbf5f22daf8b273ab6d8dafc0ed178337d2659")

    depends_on("c", type="build")  # generated

    for _version, _sha256_manpage in {
        "2.52.0": "14426e66b5a12c188e44f53f89282bc586b34ebc3a22fafa8eb80d0bbe370f10",
        "2.51.2": "811aa98750c6d5e4c67848c9991f3d0cbe6cb109da5aefaf4a08c1d760533410",
        "2.51.1": "7c4568091b95af3a52508be4e988da4fbe194f4f410024d6af3f1af3735e3b08",
        "2.51.0": "c0e5d07f0051454df2cbdfac78e22e961e15ed5b09f10c6e58e315ca303492c2",
        "2.50.1": "96088c583129c97ed9a2b01771b8b28ad79d9f2997b46786616df3e34b180ee4",
        "2.50.0": "2e5485302a60c691e7ceb8fd994d80b04fcc9bd92daac050bf063f9a0974cfa6",
        "2.49.1": "81ec532662884778c5c48ba024e539ea6f00b1d7ae60a7b83fd1b951bfbaae1a",
        "2.49.0": "b561252841ead1e32d87dbec8f257399ea08f759c98df62c3bafa5a658f2f8ac",
        "2.48.2": "b7c274da7097844fb87d6dd0f9a2073c801bd856141c8af5ae9e56ba9686d3b3",
        "2.48.1": "88742466926d3d682be5214470ae92b79a68796a9d171d393763a5767de5a581",
        "2.47.2": "8a36a81ee3a031acbfc831a0972d849aa8777926a6c49c76141b0e0e4744dcb3",
        "2.46.3": "5744ca6fd3ef39d0390400a47f2d7208668433af3d599cfbec7bb1c7140efe79",
        "2.45.3": "eae81e0d8b00f19c47d7efecfa04642e06e777dd44e3e87ef2b192ba617cddaa",
        "2.44.3": "0f76464bbf8c0f5ccccfbacbd58d121376ff1e5147c4e0753b1ab1d578b9371e",
        "2.43.6": "ce364c74d475d321acc8b710558647ee8177876ee529456bd7f92cbb9f6961d8",
        "2.42.4": "6d207f38158d9f01c26feccb99af5a65ed3df20a18451649ce1ee718aabc331d",
        "2.41.3": "4f373c1f3d35e8f22f0920928f3d9968aa99a2a5a2673a8ed9964b96c8ee10bf",
        "2.40.4": "4a03ec30184aa27f5cf4123c532590be42d80e4b4797ad096f00b82109de1486",
    }.items():
        resource(
            name="git-manpages",
            url=f"https://www.kernel.org/pub/software/scm/git/git-manpages-{_version}.tar.gz",
            sha256=_sha256_manpage,
            placement="git-manpages",
            when=f"@{_version} +man",
        )

    variant("tcltk", default=False, description="Gitk: provide Tcl/Tk in the run environment")
    variant("perl", default=True, description="Do not use Perl scripts or libraries at all")
    variant("nls", default=True, description="Enable native language support")
    variant("man", default=True, description="Install manual pages")
    variant("subtree", default=True, description="Add git-subtree command and capability")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("curl")
    depends_on("curl@7.61.0:", when="@2.48:")
    depends_on("expat")
    depends_on("gettext", when="+nls")
    depends_on("iconv")
    depends_on("libidn2")
    depends_on("openssl")
    depends_on("pcre2")
    depends_on("perl", when="+perl")
    depends_on("perl@5.26.0:", when="@2.48: +perl")
    depends_on("zlib-api")
    depends_on("openssh", type="run")
    depends_on("tk", type=("build", "link"), when="+tcltk")
    depends_on("diffutils", type="build", when="@2.48:")

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.search(r"git version (\S+)", output)
        return match.group(1) if match else None

    @classmethod
    def determine_variants(cls, exes, version_str):
        prefix = os.path.dirname(exes[0])
        variants = ""
        if "gitk" in os.listdir(prefix):
            variants += "+tcltk"
        else:
            variants += "~tcltk"
        return variants

    # See the comment in setup_build_environment re EXTLIBS.
    def patch(self):
        filter_file(r"^EXTLIBS =$", "#EXTLIBS =", "Makefile")

        custom_lines = []

        # https://github.com/git/git/commit/cdda67de0316ec29dfc1e290bb7f2154b7b95ee8
        if self.spec.satisfies("platform=linux"):
            if self.spec.satisfies("@2.50:"):
                if self.spec.satisfies("^glibc@:2.24"):
                    custom_lines.append("CSPRNG_METHOD=")
                if self.spec.satisfies("^glibc@2.36:"):
                    custom_lines.append("CSPRNG_METHOD=arc4random")

        with open("config.mak", "w") as config_file:
            for entry in custom_lines:
                config_file.write(entry + "\n")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # We use EXTLIBS rather than LDFLAGS so that git's Makefile
        # inserts the information into the proper place in the link commands
        # (alongside the # other libraries/paths that configure discovers).
        # LDFLAGS is inserted *before* libgit.a, which requires libintl.
        # EXTFLAGS is inserted *after* libgit.a.
        # This depends on the patch method above, which keeps the Makefile
        # from stepping on the value that we pass in via the environment.
        #
        # The test avoids failures when git is an external package.
        # In that case the node in the DAG gets truncated and git DOES NOT
        # have a gettext dependency.
        spec = self.spec
        if spec.satisfies("+nls"):
            if "intl" in spec["gettext"].libs.names:
                extlib_bits = []
                if not is_system_path(spec["gettext"].prefix):
                    extlib_bits.append(spec["gettext"].libs.search_flags)
                extlib_bits.append("-lintl")
                env.append_flags("EXTLIBS", " ".join(extlib_bits))

        if not self.spec["curl"].satisfies("libs=shared"):
            curlconfig = which(
                os.path.join(self.spec["curl"].prefix.bin, "curl-config"), required=True
            )
            # For configure step:
            env.append_flags("LIBS", curlconfig("--static-libs", output=str).strip())
            # For build step:
            env.append_flags("EXTLIBS", curlconfig("--static-libs", output=str).strip())

        if self.spec.satisfies("~perl"):
            env.append_flags("NO_PERL", "1")

    def configure_args(self):
        spec = self.spec

        configure_args = [
            "--with-curl={0}".format(spec["curl"].prefix),
            "--with-expat={0}".format(spec["expat"].prefix),
            "--with-openssl={0}".format(spec["openssl"].prefix),
            "--with-zlib={0}".format(spec["zlib-api"].prefix),
        ]

        if self.spec["iconv"].name == "libiconv":
            configure_args.append(f"--with-iconv={self.spec['iconv'].prefix}")

        if self.spec.satisfies("+perl"):
            configure_args.append("--with-perl={0}".format(spec["perl"].command.path))

        if self.spec.satisfies("^pcre"):
            configure_args.append("--with-libpcre={0}".format(spec["pcre"].prefix))
        if self.spec.satisfies("^pcre2"):
            configure_args.append("--with-libpcre2={0}".format(spec["pcre2"].prefix))
        if self.spec.satisfies("+tcltk"):
            configure_args.append("--with-tcltk={0}".format(self.spec["tk"].prefix.bin.wish))
        else:
            configure_args.append("--without-tcltk")

        return configure_args

    @run_after("configure")
    def filter_rt(self):
        if self.spec.satisfies("platform=darwin"):
            # Don't link with -lrt; the system has no (and needs no) librt
            filter_file(r" -lrt$", "", "Makefile")

    def check(self):
        make("test")

    def build(self, spec, prefix):
        args = []
        if self.spec.satisfies("~nls"):
            args.append("NO_GETTEXT=1")
        make(*args)

        if spec.satisfies("platform=darwin"):
            with working_dir("contrib/credential/osxkeychain"):
                make()

    def install(self, spec, prefix):
        args = ["install"]
        if self.spec.satisfies("~nls"):
            args.append("NO_GETTEXT=1")
        make(*args)

        if spec.satisfies("platform=darwin"):
            install(
                "contrib/credential/osxkeychain/git-credential-osxkeychain",
                join_path(prefix, "libexec", "git-core"),
            )

    @run_after("install")
    def install_completions(self):
        mkdirp(bash_completion_path(self.prefix))
        install(
            "contrib/completion/git-completion.bash",
            join_path(bash_completion_path(self.prefix), "git"),
        )

        mkdirp(zsh_completion_path(self.prefix))
        filter_file(
            r"\$bash_completion\/git",
            join_path(bash_completion_path(self.prefix), "git"),
            "contrib/completion/git-completion.zsh",
        )
        install(
            "contrib/completion/git-completion.zsh",
            join_path(zsh_completion_path(self.prefix), "_git"),
        )

    @run_after("install")
    def install_manpages(self):
        if self.spec.satisfies("~man"):
            return

        prefix = self.prefix

        with working_dir("git-manpages"):
            install_tree("man1", prefix.share.man.man1)
            install_tree("man5", prefix.share.man.man5)
            install_tree("man7", prefix.share.man.man7)

    @run_after("install")
    def install_subtree(self):
        if self.spec.satisfies("+subtree"):
            with working_dir("contrib/subtree"):
                make_args = ["V=1", "prefix={}".format(self.prefix.bin)]
                make(" ".join(make_args))
                install_args = ["V=1", "prefix={}".format(self.prefix.bin), "install"]
                make(" ".join(install_args))
                install("git-subtree", self.prefix.bin)
