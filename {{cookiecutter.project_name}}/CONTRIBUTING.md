# Installation development
## Clone the repository

To get started clone the `{{cookiecutter.project_name}}` repository via `ssh`:

```shell
git clone git@github.com:MaMMoS-project/{{cookiecutter.project_name}}.git
```
or `https` if you don't have an `ssh` key:

```shell
git clone https://github.com/MaMMoS-project/{{cookiecutter.project_name}}.git
```

Then enter into the repository:

```shell
cd {{cookiecutter.project_name}}
```

## Install dependencies with pixi

- install [pixi](https://pixi.sh)

- activate pre-commits by running `pre-commit install`

- run `pixi shell` to create and activate an environment in which `{{cookiecutter.project_name}}` is installed (this will install python as well)

- the following pixi tasks are provided:

  - `pixi run test-unittest`: Run unittests with pytest (reading tests/)
  - `pixi run test-docstrings`: Run doctests with pytest (reading src/{{cookiecutter.package_name}})
  - `pixi run test-notebooks`: Run nbval with pytest on notebooks (reading examples/)
  - `pixi run test-all`: run `unittest`, `doctest` and `notebooktest`
  - `pixi run examples`: start jupyter lab in examples/ directory
  - `pixi run style`: style checks on all files using `pre-commit run --all-files`
