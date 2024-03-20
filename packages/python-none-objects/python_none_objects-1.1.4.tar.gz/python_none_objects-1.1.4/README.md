# python-none-objects

[![pypi-version]][pypi]
[![Downloads](https://img.shields.io/pypi/dm/python-none-objects)](https://pypistats.org/packages/python-none-objects)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![CodeFactor](https://www.codefactor.io/repository/github/llyaudet/python-none-objects/badge)](https://www.codefactor.io/repository/github/llyaudet/python-none-objects)
[![CodeClimateMaintainability](https://api.codeclimate.com/v1/badges/266efb337cabd7d7941e/maintainability)](https://codeclimate.com/github/LLyaudet/python-none-objects/maintainability)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/4be488463e31459bb2ba02794091610d)](https://app.codacy.com/gh/LLyaudet/python-none-objects/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
![GitHub top language](https://img.shields.io/github/languages/top/llyaudet/python-none-objects)
![GitHub License](https://img.shields.io/github/license/llyaudet/python-none-objects)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-none-objects)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/llyaudet/python-none-objects)
[![GitHub Sponsors](https://img.shields.io/github/sponsors/LLyaudet)](https://github.com/sponsors/LLyaudet)

|     **A collection of "None" objects compatible with various Python types**     |

The following code yields warning for "Default argument value is mutable".

```python3
from typing import List, Dict

def foo(some: int, other: List = [], thing: Dict = {}):
    for o in other:
        bar(some, o, thing)
```

It is usually recommended to use None instead
(<https://stackoverflow.com/questions/41686829/why-does-pycharm-warn-about-mutable-default-arguments-how-can-i-work-around-the>):

```python3
from typing import List, Dict, Optional

def foo(some: int, other: Optional[List] = None, thing: Optional[Dict] = None):
    if other is None:
        other = []
    if thing is None:
        thing = {}
    for o in other:
        bar(some, o, thing)
```

But I prefer less boilerplate code like this:

```python3
from typing import Iterable, Mapping
from types import MappingProxyType

def foo(some: int, other: Iterable = (), thing: Mapping = MappingProxyType({})):
    for o in other:
        bar(some, o, thing)
```

This package introduces constants to make the code more readable:

```python3
from typing import Iterable, Mapping
from python_none_objects import NoneIterable, NoneMapping

def foo(some: int, other: Iterable = NoneIterable, thing: Mapping = NoneMapping):
    for o in other:
        bar(some, o, thing)
```

Be sure to look at the discussions on GitHub:
<https://github.com/LLyaudet/python-none-objects/discussions>.

There is a poll on the naming convention you would prefer:
<https://github.com/LLyaudet/python-none-objects/discussions/2>.

And there is a discussion on various ideas to optimize the code with these constants:
<https://github.com/LLyaudet/python-none-objects/discussions/3>.

I think it would be better to have this kind of constants in the standard library.
If you think after reading everything, that it is indeed a good idea,
add a star to this repository to let the rest of the Python community know
that you would like to see such constant objects in the language :).
<https://github.com/LLyaudet/python-none-objects/>
If the project gains popularity, I'll try to propose it officially.

[pypi-version]: https://img.shields.io/pypi/v/python-none-objects.svg
[pypi]: https://pypi.org/project/python-none-objects/
