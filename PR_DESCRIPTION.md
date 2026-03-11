# PR Description: Add all ROMS test cases and custom application support

## Summary

This PR enhances the ROMS package by adding support for all built-in test cases and enabling users to build ROMS with custom application header files.

## Changes

### 1. Add all ROMS test cases to `roms_application` variant

Expanded the `roms_application` variant from 2 test cases to all 35 test cases available in the ROMS source distribution:

- **Previously**: Only `upwelling` and `benchmark` were available
- **Now**: All 35 test cases from `ROMS/Include/` are available:
  - `basin`, `benchmark`, `bio_toy`, `bl_test`, `canyon`, `channel`, `channel_neck`, `coupling_test`, `damee_4`, `dogbone`, `double_gyre`, `estuary_test`, `flt_test`, `grav_adj`, `inlet_test`, `kelvin`, `lab_canyon`, `lake_jersey`, `lake_signell`, `lmd_test`, `mixed_layer`, `overflow`, `riverplume1`, `riverplume2`, `seamount`, `sed_test1`, `sed_toy`, `shoreface`, `soliton`, `test_chan`, `test_head`, `upwelling`, `wc13`, `weddell`, `windbasin`, and `none`

### 2. Support for custom application header files

Added a new `custom_application` variant that allows users to provide their own custom application header files for ROMS simulations. This addresses real-world use cases where researchers need to configure ROMS for specific ocean modeling scenarios beyond the built-in test cases.

**Features:**
- Accepts a file path to a custom `.h` header file
- Validates file existence early in the build process (right after concretization)
- Automatically copies the custom header to `ROMS/Include/` directory
- Extracts application name from filename and configures the build accordingly
- Prevents conflicting configurations with clear error messages

**Implementation details:**
- Added `validate_application_variants()` method with dual validation points:
  - `@run_after("concretize")` - Early validation before dependency checking
  - `@run_before("edit")` - Backup validation before build
- Custom header files are validated for existence and copied during the edit phase

## Usage Examples

### Installing with built-in test cases

```bash
# Install with the default benchmark test case
spack install roms@4.2

# Install with a specific test case
spack install roms@4.2 roms_application=double_gyre %gcc

# Install with Intel compiler
spack install roms@4.2 roms_application=basin %intel-oneapi-compilers@2025.0.4
```

### Installing with a custom application header

```bash
# Install with a custom application header file
spack install roms@4.2 roms_application=none custom_application=/path/to/gulf_stream.h

# With specific compiler
spack install roms@4.2 \
    roms_application=none \
    custom_application=/home/researcher/configs/my_ocean.h \
    %intel-oneapi-compilers@2025.0.4
```

### Error handling example

When users incorrectly specify both a built-in test case and a custom application:

```bash
spack install roms@4.2 roms_application=basin custom_application=/path/to/custom.h
```

**Error message:**
```
==> Error: InstallError: Cannot specify both custom_application and a built-in roms_application. 
Set roms_application=none when using custom_application.
```

This error is raised immediately after concretization, providing fast feedback without wasting time on dependency resolution.

## Benefits

1. **Complete test coverage**: Users can now build and test all ROMS example applications
2. **Production-ready**: Researchers can use custom configurations for real ocean modeling work
3. **User-friendly**: Clear validation and error messages guide proper usage
4. **Fast feedback**: Early validation prevents wasted time on misconfigured builds
5. **Type-safe**: Spack validates variant values and file paths before building

## Testing

The changes have been tested with:
- Built-in test cases (e.g., `basin`, `double_gyre`, `weddell`)
- Custom application header files
- Various compilers (GCC, Intel OneAPI)
- Error conditions (invalid configurations, missing files)
