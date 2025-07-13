# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import GenericBuilder, Package

# Needed to appease style checks. These names need to be exported here to be compatible
# with Package API less than v2.2, in case custom repositories import them
_ = Package
_ = GenericBuilder
