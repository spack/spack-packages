# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
param (
    [Parameter(Mandatory=$true)] [string]$SrcDir,
    [Parameter(Mandatory=$true)] [string]$DestPrefix
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$componentsFile = Join-Path $SrcDir "components"
if (-not (Test-Path $componentsFile -PathType Leaf)) {
    Write-Error "Missing components file at $componentsFile"
    exit 1
}

$components = [System.IO.File]::ReadAllLines($componentsFile) | Where-Object { $_.Trim() -ne "" }

foreach ($component in $components) {
    $manifestIn = Join-Path $SrcDir "$component\manifest.in"
    if (-not (Test-Path $manifestIn -PathType Leaf)) {
        Write-Warning "Skipping component '$component': manifest.in not found."
        continue
    }

    Write-Host "Installing component: $component"

    switch -Regex -File $manifestIn {
        "^file:(.+)" {
            $relPath = $Matches[1]
            $sourcePath = Join-Path $SrcDir "$component\$relPath"
            $destPath = Join-Path $DestPrefix $relPath

            # Ensure target directory tree exists
            $parentDir = Split-Path $destPath -Parent
            if (-not (Test-Path $parentDir)) {
                $null = New-Item -ItemType Directory -Path $parentDir -Force
            }
            
            Copy-Item -Path $sourcePath -Destination $destPath -Force
        }
        "^dir:(.+)" {
            $relPath = $Matches[1]
            $sourcePath = Join-Path $SrcDir "$component\$relPath"
            $destPath = Join-Path $DestPrefix $relPath

            # Ensure target directory exists
            if (-not (Test-Path $destPath)) {
                $null = New-Item -ItemType Directory -Path $destPath -Force
            }
            
            Copy-Item -Path "$sourcePath\*" -Destination $destPath -Recurse -Force
        }
    }
}

Write-Host "Installation completed successfully."