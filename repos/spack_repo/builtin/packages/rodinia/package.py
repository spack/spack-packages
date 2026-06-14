# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage
from spack.error import InstallError

from spack.package import *

import os

class Rodinia(MakefilePackage, CudaPackage):
	"""Rodinia: Accelerating Compute-Intensive Applications with
	Accelerators"""

	homepage = "https://rodinia.cs.virginia.edu/doku.php"
	url = "https://www.cs.virginia.edu/~kw5na/lava/Rodinia/Packages/Current/rodinia_3.1.tar.bz2"

	version("3.1", sha256="faebac7c11ed8f8fcf6bf2d7e85c3086fc2d11f72204d6dfc28dc5b2e8f2acfd")

	depends_on("cuda")
	depends_on("cuda-samples")
	depends_on("freeglut")
	depends_on("glew")
	depends_on("gl")
	depends_on("glu")

	depends_on("c")
	depends_on("cxx")

	variant("kmeans", default=False, description="enable kmeans")

	conflicts("~cuda")
	conflicts("cuda_arch=none",
		msg="Please specify cuda_arch as variant for installation.\n"
			"You can query it with \n"
			"nvidia-smi --query-gpu=name,compute_cap --format=csv"
	)

	build_targets = ["CUDA"]

	# Patch a lot of changes that are hard to implement 
	# here via filter.
	patch("initial.patch")
	patch("backprop-lavaMD.patch")
	# No need to do this now, as make clean is run.
	#patch("pie.patch")

	def edit(self, spec, prefix):
		# set cuda paths

		cuda_prefix = self.spec["cuda"].prefix
		cuda_samples_prefix = self.spec["cuda-samples"].prefix
		cuda_arch = self.spec.variants["cuda_arch"].value[0]
		if cuda_arch == "none":
			raise InstallError(
				"Rodinia requires a valid cuda_arch.\n"
				"Please include this variant cuda_arch=... in your install\n"
				"command.\n"
				"You can query it with \n"
				"nvidia-smi --query-gpu=name,compute_cap --format=csv"
			)


		filter_file(
			"CUDA_DIR = /usr/local/cuda",
			"CUDA_DIR = {0}".format(cuda_prefix),
			"common/make.config",
			string=True,
		)

		filter_file(
			"SDK_DIR = /usr/local/cuda-5.5/samples/",
			"SDK_DIR = {0}".format(cuda_samples_prefix),
			"common/make.config",
			string=True,
		)

		# set cuda arch flags in various makefiles
		filter_file(
			"compute_20",
			"compute_{0}".format(cuda_arch),
			"cuda/cfd/Makefile",
			string=True,
		)

		# Produced by find . -type f -name "Makefile"
		makefiles = [
			"cuda/srad/srad_v2/Makefile",
			"cuda/srad/Makefile",
			"cuda/myocyte/Makefile",
			"cuda/mummergpu/Makefile",
			"cuda/mummergpu/src/Makefile",
			"cuda/backprop/Makefile",
			"cuda/nn/Makefile",
			"cuda/gaussian/Makefile",
			"cuda/lud/tools/Makefile",
			"cuda/lud/base/Makefile",
			"cuda/lud/Makefile",
			"cuda/lud/cuda/Makefile",
			"cuda/huffman/Makefile",
			"cuda/hotspot3D/Makefile",
			"cuda/kmeans/Makefile",
			"cuda/hotspot/Makefile",
			"cuda/leukocyte/CUDA/Makefile",
			"cuda/leukocyte/Makefile",
			"cuda/heartwall/Makefile",
			"cuda/bfs/Makefile",
			"cuda/hybridsort/Makefile",
			"cuda/pathfinder/Makefile",
			"cuda/streamcluster/Makefile",
			"cuda/b+tree/Makefile",
			"cuda/dwt2d/Makefile",
			"cuda/nw/Makefile",
			"cuda/cfd/Makefile",
			"cuda/particlefilter/Makefile",
			# this first letter is lowercase.
			"cuda/lavaMD/makefile",
		]

		for makefile in makefiles:
			filter_file(
				"sm_[0-9]+", "sm_{0}".format(cuda_arch), makefile
			)
			# Cuda samples include path has changed
			# To find all where SDK_DIR is used, grep -rn "SDK_DIR" .
			filter_file(
				r"/common/inc", "/common", makefile
			)
			# No need to do this now, as make clean is run
			#filter_file(
			#	r"^CC_FLAGS =", "CC_FLAGS = -fPIE", makefile
			#)


		# fix broken makefile rule
		filter_file("%.o: %.[ch]", "%.o: %.c", "cuda/kmeans/Makefile", string=True)

		# fix missing include for lseek(), read()
		filter_file(
			"#include <stdint.h>",
			"#include <stdint.h>\n#include <unistd.h>",
			"cuda/mummergpu/src/suffix-tree.cpp",
			string=True,
		)

		if self.spec.satisfies("%cuda@12.0:"):
			for cuda_dir, _, files in os.walk(
				join_path(self.stage.source_path, "cuda")
			):
				for fp in files:
					# The old cudaThreadSynchronize is deprecated.
					# Replace that with the new cudaDeviceSynchronize.
					filter_file(
						"cudaThreadSynchronize", "cudaDeviceSynchronize",
						os.path.join(cuda_dir, fp)
					)
					# Change various old names to new names
					filter_file(
						r"deviceProp\.\s*deviceOverlap",
						"(deviceProp.asyncEngineCount > 0)",
						os.path.join(cuda_dir, fp)
					)
					filter_file(
						r"deviceProp\.\s*clockRate",
						"9999", # removed
						os.path.join(cuda_dir, fp)
					)
			
			# Temporarily disable kmeans as the textures need
			# to be ported to new API.
			if (self.spec.satisfies("-kmeans")):
				filter_file(
					"cd cuda/kmeans",
					"#cd cuda/kmeans",
					"Makefile"
				)

	# Override this to run make clean before all
	def build(self, spec: Spec, prefix) -> None:
		with working_dir(self.build_directory):
			make("clean")
			make(*self.build_targets)


	def install(self, spec, prefix):
		mkdirp(prefix.bin)
		install_tree("bin/linux/cuda", prefix.bin)

