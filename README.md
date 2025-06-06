# Spack Packages

This is the default [Spack](https://github.com/spack/spack) packages repository, which
contains the set of packages maintained by the Spack community. In Spack v1.0 and later,
the repository here is automatically added to the Spack configuration.

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
3. Allow multiple reositories (e.g. something in addition to `builtin` to live in the
   same git repository.

If you use an editor like vscode, you should be able to point it directly to the `repos/`
directory and have the editor understand the package code.

## Contributing

To contribute, simply make a pull request to this repository with your package changes.
We run continuous integration on this repository to test builds of a large number of
Spack packages.

If you are trying to migrate your pull requests from
[github.com/spack/spack](https://github.com/spack/spack), there are several ways you can
do this. You can
[cherry-pick](https://stackoverflow.com/questions/5120038/is-it-possible-to-cherry-pick-a-commit-from-another-git-repository)
your PR from the main repository. Alternately, we are working on a
[migration script](https://gist.github.com/haampie/0bd28e75f91b3be6287094a1111391cf)
that you can try out. More instructions are coming soon.

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
