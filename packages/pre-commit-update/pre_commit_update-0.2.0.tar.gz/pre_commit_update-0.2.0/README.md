# pre-commit-update

![Version](https://img.shields.io/pypi/pyversions/pre-commit-update)
![Downloads](https://pepy.tech/badge/pre-commit-update)
![Formatter](https://img.shields.io/badge/code%20style-black-black)
![License](https://img.shields.io/pypi/l/pre-commit-update)

**pre-commit-update** is a simple CLI tool to check and update pre-commit hooks.

## Table of contents

1. [ Reasoning ](#reasoning)
2. [ Features ](#features)
3. [ Installation ](#installation)
4. [ Usage ](#usage)
    1. [ Pipeline usage example ](#pipeline-usage-example)
    2. [ pre-commit hook usage example ](#pre-commit-hook-usage-example)
    3. [ pyproject.toml usage example ](#pyprojecttoml-usage-example)

## Reasoning

`pre-commit` is a nice little tool that helps you polish your code before releasing it into the wild.
It is fairly easy to use. A single `pre-commit-config.yaml` file can hold multiple hooks (checks) that will go through
your code or repository and do certain checks. The problem is that the file is static and once you pin your hook versions
after a while they get outdated.

`pre-commit-update` was created because there is no easy way to update your hooks by using
`pre-commit autoupdate` as it is not versatile enough.


## Features

|                      Feature                       | pre-commit-update |            pre-commit autoupdate            |
|:--------------------------------------------------:|:-----------------:|:-------------------------------------------:|
|   Dry run (checks for updates, does not update)    |        Yes        |                     No                      |
|                Stable versions only                |        Yes        |                     No                      |
|         Exclude repo(s) from update check          |        Yes        | Workaround (updates only specified repo(s)) |
| Keep repo(s) (checks for updates, does not update) |        Yes        |                     No                      |
|           Update by hash instead of tag            |        Yes        |                     Yes                     |
|          Can be used as a pre-commit hook          |        Yes        |                     No                      |
|       Can be configured in `pyproject.toml`        |        Yes        |                     No                      |


## Installation

`pre-commit-update` is available on PyPI:
```console 
$ python -m pip install pre-commit-update
```
Python >= 3.7 is supported.

**NOTE:** Please make sure that `git` is installed.


## Usage

`pre-commit-update` CLI can be used as below:

```console
Usage: pre-commit-update [OPTIONS]

Options:
  -d, --dry-run / -nd, --no-dry-run             Dry run only checks for the new versions without updating  [default: nd]
  -a, --all-versions / -na, --no-all-versions   Include the alpha/beta versions when updating  [default: na]
  -v, --verbose / -nv, --no-verbose             Display the complete output  [default: nv]
  -e, --exclude TEXT                            Exclude specific repo(s) by the `repo` url trim
  -k, --keep TEXT                               Keep the version of specific repo(s) by the `repo` url trim (still checks for the new versions)
  -h, --help                                    Show this message and exit.
```

If you want to just check for updates (without updating `pre-commit-config.yaml`), for example, you would use:
```console
$ pre-commit-update -d
```
or
```console
$ pre-commit-update --dry-run
```

**NOTE:** If you are to use the `exclude` or `keep` options, please pass the repo url trim as a parameter.
Keep in mind that if you have multiple hooks (id's) configured for a single repo and you `exclude` that repo,
**NONE** of the hooks will be updated, whole repo will be excluded.

Example of repo url trim: https://github.com/ambv/black -> `black` (you will only pass `black` as a parameter to
`exclude` or `keep`)

### Pipeline usage example
#### GitLab job:

```yaml
pre-commit-hooks-update:
  stage: update
  script:
    # install git if not present in the image
    - pip install pre-commit-update
    - pre-commit-update --dry-run
  except:
    - main
  when: manual
  allow_failure: true
```

**NOTE:** This is just an example, feel free to do your own configuration

### pre-commit hook usage example

You can also use `pre-commit-update` as a hook in your `pre-commit` hooks:

```yaml
- repo: https://gitlab.com/vojko.pribudic/pre-commit-update
  rev: v0.1.7  # Insert the latest tag here
  hooks:
    - id: pre-commit-update
      args: [--dry-run, --exclude, black, --keep, isort]
```

### pyproject.toml usage example

You can configure `pre-commit-update` in your `pyproject.toml` as below (feel free to do your own configuration):

```toml
[tool.pre-commit-update]
dry_run = true
all_versions = false
verbose = true
exclude = ["isort"]
keep = ["black"]
```

**NOTE:** If some of the options are missing (for example `exclude` option), `pre-commit-update`
will use default value for that option (default for `exclude` option would be an empty list).

***IMPORTANT*** If you invoke `pre-commit-update` with any arguments (e.g. `pre-commit-update -d`),
`pyproject.toml` configuration will be **overridden**. This means that all the arguments passed while
calling `pre-commit-update` will have priority over configuration defined inside `pyproject.toml`.
If you want to override boolean flags, you can do so by passing the negative flag value.
For example, given the configuration above, to override `verbose` flag from `pyproject.toml`, you
would invoke `pre-commit-update` with either `--no-verbose` or `-nv`.
