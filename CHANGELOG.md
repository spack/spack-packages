# Spack packages v2025.11.0

The 2025.11.0 release of the spack packages is released in conjunction
with the Spack 1.1.0 release.  You can read about the [Spack 1.1
release here](https://github.com/spack/spack/releases/v1.1.0).

## Spack package API version

This release uses Package API v2.4. We are guaranteeing that any Spack
release v1.x from v1.1.0 onwards will be backward compatible with
Package API v.2.4 -- i.e., it can execute code from packages in this
release.

See the [Package API
Documentation](https://spack.readthedocs.io/en/latest/package_api.html)
for full details on package versioning and compatibility.

## Package statistics

There are now 8611 packages in the spack-packages builtin repo. This
is up from 8499 in the previous release.

## New and removed packages

All package versions deprecated prior to the 2025.07 release have been
removed, as have all versions that are unusable without versions
deprecated by that time, with the exception of deprecated versions of
the `gcc` package.

All packages for which all versions were removed were removed from the repo.

### New packages

* alpscore
* aretomo
* aretomo2
* babeltrace2
* cohomcalg
* cpptrace
* croc
* cublasmp
* cufftmp
* cusolvermp
* cusparselt
* ddc
* deno
* dolfinx-mpc
* dplasma
* elastix
* erf
* fairroot
* fairsoft-bundle
* fairsoft-config
* fastplong
* frobby
* fwq
* geany
* givaro
* glib-bootstrap
* go-sh
* green-mbpt
* green-seet
* gribjump
* gspell
* hsa-amd-aqlprofile
* imod
* jonquil
* just
* kenlm
* kynema
* libftdi
* libgee
* libgit2-glib
* libhandy
* libmetatensor
* libmetatensor-torch
* libmetatomic-torch
* mamba
* model-angelo
* mozjs
* mscclpp
* mstore
* nvidia-container-toolkit
* openfpgaloader
* padicotm
* pbzip2
* pioman
* podman-compose
* puk
* pukabi
* py-acres
* py-adios4dolfinx
* py-apebench
* py-app-model
* py-autoreject
* py-backports-tarfile
* py-bidict
* py-bids-validator-deno
* py-bidsschematools
* py-binary
* py-biosppy
* py-blake3
* py-cachey
* py-cbor2
* py-choreographer
* py-coherent-licensed
* py-courlan
* py-cramjam
* py-crc32c
* py-cuda-bindings
* py-dask-awkward
* py-dask-histogram
* py-dask-jobqueue
* py-dataproperty
* py-datatrove
* py-dolfinx-mpc
* py-eval-type-backport
* py-evaluate
* py-exponax
* py-fasttext-numpy2-wheel
* py-faust-cchardet
* py-flexcache
* py-flexparser
* py-freetype-py
* py-google-cloud-bigquery
* py-gpaw-data
* py-gromacswrapper
* py-hf-xet
* py-hsluv
* py-htmldate
* py-imutils
* py-in-n-out
* py-inscriptis
* py-ipython-pygments-lexers
* py-jaraco-context
* py-json-tricks
* py-justext
* py-lil-aretomo
* py-logistro
* py-magicgui
* py-makefun
* py-mbstrdecoder
* py-mdocfile
* py-metatensor-core
* py-metatensor-learn
* py-metatensor-operations
* py-metatensor-torch
* py-metatomic-torch
* py-microsoft-aurora
* py-morphosamplers
* py-mumps4py
* py-napari
* py-napari-console
* py-napari-plugin-engine
* py-napari-plugin-manager
* py-napari-svg
* py-nh3
* py-npe2
* py-numbagg
* py-numkit
* py-numpy-indexed
* py-nvidia-nvimagecodec
* py-nvidia-nvjpeg2k
* py-nvidia-nvtiff
* py-opencv-python
* py-paho-mqtt
* py-pathvalidate
* py-pdequinox
* py-peakutils
* py-psygnal
* py-pyahocorasick
* py-pyclibrary
* py-pyconify
* py-pydantic-compat
* py-pygrib
* py-pypinfo
* py-pypistats
* py-pysmiles
* py-pytablewriter
* py-pytest-memray
* py-relion
* py-relion-blush
* py-relion-classranker
* py-rouge-score
* py-scifem
* py-scikit-matter
* py-setuptools-reproducible
* py-simple-slurm
* py-simsimd
* py-snakeviz
* py-starfile
* py-stringzilla
* py-tabledata
* py-tcolorpy
* py-textual-plotext
* py-tilelang
* py-tinyrecord
* py-tld
* py-torchtoolbox
* py-trafilatura
* py-trainax
* py-typepy
* py-universal-pathlib
* py-vermouth-martinize
* py-vesin
* py-vispy
* py-warcio
* py-xcdat
* py-xgcm
* quest
* r-reformulas
* regenie
* repeatafterme
* ruby-charlock-holmes
* sandia-micro-benchmarks
* scorecard
* shred
* spack-configs-facilities
* spack-configs-tools-sdk
* tcl-bwidget
* tcl-togl
* tempestextremes
* terminalimageviewer
* topaz-3dem
* topcom
* torch-scatter
* tsne-cuda
* xcrysden*

### Removed packages

* apcomp
* autofact
* bcl2fastq2
* blast-legacy
* compiz
* cupla
* ddt
* dray
* exa
* examinimd
* gconf
* geoip
* grandr
* grib-api
* ip2
* kokkos-kernels-legacy
* kokkos-legacy
* lbzip2
* libuuid
* melissa-api
* memsurfer
* micromamba
* miniaero
* miniconda2
* mongodb
* mvapich2-gdr
* mvapich2x
* oce
* openturbine
* paraver
* parquet-cpp
* perl-alien-svn
* py-azure-cli
* py-azureml-automl-core
* py-azureml-core
* py-azureml-dataprep
* py-azureml-dataprep-native
* py-azureml-dataprep-rslex
* py-azureml-dataset-runtime
* py-azureml-pipeline
* py-azureml-pipeline-core
* py-azureml-pipeline-steps
* py-azureml-sdk
* py-azureml-telemetry
* py-azureml-train
* py-azureml-train-automl-client
* py-azureml-train-core
* py-azureml-train-restclients-hyperdrive
* py-cylc-uiserver
* py-deepsig
* py-dlio-profiler-py
* py-gdbgui
* py-graphene-tornado
* py-haphpipe
* py-motor
* py-mysqldb1
* py-nibetaseries
* py-ninja
* py-nistats
* py-ocp-models
* py-pydv
* py-pyside
* py-rq
* py-sanic
* py-shiboken
* py-sierrapy
* py-xrootd-pyfs
* qbank
* r-kegg-db
* shortbred
* singularity-legacy
* sollve
* sparrow
* supernova
* testdfsio
* virtuoso
* votca-csg
* votca-csg-tutorials
* votca-csgapps
* votca-ctp
* votca-tools
* votca-xtp
* xsdk-examples


# Spack Packages v2025.07.0

This is the initial release of the Spack package repository as its own project, separate from the core Spack tool.

## Package API version

Starting with Spack `v1.0`, the [Spack Package API](https://spack.readthedocs.io/en/latest/package_api.html) is separately versioned from Spack.

This release uses Package API `v2.2`. We are guaranteeing that any Spack `v1.x` release will be backward compatible with Package API `v.2.2` -- i.e., it can execute code from packages in this release.

See the [Package API Documentation](https://spack.readthedocs.io/en/latest/package_api.html) for full details
on package versioning and compatibility. The high level details are:

1. The `spack.package` Python module defines the Package API;
2. The Package API *minor version* is incremented when new functions or classes are exported from `spack.package`; and
3. The major version is incremented when functions or classes are removed or have breaking changes to their signatures (a rare occurrence).

This independent versioning allows package authors to utilize new Spack features without waiting for a new Spack release.

## Major changes from the `builtin` repository as it existed within Spack core
- Spack packages are defined in this repo;
- Spack build system classes are defined in this repo, in the `spack_repo.builtin.build_systems` module (previously in core in the `spack.build_systems` module).
- The structure of v2.x Spack repositories has changed. Directory names are now normalized so they are valid Python modules. Previously, directory names could contain hyphens and were not understood by editors and Python tooling. Now the naming scheme is:
  - `py-numpy/package.py` -> `py_numpy/package.py` (hyphen is replaced by underscore)
    - `7zip/package.py` -> `_7zip/package.py` (leading digits are now preceded by an underscore)
      - `pass/package.py` -> `_pass/package.py` (reserved keywords are preceded by an underscore)

## Spack version 1.0

Further information about new features and changes to packages since the `v0.23` release can be found in the [Spack v1.0.0 release notes](https://github.com/spack/spack/releases/tag/v1.0.0).
