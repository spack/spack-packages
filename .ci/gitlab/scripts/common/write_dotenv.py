import os
import sys

CI_PROJECT_DIR = "."
CI_AUX_DIR = os.path.join(".ci", "tmp", "spack")


def configure_packages_repo(dotenv):
    dotenv["SPACK_CI_PACKAGES_ROOT"] = CI_PROJECT_DIR
    dotenv["SPACK_CI_SPACK_ROOT"] = CI_AUX_DIR


def configure_core_repo(dotenv):
    dotenv["SPACK_CI_PACKAGES_ROOT"] = CI_AUX_DIR
    dotenv["SPACK_CI_SPACK_ROOT"] = CI_PROJECT_DIR


def read_dotenv(file):
    dotenv = {}
    for line in file:
        if "=" in line:
            key, value = line.split("=", 1)
            dotenv[key] = value.strip()
    return dotenv


def write_dotenv(env, file):
    for var, value in env.items():
        file.write(f"{var}={value}\n")


if __name__ == "__main__":
    dotenv = {}
    base_dotenv = sys.argv[1] if len(sys.argv) > 1 else None
    if base_dotenv:
        if os.path.exists(base_dotenv):
            print(f"Found base dotenv: {base_dotenv}")
            with open(base_dotenv, "r", encoding="utf-8") as fd:
                dotenv = read_dotenv(fd)
        else:
            print(f"File does not exist: {base_dotenv}")

    # Setup the repo/version to be used for checkout
    for checkout_var in ("SPACK_CHECKOUT_REPO", "SPACK_CHECKOUT_VERSION"):
        if checkout_var in os.environ:
            dotenv[checkout_var] = os.environ[checkout_var]

    repo_override = os.environ.get("CI_PROJECT_NAME")
    if repo_override and not repo_override.endswith("packages"):
        configure_core_repo(dotenv)
    else:
        configure_packages_repo(dotenv)

    with open("env", "w", encoding="utf-8") as fd:
        write_dotenv(dotenv, fd)
