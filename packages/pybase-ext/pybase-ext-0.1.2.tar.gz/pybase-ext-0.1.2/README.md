![tests_badge](https://github.com/Jtachan/PyBaseExtension/actions/workflows/unittests.yml/badge.svg)
[![PyPI Version](https://img.shields.io/pypi/v/pybase-ext)](https://pypi.org/project/pybase-ext/)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue)](https://www.python.org/downloads/) 
[![PyPI Downloads](https://img.shields.io/pypi/dm/pybase-ext)](https://pypi.org/project/pybase-ext/) 
[![MIT License](https://img.shields.io/github/license/Jtachan/PyBaseExtension)](https://github.com/Jtachan/PyBaseExtension/blob/master/LICENSE)
[![Docs](https://img.shields.io/badge/Mkdocs-page-blue)](https://Jtachan.github.io/PyBaseExtension/)

# Python Base Extension

❗ This is a legacy release. This version won't be updated.
Please update to [`PyBackport`](https://github.com/Jtachan/PyBackport) to continue using a maintained version.
`pybase-ext` will be deprecated when `py-backport` has its major release v1.0.

The `pybase-ext` modules serve three purposes:

* Enable the use of new base classes in older Python versions. For example, `enum.StrEnum` is new in Python 3.11, but `pybase-ext` allows users on previous versions to use it too.
* Enable experimental classes not implemented in other modules. For example, `enum.TupleEnum` is not implemented in `enum`, but `pybase-ext` allows users to create enumerations where its members are tuples.
* Provide of new classes containing commonly used constant values. For example, `pybase-ext.colors` provides a wrapper to commonly used BGR color codes, like `BGR.WHITE` to use the color code `(255, 255, 255)`


## Setup

Install the package via pip.

```shell
pip install pybase-ext
```

## 📖 Documentation

Documentation can be found:

- At the released [mkdocs page](https://Jtachan.github.io/PyBaseExtension/).
- Within the [`docs`](https://github.com/Jtachan/PyBaseExtension/blob/main/docs/index.md) folder.
