# Uast

Uast, User friendly Abstract Syntax Tree, is a wrapper of the python module AST. It provides an user friendly
interface to work with abstract syntax tree.

# Quickstart

To install Sequentium, use the following command:
```shell
pip install sequentium
```
Suppose that you want really to know what is contained in the script: `example/example_1.py`, but you don't want to
open it because it is too big and so complicated. You can just print a schema of its structure to have an ideas what is
going on:

````python
import uast

parsed_script = uast.parse(source='example/example_1.py')
print(parsed_script.schema())
````

# Quick start

Uast permits to past entire scripts or just Python syntax

## Parse a script

## Parse a Python Snippet

Suppose we have the following python snippet of code
```python
example = """
class User:

    def __init__(self, username: str, password: str):
        username = self.username
        password = self.password

    def check_password(self) -> bool:
        self.password == 'foo'
"""
```
We can parse it using the following
```python
import uast

parsed_code = uast.parse(example)
```

# Command line interface

