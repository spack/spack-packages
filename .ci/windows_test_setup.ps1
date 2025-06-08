$ErrorActionPreference = "SilentlyContinue"
Write-Output F|xcopy .\spack-core\share\spack\qa\configuration\windows_config.yaml "$env:USERPROFILE\.spack\windows\config.yaml"
# The line below prevents the _spack_root symlink from causing issues with cyclic symlinks on Windows
(Get-Item '.\spack-core\lib\spack\docs\_spack_root').Delete()
./spack-core/share/spack/setup-env.ps1
