## LUA TO PYTHON

[![DOI](https://zenodo.org/badge/533039981.svg)](https://zenodo.org/badge/latestdoi/533039981)

Welcome to Group 44 repository for 2022 fall Software Engineering homework 2 & 3!

This homework aims to port a program written in Lua (source) to Python while using good software engineering practices. The program reads a CSV file and generate summaries of columns (medians and standard deviation for numerics; mode and entropy for symbolic columns). This intends to read a CSV file and generate summaries of both numeric and symbolic columns, that is, medians and standard deviation for numeric columns, and mode and entropy for symbolic columns.

## TEST CASES

[![Python package](https://github.com/VrushankiPatel/sehw2/actions/workflows/python-package.yml/badge.svg)](https://github.com/VrushankiPatel/sehw2/actions/workflows/python-package.yml)

Test cases are called by using pytest in python. Here the test cases in the test folder checks the coverage for the code written. Test cases work by calling all the functions in the code folder and checking if the input given matches with the result. If the condition is fulfilled than the test case is passed or else it is failed.

## Installation

Pytest is available for Python version 3.7+ and can be installed through terminal by pip command.

```python
pip install -U pytest
```
To check the version installed run the following command.

```python
pytest --version
```

Note: For local setup it is recommended to add git hooks to run tests after each commit. To copy add links to .git/hooks, run the following command.
```shell script
ln -s -f git_hooks/post-commit .git/hooks/post-commit
```

## USAGE

The following is the example test case written in python using the pytest.

```python
def decrement(x):
    return x - 1

def test_case1():
    assert decrement(3) == 2
 ```
Then the results are as follows:-

![WhatsApp Image 2022-09-14 at 10 52 29 AM](https://user-images.githubusercontent.com/111928135/190189229-f867cebd-4dde-479f-9dd2-9da318ae2dab.jpeg)

## COVERAGE

![coverage](https://user-images.githubusercontent.com/111928135/191138865-497f52df-58f8-4142-8b30-9b4155690198.png)


## CONTRIBUTORS:-

Nirav Shah,
Vishwa Gandhi, 
Vrushanki Patel,
Pradyumna Khawas,
Priya Saroj

## LICENSE
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
 


