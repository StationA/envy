# envy

[![pypi version](https://badge.fury.io/py/envy-config.svg)](https://badge.fury.io/py/envy-config)

Environment-based configurations that you will envy.

envy implements the guiding principles for configuration of the
["Twelve-Factor App"](https://12factor.net/config), allowing application development to rely solely
on its environment for configuration. This enables the idea of "one codebase, many deploys" as it
allows very granular control over an app's configuration by allowing each deploy to specify its own
values.

### Requirements

* Python 2.7+ or 3.6+

### Install from PyPI (recommended)

```
pip install envy-config
```

### Installing from Github

```
pip install git+https://github.com/StationA/envy.git#egg=envy-config
```

### Installing from source

```
git clone https://github.com/StationA/envy.git
cd envy
pip install .
```

# Usage

Check out some of the usage examples in the [`examples/` directory](examples)

# Contributing

### Installing for development

```
pip install --editable .
```

### Running tests

```
tox -e dev
```
