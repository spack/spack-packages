<h2>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/spack/spack-packages/refs/heads/develop/logo/spack-packages-logo-white-text.svg" width="368">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/spack/spack-packages/refs/heads/develop/logo/spack-packages-logo-text.svg" width="368">
  <img alt="Spack" src="https://raw.githubusercontent.com/spack/spack-packages/refs/heads/develop/logo/spack-packages-logo-text.svg" width="368">
</picture>

<br>
<br clear="all">

<a href="https://spack.readthedocs.io"><img src="https://readthedocs.org/projects/spack/badge/?version=latest" alt="Documentation Status"></a>
<a href="https://slack.spack.io"><img src="https://slack.spack.io/badge.svg" alt="Slack"/></a>
<a href="https://matrix.to/#/#spack-space:matrix.org"><img src="https://img.shields.io/matrix/spack-space%3Amatrix.org?label=matrix" alt="Matrix"/></a>

</h2>

**[Getting Started] &nbsp; • &nbsp; [Community] &nbsp; • &nbsp; [Packaging Guide] &nbsp; • &nbsp; [Spack]**

This is the default [Spack](https://github.com/spack/spack) package repository, which contains the set of packages maintained by the Spack community.
In Spack v1.0 and later, the repository here is automatically added to the Spack configuration.

## Contributing

To contribute, make a pull request to this repository with your package changes.
We run continuous integration to test builds of a large number of Spack packages.

If you want to test your changes locally before submitting a PR, you can make
Spack use your local clone of `spack-packages` like this:

```
spack repo set --destination /path/to/local/spack-packages builtin
```

`$spack` can be used to form a relative path to your Spack root directory.

If you are migrating your pull requests from
[github.com/spack/spack](https://github.com/spack/spack), it is recommended to use the [migration tool](https://github.com/spack/migrate-package-prs).

## Community

Spack is an open source project.  Questions, discussion, and contributions are welcome.

* **Slack workspace**: [spackpm.slack.com](https://spackpm.slack.com).
  To get an invitation, visit [slack.spack.io](https://slack.spack.io).
* **Matrix space**: [#spack-space:matrix.org](https://matrix.to/#/#spack-space:matrix.org):
  [bridged](https://github.com/matrix-org/matrix-appservice-slack#matrix-appservice-slack) to Slack.

## Structure of this repo

This repository does not look like the original Spack package repositories. Its structure
has been renovated a bit to make it work better with modern python tooling. The repo
looks like this:

```
spack-packages/
    repos/                          # add this to PYTHONPATH for your editor
        spack_repo/                 # dedicated python package for spack repositories
            builtin/                # namespace of this package repository
                build_systems/      # build_systems: common base classes used by many packages
                packages/           # This is where all the package.py files go
                    <PKG_NAME>/     # e.g., hdf5, zlib, mfem
                        package.py  # actual package recipes
```

The new repository structure is designed around several goals:

1. Make it easy to add the repository to `PYTHONPATH`;
2. Allow common python code like `build_systems` to live in the package repo, not core
   Spack; and
3. Allow multiple repositories (e.g. something in addition to `builtin`) to live in the
   same git repository.

If you use an editor like vscode, you should be able to point it directly to the `repos/`
directory and have the editor understand the package code.

## Searching Spack packages

You can query the packages built in this repository by visiting
[packages.spack.io](https://packages.spack.io).

## Binary builds of Spack packages

The packages we build in CI here are available as Spack build caches. You can
search hosted binaries at [cache.spack.io](https://cache.spack.io).

License
----------------

Spack is distributed under the terms of both the MIT license and the
Apache License (Version 2.0). Users may choose either license, at their
option.

All new contributions must be made under both the MIT and Apache-2.0
licenses.

See [LICENSE-MIT](https://github.com/spack/spack-packages/blob/develop/LICENSE-MIT),
[LICENSE-APACHE](https://github.com/spack/spack-packages/blob/develop/LICENSE-APACHE),
[COPYRIGHT](https://github.com/spack/spack-packages/blob/develop/COPYRIGHT), and
[NOTICE](https://github.com/spack/spack-packages/blob/develop/NOTICE) for details.

SPDX-License-Identifier: (Apache-2.0 OR MIT)

LLNL-CODE-811652

[Getting Started]: https://spack.readthedocs.io/en/latest/getting_started.html
[Community]: #community
[Packaging Guide]: https://spack.readthedocs.io/en/latest/packaging_guide_creation.html
[Spack]: https://github.com/spack/spack
