# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Pumi(CMakePackage):
    """SCOREC RPI's Parallel Unstructured Mesh Infrastructure (PUMI).
    An efficient distributed mesh data structure and methods to support
    parallel adaptive analysis including general mesh-based operations,
    such as mesh entity creation/deletion, adjacency and geometric
    classification, iterators, arbitrary (field) data attachable to mesh
    entities, efficient communication involving entities duplicated
    across multiple tasks, migration of mesh entities between tasks,
    and dynamic load balancing."""

    homepage = "https://www.scorec.rpi.edu/pumi"
    git = "https://github.com/SCOREC/core.git"

    maintainers("cwsmith")

    tags = ["e4s"]

    license("BSD-3-Clause")

    # We will use the scorec/core master branch as the 'nightly' version
    # of pumi in spack.  The master branch is more stable than the
    # scorec/core develop branch and we prefer not to expose spack users
    # to the added instability.
    version("master", submodules=True, branch="master")
    version(
        "2.2.9", submodules=True, commit="f87525cae7597322edfb2ccf1c7d4437402d9481"
    )  # tag 2.2.9
    version(
        "2.2.8", submodules=True, commit="736bb87ccd8db51fc499a1b91e53717a88841b1f"
    )  # tag 2.2.8
    version(
        "2.2.7", submodules=True, commit="a295720d7b4828282484f2b78bac1f6504512de4"
    )  # tag 2.2.7
    version("2.2.6", commit="4dd330e960b1921ae0d8d4039b8de8680a20d993")  # tag 2.2.6
    version("2.2.5", commit="73c16eae073b179e45ec625a5abe4915bc589af2")  # tag 2.2.5
    version("2.2.4", commit="8072fdbafd53e0c9a63248a269f4cce5000a4a8e")  # tag 2.2.4
    version("2.2.3", commit="d200cb366813695d0f18b514d8d8ecc382cb79fc")  # tag 2.2.3
    version("2.2.2", commit="bc34e3f7cfd8ab314968510c71486b140223a68f")  # tag 2.2.2
    version("2.2.1", commit="cd826205db21b8439026db1f6af61a8ed4a18564")  # tag 2.2.1
    version("2.2.0", commit="8c7e6f13943893b2bc1ece15003e4869a0e9634f")  # tag 2.2.0
    version("2.1.0", commit="840fbf6ec49a63aeaa3945f11ddb224f6055ac9f")

    variant("int64", default=False, description="Enable 64bit mesh entity ids")
    variant("shared", default=False, description="Build shared libraries")
    variant("zoltan", default=False, description="Enable Zoltan Features")
    variant("fortran", default=False, description="Enable FORTRAN interface")
    variant("testing", default=False, description="Enable all tests")
    variant(
        "simmodsuite",
        default="none",
        values=("none", "base", "kernels", "full"),
        description="Enable Simmetrix SimModSuite Support: 'base' enables "
        "the minimum set of functionality, 'kernels' adds CAD kernel "
        "support to 'base', and 'full' enables all functionality.",
    )
    variant(
        "simmodsuite_version_check",
        default=True,
        description="Enable check of Simmetrix SimModSuite version. "
        "Disable the check for testing new versions.",
    )

    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("fortran", type="build", when="+fortran")

    depends_on("mpi")
    depends_on("cmake@3:", type="build")
    depends_on("zoltan", when="+zoltan")
    depends_on("zoltan+int64", when="+zoltan+int64")
    simbase = "+base"
    simkernels = simbase + "+parasolid+acis+discrete"
    simfull = simkernels + "+abstract+adv+advmodel+import+paralleladapt+parallelmesh"
    depends_on("simmetrix-simmodsuite" + simbase, when="simmodsuite=base")
    depends_on("simmetrix-simmodsuite" + simkernels, when="simmodsuite=kernels")
    depends_on("simmetrix-simmodsuite" + simfull, when="simmodsuite=full")

    def patch(self):
        '''mds/apfMDS.cc: getFaceIdInRegion() and getEdgeIdInFace() (helpers used by
           apf::deriveMdlFromManifold()/apf::derive2DMdlFromManifold(), called from
           proteus's MeshAdaptPUMIDrvr::reconstructFromProteus2()) look up the
           "_vert_id" tag via mesh->findTag("_vert_id") and read it with
           getIntTag() into a 4-byte int/int[2]. But "_vert_id" is created a few
           lines above (and identically in the sibling deriveMdlFromManifold) via
           mesh->createLongTag("_vert_id", 1) -- an 8-byte long. SCOREC's generic
           tag storage (MeshMDS::getTag) does an unconditional
           memcpy(dest, storage, tag->bytes) with no type/size check, so every
           call here is an 8-byte-into-4-byte stack buffer overflow -- confirmed
           via gdb on aarch64 (petsc/download-proteus-support session,
           2026-08-01): this exact bug crashes every PUMI-mesh-generation test
           that goes through this code path (reconstructFromProteus2 ->
           derive2DMdlFromManifold), reproducing here too as a glibc
           stack-protector "*** buffer overflow detected ***" abort inside
           derive2DMdlFromManifold when this same pumi is built via Spack rather
           than PETSc's own --download-scorec (which already carries this fix via
           config/BuildSystem/config/packages/scorec.py in the
           gitlab.com/cekees/petsc download-proteus-support fork -- this file is
           the Spack-side equivalent so py-proteus+scorec gets the same fix).
           Fixed by matching the tag's actual type (getLongTag/long, not
           getIntTag/int) in both helpers, plus replacing the silent
           "return 12; // Should give segmentation fault" fallback (apf::Downward
           is a fixed MeshEntity*[12]; indexing it with 12 is UB regardless of
           what causes the "no match" case) with an explicit assertion so a
           genuinely unmatched vertex/edge aborts loudly at the fault site
           instead of silently indexing one past the array.'''
        apfmds_cc = join_path(self.stage.source_path, 'mds', 'apfMDS.cc')
        with open(apfmds_cc, 'r') as f:
            content = f.read()
        orig = content
        content = content.replace(
            'apf::Downward verts;\n'
            '  apf::MeshTag* vIDTag = mesh->findTag("_vert_id");\n'
            '  int vID;\n'
            '  mesh->getDownward(region, 0, verts);\n'
            '  // Go through all vertices. What vertex is not on the face can be used to determine the face id.\n'
            '  // TODO: Good way to assert that the rest of the 3 actually exist?\n'
            '  mesh->getIntTag(verts[0], vIDTag, &vID);\n'
            '  if (vID != bface_data[2] && vID != bface_data[3] && vID != bface_data[4])\n'
            '    return 2;\n'
            '  mesh->getIntTag(verts[1], vIDTag, &vID);\n'
            '  if (vID != bface_data[2] && vID != bface_data[3] && vID != bface_data[4])\n'
            '    return 3;\n'
            '  mesh->getIntTag(verts[2], vIDTag, &vID);\n'
            '  if (vID != bface_data[2] && vID != bface_data[3] && vID != bface_data[4])\n'
            '    return 1;\n'
            '  mesh->getIntTag(verts[3], vIDTag, &vID);\n'
            '  if (vID != bface_data[2] && vID != bface_data[3] && vID != bface_data[4])\n'
            '    return 0;\n'
            '  return 12; // Should give segmentation fault\n'
            '}',
            'apf::Downward verts;\n'
            '  apf::MeshTag* vIDTag = mesh->findTag("_vert_id");\n'
            '  PCU_ALWAYS_ASSERT(mesh->getTagType(vIDTag) == Mesh::LONG);\n'
            '  long vID;\n'
            '  mesh->getDownward(region, 0, verts);\n'
            '  // Go through all vertices. What vertex is not on the face can be used to determine the face id.\n'
            '  // TODO: Good way to assert that the rest of the 3 actually exist?\n'
            '  mesh->getLongTag(verts[0], vIDTag, &vID);\n'
            '  if (vID != bface_data[2] && vID != bface_data[3] && vID != bface_data[4])\n'
            '    return 2;\n'
            '  mesh->getLongTag(verts[1], vIDTag, &vID);\n'
            '  if (vID != bface_data[2] && vID != bface_data[3] && vID != bface_data[4])\n'
            '    return 3;\n'
            '  mesh->getLongTag(verts[2], vIDTag, &vID);\n'
            '  if (vID != bface_data[2] && vID != bface_data[3] && vID != bface_data[4])\n'
            '    return 1;\n'
            '  mesh->getLongTag(verts[3], vIDTag, &vID);\n'
            '  if (vID != bface_data[2] && vID != bface_data[3] && vID != bface_data[4])\n'
            '    return 0;\n'
            '  PCU_ALWAYS_ASSERT_VERBOSE(false, "getFaceIdInRegion: no matching vertex found");\n'
            '  return 12; // unreachable\n'
            '}')
        content = content.replace(
            'apf::Downward verts, edges;\n'
            '  apf::MeshTag* vIDTag = mesh->findTag("_vert_id");\n'
            '  int vID[2], eID;\n'
            '  mesh->getDownward(face, 1, edges);\n'
            '  for (eID = 0; eID < 3; ++eID) {\n'
            '    mesh->getDownward(edges[eID], 0, verts);\n'
            '    mesh->getIntTag(verts[0], vIDTag, &vID[0]);\n'
            '    mesh->getIntTag(verts[1], vIDTag, &vID[1]);\n'
            '    if((vID[0] == bedge_data[2] && vID[1] == bedge_data[3]) ||\n'
            '       (vID[0] == bedge_data[3] && vID[1] == bedge_data[2])) {\n'
            '      return eID;\n'
            '    }\n'
            '  }\n'
            '\n'
            '  return 12; // Should give segmentation fault\n'
            '}',
            'apf::Downward verts, edges;\n'
            '  apf::MeshTag* vIDTag = mesh->findTag("_vert_id");\n'
            '  PCU_ALWAYS_ASSERT(mesh->getTagType(vIDTag) == Mesh::LONG);\n'
            '  long vID[2];\n'
            '  int eID;\n'
            '  mesh->getDownward(face, 1, edges);\n'
            '  for (eID = 0; eID < 3; ++eID) {\n'
            '    mesh->getDownward(edges[eID], 0, verts);\n'
            '    mesh->getLongTag(verts[0], vIDTag, &vID[0]);\n'
            '    mesh->getLongTag(verts[1], vIDTag, &vID[1]);\n'
            '    if((vID[0] == bedge_data[2] && vID[1] == bedge_data[3]) ||\n'
            '       (vID[0] == bedge_data[3] && vID[1] == bedge_data[2])) {\n'
            '      return eID;\n'
            '    }\n'
            '  }\n'
            '\n'
            '  PCU_ALWAYS_ASSERT_VERBOSE(false, "getEdgeIdInFace: no matching edge found");\n'
            '  return 12; // unreachable\n'
            '}')
        if content == orig:
            tty.warn('pumi patch(): apfMDS.cc _vert_id int/long fix found nothing to replace -- upstream source may have changed, check getFaceIdInRegion/getEdgeIdInFace by hand')
        else:
            with open(apfmds_cc, 'w') as f:
                f.write(content)

    def cmake_args(self):
        spec = self.spec

        args = [
            "-DSCOREC_CXX_WARNINGS=OFF",
            self.define_from_variant("ENABLE_ZOLTAN", "zoltan"),
            "-DCMAKE_C_COMPILER=%s" % spec["mpi"].mpicc,
            "-DCMAKE_CXX_COMPILER=%s" % spec["mpi"].mpicxx,
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("PUMI_FORTRAN_INTERFACE", "fortran"),
            "-DMDS_ID_TYPE=%s" % ("long" if "+int64" in spec else "int"),
            "-DSKIP_SIMMETRIX_VERSION_CHECK=%s"
            % ("ON" if "~simmodsuite_version_check" in spec else "OFF"),
            self.define_from_variant("IS_TESTING", "testing"),
            "-DMESHES=%s" % join_path(self.stage.source_path, "pumi-meshes"),
        ]
        if spec.satisfies("fortran"):
            args += ["-DCMAKE_Fortran_COMPILER=%s" % spec["mpi"].mpifc]
        if spec.satisfies("@2.2.3"):
            args += ["-DCMAKE_CXX_STANDARD=11"]
        if self.spec.variants["simmodsuite"].value != "none":
            args.append("-DENABLE_SIMMETRIX=ON")
            mpi_id = spec["mpi"].name + spec["mpi"].version.up_to(1).string
            args.append("-DSIM_MPI=" + mpi_id)
            if self.spec.variants["simmodsuite"].value in ["kernels", "full"]:
                args.append("-DENABLE_SIMMETRIX=ON")
                args.append("-DSIM_PARASOLID=ON")
                args.append("-DSIM_ACIS=ON")
                args.append("-DSIM_DISCRETE=ON")
        return args

    def test_partition(self):
        """Testing pumi mesh partitioning"""
        if self.spec.satisfies("@:2.2.6"):
            raise SkipTest("Package must be installed as version @2.2.7 or later")

        options = [
            "-n",
            "2",
            join_path(self.prefix.bin, "split"),
            join_path(self.prefix.share.testdata, "pipe.dmg"),
            join_path(self.prefix.share.testdata, "pipe.smb"),
            "pipe_2_.smb",
            "2",
        ]
        mpiexe_list = ["mpirun", "mpiexec", "srun"]
        for mpiexe in mpiexe_list:
            tty.info(f"Attempting to build and launch with {os.path.basename(mpiexe)}")
            try:
                options = ["--immediate=30"] + options if mpiexe == "srun" else options
                exe = which(mpiexe, required=True)
                out = exe(*options, output=str.split, error=str.split)
                assert "mesh pipe_2_.smb written" in out
                return
            except (Exception, ProcessError) as err:
                tty.info(f"Skipping {mpiexe}: {str(err)}")
        assert False, "No MPI executable was found"

    def test_refine(self):
        """Testing pumi uniform mesh refinement"""
        if self.spec.satisfies("@:2.2.6"):
            raise SkipTest("Package must be installed as version @2.2.7 or later")

        options = [
            join_path(self.prefix.share.testdata, "pipe.dmg"),
            join_path(self.prefix.share.testdata, "pipe.smb"),
            "pipe_unif.smb",
        ]
        exe = which(self.prefix.bin.uniform, required=True)
        out = exe(*options, output=str.split, error=str.split)
        assert "mesh pipe_unif.smb written" in out
