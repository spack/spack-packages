# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

# nextflow distributions are available at
# https://github.com/nextflow-io/nextflow/releases
#
# The "release" distribution of the nextflow binary contains no bundled plugins and is
# 'nextflow' in the project's release assets. The "standalone" distribution bundles all
# first-party plugins and is 'nextflow-<version>-dist' in the project's release assets.
# Only one or the other will be installed, as dictated by the `standalone` variant. At
# this time, "edge" (pre-release) versions of nextflow are not supported by this
# package.
#
# For each version, booleans "deprecated" or "preferred" can be defined. E.g.
#     "25.10.2": {
#         "preferred": True,
#         "release": { ...
#         },
#         "standalone": { ...
#         },
#     },
#     "21.04.3": {
#         "deprecated": True,
#         "release": { ...
#         },
#         "standalone": { ...
#         },
#     },
_VERSIONS = {
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
            "sha256": "0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5"
        },
    },
    "24.04.3": {
        "release": {
            "sha256": "e258f6395a38f044eb734cba6790af98b561aa521f63e2701fe95c050986e11c"
        },
        "standalone": {
            "sha256": "0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5"
        },
    },
    "24.04.1": {
        "release": {
            "sha256": "d1199179e31d0701d86e6c38afa9ccade93f62d545e800824be7767a130510ba"
        },
        "standalone": {
            "sha256": "0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5"
        },
    },
    "23.10.1": {
        "release": {
            "sha256": "9abc54f1ffb2b834a8135d44300404552d1e27719659cbb635199898677b660a"
        },
        "standalone": {
            "sha256": "0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5"
        },
    },
    "23.10.0": {
        "release": {
            "sha256": "4b7fba61ecc6d53a6850390bb435455a54ae4d0c3108199f88b16b49e555afdd"
        },
        "standalone": {
            "sha256": "0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5"
        },
    },
    "23.04.3": {
        "release": {
            "sha256": "258714c0772db3cab567267e8441c5b72102381f6bd58fc6957c2972235be7e0"
        },
        "standalone": {
            "sha256": "0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5"
        },
    },
    "23.04.1": {
        "release": {
            "sha256": "5de3e09117ca648b2b50778d3209feb249b35de0f97cdbcf52c7d92c7a96415c"
        },
        "standalone": {
            "sha256": "0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5"
        },
    },
    "22.10.4": {
        "release": {
            "sha256": "612a085e183546688e0733ebf342fb73865f560ad1315d999354048fbca5954d"
        },
        "standalone": {
            "sha256": "0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5"
        },
    },
    "22.10.3": {
        "release": {
            "sha256": "8d67046ca3b645fab2642d90848550a425c9905fd7dfc2b4753b8bcaccaa70dd"
        },
        "standalone": {
            "sha256": "0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5"
        },
    },
    "22.10.1": {
        "release": {
            "sha256": "fa6b6faa8b213860212da413e77141a56a5e128662d21ea6603aeb9717817c4c"
        },
        "standalone": {
            "sha256": "0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5"
        },
    },
    "22.10.0": {
        "release": {
            "sha256": "6acea8bd21f7f66b1363eef900cd696d9523d2b9edb53327940f093189c1535e"
        },
        "standalone": {
            "sha256": "0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5"
        },
    },
    "22.04.4": {
        "release": {
            "sha256": "e5ebf9942af4569db9199e8528016d9a52f73010ed476049774a76b201cd4b10"
        },
        "standalone": {
            "sha256": "0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5"
        },
    },
    "22.04.3": {
        "release": {
            "sha256": "a1a79c619200b9f2719e8467cd5b8fbcb427f43adf945233ba9e03cd2f2d814e"
        },
        "standalone": {
            "sha256": "0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5"
        },
    },
    "22.04.1": {
        "release": {
            "sha256": "89ef482a53d2866a3cee84b3576053278b53507bde62db4ad05b1fcd63a9368a"
        },
        "standalone": {
            "sha256": "0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5"
        },
    },
    "22.04.0": {
        "release": {
            "sha256": "8eba475aa395438ed222ff14df8fbe93928c14ffc68727a15b8308178edf9056"
        },
        "standalone": {
            "sha256": "0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5"
        },
    },
}


def get_attrs_for_version(version: str, standalone: bool = False) -> Dict[str,str]:
    """
    Given a string `version` and a boolean `standalone`, return sha256 hash of the
    version's standalone distribution if `standalone` is true, else return the sha256
    hash of the version's release distribution.
    """
    if standalone:
        return _VERSIONS[version]["standalone"]
    else:
        return _VERSIONS[version]["release"]


class Nextflow(Package):
    """Data-driven computational pipelines."""

    homepage = "https://www.nextflow.io"

    maintainers("dialvarezs", "marcodelapierre")

    variant(
        "standalone",
        default=False,
        description="Install the nextflow standalone distribution"
    )

    is_deprecated = False
    is_preferred = False

    standalone = False

    with when("+standalone"):
        standalone = True

    for ver, attrs in _VERSIONS.items():
        if "deprecated" in attrs:
            is_deprecated = attrs["deprecated"]

        if "preferred" in attrs:
            is_preferred = attrs["preferred"]

        version(
            ver,
            sha256=get_attrs_for_version(ver, standalone)["sha256"],
            expand=False,
            preferred=is_preferred,
            deprecated=is_deprecated,
        )

    depends_on("java@17:", type="run", when="@25:")
    depends_on("java@11:", type="run", when="@23:")
    depends_on("java@8:", type="run")

    def url_for_version(self, version):
        uri = f"https://github.com/nextflow-io/nextflow/releases/download/v{version}"
        if self.spec.satisfies("+standalone"):
            return f"{uri}/nextflow-{version}-dist"
        else:
            return f"{uri}/nextflow"

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(self.stage.archive_file, join_path(prefix.bin, "nextflow"))
        set_executable(join_path(prefix.bin, "nextflow"))
