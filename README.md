# Poetry Extended (Poetryx)

<p align="center">
  <img src="https://raw.githubusercontent.com/nachatz/poetryx/master/docs/img/poetryx.jpg">
</p>

<p align="center">
Augmenting the flow of functionality for Poetry projects, setup, and debugging. Enabling streamlined user experience within specific IDEs, scaffolding projects, and generic utilities.
</p>

<div align="center">

[![v0.1.0](https://img.shields.io/badge/version-v0.1.0-blue.svg)](https://github.com/nachatz/poetryx)
[![Test](https://github.com/nachatz/poetryx/actions/workflows/validate.yaml/badge.svg)](https://github.com/nachatz/poetryx/actions/workflows/validate.yaml)
[![License](https://img.shields.io/badge/license-Apache%202-brightgreen.svg)](https://github.com/nachatz/poetryx/blob/master/LICENSE.txt)

</div>

---

&nbsp; 
## Getting started

This CLI is built on-top of Poetry, so likely you have already downloaded Poetry. If not, you can install [here](https://python-poetry.org/docs/):

### 1. Install Poetryx

```shell 
pip install poetryx
```
### 2. Configure Poetryx for your IDE

```shell
poetryx configure
```

&nbsp; 
## Provided utilities 

### 1. IDE configuration (**currently only VSCode**)
Configure poetryx to target specific requirements for your poetry environments including the IDE you're using.
```shell
poetryx configure
```

### 2. Factory reset
Reset poetryx to the default settings
```shell
poetryx clean
```

&nbsp;
## Contributions

### Style guide

This library conforms to standard Black-check formatting, Pylint linting, and typing. Further, it enforces and follows standards from Google's Python style guide: https://google.github.io/styleguide/pyguide.html

### Releases

Releases are managed via PyPl and the [release.yaml](.github/workflows/release.yaml). Admins creating a release in GitHub will trigger a published distribution to PyPl for users to take advantage of. Ensure to bump the version in the `pyproject.toml` and `README.md`.