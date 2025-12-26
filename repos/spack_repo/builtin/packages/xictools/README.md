This report provides a summary of licenses found in xictools-4.3.23, including
expanded tarball content. Short-form SPDX license identifiers are used in this
document where possible.

## Summary

1. The XicTools codebase is primarily released under **Apache-2.0**, with
   specific exceptions for third-party components and inherited code. The
   `license/header` file contains the standard **Apache-2.0** header used
   throughout the codebase.
2. `xt_base/` is required when building xictools. Most files are licensed under
   **Apache-2.0**. Some files are licensed under **Spencer-94 AND BSD-4-Clause-UC**, 
   see `xt_base/regex/COPYRIGHT`. `xt_base/miscutil/randval.cc` contains both
   **Apache-2.0** and **BSD-4-Clause-UC** text. `xt_base/sparse/` contains code
   derived from Berkeley's Sparse package used in SPICE3 under a historical
   license similar to **HPND-UC** but with additional attribution requirements. 
3. Building WRspice will include several GPL and LGPL components:
    1. `adms/` contains **GPL-3.0-or-later** licensed code.
    2. `KLU/SuiteSparse/` expanded from `KLU/SuiteSparse-4.4.6.tar.gz` contains
       components with **LGPL-2.1-or-later**, **GPL-2.0-or-later**, and
       **BSD-3-Clause** licenses. Only the **LGPL-2.1-or-later code** is used by
       WRspice (see `KLU/Makefile.sample`).
    3. `vl/` contains code derived from UC Berkeley that requires propagating a
       copyright notice. Some examples are licensed under **GPL-2.0-or-later**.
       WRspice requires `vl`, xic does not. 
    4. `wrspice/mmjco/` contains **GPL-3.0-or-later** licensed code.
       `wrspice/mmjco/cmpfit-1.4/` contains **Minpack** licensed code.
    5. Some files contain UC Berkeley copyright notices (from SPICE3) requiring
       propagation of the copyright notice, similar to `vl`.
4. `mozy/` provides the help system and viewer and contains
   **LGPL-2.0-or-later** licensed code in `mozy/src/htm/`. 
5. `fastcap/` and `fasthenry/` contain permissively licensed code without a SPDX
   identifier. The license is identical to
   https://www.rle.mit.edu/cpg/copyright_disclaimer.htm. However, `fasthenry` 
   depends on `KLU` and is built with **LGPL-2.1-or-later** code.
6. `mrouter/` contains **Apache-2.0** licensed code. Code in tarballs in
   `mrouter/source.lefdef/` is from Cadence and also **Apache-2.0** licensed. 
7. `secure/` contains **Apache-2.0** licensed code. This is legacy license
   server code not built by package.py. 

## KLU/ details

The `SuiteSparse/` directory expanded from SuiteSparse-4.4.6.tar.gz contains
multiple components with different licenses. Only the AMD, BTF, COLAMD, KLU, and
SuiteSparse_config folders are used for WRspice. No licensing restrictions apply 
to SuiteSparse_config/ per SuiteSparse_config.h.

### **LGPL-2.1-or-later** Components
- `AMD/`
- `BTF/`
- `CAMD/`
- `CCOLAMD/`
- `CHOLMOD/Check/`
- `CHOLMOD/Cholesky/`
- `CHOLMOD/Core/`
- `CHOLMOD/Partition/`
- `COLAMD/`
- `CSparse/`
- `CXSparse/`
- `CXSparse_newfiles/`
- `KLU/`
- `LDL/`

### **GPL-2.0-or-later** Components
- `CHOLMOD/Demo/`
- `CHOLMOD/GPU/`
- `CHOLMOD/Include`
- `CHOLMOD/MatrixOps/`
- `CHOLMOD/Modify/`
- `CHOLMOD/Supernodal/`
- `GPUQREngine/`
- `RBio/`
- `SPQR/`
- `SuiteSparse_GPURuntime/`
- `UMFPACK/`

### **BSD-3-Clause**
- `UFget/UFhelp.html`

### No Licensing Information
- `MATLAB_Tools/`
