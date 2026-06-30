import os
import enum
from typing import Optional, List

from spack.package import (
    depends_on,
    disjoint_sets,
    variant,
)


class CompilationCache(enum.Enum):
    """Enum for compilation cache names
    """
    SCCACHE = "sccache"
    CCACHE = "ccache"


def configure(choices: List[CompilationCache] = [CompilationCache.SCCACHE, CompilationCache.CCACHE]):
    """Add configuration for packages that enable compilation caching tools

    Adds variant ccache with options 'none', 'auto', 'ccache', and 'sccache'

        * 'none' - Disable compilation cacheing for a specific package
        * 'auto' - Check the environment variable SPACK_CCACHE during concretization.
                   If unset, assumes ccache.
        * 'sccache' - Use sccache
        * 'ccache' - Use ccache
    """

    variant(
        "ccache",
        values=disjoint_sets(("none",), ("auto",), tuple(map(lambda x: x.value, choices)))
        .with_non_feature_values("auto")
        .with_non_feature_values("none")
        .with_default("auto"),
        description="enable detection and usage of compilation cacheing",
    )

    # Ensure the enabled compiler wrappers exist in the dag
    # The behavior of auto can be influenced by using the environment variable
    # SPACK_CCACHE to specify which tool to inject
    detected_ccache = os.environ.get("SPACK_CCACHE", "ccache")
    if detected_ccache == "sccache":
        depends_on("sccache", type="build", when="ccache=auto")
    elif detected_ccache == "ccache":
        depends_on("ccache", type="build", when="ccache=auto")

    depends_on("ccache", type="build", when="ccache=ccache")
    depends_on("sccache", type="build", when="ccache=sccache")


def determine_from_spec(spec: "spack.spec.Spec") -> Optional[CompilationCache]:
    """Determine the compilation cache tool configured for a spec.

    Parameters:
        spec: concrete spec to determine the compilation cache tool for

    Return:
        The correponding enum fot the compilation cache tool or None
    """

    ccache = None
    try:
        ccache = spec.variants["ccache"].value[0]
        ccache = CompilationCache(ccache)
    except KeyError:
        # Skip, there is no ccache variant
        pass
    except ValueError:
        # ccache is either none or auto

        # If it is auto, search for the corresponding compilation cache tool
        # in the spec.
        if ccache == "auto":
            for cc in CompilationCache:
                if cc.value in spec:
                    ccache = cc
                    break

    return ccache
