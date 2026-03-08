# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTrimesh(PythonPackage):
    """Import, export, process, analyze and view triangular meshes"""

    homepage = "https://github.com/mikedh/trimesh"
    pypi = "trimesh/trimesh-2.38.10.tar.gz"

    license("MIT")

    version(
        "4.11.2", sha256="30fbde5b8dd7c157e7ff4d54286cb35291844fd3f4d0364e8b2727f1b308fb06"
    )  # FIXME
    version(
        "4.11.1", sha256="9a10040ca5d1c4438e0b7af94433edf6b043f5204393fc97bb85c9159a8bf21e"
    )  # FIXME
    version(
        "4.11.0", sha256="0b4acdcf28f21013385ccf81619a9dce703af348f69b198180a2212b1bc67821"
    )  # FIXME
    version(
        "4.10.1", sha256="2067ebb8dcde0d7f00c2a85bfcae4aa891c40898e5f14232592429025ee2c593"
    )  # FIXME
    version(
        "4.10.0", sha256="502710a0b1f0317816507828a41e0cb1c595b895e344567fa42cd47388c2b72b"
    )  # FIXME
    version("4.9.0", sha256="ad907a223867f614ef1598d85a4c978845f39365cb7ccc93fa5800901fba3ef9")
    version("4.8.3", sha256="d2a1974efccb0737a1faac14d69740c644bb6738a99c790c1df752fe72c2a759")
    version("4.8.2", sha256="1b9e50feb77dac820428b7408f6cea707577342cd37a493e4491765bd5a67da3")
    version("4.8.1", sha256="b6dcce47a177cbe8083aa453c872a38703cd3e4b6384e84ff1525a6916d642d3")
    version("4.8.0", sha256="98f726cf573604264daade22cb57d4e229061734d0be7d4f3062561e31439ab3")
    version("4.7.4", sha256="8d242dfabd9bc4e99a4f0c75bf8c0a41fbb252924e3484b53a8b0096accb49e1")
    version("4.7.3", sha256="b4409f505da6a703ed968234b6ea5058ffbcd7ea0bb93459012b7f5d01712abc")
    version("4.7.1", sha256="3863c2b2281fc7a99bf0b5de4a0011229bde4663babc0c1b53a1f855149ec898")
    version("4.7.0", sha256="13eb97c1f417f744b682d24ab77f86a21c6ccd1e3fb6ce3aa173a94ca982deee")
    version("4.6.13", sha256="2950dd6c3c9c9948a652f7a2966319b47130467bbbf447b254e02b9d90c94f14")
    version("4.6.12", sha256="cf8ad4a5c2d9b0277f34d999a077aa9331c465040c402774e1455054a6c20e67")
    version("4.6.11", sha256="a10d92f2984f6ac9a5a53a6bd0ef0df309feed5c6b995c286edeea4abc553a68")
    version("4.6.10", sha256="bd2a34e3ab981a5bae93768658bd73fc18e505551355eb14d4750bfbddc0fd8f")
    version("4.6.9", sha256="c46ee5b9edabf0d613ff582ac8ec466db78c998a4f6992dfd3f45dbf49f25fb1")
    version("4.6.8", sha256="d00b1834eaeea2b4326a2f3a98c9e28553f3508430e555bbc424c26a74e01154")
    version("4.6.7", sha256="35df6ecd71bbd0dcb347fa42366df209ca281e3ee0ec6cbedb912ba4b2a313df")
    version("4.6.6", sha256="6c300190e21799a4f6a905316d8edb502bc1e2462ee6625dc06d5a726875788e")
    version("4.6.5", sha256="19a6ea2ad18f8db8bde47ffb3deccb6cddb4d5de717f9b3df47932954f86ee8c")
    version("4.6.4", sha256="bd052cd94650860c4e68f6cbf48a14d43a43ceb4d7a8152f4650ff62b6b9965d")
    version("4.6.3", sha256="fda9bd5e88c15bb6aa47b82968d24780a7e0384ec491ff73020db46526e7ca08")
    version("4.6.2", sha256="cfb9968b59626c26612ea5cadac055d97d119247f460d75b33f4f781177855d6")
    version("4.6.1", sha256="feea2218584a6671338a70ebc94330a68c59c1282057464f77d92a801d6f40f2")
    version("4.6.0", sha256="5f248ca790efc241c46ec9a3d7ee744cc728a67cf52a8479f766591be51fa1a4")
    version("4.5.3", sha256="b1af60399f64f4715d744c5195754068bfeb98981b92feb0c15d016c99379f87")
    version("4.5.2", sha256="165b12f2898c3e8dec99a2ed05ec5c83eafa2fc8150ba8c30f8b3a62f693433f")
    version("4.5.1", sha256="2e85179fdbee1e872aa00d42a5b28605a05302968857a8321a4dfa4390725b1c")
    version("4.5.0", sha256="fc49d9fbc29e25017775a024e5df80f625c9dddbf982ce3ea5d3445070950425")
    version("4.4.9", sha256="e9f54cb4ef70f9db49446cad3845b7a8043fc7d62d9192b241741f3fb0d813ac")
    version("4.4.8", sha256="e8c1d36032c7de9a331a90147d3b19b694dddbc44c8002f41129401a39ec1fce")
    version("4.4.7", sha256="e6619c70c99006d41f175bd5e1ba2c8c3dfdb00c2b41d65059917942e2f6971a")
    version("4.4.6", sha256="b0e64bf060c8d3a7173024fb6fe099f70e7aa306303568882cbac90e6599f45b")
    version("4.4.4", sha256="5c53f6fe01e2fae357ad33b796dbfdb4eafeb2114354f46cf39608806114ecf8")
    version("4.4.3", sha256="a4110ad6832d23ccf4df32872a3804eeea216421352913d1514ed9dad2001d5e")
    version("4.4.2", sha256="c8de6895da005c7df29e9d199e85ca38c80c79a0edb709afcbc53feb12c47cfc")
    version("4.4.1", sha256="767fe3c866ba74e6d9a9d216c34ecc1cfe2fbf3f129a6c11d59871705a591aba")
    version("4.4.0", sha256="daf6e56715de2e93dd905e926f9bb10d23dc4157f9724aa7caab5d0e28963e56")
    version("4.3.2", sha256="1450dbd1aae8dd825eddd56c5a7d7d1b35cad7efc2c63d535e19569577c25916")
    version("4.3.1", sha256="4850fe9d954d6fdd3e515756999c27184185db5cca844ee67c53e7d8796e8b31")
    version("4.3.0", sha256="9145e2dba3611464b796219a1877e6d074d15979676886bcd25c602d0ff41723")
    version("4.2.4", sha256="6aeb201638587b46ff85dfacced8b81a9322977345ebfcae5d26a3cbfd496576")
    version("4.2.3", sha256="4f918d0b3d9a283c37bd83c61441b10573c30e8881e3ac44c564ee716c1823be")
    version("4.2.2", sha256="972b1c6fb6189d3e00ee3b93d7ef420656f80e8784d4c4f8e993e14498026bae")
    version("4.2.1", sha256="0809faeccd53e3c27dcb5f102f5b230f7479eea7e6f4562d2bddd3abad161251")
    version("4.2.0", sha256="b92ea854d4be24137ad521150f02d00e809feb44b0a9757bf37d44d89fa16fb2")
    version("4.1.8", sha256="a06d147a3a947bef0e72049917f2e7fd00bbd0689f8871e4908e447a53c5fb40")
    version("4.1.7", sha256="6ceedf22b93e49c4afcf58b02cc74f37e7caf53e55848122b717594672c14b10")
    version("4.1.6", sha256="a6cf7dfb7243c8ab81db91b5861a3a302943169e3c37f7416ab1d95297192b7d")
    version("4.1.5", sha256="9bb421c7cbdd400b6f06d252fb89d0412874aa7a7f4d15e8721fd626093fec42")
    version("4.1.4", sha256="25e511bb0d1822620a4708b7e6d6160dae4242a61f3d99be34989aa7c428ea61")
    version("4.1.3", sha256="4881c803a1caa3729aeab999ac165f4a637fb0d7c48d2226614b5bb50b37a334")
    version("4.1.2", sha256="f5c14ce74b22cb8c61700a1eacba4da0b72812b4072ba5ff6b6545d3559a4e1e")
    version("4.1.0", sha256="71ad0acad70f65a7e5af4785fc24706d64a3994cca3526d59172db435b1c1d9f")
    version("4.0.10", sha256="36e33b1145e5d505b41f250f180c9e5432390e1b7808cbbfb9f50b28d5b46cdc")
    version("4.0.9", sha256="96750ebab25edd208d61b0dda449403f622764ba0ab5e2a59895951b31c10162")
    version("4.0.8", sha256="16f3050b587782eeb58d93d23e6c581d09b19f160a9ad60079c73fd084fd13c2")
    version("4.0.7", sha256="393e510dea417dc9a97beba0eb391917a4ca4350eef5762fb6acfc577b161c13")
    version("4.0.6", sha256="c1b70db4812b00e4b620728d6be11f4849b166e950d936ab05d3bc4a6b5e7d4d")
    version("4.0.5", sha256="b9bfcfec03b70ab4d21f055df1ab73e8740dd0bc8fd5648273eef8fec76cddf9")
    version("4.0.4", sha256="dd7a67706e8848a414fa1a89a6f724f36b3405882f6293469f7cdc756901e4fb")
    version("4.0.3", sha256="4f525c155cb81ddc2018186de37c11d1a3edd7cf363d03c15905cea5cd2b22be")
    version("4.0.2", sha256="d97f618bf48a5485d2dee48d6e4093d036a928f4b9d9942571a9c862f062fee9")
    version("4.0.1", sha256="8c1550a98341f0fec4d3191c4c7eae6266c167f9793fd54bb72c91431abf7ce6")
    version("4.0.0", sha256="ccf183f5574c31275385dfc8576c0b178340d65650cbd6b448ec8e9141872bb7")
    version("3.23.5", sha256="bdfd669eccc4b3faff2328200a49408cd5ecad9f19b6022c4adb554bbb3a2621")
    version("3.23.3", sha256="eb59cccadaea73bc3b21b3bb4d7ec7e0ee0362854bf4c4c16ac377503c78f76c")
    version("3.23.2", sha256="c4d1cf95db688a3c101f2b9641de39424d9c4e3822d20d1ef05fac7a6f804505")
    version("3.23.1", sha256="d8c40925a4f3a437ae93d04f2dbcf05ad6cb0b78f377b86dda81ab54c0974687")
    version("3.23.0", sha256="4e39cde60ab386c3764bf01caa2a39a47df7456fd9a7769ca2523e07eb126910")
    version("3.22.5", sha256="2e4df41d285b55205e89c95fc4952477b5b61dfbcbb19894758a9e6cb23ba2dc")
    version("3.22.4", sha256="0c53ad6a7aeb73726e7eebb9c9b6db734c495f6f42569dad14e3fddd016825e3")
    version("3.22.3", sha256="3eb5ea0583841425c866c8a18489a1d6cc1b185442a324c697cd9d91f044eda5")
    version("3.22.2", sha256="613f4fa27bf3d7d4aa1c02543bdfca49a04f42b5b65bef8c44d805ffc2f438f7")
    version("3.22.1", sha256="f40546d4214e16794802ca0a949d10cd54b1f5a630b0819afddaf4f0e16c64b2")
    version("3.22.0", sha256="2ae13c11597855b20546575d77e0aabe3f9a2d653ff593209a0c9e9bd8a76374")
    version("3.21.7", sha256="c2d1addcf502522488890440dcdc4ed673c4df95d00e2a567ebc1229d0c186d1")
    version("3.21.6", sha256="fa016a6406c62e834374e99bc4494ac1bd1063b0497ce519543efcf3c4fa794f")
    version("3.21.5", sha256="74741bc7f9fcb94b98951db8dc8ec8364a2ef52ac2ca0761c7ba06182ef329be")
    version("3.21.4", sha256="56445ef49a407bdcfed728ba0bc38308f2ac5d8b0fc927910b8f74ac5034a785")
    version("3.21.3", sha256="980b52a68f46c58e9eb972516741e4a8cf7e3645b8dbbf91c3b49856d62eba95")
    version("3.21.2", sha256="5513c4fb540b286cb95bdf626b906e3cdb661ff7a85ee940a52f27f1275049a4")
    version("3.21.1", sha256="ec6ec3abbb734b71d22b8cd70e363dd4eed6fac0c3dc8dcac0ee47ec1918fcbc")
    version("3.21.0", sha256="2aa8c312900e24a7487744a7e9d47e794bd6e79ad629aaa48cde0d37ee63a094")
    version("3.20.2", sha256="ead4ab5a8be055311c7037a5505af0f04d6087288f994b040125bc9063d40613")
    version("3.20.1", sha256="5149331d0a11082ed2990800e2ecf4f49fca4718b3af92e1c026286c8358d607")
    version("3.20.0", sha256="2599772355f46dd4366a5cf6ce8ccfa3a03222f08b1c396494d45bf5c95818d1")
    version("3.19.4", sha256="bcfd4a8655482e59fa03475f8e73284ae213e145ea7661311309bf7807013888")
    version("3.19.3", sha256="d370ba04f8d59ac493b09488527872c689d2aaf4c4737664070f3141e008c16c")
    version("3.18.3", sha256="955a01041af3ca1ad2991d85334c68f1424108e4a1c1a60eac8a5e030427efa3")
    version("3.18.2", sha256="9785d101421c07c2f4aa62b051610f18eb662f74f70d9a728baba388dc7ac410")
    version("3.18.1", sha256="f09c396261ec01372171c8623eac6ac40f8f62097b7a5a992ea1bcbd3bbf6f49")
    version("3.18.0", sha256="4588c975b8bad2f1c3c254a12a61282ba8379a6b5bddebae33daaf76aa67e681")
    version("3.17.1", sha256="025bb2fa3a2e87bdd6873f11db45a7ca19216f2f8b6aed29140fca57e32c298e")
    version("2.38.10", sha256="866e73ea35641ff2af73867c891d7f9b90c75ccb8a3c1e8e06e16ff9af1f8c64")

    variant(
        "easy",
        default=False,
        description="Install soft dependencies and unlock extra functionality",
    )

    depends_on("py-setuptools@40.8:", type="build")

    depends_on("py-chardet", type=("build", "run"), when="+easy")
    depends_on("py-colorlog", type=("build", "run"), when="+easy")
    depends_on("py-jsonschema", type=("build", "run"), when="+easy")
    depends_on("py-lxml", type=("build", "run"), when="+easy")
    depends_on("py-mapbox-earcut", type=("build", "run"), when="+easy")
    depends_on("py-msgpack", type=("build", "run"), when="+easy")
    depends_on("py-networkx", type=("build", "run"), when="+easy")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("pil", type=("build", "run"), when="+easy")
    depends_on("py-pycollada", type=("build", "run"), when="+easy")
    depends_on("py-pyglet@:1", type=("build", "run"), when="+easy")
    depends_on("py-requests", type=("build", "run"), when="+easy")
    depends_on("py-rtree", type=("build", "run"), when="+easy")
    depends_on("py-scipy", type=("build", "run"), when="+easy")
    depends_on("py-setuptools", type=("build", "run"), when="+easy")
    depends_on("py-shapely", type=("build", "run"), when="+easy")
    depends_on("py-svgpath", type=("build", "run"), when="+easy")
    depends_on("py-sympy", type=("build", "run"), when="+easy")
    depends_on("py-xxhash", type=("build", "run"), when="+easy")
