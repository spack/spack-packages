# GitHub Copilot Instructions for Spack Package Repository

This repository contains package definitions for [Spack](https://github.com/spack/spack/), a multi-platform package manager that builds and installs multiple versions and configurations of software. Spack works on Linux, macOS, and Windows, including many supercomputers.

## Repository Structure

- **Package files**: Located in `repos/spack_repo/builtin/packages/*/package.py`
- **Build systems**: Common base classes in `repos/spack_repo/builtin/build_systems/`
- **Tests**: Package tests in `tests/`
- **Stacks**: Environment definitions in `stacks/` that are automatically built on a Gitlab mirror and must succeed before pull requests can be merged

## Package Development Guidelines

### Setting up Spack itself

To get `spack` in your path, use the following commands:

```
git clone --depth=1 https://github.com/spack/spack.git
. spack/share/spack/setup-env.sh
```

### Multi-Version Support

Spack packages support multiple versions simultaneously. When adding new versions:

1. **Always preserve existing versions** unless marked deprecated with ``deprecated=True``. Only deprecated versions can be removed.
2. **Update dependencies carefully** to maintain compatibility across all supported versions
3. **Use version-specific constraints** with `when="@version:"` syntax when needed

### Key Package Fields

When working with package files, pay special attention to:

- **`git` field**: Points to the source repository for inspecting diffs between versions
- **`url` field**: Generic location from which version-specific URLs are derived
- **`version()`**: Each version should include SHA256 checksums (use `spack checksum <package-name>` to generate them; CI automatically verifies checksums for newly added versions)
- **`depends_on()`**: Dependencies with version constraints using `when="@version:"` syntax
- **`homepage`**: Official project website
- **`maintainers()`**: Package maintainers (GitHub usernames)

### Version Management Best Practices

```python
# Good: Versions are listed in descending order with SHA256 checksums
version("1.3.0", sha256="abcd1234...")
version("1.2.2", sha256="efgh5678...")
version("1.1.0", sha256="ijkl9012...")

# Good: backwards compatibility bounds
depends_on("python@3.8:", when="@1.3:", type=("build", "run"))
depends_on("python@3.7:", when="@1.2:", type=("build", "run"))
depends_on("python@3.6:", type=("build", "run"))

# Good: forward-compatibility bounds
depends_on("python@:3.13", when="@:1.2", type=("build", "run"))

# Good: Conditional features based on version
variant("new_feature", default=False, description="Enable new feature", when="@1.2.3:")
```

* `@1.2:` matches versions 1.2, 1.2.0, 1.2.1, 1.3, etc.
* `@:1.4` matches 1.0.0, 1.3.2, 1.4, 1.4.8 including any 1.4.x release, but not 1.5.0 or later. So `python@:3.14` matches any Python up to and including 3.14.x, but not 3.15 or later.

### Dependency Updates

You can use 

```
$ spack stage --path ./sources pkg@1.2.3
$ cd sources/spack-src
```

to check out source code of a specific version and inspect the `pyproject.toml` or `CMakeLists.txt` to see how dependencies have evolved between versions. This helps ensure that you update dependencies correctly when adding new versions.

When adding new package versions:

1. **Check for new dependencies** that the new version requires
2. **Update existing dependency version constraints** if needed
3. **Ensure backwards compatibility** with older versions where possible

Example of proper dependency evolution:
```python
# Version-specific dependency updates
depends_on("cmake@3.16:", when="@2.0:", type="build")
depends_on("cmake@3.12:", when="@1.0:", type="build")
depends_on("boost@1.70:", when="@2.1:", type=("build", "link"))
depends_on("boost@1.60:", type=("build", "link"))
```

### Package validation

You can verify that the `depends_on`, `version`, and other directives in your package files are correct by running: 

```
spack audit packages my-pkg
```

## Platform Support

Spack supports Linux, macOS, and Windows. When contributing:

- **Test on multiple platforms** when possible
- **Use platform-specific variants** when needed:
  ```python
  variant("shared", default=True, description="Build shared libraries")
  # Windows-specific considerations
  conflicts("+shared", when="platform=windows", msg="Windows requires static libraries")
  ```
- **Consider platform-specific dependencies**
- **Use conditional logic** for platform differences

## Code Style and Quality

The repository enforces strict code quality standards:

### Style Requirements

- **Python code style**: Enforced by `flake8`, `isort`, and `black`
- **Line length**: 99 characters maximum
- **Import organization**: Use `isort` for consistent import ordering
- **Code formatting**: Use `black` for consistent formatting

### Running Style Checks

```bash
# Run style checks (from repository root)
.ci/style_check.sh

# Fix style issues automatically
.ci/style_check.sh --fix
```

### Conditional Dependencies

```python
# Version-based conditions
depends_on("new-dep@1.0:", when="@2.0:")
depends_on("old-dep")

# Variant-based conditions  
depends_on("optional-dep", when="+feature")

# Platform-based conditions
depends_on("linux-only-dep", when="platform=linux")
```

### Handling Build Systems

```python
from spack_repo.builtin.build_systems.cmake import CMakePackage

class MyCMakePackage(CMakePackage):
    """CMake-based package"""
    
    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared")
        ]
        if self.spec.satisfies("@2.0:"):
            args.append(self.define("NEW_FEATURE", True))
        return args
        
    # Use dedicated helper functions to set configuration options
    # as defined in the build_systems packages inherited by individual packages
```

## Error Prevention

### Common Mistakes to Avoid

1. **Don't delete existing versions** unless absolutely necessary (when removing packages, flag in PR summary and explain justification)
2. **Don't break existing dependency relationships** when adding new versions
3. **Always include SHA256 checksums** for new versions
4. **Don't ignore platform-specific issues**
5. **Don't skip audit checks** - they catch many common problems

### Useful Debugging Commands

```bash
# Check package syntax
spack info <package-name>

# Validate package dependencies
spack spec <package-name>@<version>
```

## Additional Resources

- [Spack Documentation](https://spack.readthedocs.io/)
- [Packaging Guide](https://spack.readthedocs.io/en/latest/packaging_guide.html)
- [Package Repository Guidelines](https://github.com/spack/spack-packages/blob/develop/CONTRIBUTING.md)
- [Spack Main Repository](https://github.com/spack/spack)
- [Spack Slack Community](https://slack.spack.io)

## Summary

When contributing to this repository:

1. **Preserve multi-version support** - don't break existing installations
2. **Update dependencies thoughtfully** using version constraints
3. **Use `git` and `url` fields** to understand version changes
4. **Follow style guidelines** and pass all audit checks

This approach ensures that Spack continues to provide its core value proposition: supporting multiple versions and configurations of software simultaneously across diverse computing environments.