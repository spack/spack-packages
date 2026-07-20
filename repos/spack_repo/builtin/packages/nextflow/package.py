# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Nextflow(Package):
    """Data-driven computational pipelines."""

    homepage = "https://www.nextflow.io"
    url = "https://github.com/nextflow-io/nextflow/releases/download/v25.10.2/nextflow"

    maintainers("dialvarezs", "marcodelapierre")

    # The "release" distribution of the nextflow binary contains no bundled plugins and
    # is 'nextflow' in the project's release assets. The "standalone" distribution
    # bundles all first-party plugins and is 'nextflow-<version>-dist' in the project's
    # release assets. Only one or the other will be installed, as dictated by the
    # version string specified by the user. 'edge' releases are also supported. For each
    # version, boolean "deprecated" can be defined to deprecated all distributions of
    # that version. E.g.
    #     "25.12.0-edge": {
    #         "release": {
    #             ...
    #          },
    #          "standalone": {
    #             ...
    #          },
    #     },
    #     "25.10.2": {
    #         "release": {
    #             ...
    #         },
    #         "standalone": {
    #             ...
    #         },
    #     },
    #     "21.04.3": {
    #         "deprecated": True,
    #         "release": {
    #             ...
    #         },
    #         "standalone": {
    #             ...
    #         },
    #     },
    nf_versions = {
        "26.04.0": {
            "release": {
                "sha256": "2f0e68fa22df782bbebad4a964138756f2cf19a5544c07af2913a5f730646e44"
            },
            "standalone": {
                "sha256": "5e2b4a354b4d7634d7211b71417d61606878fb49e9b224b50ded6e2c69114870"
            },
        },
        "25.10.5": {
            "release": {
                "sha256": "a414e4581f90d1990408edc9f3192726b4c80d23a798503fd280310aa54e027a"
            },
            "standalone": {
                "sha256": "a6ff4fcd610ce00affb236587bc4bff6481733b27044730450ef753a239c2a9b"
            },
        },
        "25.10.2": {
            "release": {
                "sha256": "60aff30ad532030657296ca1fa72e37befda236bfd4fc7358a3cabf5e7589dd7"
            },
            "standalone": {
                "sha256": "59c6f48fce6139157b2e8a28fdca8166bc502a22d9ef1a0a70065ecc9c3ae4a3"
            },
        },
        "25.10.0": {
            "release": {
                "sha256": "2a398d1dbf3a7258218ae8991429369ac4fdd86cb99b8c6c8f6c922202d9d524"
            },
            "standalone": {
                "sha256": "294376ec555695ee0b92e21477600f97c113f2d1ed3fb1f480daf2ee439c4626"
            },
        },
        "25.04.8": {
            "release": {
                "sha256": "e115fbc1b2a95eee93aaa6666fccc82c0abc4760706c97d2ce971711d5dcc96b"
            },
            "standalone": {
                "sha256": "df18b2c5d89b47f471c71379a8f830a79973c1ba6ff56a55289483764d5e02ac"
            },
        },
        "25.04.6": {
            "release": {
                "sha256": "a94f8bd1db9c0271ad58ec40b9c71f812d081a66f782396928b9b1f740f0be5f"
            },
            "standalone": {
                "sha256": "c2424e11bdd5746cf5b522d5e013c66a96905c1bc69b23654aa38924e94e6cec"
            },
        },
        "25.04.3": {
            "release": {
                "sha256": "f33571f9298e930993aa4afcde84bc0d0815a59ee7168d8a153093ad08e9b263"
            },
            "standalone": {
                "sha256": "53c232cdd8a9419d2c205dc7c6c4dd2646182c997300e6439a453099e28aa21a"
            },
        },
        "25.04.0": {
            "release": {
                "sha256": "33d888b1e0127566950719316bac735975e15800018768cceb7d3d77ad0719eb"
            },
            "standalone": {
                "sha256": "9108049698bf1d8a13d8d33d920502b82d85c04780f70fcffa0ba33ab8247480"
            },
        },
        "24.10.9": {
            "release": {
                "sha256": "9080820f9c36a08d166d509a6c6df15a1de2e3e04b969aaeef148ef2d87e3025"
            },
            "standalone": {
                "sha256": "627d5eaf1ecea49caa88cc71e21d5a9548d9b12c1fedbacbb74f76fa202db35e"
            },
        },
        "24.10.5": {
            "release": {
                "sha256": "a9733a736cfecdd70e504b942e823da7005f9afc288902e67afe86b43dc9bcdb"
            },
            "standalone": {
                "sha256": "79c7601a7d8d6f77dd9393377da453cd1ab59e821fa41324badcdd5dfc54855b"
            },
        },
        "24.10.3": {
            "release": {
                "sha256": "01110949bb3256bf6cbf1d4b3ea17369491b3f693b6d86a0c9ab8171b1619ba0"
            },
            "standalone": {
                "sha256": "c1a0f9a59406bc5d0c56734a5cc35294c9d0e600c08d0685b4072659cf69b8f2"
            },
        },
        "24.10.2": {
            "release": {
                "sha256": "e12bf1fc1e11629f2aef22a9a6ddecc31522bcd5988d1c48d263de699b4e5289"
            },
            "standalone": {
                "sha256": "972bb4f4bcd30bb474c29c247ccf79289bbcd444f799f0307f61123e6b0f7475"
            },
        },
        "24.10.0": {
            "release": {
                "sha256": "e848918fb9b85762822c078435d9ff71979a88cccff81ce5babd75d5eee52fe6"
            },
            "standalone": {
                "sha256": "336019d1b526923b70b4f0cd1f80a9e37285826bb081032effa329ff177208cb"
            },
        },
        "24.04.6": {
            "release": {
                "sha256": "77f43bc1c3d1749a68f294ae07e5cc0ffadde92f57106ea9711c4bafd68a6c64"
            },
            "standalone": {
                "sha256": "024542ca21b00e44a1516265ae0b81396e22c468d4a11527a7dfe5e9de16ef76"
            },
        },
        "24.04.3": {
            "release": {
                "sha256": "e258f6395a38f044eb734cba6790af98b561aa521f63e2701fe95c050986e11c"
            },
            "standalone": {
                "sha256": "7e6dce2df4565fcd1fb9bfea3f68087e51cb5b7aa3010eec20116917bea3a07b"
            },
        },
        "24.04.1": {
            "release": {
                "sha256": "d1199179e31d0701d86e6c38afa9ccade93f62d545e800824be7767a130510ba"
            },
            "standalone": {
                "sha256": "bf98f93c90318fd06109855986caba06086b197256ce2068509372bed2b517a6"
            },
        },
        "23.10.1": {
            "release": {
                "sha256": "9abc54f1ffb2b834a8135d44300404552d1e27719659cbb635199898677b660a"
            },
            "standalone": {
                "sha256": "5d8eb1b849108e058dbbcc0dbc737731215a85a4535321936c365e8c06c7409e"
            },
        },
        "23.10.0": {
            "release": {
                "sha256": "4b7fba61ecc6d53a6850390bb435455a54ae4d0c3108199f88b16b49e555afdd"
            },
            "standalone": {
                "sha256": "c69f6055c97741b828b6ee67de38125a42f1774f1621afd34c0eb72ffea171a6"
            },
        },
        "23.04.3": {
            "release": {
                "sha256": "258714c0772db3cab567267e8441c5b72102381f6bd58fc6957c2972235be7e0"
            },
            "standalone": {
                "sha256": "731b3fa6acf52440c05c9e8d9422edce24eb2cae3acc1603e8be55ca10ca6ac4"
            },
        },
        "23.04.1": {
            "release": {
                "sha256": "5de3e09117ca648b2b50778d3209feb249b35de0f97cdbcf52c7d92c7a96415c"
            },
            "standalone": {
                "sha256": "1c6591adaedaa05aadd9f4c2cb4fe22d61c8d2a7ddcc99474125e9e94865d6a4"
            },
        },
        "22.10.4": {
            "release": {
                "sha256": "612a085e183546688e0733ebf342fb73865f560ad1315d999354048fbca5954d"
            },
            "standalone": {
                "sha256": "feec0b078a1053512f2c21cdfc92f624f92062c49a3c14a201e6b7458ae5ac71"
            },
        },
        "22.10.3": {
            "release": {
                "sha256": "8d67046ca3b645fab2642d90848550a425c9905fd7dfc2b4753b8bcaccaa70dd"
            },
            "standalone": {
                "sha256": "640b72aaf691db1b11f43306f6557df06518408eca01c2fa7429cbe37264db8b"
            },
        },
        "22.10.1": {
            "release": {
                "sha256": "fa6b6faa8b213860212da413e77141a56a5e128662d21ea6603aeb9717817c4c"
            },
            "standalone": {
                "sha256": "c5edc9fc81d9c6eb4f628505f14f8bb4fe044d4fc7d9ef60654ba0d73abf5a80"
            },
        },
        "22.10.0": {
            "release": {
                "sha256": "6acea8bd21f7f66b1363eef900cd696d9523d2b9edb53327940f093189c1535e"
            },
            "standalone": {
                "sha256": "a714beebcb544d6c140286219340a9440d412d2ad57a691de0f0610684204e83"
            },
        },
        "22.04.4": {
            "release": {
                "sha256": "e5ebf9942af4569db9199e8528016d9a52f73010ed476049774a76b201cd4b10"
            },
            "standalone": {
                "sha256": "8d341a11d3efa95e8dbdcb26909942dcd6ce09c659f5372021b205403521d9bd"
            },
        },
        "22.04.3": {
            "release": {
                "sha256": "a1a79c619200b9f2719e8467cd5b8fbcb427f43adf945233ba9e03cd2f2d814e"
            },
            "standalone": {
                "sha256": "5a16941b80361e3a5add8a169f636862c886df777c10b10d360be14df7268d5b"
            },
        },
        "22.04.1": {
            "release": {
                "sha256": "89ef482a53d2866a3cee84b3576053278b53507bde62db4ad05b1fcd63a9368a"
            },
            "standalone": {
                "sha256": "56cca853251771e81e50e8db213582ad4714c59484016e8c48d25001b7178df9"
            },
        },
        "22.04.0": {
            "release": {
                "sha256": "8eba475aa395438ed222ff14df8fbe93928c14ffc68727a15b8308178edf9056"
            },
            "standalone": {
                "sha256": "f366f14df881fb26dc2f815d34e91180eef6e2ba51d289b9776f71b905a36750"
            },
        },
    }

    for ver, attrs in nf_versions.items():
        is_deprecated = False

        if "deprecated" in attrs:
            is_deprecated = attrs["deprecated"]

        # Edge release. Not preferred.
        if "edge" in ver:
            version(
                ver,
                sha256=attrs["release"]["sha256"],
                expand=False,
                preferred=False,
                deprecated=is_deprecated,
            )

        else:
            # Release dist for stable version. Preferred.
            version(
                ver,
                sha256=attrs["release"]["sha256"],
                expand=False,
                preferred=True,
                deprecated=is_deprecated,
            )

        # Standalone dist for version.
        version(
            f"{ver}-standalone",
            sha256=attrs["standalone"]["sha256"],
            expand=False,
            preferred=False,
            deprecated=is_deprecated,
        )

    depends_on("java@17:", type="run", when="@25:")
    depends_on("java@11:", type="run", when="@23:")
    depends_on("java@11:", type="run", when="platform=darwin")
    depends_on("java@8:", type="run")

    def url_for_version(self, version):
        ver = str(version).replace("-standalone", "")
        uri = f"https://github.com/nextflow-io/nextflow/releases/download/v{ver}"
        if "standalone" in str(version):
            # standalone binary name changed with 24.07.0-edge
            if version < Version("24.07.0"):
                return f"{uri}/nextflow-{ver}-all"
            else:
                return f"{uri}/nextflow-{ver}-dist"
        else:
            return f"{uri}/nextflow"

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(self.stage.archive_file, join_path(prefix.bin, "nextflow"))
        set_executable(join_path(prefix.bin, "nextflow"))
