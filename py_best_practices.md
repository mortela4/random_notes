# Python 'Best Practices'
___

# Introduction

Why Python?
- Python is #1 most popular language (TIOBE ranking)
- Python user community is VERY large, inclusive, diverse - in gender(s), industries and geographically - and very active! (see [PyCon](https://pycon.org) ) 
- Python is used 'everywhere'
- Libraries for 'everything' has been written in Python, and is typically globally accessible via [PyPi](https://pypi.org)
- Python comes with 'batteries included' (a standard library covering most common tasks)
- binding to C/C++ code is (relatively) easy in Python
- Python is dynamically typed, and is object-oriented by design
- Python is an interpreted language; easy to experiment and prototype - no compilation required!

Famous Quote: "Python is the answer! ... What was the question?"

Why NOT Python???
- Python is slow (compared to C/C++, Rust) - but, even scientific SW has been written in JavaScript ...
- Python is dynamically typed, and is object-oriented by design (some holds this against Python ...)
- Python is an interpreted language ...

Famous Quote: “There are only two kinds of languages: the ones people complain about and the ones nobody uses.” - Bjarne Stroustrup


Python has become a general-purpose language on its own, 
while complementing others as a scripting-overlay mechanism.
It has successfully bridged programming/computer science and 
other academic research and technical professions.

Its use is at all 3 levels of the SW hierarchy:
1) As a scripting solution only (e.g. in CAD/CAE/CAM), often replacing embedded scripting based on Tcl and Lisp-dialects, or custom/omain-specific languages
2) As a middleware solution (e.g. YouTube has major parts written in Python), or framework integrating components in a low-level language (e.g. PyQt)
3) As a language to implement complete applications (although these might bind to C/C++ libraries for low-level I/O and/or performance) 
The last category includes projects like DropBox, and numerous web-frameworks like Django, Flask and FastAPI.


# Python core language usage

## In General

### Project Structure (opinionated)
Remember that first rule is to ensure that project can be picked up by other developer(s) 
with no prior knowledge of project. This depends heavily on good documentation, 
and (preferrably) automated CI/CD operations. If the latter is *not* in place, 
an option is to document carefully the manual steps involved, with description of all dependencies (or, 'assumptions').
 
Use a descriptive project name, and have a README(.md) under top-level directory 
with extensive description. Folder structure should be (but not 'shall' ...):
- "src" folder for code, multiple sub-folders below this (w. descriptive names) if complex project with several layers or similar
- "tests" folder for unit-tests
- "docs" for documentation, including auto-docs built with Sphinx, PDoc, Doxygen etc.

Optional folders:
- "assets" for non-code items that are *required* by application, e.g. icons, tokenfiles, datafiles etc.
- "config" folder may be relevant, especially if multiple run-time configurations apply 
- "build" for buildout-scripts, Makefiles, Ansible-config etc.etc. (especially important for mixed Python and C/C++ projects)
- "deploy" for deployment-scripts (e.g. bash, powerShell, or Python) and (if relevant) Dockerfiles

If no factual 'build'-step is required, "build" folder can be skipped leaving only "deploy" of the two. 
Likewise, if the project represents a package (to be e.g. installed via 'python -m pip <package name>'), 
the "deploy" folder may be redundant.


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

