import os

from spack.error import InstallError
from spack.package import *
from spack.util.executable import which


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
    license("LicenseRef-Multiwfn")

    # GUI
    variant("gui", default=False, description="Enable GUI (requires Motif)")

    # Versions
    version(
        "2026.10.1-nogui",
        url="http://sobereva.com/multiwfn/misc/Multiwfn_2026.10.1_bin_Linux_noGUI.zip",
        sha256="96a4ba4be280f5ae4f63dd66a75dfe60084a8c46d06674e74f6f253d8db97aa5",
    )

    version(
        "2026.10.1-gui",
        url="http://sobereva.com/multiwfn/misc/Multiwfn_2026.10.1_bin_Linux.zip",
        sha256="df6f571abeb9470b9815d1eef6b97b5bf7dc8acd80649a8136e019b9ec1be484",
    )

    conflicts("~gui", when="@2026.10.1-gui")
    conflicts("+gui", when="@2026.10.1-nogui")

    depends_on("unzip", type="build")
    depends_on("motif", when="+gui")

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
                        ["lscpu", "-p=CPU,Core,Socket"], universal_newlines=True
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
                except (subprocess.CalledProcessError, OSError, ValueError):
                    return 4

            def replace_or_add(lines, key, value, quote=False):
                """Replace or add key=value in settings.ini while preserving comments."""
                new_lines = []
                replaced = False
                for line in lines:
                    stripped = line.strip()
                    if stripped.startswith(key + "="):
                        if "//" in line:
                            _, comment = line.split("//", 1)
                            comment = "//" + comment
                        else:
                            comment = ""
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

            # Write back to settings.ini
            with open(settings, "w") as f:
                f.writelines(lines)

        # Executable wrapper
        exe_name = "Multiwfn" if "+gui" in spec else "Multiwfn_noGUI"
        real_exe = os.path.join(prefix, exe_name)
        set_executable(real_exe)

        mkdirp(prefix.bin)
        settings_dir = os.path.expanduser("~/spack_Multiwfnpath_settings_ini/")
        wrapper = os.path.join(prefix.bin, exe_name)

        with open(wrapper, "w") as f:
            f.write(
                f"""#!/bin/bash
ulimit -s unlimited
export OMP_STACKSIZE=200M
mkdir -p "{settings_dir}"
if test -f "{prefix}/settings.ini"; then
    cp -n "{prefix}/settings.ini" "{settings_dir}" || true
fi
export Multiwfnpath="{settings_dir}"
exec "{real_exe}" "$@"
"""
            )
        set_executable(wrapper)

    # Runtime environment
    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin)
        env.set("OMP_STACKSIZE", "200M")
        env.set("Multiwfnpath", os.path.expanduser("~/spack_Multiwfnpath_settings_ini/"))
        if self.spec.satisfies("+gui"):
            env.prepend_path("LD_LIBRARY_PATH", self.spec["motif"].prefix.lib)
