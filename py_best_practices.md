# Python 'Best Practices'
___

# Python core language usage

## In General

### Values

- "Build tools for others that you want to be built for you." - Kenneth Reitz
- "Simplicity is alway better than functionality." - Pieter Hintjens
- "Fit the 90% use-case. Ignore the nay sayers." - Kenneth Reitz
- "Beautiful is better than ugly." - [PEP 20][]
- Build for open source (even for closed source projects).

### General Development Guidelines

- "Explicit is better than implicit" - [PEP 20][]
- "Readability counts." - [PEP 20][]
- "Anybody can fix anything." - [Khan Academy Development Docs][]
- Fix each [broken window](http://www.artima.com/intv/fixit2.html) (bad design, wrong decision, or poor code) *as soon as it is discovered*.
- "Now is better than never." - [PEP 20][]
- Test ruthlessly. Write docs for new features.
- Even more important that Test-Driven Development--*Human-Driven Development*
- These guidelines may--and probably will--change.

## In Particular

### Style

Follow [PEP 8][], when sensible.

#### Naming

- Variables, functions, methods, packages, modules
    - `lower_case_with_underscores`
- Classes and Exceptions
    - `CapWords`
- Protected methods and internal functions
    - `_single_leading_underscore(self, ...)`
- Private methods
    - `__double_leading_underscore(self, ...)`
- Constants
    - `ALL_CAPS_WITH_UNDERSCORES`

###### General Naming Guidelines 

Avoid one-letter variables (esp. `l`, `O`, `I`). 

*Exception*: In very short blocks, when the meaning is clearly visible from the immediate context

**Fine**
```python
for e in elements:
    e.mutate()
```

Avoid redundant labeling.

**Yes**
```python
import audio

core = audio.Core()
controller = audio.Controller()
```

**No**
```python
import audio

core = audio.AudioCore()
controller = audio.AudioController()
```

Prefer "reverse notation".

**Yes**
```python
elements = ...
elements_active = ...
elements_defunct = ...
```

**No**
```python
elements = ...
active_elements = ...
defunct_elements ...
```

Avoid getter and setter methods.

**Yes**
```python
person.age = 42
```

**No**
```python
person.set_age(42)
```

#### Indentation

Use 4 spaces--never tabs. Enough said.

#### Imports

Import entire modules instead of individual symbols within a module. For example, for a top-level module `canteen` that has a file `canteen/sessions.py`,

**Yes**

```python
import canteen
import canteen.sessions
from canteen import sessions
```

**No**

```python
from canteen import get_user  # Symbol from canteen/__init__.py
from canteen.sessions import get_session  # Symbol from canteen/sessions.py
```

*Exception*: For third-party code where documentation explicitly says to import individual symbols.

*Rationale*: Avoids circular imports. See [here](https://sites.google.com/a/khanacademy.org/forge/for-developers/styleguide/python#TOC-Imports).

Put all imports at the top of the page with three sections, each separated by a blank line, in this order:

1. System imports
2. Third-party imports
3. Local source tree imports

*Rationale*: Makes it clear where each module is coming from.

#### Documentation

Follow [PEP 257][]'s docstring guidelines. [reStructured Text](http://docutils.sourceforge.net/docs/user/rst/quickref.html) and [Sphinx](http://sphinx-doc.org/) can help to enforce these standards.

Use one-line docstrings for obvious functions.

```python
"""Return the pathname of ``foo``."""
```

Multiline docstrings should include

- Summary line
- Use case, if appropriate
- Args
- Return type and semantics, unless ``None`` is returned

```python
"""Train a model to classify Foos and Bars.

Usage::

    >>> import klassify
    >>> data = [("green", "foo"), ("orange", "bar")]
    >>> classifier = klassify.train(data)

:param train_data: A list of tuples of the form ``(color, label)``.
:rtype: A :class:`Classifier <Classifier>`
"""
```

Notes

- Use action words ("Return") rather than descriptions ("Returns").
- Document `__init__` methods in the docstring for the class.

```python
class Person(object):
    """A simple representation of a human being.

    :param name: A string, the person's name.
    :param age: An int, the person's age.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

##### On comments

Use them sparingly. Prefer code readability to writing a lot of comments. Often, small methods are more effective than comments.

*No*

```python
# If the sign is a stop sign
if sign.color == 'red' and sign.sides == 8:
    stop()
```

*Yes*

```python
def is_stop_sign(sign):
    return sign.color == 'red' and sign.sides == 8

if is_stop_sign(sign):
    stop()
```

When you do write comments, remember: "Strunk and White apply." - [PEP 8][]

#### Line lengths

Don't stress over it. 80-100 characters is fine.

Use parentheses for line continuations.

```python
wiki = (
    "The Colt Python is a .357 Magnum caliber revolver formerly manufactured "
    "by Colt's Manufacturing Company of Hartford, Connecticut. It is sometimes "
    'referred to as a "Combat Magnum". It was first introduced in 1955, the '
    "same year as Smith & Wesson's M29 .44 Magnum."
)
```

### Testing

Strive for 100% code coverage, but don't get obsess over the coverage score.

#### General testing guidelines

- Use long, descriptive names. This often obviates the need for doctrings in test methods.
- Tests should be isolated. Don't interact with a real database or network. Use a separate test database that gets torn down or use mock objects.
- Prefer [factories](https://github.com/rbarrois/factory_boy) to fixtures.
- Never let incomplete tests pass, else you run the risk of forgetting about them. Instead, add a placeholder like `assert False, "TODO: finish me"`.

#### Unit Tests

- Focus on one tiny bit of functionality.
- Should be fast, but a slow test is better than no test.
- It often makes sense to have one testcase class for a single class or model.

```python
import unittest
import factories

class PersonTest(unittest.TestCase):
    def setUp(self):
        self.person = factories.PersonFactory()

    def test_has_age_in_dog_years(self):
        self.assertEqual(self.person.dog_years, self.person.age / 7)
```

#### Functional Tests

Functional tests are higher level tests that are closer to how an end-user would interact with your application. They are typically used for web and GUI applications.

- Write tests as scenarios. Testcase and test method names should read like a scenario description.
- Use comments to write out stories, *before writing the test code*.

```python
import unittest

class TestAUser(unittest.TestCase):

    def test_can_write_a_blog_post(self):
        # Goes to the her dashboard
        ...
        # Clicks "New Post"
        ...
        # Fills out the post form
        ...
        # Clicks "Submit"
        ...
        # Can see the new post
        ...
```

Notice how the testcase and test method read together like "Test A User can write a blog post".


## References
See also:
- [PEP 20 (The Zen of Python)][PEP 20]
- [PEP 8 (Style Guide for Python)][PEP 8]
- [The Hitchiker's Guide to Python][python-guide]
- [Khan Academy Development Docs][]
- [Python Best Practice Patterns][]
- [Pythonic Sensibilities][]
- [The Pragmatic Programmer][]
- and many other bits and bytes

[Pythonic Sensibilities]: http://www.nilunder.com/blog/2013/08/03/pythonic-sensibilities/
[Python Best Practice Patterns]: http://youtu.be/GZNUfkVIHAY
[python-guide]: http://docs.python-guide.org/en/latest/
[PEP 20]: http://www.python.org/dev/peps/pep-0020/
[PEP 257]: http://www.python.org/dev/peps/pep-0257/
[PEP 8]: http://www.python.org/dev/peps/pep-0008/
[Khan Academy Development Docs]: https://sites.google.com/a/khanacademy.org/forge/for-developers
[The Pragmatic Programmer]: http://www.amazon.com/The-Pragmatic-Programmer-Journeyman-Master/dp/020161622X/ref=sr_1_1?ie=UTF8&qid=1381886835&sr=8-1&key
___

# Python project-generators

## Generator Scripts
These are scripts (or full-fledged applications) that set up project structure (folders), 
and populates them with a minimal setup - often including skeleton source-file(s) and example documentation.
Typically, packaging setup for publishing the project as a package (to PyPi or similar) is supplied.

### cookiecutter
By far the most popular tool. Also popular for creating JavaScript/TypeScript and C/C++ projects.
Usage:
```sh
cookiecutter <GitHub URL>
```

The template is specified in a "cookiecutter.json" file (i.e. JSON format).
 

### PyScaffold
Probably the second most popular tool for project generation.
Does not refer to GitHub repositories for templates, 
but use a combination of "setup.cfg"-file (using 'setuptools' syntax), 
.yml-files(YAML-markup, for steps/pipeline-setup) and/or commandline-arguments 
for project generation.

Usage:
```sh
putup <project name>
```

or with interactive editing of arguments to 'putup':
```sh
putup -i <project name>
```

As such, 'PyScaffold' is a primarily *generic* tool for users that require high degree of customization.
For fast-track solutions, it bundles the following modules:
- pyscaffold.extensions --> for typical CI/CD pipeline setup, like GitHub-actions etc.
- pyscaffold.templates --> for composing and load/store of templates(.template-files ends up as "setup.cfg") 


### Other/standalone (not template-based)
- https://github.com/Aaronontheweb/scaffold-py --> PyPi-packagename 'Scaffold' (simple fork of pyscaffold?)
- https://github.com/s3rius/FastAPI-template --> Complete Py-package based on cookiecutter. Feature-rich; choice of API-accessmethod, database etc.

## Generator Templates

### CookieCutter-based
The full list of *published* templates (on GitHub) for cookiecutter is at:
http://cookiecutter-templates.sebastianruml.name/

Simple:
- cookiecutter https://github.com/luphord/cookiecutter-pyscript.git --> single-file Py-script
- cookiecutter https://github.com/luphord/cookiecutter-pyscript --> same
- cookiecutter https://github.com/dataloudlabs/cookiecutter-pyscript --> w. basic test-capability

Stand-alone apps:
- cookiecutter https://github.com/benwebber/cookiecutter-standalone --> flexible, can generate Py-wheel, EXE or RPM (best for CLI-tools)
- cookiecutter https://github.com/William-Lake/ScriptToExeCC.git --> generates Win-EXE using GitHub-action='pyinstaller-windows'

WebDev-focused:
- https://github.com/tiangolo/full-stack --> choice of Flask or FastAPI as back-end server
- https://github.com/BrentGruber/fastapi-mysql-cookiecutter
- https://github.com/nhjeon/cookiecutter-fastapi-mysql
- https://github.com/rwinte/cookiecutter-fastapi-sqlite
- https://github.com/jonatasoli/fastapi-template-cookiecutter

Generic:
- https://github.com/cjolowicz/cookiecutter-hypermodern-python --> with ALL bells & whistles ...


### Py-Scaffold based
- https://github.com/SarthakJariwala/PyScaffold-Interactive


## NOTES

### Dockerfiles
Most of the template-based solutions (at least for 'cookiecutter') has a Dockerfile option for deployment. 
A basic TOML (or YAML) docker-compose specification file is typically given in combination with a Dockerfile, 
unless a Dockerfile-only basic setup is given.

Use 'docker ps' after startup of Dockerfile to see details like ID, hostname and assigned IP-address.

### TAR-archives
Rarely used anymore. A Python-sourcetree is expanded from a tarball into a in-memory virtual filesystem.
The application then runs from there, and can refer to files both in this virtual filesystem as well as others.

### PyInstaller-deployment


___

# Pythonic Code

General rule is to follow PEP8 rules - 
which are built into tools like PyCharm, Che/Theia and VSCode, 
and used by linters/auto-formatters like Flake and Black.

## Operators

Use logic operators 'and', 'or' and 'not' in logic operations, never '+', '-' !!

Remember that '&', '|', '^' and '~' are BIT-WISE operators!


## Variables

Remember that *everything* in Python is a **class**, even ints and floats!
And, as the 'Zen of Python' dictates - explicit is better than implicit.
It is therefore better to use:
```python
val = float(123)
```
than:
```python
val = 123
```
which ends up as an integer first, then e.g. val = val / 7 makes it (silently) end up as a float.

### Temporary and intermediate variables (or, 'helper variables')
Should be used at the very minimum!

Do not use loop-counters or increment/decrement-variables in iterations if it can be avoided. 
E.g:

*No*

```python
word_list = ["first", "second", "third"]
i = 0
for word in word_list:
    print(f"Word number {i} is '{word}'")
	i += 1
```

*Yes*

```python
word_list = ["first", "second", "third"]
for i, word in enumerate(word_list):
    print(f"Word number {i} is '{word}'")
```

### Context Managers
Use a context manager whenever you want to restrict usage of a resource in a 'logical' way.
This is especially important when doing I/O, and it is mandatory to keep the OS or HW resource 
opened only during the actual data commit or retrieval.
E.g:
```python
with open(filename, 'w') as outfile:
        outfile.write(some_data)
```
Typical usage is file and database I/O.


## Iterators and Collections

Python's built-in datatypes list, set, dict -
as well as the popular (NumPy-)arrays, queue and fifo datatypes from libraries -
are examples of *collections*.

Iterating over them are straightforward and intuitive (maybe except from dict() datatype):
```python
a_simple_set = ('a', 'b', 'c')
for ch in a_simple_set:
    print(ch)
```
	
Prefer *direct* collection-object operations over loops. 
Especially for up-front generation of values.
E.g:
```python
even_numbers = [x for x in range(20) if 0 == (x % 2)]
odd_numbers = [x for x in range(20) if 1 == (x % 2)]

print(even_numbers)
print(odd_numbers)
```
Lots of examples available - just google 'python <collection object type> comprehensions' ...

Note that collections can be derived from other collections. 
E.g:
```python
a_list = range(1, 4)
a_derived_set = set(a_list)
for val in a_derived_set:
    print(val)
```
But, beware of side-effects! Also note that it results in a (deep) copy of data. 
Changing the list above, does not affect the derived set.

### Dictionaries and its siblings 
Dictionaries are a bit different from lists, (NumPy-)arrays, sets, queues and fifos -
but still they are a collection of data, and can be iterated over.
The simplest form of iteration will return **keys** only:
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(f"Dictionary key: {key}")  
```
	
Often it is necessary to iterate over complete dictionary, and operate on both keys and values:
dict()-type's built-in 'items()' method is used for retrieving a Key,Value-pair as a tuple() object.
```python
for key, value in my_dict.items():
    print(f"Key = {key}, value = {value}")
```

The above iteration is intrinsically safe - as every element in an *existing* dictionary 
is guaranteed to have both a key and value.
However, when attempting to retrieve values using a key for which there is no guarantee 
that exists in a given dictionary, one should use the 'get' method and check value - 
*NOT* the '[<key>]' operator!
E.g:

*No*
```python
val = my_dict[my_key]	# Can throw 'KeyError'-exception --> must use try-except block!
```


## Functions and Methods

Return 'None' *explicitly* if arguments or internal data cannot compute valid result, 
**and** return value is allowed to be polyvalue.
Remember that any code-paths that returns nothing, will result in 'None' returned anyway!

Else, throwing exception is acceptable. Caller site must be prepared for both cases!

### Arguments
Use *named arguments*. E.g:

*No*

```python
def linear_func(a, b, x):
    return a*x + b

x = 7
a = 1.23
b = 4.567
linear_func(a, b, x)
```

*Yes*

```python
x = 7
a = 1.23
b = 4.567
linear_func(a=a, b=b, x=x)
```

Or, use a dataclass as argument:
```python
from dataclasses import dataclass   # Part of standard library (Py=3.x)

@dataclass
class LinearFuncParams:
    a: float
    b: float
    x: float

def linear_func(params: LinearFuncParams) -> float:
    if params is not instanceof(LinearFuncParams):
        throw ValueError
    #
    a = params.a
    b = params.b
    x = params.x
    #
    return a*x + b
 
func_params = LinearFuncParams(a=1.23, b=4.567, x=7)
linear_func(func_params)
```

But - it is sometimes just as easy to use (data-)class itself:
```python
import numpy as np

@dataclass
class LinearFunc:
    a: float
    b: float
    x: float

    def calculate(self) -> float:
        return a*x + b
 
lin_func = LinearFuncParams(a=1.23, b=4.567, x=np.linspace(0, 10, 0.1))
result_array = lin_func.calculate()
```

But remember, apart from 'x', 'y' and 'z' - arguments (and variables) should **not** be single-character!


### Scoped Functions
If a function is used in one, single other function - 
it can be embedded within the calling function itself.
Example:
```python
def cube(width=0, length=0, height=0, op='none'):
    #
    def area():
        return width * length
    def volume():
        return height * area()
    # Logic:
    if 'area' == op :
        val = area()
    elif 'volume' == op:
        val = volume()
    else:
        val = None
    return val 


print(f"{cube(2, 3, 0, 'area')}")       # Prints '6'
print(f"{cube(2, 3, 4, 'volume')}")     # Prints '24'
print(f"{cube(2, 3, 0)}")               # Prints 'None'
```
Typically, this is mostly relevant when the scoped function is used multiple times within another function.


### Return Values
Python can easily return multiple values from a function or method:
```python
def cube(width=0, length=0, height=0):
    #
    def area():
        return width * length
    def volume():
        return height * area()
    # 
    return area(), volume() 

area, volume = cube(2, 3, 4) 
print(f"Cube area = {area}, and volume = {volume}")       
```

However, using a *named tuple* is better, 
as it is harder to mix the returned values:
```python
from collections import namedtuple

CubeReturnType = namedtuple("CubeReturnType", "area volume")

def cube(width=0, length=0, height=0):
    #
    def area():
        return width * length
    def volume():
        return height * area()
    # 
	ret_val = CubeReturnType(area=area(), volume=volume())
    return ret_val

results = cube(2, 3, 4) 
print(f"Cube area = {results.area}, and volume = {results.volume}")       
```

### Lambdas
Special case of function, created with 'lambda' keyword, often referred to as 'anonymous function'.
Can be useful for SWITCH-CASE type constructs, and iterations with simple operations.
E.g:
```python
def cube(width=0, length=0, height=0, op='none'):
	# Functions:
	area = lambda w, l: w * l
	volume = lambda w, l, h: w * l * h
	# Logic:
    if 'area' == op :
        val = area(width, length)
    elif 'volume' == op:
        val = volume(width, length, height)
    else:
        val = None
    return val 


print(f"{cube(2, 3, 0, 'area')}")       # Prints '6'
print(f"{cube(2, 3, 4, 'volume')}")     # Prints '24'
print(f"{cube(2, 3, 0)}")               # Prints 'None'
```


### Ordinary methods, class methods and staticmethods



## Classes

*Always* use 'CamelCase' in class name! E.g. 'class MyClass:'

Use 'dataclass' objects when only *class-internal* data is used, 
and serialization/de-serialization of class instances is relevant.
 