Follow [PEP 8](https://peps.python.org/pep-0008/#programming-recommendations), when sensible (which is ... always).

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

Use parentheses for line continuations (unless raw strings used).

```python
wiki = (
    "The Colt Python is a .357 Magnum caliber revolver formerly manufactured "
    "by Colt's Manufacturing Company of Hartford, Connecticut. It is sometimes "
    'referred to as a "Combat Magnum". It was first introduced in 1955, the '
    "same year as Smith & Wesson's M29 .44 Magnum."
)
```
Note the complementary use of ' and " here. 


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
        # Goes to the dashboard
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


### Yeoman
[Yeoman](https://yeoman.io) is another language-agnostic tool for project-generation.
Once again, it takes YAML for configuration.


### Other/standalone (not template-based)
The use of these are typically based on checkout of the template-project from GitHub, 
and then manual modification or running a setup-script afterwards (or both).
Some examples:
- https://github.com/Aaronontheweb/scaffold-py --> PyPi-packagename 'Scaffold' (simple fork of pyscaffold?)
- https://github.com/s3rius/FastAPI-template --> Complete Py-package based on cookiecutter. Feature-rich; choice of API-accessmethod, database etc.
- https://github.com/rednafi/fastapi-nano.git


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


### Yeoman-based
- https://github.com/vutran1710/YeomanPywork


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

## Strings (somewhat opinionated)
Use F-strings consistently for string formatting. 
There are very few exceptions to this rule ... (unless it is *required* to use Python2.7 ...).

Use UTF-8 unless working with ASCII-based protocols
(although 7-bit ASCII maps directly into UTF-8 ...).
Ensure editor/IDE is set up to use UTF-8.
**Note**: The '# -*- coding: latin-1 -*-' directive (or similar) that used to be placed on top of .py-files is no longer relevant!

Use double-quotes (") always, *NOT* single ('), unless it is meant to signify the use of a single character
(but beware, it is still a string! my_char = 'c' is equivalent to my_char = str('c').
Use triple double-quotes (""") around multi-line strings, and strings containing single or 
double double-quotes( e.g."""Dette er en "rar" streng ...""") or single-quotes.

Use raw strings for multi-line strings (*without* '\n') and JSON-data 
(or whatever data that use characters that otherwise would have to be escaped).
E.g.
```python
tst = r"""Dette
er 
en 
test ...
sjekk C:\Users\MortenL\Documents\python_best_practices"""

print(tst)

json_data = r"""{
    "my_key_a": 123,
    "my_key_b": "7Sense AS"
}"""

print(json_data)
```


## Operators

### Logic Operators
Use logic operators 'and', 'or' and 'not' in logic operations, NEVER arithmetic ones '+', '-' !!

Remember that '&', '|', '^' and '~' are BIT-WISE operators!

### NO-OP operation
The 'pass' keyword should be used to *explicitly* mark a code-path or block as NO-OP.
E.g:
```python
val = 'z'
if 'x' == val:
    do_x()
elif 'y' == val:
    do_y()
else:
    pass	# This shows INTENTION behind the code!
```


## Variables

Remember that *everything* in Python is a ***class***, even ints and floats!
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

Never use '[]'-type (i.e. 'indexed') access to collections, unless no other options exists!
Use built-in functions (like 'zip()', 'sum()' etc.) or collection-type's member functions 
(e.g. 'append()', 'sort()' etc.)

Example:
```python
tst = [11, 2, 3, 7, 4, 8]
tst.sort()
print(f"{tst}")
print(f"{sum(tst)}")
```

A notable exception may be string 'split()' method, given that number of elements in returned list 
is checked before doing 'sub_string = splitted[index]' type assignments.
Libraries exist for this type of operations, especially structured text like CSV, XML etc.


### Collection Comprehensions	
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
But, beware of side-effects! Also note that it results in a relatively costly (deep) copy of data. 
Changing the list above, does not affect the derived set.


### Collection Generators
The 'yield' keyword implies recursion.
This can accumulate a lot of data on stack, and - especially on small systems - eat up all available RAM.
Don't use it on small systems unless you *know* what you are up to!
However, for relatively moderate data-ranges where multiple values are generated (e.g. tuples), 
generators may be useful:
```python
def value_from_bits(num_bits: int = 0) -> int:
    """ Calculate max value for given number of bits in range 1-num_bits """
    bit_num = 0
    val = 2
    while num_bits > bit_num:
        bit_num = bit_num + 1
        # Accumulate value in collection = list-of-tuples:
        yield bit_num, val
        # Update value:
        val = 2 * val

values = value_from_bits(8)

for bit_no, val in values:
    print(f"A {bit_no}-bit word can represent a maximum value of {val}")
```        
        
As it is a stateful technique, it is important to keep in mind that arguments to generator functions 
remains the same for each iteration, it is just the function's *internal* variables that change.


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

Note that dataclasses can be directly converted to dictionaries via 'asdict()' function. 
E.g.
```python
import json
from dataclasses import dataclass, asdict

@dataclass
class ProtocolParser:
    header: str = None
    body: str = None
    footer: str = None

    def parse(self, data: str):
    	PROTO_DELIMITER = ':'
    	CRC_HEX_STR_SIZE = len("FFFF")	# 16-bit CRC appended to data as hex-string
    	fields = data.split(PROTO_DELIMITER)
    	if 2 == len(fields):
    	    self.header = fields[0]
    	    self.body = fields[1][:-CRC_HEX_STR_SIZE]
    	    self.footer = fields[1][-4]
    	else:
    		print("Data is NOT in conformance with protocol!")
    	# Return a dictionary:
    	return asdict(self)


proto = ProtocolParser()
parsed = proto.parse("PROTO.V4:dette er noe data\n7E8C")

print(f"Header: {parsed.get('header')}")
print(f"Body: {parsed.get('body')}")
print(f"Footer: {parsed.get('footer')}")

# Convert to JSON:
parsed_as_json = json.dumps(parsed)
print(parsed_as_json)
```


## Functions and Methods

Return 'None' *explicitly* if arguments or internal data (or both in combination) cannot compute valid result, 
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

Use *default argument values* for arguments that may be optional, or seldom have more than one, 'typical' value!

*No*

```python
def activate(trace_activity):    # Need to supply argument value in every call.
    if trace_activity:
        print("ACTIVATING!")     # But we do NOT want to execute this code except during debug!
    set_relays_on()
    set_power_on()
```

*Yes*

```python
def activate(trace_activity: bool = False):
    if trace_activity:
        print("ACTIVATING!")
    set_relays_on()
    set_power_on()
```


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
as it is harder to mix up the returned values:
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

Note that both (references to) functions and lambdas can be stored in any 
Python data-container class, like the built-in collections.

However, lambdas are more flexible e.g. when used with a dictionary 
for looking up a callable object from a string as key.
You cannot have arguments to a function in a dict() except constants - 
which means the function is evaluated and the return-value is used instead 
of the function as dictionary value. I.e.
```python
map_cmd_to_function = { "on": set_on(intensity), "off": set_off() }  # Won't work ...

map_cmd_to_function = { "on": (lambda intensity: set_on(intensity)), "off": set_off() }  # This works!
```

The example below maps a dictionary directly to class-properties 
(or, 'members' - as C#/Java-type 'properties' is not built-in to Python)
via the 'set_props_fromdict()' method of the class:
```python
class MyTestClass:

    def __init__(self, a_val: int, b_val: int, c_val: int):
        self._a_val = a_val
        self._b_val = b_val
        self._c_val = c_val
        self.attr_map = {'a': '_a_val', 'b': '_b_val', 'c': '_c_val'}

    def print_props_properly(self):
        for key in self.attr_map.keys():
            print(f"'{key}' = { getattr(self, self.attr_map.get(key))}")

    def set_props_fromdict(self, prop_set: dict):
        attr_setter = {
            'a': (lambda val:  setattr(self, '_a_val', val)), 
            'b': (lambda val:  setattr(self, '_b_val', val)), 
            'c': (lambda val:  setattr(self, '_c_val', val))
            }
        for name, val in prop_set.items():
            print(f"Setting '{name}' to value={val} ...")
            attr_setter[name](val)							# Equivalent to SWITCH-CASE block ...

# Construct a test-instance:
tst = MyTestClass(3, 5, 7)
tst.print_props_properly()
# Test using a complete dict(='config'):
config1 = {'a': 123, 'b': 357, 'c': 5790}
tst.set_props_fromdict(prop_set=config1)
tst.print_props_properly()
print(f"'a' = {tst._a_val}")    
# Test using shorter dict:
config2 = {'a': -666, 'b': -3}
tst.set_props_fromdict(prop_set=config2)
print(f"'a' = {tst._a_val}")
tst.print_props_properly()
```
Because JSON(-strings) can be converted directly into dictionaries in Python, 
the technique above can be utilized to modify objects via internal lookup using JSON as input data.


### Ordinary methods, class methods and staticmethods

TODO ...


### Decorators

Use existing set of decorators from the standard library's modules, 
or from external, utility packages. Do NOT re-invent the wheel!
(or phone, or fax ...)

However, for certain tasks you may need to implement your own.
Example:
```python
def setInterval(interval):
    """
    Decorator which runs the decorated function periodically, 
    and in a separate thread, with period='interval' value.
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            stopped = threading.Event()

            def loop(): # executed in another thread
                while not stopped.wait(interval): # until stopped
                    function(*args, **kwargs)     # standard way of wrapping functions

            t = threading.Thread(target=loop)
            t.daemon = True # stop if the program exits
            t.start()
            return stopped
        return wrapper
    return decorator


class BaseUnit(threading.Thread):
    def __init__(self, mach_data: MachineRuntimeData = None, config = def_config, log = None, interval = 0.0, debug = False):
        super().__init__()
        # Argumented properties:
        self.config = config
        self.log = log
        self.update_interval = interval
        self.debug = debug
        if mach_data:
            self.mach_data = mach_data
        else:
            self.mach_data = MachineRuntimeData()
        # Intrinsic properties:
        self.base_data = BaseData()
        self.timed_task = None
        self.is_active = True
    
    def wrap_timed_task(self):
        @setInterval(self.update_interval)      # Function 'update_presence()' is decorated with 'setInterval()' decorator.
        def update_presence(self):
            log.debug("Updating presence ...")
            api_post_data(api_endpoint=self.config.get_machine_presence_ep(), log=self.log, data=None, debug=self.debug, dry_run=True)
        self.timed_task = update_presence(self)

    def start_presence_update(self):
        log.info("Machine usage started - updating presence ...")
        if self.timed_task is None: 
            self.wrap_timed_task()

    def stop_presence_update(self):
        log.info("Stopping PRESENCE update...")
        self.timed_task.set()
        self.timed_task = None
        
```

    
## Classes

*Always* use 'CamelCase' in class name! E.g. 'class MyClass:'

'dataclass' objects should be used when only *class-internal* data is used, 
and serialization/de-serialization of class instances is relevant.
 
### Data Encapsulation in Classes
Note that 'private'-like class members are prefixed with a *double* underscore, 
but ***internally renamed*** with a underscore plus class-name to ensure access via 
same name directly is not possible!
E.g:
```python
class Testo:
    def __init__(self):
        self.__private_var = 123        # NOT accessible externally!
        self._non_private_var = 678     # Accessible externally.  
    def show(self):
        print(f"__private_var = {self.__private_var}")
    def show_aliased(self):
        print(f"__private_var aliased = {self._Testo__private_var}")

tst = Testo()

tst.show()
try:
    tst.__private_var = 345     # Won't work ...
except Exception:
    pass

setattr(tst, "__private_var", 666)
tst.show()                                          # Prints 123
print(f"""{getattr(tst, "__private_var")}""")       # Prints 666 --> a 'ghost' attribute has been created!

tst.show_aliased()                     # ???

setattr(tst, "_Testo__private_var", 345)
print(f"""{getattr(tst, "_Testo__private_var")}""")     # Finally - this works!
tst.show()

tst._Testo__private_var = 999                           # And this too ...
tst.show()
```

### Class Composition

Python supports multiple inheritance and class polymorphism.
Example:
```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

Albeit sometimes very useful, this may give rise to a bunch of problems.
As in other languages that supports multiple inheritance (like C++), 
the general rule is to use composition instead, but dataclasses with 
no logic may be an exception. 
Typical example:
```python
@dataclass
class Person:
    first_name: str
    second_name: str
    age: int

@dataclass Customer:
    person: Person
    user_name: str
    customer_id: int
```


## Modules

### Stand-alone, Functional Test of Modules
Apart from unit-testing, most every Python module can be functional-tested.
Also, it is often relevant to run a module as a script - i.e. 'stand-alone'.

The module to be run 'stand-alone' must have code like shown below at the end of the module-file:
via the 'set_props_fromdict()' method of the class:
```python
if __name__ == "__main__":
    # Insert code for stand-alone execution, or module functional test here.
    <... code ...>
```

This can be used even when the module is **NOT** supposed to be run stand-alone:
```python
if __name__ == "__main__":
    print("This module is supposed to be run from 'main' module - no standalone execution facilitated!")
    sys.exit(1)
```
This is useful to avoid misunderstandings and mis-use of module.


## Program Structure (also opinionated)

### Fail Early

There is no 'single-point-of-return' preference in Python.
Instead, it is encouraged to fail early - 
to enhance performance and maintain readability.
Example:
```python
import logging

COMMANDS = ["on", "off", "alarm", "shutdown"]

log = logging.getLogger()

def function_that_may_fail(cmd: str = None)
    if str is None:
        log.error("No command issued!")
        return
    if str not in COMMANDS:
        log.error(f"Invalid command '{cmd}'!")
    # Process command:
    ...
```
Note that final 'return' at end of function is *implicit* in Python.
It makes no difference to put a 'return' as last line in function, or not.
In both cases, the function will return a 'None'-object.


### Use a Configuration File

Always use a configuration file if 
- the number of *mandatory* command-line arguments have exceeded 7 (yes, seven ...)
- application settings are to be stored between sessions
- application run-time configuration is dynamic, and can optionally be set remotely (via webservice etc.)
- application is to be run as a server/daemon

Use 'whatever' format that suits you - just DON'T RE-INVENT THE FAX!
Therefore, use a configuration file format that is either obvious (like a Python-module with a Config-(data)class), 
or use a 'standard' format like JSON, YAML, XML etc. with built-in parsers or good Python-support from external packages. 

NOTE: JSON is preferred, as it is widely used, (relatively) readable, supports hierarchy and can easily be used over webservices.

Session-configs on a per-user basis is typically based on $HOME or %UserData% environment variables or similar.
Server configs (on Linux/UNIX) are often stored somewhere below "/etc", but applications should offer alternatives 
(like a command-line argument) to allow simplified testing (i.e. application *not* run by 'systemd' or similar).


### Handle Signals

Always install signal-handlers to ensure CLI-applications and server-applications can shut down gracefully!
Typically, this is achieved 
- either directly, by calling 'exit()' 
Example (a complex one ...):
```python
# Signal Handlers:
def panic_signal_handler(signal, frame):
    global run_flag
    warning("******** KILLING BASE UNIT PROCESS! (CTRL-Z received) ********\n")
    sys.exit(1)

def stop_signal_handler(signal, frame):
    global run_flag
    info("******** STOPPING BASE UNIT PROCESS ********\n")
    run_flag = False

def restart_signal_handler(signal, frame):
    warning("***************** Attempting ReSTART of application!! **********************")
    os.execv(sys.executable, ['python'] + sys.argv)   

def reboot_signal_handler(signal, frame):
    global run_flag
    global watchdog_start_on_exit_flag
    warning("***************** Attempting ReBOOT of entire system (i.e. OS reboots)!! **********************")
    run_flag = False                       # To stop the application first ...
    watchdog_start_on_exit_flag = True     # ... then, to flag watchdog should be started on app exit!


if __name__ == "__main__":
    host_platform_name = platform.machine()

    # No point in remote-debug if host=devhost(=x86):
    if app_config.get_remotedebug_config() and platform.machine() in ["aarch64", "arm"]:
        import debugpy
        # Std. remote-debug intro --> target hostname and port below must match debug-config settings (see: "launch.json") !
        # ================================================================================================================== 
        debugpy.listen(address = ('ccimx8x-sbc-pro.7sense.no', 3333))   # TODO: devhost(name or IP-address) and port should be specified in .INI-file!
        print("Waiting for debugger attach")
        debugpy.wait_for_client()
        print("Attached!")
        debugpy.breakpoint()
        print(f"OS: {sys.platform}")    # Start from breakpoint here ...

    # Handle Ctrl-C in console, or 'kill -5' (SIGINT) from other process, or 'kill -15' (SIGTERM) from other process:
    signal.signal(signal.SIGINT, stop_signal_handler)
    signal.signal(signal.SIGTERM, stop_signal_handler)
    signal.signal(signal.SIGTSTP, stop_signal_handler)      # Ctrl-S --> signal(20). NOTE: SIGSTOP(signal(20)) cannot be caught!
    signal.signal(signal.SIGQUIT, panic_signal_handler)      # Ctrl-Z --> signal(3) 

    # Handle terminate-and-restart event:
    signal.signal(signal.SIGUSR1, restart_signal_handler)    # NOTE: ignore 'problem'-warnings from VSCode when running on Windows rgd. missing 'SIGUSR1' member! (non-existent on non-POSIX)
    # Handle terminate-and-reboot event:
    signal.signal(signal.SIGUSR2, reboot_signal_handler)   # NOTE: ignore 'problem'-warnings from VSCode when running on Windows rgd. missing 'SIGUSR2' member! (non-existent on non-POSIX)

    while run_flag:
        if threads_alive_and_well(monitored_threads):
            time.sleep(THREAD_ALIVE_CHECK_INTERVAL)
        else:
            break
    
    # Clean up (i.e. 'graceful' shutdown):
    if mqttClient.is_alive():
        # Invalidate 'machine'-field in MQTTclient class instance:
        mqttClient.machine = None
        mqttClient.join()
        info("Terminated MQTT-client thread")
    else:
        warning("MQTTclient-thread not active - cannot join!")
    if machine.is_alive():
        machine.join()
        info("Terminated machine-thread")
    else:
        warning("Machine-thread not active - cannot join!")
    
    info("Terminated all threads - exiting ...\n\n")

    # Last Will & Testament - application AND (on target HW) system will be REBORN if reboot-flag set:
    if watchdog_start_on_exit_flag:
        if host_platform_name in ["aarch64", "arm"]:
            status = os.system(WATCHDOG_START_CMD)                # NOTE: from here on, it will last N seconds (default N=15) before system reboots - no further sync'ing of open files etc!
            if status == 0:
                warning("Watchdog has been started - system will reboot in 15 seconds!")
            else:
                error("Failed to start watchdog - system will NOT be rebooted!")
        else:
            warning("System reboot is NO-OP on x86 devhost - restarting app via 'execv()' system call instead!")
            os.execv(sys.executable, ['python3'] + sys.argv)
    else:
        sys.exit(0)
        
```

In short, do *NOT* trust the system to do 'automatic release' of used resources, and cleanup of dangling file-pointers etc.
CLI-applications should be able to terminate via Ctrl-C, and NOT relay on using 'kill -9 <PID>' or similar!


## Packages

The number of Python packages are endless.
This section barely scratches the surface, 
only giving advice for general usage - or pointing to the most used ones.
See also:
[Awesome Python](https://awesome-python.com/)


### Prefer use of Standard Library over external packages
Use the SL to the full extent, use external packages only when you have *very specific requirements*.
E.g. the 'logging' module has lots of good alternatives, but you rarely need those unless you 
work with frameworks that require them, or advocate the use of such.

Note that many external packages have made it into the SL, either because they were 'de-facto' 
standard, or were the first to offer dearly needed functionality.
Installing external packages will anyway 'pollute' your Python installation - 
at least if you install them with 'sudo' on Linux ...
(therefore, use only 'python -m pip install <packagename>' for development).


### Prefer cross-platform, 'native' packages
If multiple choices exist w. regard to packages for a given functionality, 
use the one which is
- cross-platform
- OS-agnostic, so that API is uniform between platforms 
- package project (or package vendor) offer bindings to multiple languages (e.g. C/C++, Rust, JavaScript, C#, Java, Go) in addition to Python
- use direct bindings to native (C/C++ -)code, preferrably distributed with the package (not relying on naive loading of external DLLs)

The last item means stay away from packages that loads external DLLs,
or opens external applications if you have a choice ...

A package like 'pyserial' is an example of a Python package that meet all requirements above, 
and is the natural (or only ...) choice for any serial-port access whatever platform is in question (WinXX, Linux, MacOS, Android).

A project developing a given Python package, that also maintain bindings for other languages, 
may be a better choice than a Python-only project with same functionality.
This is simply because of added flexibility and multiple choices - 
it can be relevant to move a project from Python to e.g. C/C++ because of more low-level control or higher performance required.


### Cross-platform Utilities
The built-in 'os' and 'sys' packages from the standard library are OK for simpler tasks.
However, they do handle subtle, cross-platform issues a bit inadequate.

Use the 'platform' package for cross-platform, OS-related functionality, 
e.g. making code sections platform-dependent:
```python
import platform

if __name__ == "__main__":
    # Application can only run on ARM-platform.
    if platform.machine() in ["aarch64", "arm"]:
    	do_hw_dependent_stuff()
    else:
    	print(f"FATAL: cannot execute application on machine={platform.machine()}!! Bailing out ...")
    	sys.exit(1)
```

For managing and monitoring process execution, the 'psutil' package is recommended. 


### Common Utilities
- 'pathlib' package for file and folder manipulations
- 'datetime' for *basic* date and time operations, while 'pendulum', 'arrow', and 'delorean' can be considered for complex manipulations! 
- 'json' package for JSON manipulations (although lots of good alternatives exist)

Example:
```python
import json

json_data = r"""{"name": "distance", "unit": "meters", "value": 123}"""

dict_from_json = json.loads(json_data)		# Produces a dictionary.

print(dict_from_json)               		# This should LOOK like a dictionary (which it is) ...

name = dict_from_json.get("name")
unit = dict_from_json.get("unit")
value = dict_from_json.get("value")
json_field_values = (name, unit, value)

if None not in json_field_values:
    print(f"{name} in {unit}: {value}")
else:
    print("JSON data error - at least one field missing")   # NOTE: might be appropriate to thow exception after this ...
```


### Web Utilities
- 'requests' for HTTP requests --> lacks async requests support (may be fixed in recent versions?)
- 'urllib3' is a good replacement, or complement (depends)
- 'httpx' if you need async requests --> has a CLI available which is most useful (a la CURL)

In terms of web-services frameworks, there is a long list which includes prominent projects like 
- Django
- Flask
- FastAPI
- TurboGears


### Database Access
- 'sqlalchemy', or libraries that bundles it. 
This is a project which encompasses a lot of sub-projects for 
all kinds of DB-tasks, like 'alembic' for DB-migrations.


### Scientific Computing
This is where 'Python is King' is *not* an overstatement!
Python is the dominant language in
- AI/ML(-pipelines)
- VR/AR
- Computer Graphics pipelines and composition (Blender, Maya +++)
- Experimental Physics, e.g. robotics experimentation (ROS2 +++)
- Experimental Chemistry and biomolecular research  

For most generic, numerical computation tasks, NumPy is the go-to library.
It is even bundled in many popular Python distributions (Anaconda, ScientificPython, PytonXYZ +++).
It makes computations on vectors and matrices as simple as using scalars:
```python
import numpy as np


def triple_it(values: float) -> float:
    tripled = 3 * values            	# NumPy has overloads for all arithmetic operands relevant for vectors.
    return tripled


in_val = np.linspace(0, 10, 20)     # Yields 20 values, with distance = 10/20 = 0.5 between
print(in_val)                       # Conceptually a list - but it's a vector ...

result = triple_it(values=in_val)
print(result)                       # Result is a vector too ...

for val in result:
    print(val)

result = triple_it(values=1.23)     # Same function works for scalars also!
print(result)
for val in result:                  # But iteration will fail, as returned value is a scalar ...
    print(val)
```

The excellent [SciPy](https://scipy.org/) package (or rather collection of packages) 
is a superset of NumPy. It is most useful for complex transforms, and polynomial integration and derivation.

[MatPlotLib](https://matplotlib.org/) is the obvious choice for scientific plotting, 
but in recent years [Dash](https://plotly.com/dash/) has moved in - especially for web-based plots (i.e. 'dashboards').

### HW Access
- 'pyusb' for direct, low-level USB-access (cross-platform)
- 'pyblue'(cross-platform) and 'pybluez'(Linux) for Bluetooth/BLE low-level access
- 'pyserial' for serial ports (including virtual ones over e.g. USB) configguration and I/O 
- 'mraa' for low-level, embedded I/O (SPI, I2C, GPIO) on a range of platforms (and languages), 
with accompanying 'upm' library for a range of sensor-drivers. See [UPM project](https://upm.mraa.io/)

Note that these packages are often not cross-platform, typically just supporting one, single OS/platform.
This is due to HW-access being treated very differently on different platforms.

### Networking
TODO - if I care ... ;-)

There are simply too many to mention, 
and the standard library has a lot in place for e.g. simple TCP/UPD clients and servers.

___


# Development Tools Usage

### Prototyping and POC-code

Use the Python shell/terminal for simple experiments, instead of writing small, non-reuseable modules.
Online REPL-tools (even incorporating debugger) can also be used, like [OnlineGDB](https://www.onlinegdb.com/)


## Debug

### Remote Debug

This requires the debug server (or, 'agent') - typically based on 'pdb' debugmodule - to be installed on remote target.
VSCode plays nicely with the 'debugpy' package, and offer a near-transparent debug connection over the 'standard' PDB protocol.

The following modifications are required on target in order to support remote debug with VSCode debugger as client:
- the 'debugpy' package must be installed on target 
- A hook-up point must be inserted in the code - immediately after top-level entry point 
(typically 'if __name__ == "__main__":' line) - to start up the server and make it wait for a remote client connection.
Example:
```python
if __name__ == "__main__":
    host_platform_name = platform.machine()

    # No point in remote-debug if host=devhost(=x86):
    if app_config.get_remotedebug_config() and platform.machine() in ["aarch64", "arm"]:
        import debugpy
        # Std. remote-debug intro --> target hostname and port below must match debug-config settings (see: "launch.json") !
        # ================================================================================================================== 
        debugpy.listen(address = ('ccimx8x-sbc-pro.7sense.no', 3333))   # TODO: devhost(name or IP-address) and port should be specified in config-file!
        print("Waiting for debugger attach")
        debugpy.wait_for_client()
        print("Attached!")
        debugpy.breakpoint()
        print(f"OS: {sys.platform}")    # Start from breakpoint here ...

    <rest of your top-level module or script's code ...>
    
```

In VSCode, remote debug client-access is set up in the "launch,json"-file (found under "/.vscode" folder in project) 
in the following way:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Remote Attach",
            "type": "python",
            "request": "attach",
            "connect": {
                "host": "ccimx8x-sbc-pro",
                "port": 3333
            },
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}/naeva_base/base_unit_firestore_client",
                    "remoteRoot": "/usr/local/NAEVA/base_unit_firestore_client"
                }
            ]
        },
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```

The 'Python: Remote Attach' configuration sets up 
- the remote-servers host-name(or, IP-address)
- the TCP port-number
- the mapping between source-location on devhost and where the (identical) Python-code is found on remote target

The last item is ***very*** important in order to make debug work!
It implies that Python code on both machines must be identical/in-sync, 
which can be achieved in multiple ways (e.g. NFS-mount of devhost's source-dir).
It is possible to set up a pre-debug step in VSCode (and other tools), 
where source-dir is updated via 'rsync' or SSH.

 
# Closing Notes

## Use Generic 'Best Practices'

Use patterns and workflows that applies to *all* programming languages as 'best practices'!
Those are:
- a sound VCS system that allows distributed work and co-operation
- integrated with a CI/CD system for complete 'develop-build-test-integrate-deploy' pipeline
- continuous feedback from development (e.g. from CI/CD tool, or issue-tracker tool)
- continuous feedback from production (e.g. logs via syslog-daemon, or higher-level monitoring tools like 'OpenTelemetry', Nagios etc.)


## Follow DRY Principle

**Do NOT Repeat Yourself!!!** 
A one-off solution to a common problem, often encountered in many applications, is a wasted one!
First, investigate if the standard library collection can offer a solution, then - 
search the 'net for a library offering the required functionality. Only when you do *not* find 
any other solution, consider making a library yourself. And - do make it into a library!
If you probably need to use it later in some other project, the code should 
- be made 'generic' and flexible, i.e. not tightly integrated with the application
- be made fit for multiple use-cases
- be made standalone
- be equipped with documentation for use (as it might be picked up again much later ...)
- be stored in a separate repository, or along with other modules in a 'utilities'-repository

One example is retrying actions, e.g. re-establishing a connection to a server or similar a given number of times.
This involves the typical pattern of executing an action in a loop, 
breaking out if the action succeeds or taking some other action if the loop runs to completion (i.e. tries failed).
Excellent libraries exist for this, where some takes a function as argument (or, is decorator thereof ...) along 
with integer N for number of attempts. But in many scenarios, typical libraries involved have the same functionality built-in.
Example:
```python
import urllib3

from urllib3.util import Retry
from urllib3.exceptions import MaxRetryError


GET_ENDPOINT = "http://www.problemserver.com/maybe/responsive"
NUM_RETRIES = 3							# Yes, very typical number ...


http = urllib3.PoolManager()

# Set up 'Retry' to raise an exception if HTTP-status returned NUM_RETRIES times is in the range 500-599 (covers multiple types of connection failures):
retry = Retry(NUM_RETRIES, raise_on_status=True, status_forcelist=range(500, 600))

try:
    # If successful, 'result' will be usable as a GET-request object (HTTP status, header & body).
    result = http.request("GET", GET_ENDPOINT, retries=retry)	
except MaxRetryError as retry_err:
    # Else, an exception is raised - and we can log error:
    logger.error(f"GET-request to {GET_ENDPOINT} failed! Reason: {retry_err.reason}")
```




