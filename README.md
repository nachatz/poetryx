# Poetry Extended (Poetryx)

<p align="center">
  <img src="https://raw.githubusercontent.com/nachatz/poetryx/master/docs/img/poetryx.jpg" width="400" height="400" style="border-radius: 50%;">
</p>


<p align="center">
Extending the native functionality of Poetry, enabling streamlined user experience within specific IDEs, scaffolding projects, and generic utilities.
</p>

<div align="center">

[![v0.0.2](https://img.shields.io/badge/version-v0.0.2-blue.svg)](https://github.com/nachatz/poetryx)
[![Test](https://github.com/nachatz/poetryx/actions/workflows/validate.yaml/badge.svg)](https://github.com/nachatz/poetryx/actions/workflows/validate.yaml)
[![License](https://img.shields.io/badge/license-Apache%202-brightgreen.svg)](https://github.com/nachatz/poetryx/blob/master/LICENSE.txt)

</div>

---

&nbsp; 
## Getting started

This CLI is built on-top of Poetry, so likely you have already downloaded Poetry. If not, you can set it up natively through Poetryx:

1. Install Poetryx

```shell 
pip install poetryx
```
2. Setup Poetryx 

```shell
poetryx setup
```

3. Run native Poetry commands

```shell
poetryx install
```

4. Take advantage of Poetryx utilities (example configures VScode for the poetry env)

```shell
poetryx code configure
```

&nbsp; 
## Provided utilities 

### Native poetry commands - `poetryx {any poetry command}`

Run any poetry command directly through `poetryx`

### VSCode configuration - `poetryx code configure`

Configure VScode to use the current poetry environments for debugging and interpreting. Enabling immediate debugging through the `Testing` extension