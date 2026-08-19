from spack.package import *
from spack.util.executable import which
from spack.error import InstallError
import os
import re


class Multiwfn(Package):
    """
    Multiwfn: A multifunctional wavefunction analyzer.
    The default version is the non-GUI version. During installation, you can
    choose whether to enable the GUI.
    For example, “spack install multiwfn” installs the non-GUI version, while
    “spack install multiwfn+gui” enables the GUI version.
    Enabling the GUI version requires support from the Motif library.

    LICENSE INFORMATION:

    To use Multiwfn, you are required to read and agree the following terms:

    (a) Currently Multiwfn is free of charge and open-source for both academic
        and commercial usages, anyone is allowed to freely distribute the
        original or their modified Multiwfn codes to others.

    (b) Multiwfn can be distributed as a free component of commercial code.
        Selling modified version of Multiwfn may also be granted, however,
        obtaining prior consent from the original author of Multiwfn (Tian Lu)
        is needed.

    (c) If Multiwfn is utilized in your work, or your own code incorporated
        any part of Multiwfn code, at least the following original papers of
        Multiwfn MUST BE cited in main text of your paper or code:
        - Tian Lu, Feiwu Chen, J. Comput. Chem., 33, 580-592 (2012)
        - Tian Lu, J. Chem. Phys., 161, 082503 (2024)

    (d) There is no warranty of correctness of the results produced by
        Multiwfn, the author of Multiwfn does not hold responsibility in any
        way for any consequences arising from the use of Multiwfn.

    Whenever possible, please mention and cite Multiwfn in main text rather
    than in supplemental information.
    """

    homepage = "http://sobereva.com/multiwfn/"
    maintainers("MollyMD")
    license("see LICENSE INFORMATION in the description")

    # GUI
    variant("gui", default=False, description="Enable GUI (requires Motif)")

    # External program support (switch + path)
    variant("gaussian", default=False, description="Enable Gaussian support")
    variant(
        "gaupath",
        default="/sob/g16/g16",
        values=str,
        description=(
            "Path to Gaussian executable (g16/g09 or a user-defined executable name). "
            "Such as +gaussian gaupath=/sob/g16/g16"
        ),
    )

    variant("orca", default=False, description="Enable ORCA support")
    variant(
        "orcapath",
        default="D:\study\orca5\orca.exe",
        values=str,
        description=(
            "Path to ORCA executable (orca or a user-defined executable name). "
            "Such as +orca orcapath=D:\study\orca5\orca.exe"
        ),
    )

    variant("orca_2mkl", default=False, description="Enable orca_2mkl support")
    variant(
        "orca_2mklpath",
        default="/sob/orca/orca_2mkl",
        values=str,
        description=(
            "Path to orca_2mkl executable (orca_2mkl or a user-defined executable name). "
            "Such as +orca_2mkl orca_2mklpath=/sob/orca/orca_2mkl"
        ),
    )

    variant("formchk", default=False, description="Enable formchk support")
    variant(
        "formchkpath",
        default="/sob/g16/formchk",
        values=str,
        description=(
            "Path to Gaussian formchk executable (formchk or a user-defined executable name). "
            "Such as +formchk formchkpath=/sob/g16/formchk"
        ),
    )

    # Versions
    version(
        "2026.3.27-nogui",
        url="http://sobereva.com/multiwfn/misc/Multiwfn_2026.3.27_bin_Linux_noGUI.zip",
        sha256="cd8e90b501066783d9dd340b032329b27c76fb5bd39a0e2a056cad9adfb6b656",
    )

    version(
        "2026.3.27-gui",
        url="http://sobereva.com/multiwfn/misc/Multiwfn_2026.3.27_bin_Linux.zip",
        sha256="4f3d6290eb384a06b369b97f56df57e47ebbb0d23bcb59f73d24de9e986a8dae",
    )

    conflicts("~gui", when="@2026.3.27-gui")
    conflicts("+gui", when="@2026.3.27-nogui")

    depends_on("unzip", type="build")
    depends_on("motif", when="+gui")

    # Parameter validation
    def validate(self):
        spec = self.spec

        if spec.variants["gaupath"].value and "+gaussian" not in spec:
            raise InstallError("gaupath requires +gaussian")

        if spec.variants["orcapath"].value and "+orca" not in spec:
            raise InstallError("orcapath requires +orca")

        if spec.variants["orca_2mklpath"].value and "+orca_2mkl" not in spec:
            raise InstallError("orca_2mklpath requires +orca_2mkl")

        if spec.variants["formchkpath"].value and "+formchk" not in spec:
            raise InstallError("formchkpath requires +formchk")

    # Install
    def install(self, spec, prefix):
        # Extract ZIP file
        unzip = which("unzip")
        unzip(self.stage.archive_file, "-d", self.stage.source_path)

        # Automatically detect the extracted source directory
        dirs = [
            d
            for d in os.listdir(self.stage.source_path)
            if os.path.isdir(os.path.join(self.stage.source_path, d))
        ]
        if not dirs:
            raise InstallError("No directories found in the extracted archive.")
        elif len(dirs) == 1:
            src_dir = os.path.join(self.stage.source_path, dirs[0])
        else:
            candidates = [d for d in dirs if d.startswith("Multiwfn")]
            if not candidates:
                src_dir = os.path.join(self.stage.source_path, dirs[0])
            else:
                src_dir = os.path.join(self.stage.source_path, candidates[0])

        # Copy to the installation prefix
        install_tree(src_dir, prefix)

        # Modify settings.ini
        settings = os.path.join(prefix, "settings.ini")
        if os.path.exists(settings):
            with open(settings, "r") as f:
                lines = f.readlines()

            def get_physical_cores():
                """Get the number of physical cores, compatible with hyper-threading."""
                import subprocess

                try:
                    output = subprocess.check_output(
                        "lscpu -p=CPU,Core,Socket", shell=True, text=True
                    )
                    cores = set()
                    for line in output.splitlines():
                        if line.startswith("#"):
                            continue
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue
                        core_id = int(parts[1])
                        socket_id = int(parts[2])
                        cores.add((socket_id, core_id))
                    n_cores = len(cores)
                    return max(1, n_cores)
                except Exception:
                    return 4

            def resolve_exe(user_path, names):
                if user_path:
                    return user_path
                for n in names:
                    p = which(n)
                    if p:
                        return p
                return None

            def replace_or_add(lines, key, value, quote=False):
                """Replace or add key=value in settings.ini while preserving comments."""
                new_lines = []
                replaced = False
                for line in lines:
                    stripped = line.strip()
                    if stripped.startswith(key + "="):
                        if "//" in line:
                            code, comment = line.split("//", 1)
                            comment = "//" + comment
                        else:
                            code, comment = line, ""
                        indent = line[: len(line) - len(line.lstrip())]
                        val_str = f'"{value}"' if quote else str(value)
                        new_line = f"{indent}{key}= {val_str} {comment}\n"
                        new_lines.append(new_line)
                        replaced = True
                    else:
                        new_lines.append(line)
                if not replaced:
                    val_str = f'"{value}"' if quote else str(value)
                    new_lines.append(f"{key}= {val_str}\n")
                return new_lines

            # Set nthreads to the number of physical cores
            nthreads = get_physical_cores()
            lines = replace_or_add(lines, "nthreads", nthreads, quote=False)

            # Write the external program paths
            if "+gaussian" in spec:
                p = resolve_exe(spec.variants["gaupath"].value, ["g16", "g09"])
                if p:
                    lines = replace_or_add(lines, "gaupath", p, quote=True)

            if "+orca" in spec:
                p = resolve_exe(spec.variants["orcapath"].value, ["orca"])
                if p:
                    lines = replace_or_add(lines, "orcapath", p, quote=True)

            if "+orca_2mkl" in spec:
                p = resolve_exe(spec.variants["orca_2mklpath"].value, ["orca_2mkl"])
                if p:
                    lines = replace_or_add(lines, "orca_2mklpath", p, quote=True)

            if "+formchk" in spec:
                p = resolve_exe(spec.variants["formchkpath"].value, ["formchk"])
                if p:
                    lines = replace_or_add(lines, "formchkpath", p, quote=True)

            # Write back to settings.ini
            with open(settings, "w") as f:
                f.writelines(lines)

        # Executable wrapper
        exe_name = "Multiwfn" if "+gui" in spec else "Multiwfn_noGUI"
        real_exe = os.path.join(prefix, exe_name)
        set_executable(real_exe)

        mkdirp(prefix.bin)
        wrapper = os.path.join(prefix.bin, exe_name)

        with open(wrapper, "w") as f:
            f.write(
                f"""#!/bin/bash
ulimit -s unlimited
export OMP_STACKSIZE=200M
mkdir -p ~/spack_Multiwfnpath_settings_ini/
cp -n "{prefix}/settings.ini" ~/spack_Multiwfnpath_settings_ini/
export Multiwfnpath="~/spack_Multiwfnpath_settings_ini/"
exec "{real_exe}" "$@"
"""
            )
        set_executable(wrapper)

    # Runtime environment
    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin)
        env.set("OMP_STACKSIZE", "200M")
        env.set(
            "Multiwfnpath", os.path.expanduser("~/spack_Multiwfnpath_settings_ini/")
        )