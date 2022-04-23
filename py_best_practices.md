# Python 'Best Practices'
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
https://github.com/Aaronontheweb/scaffold-py --> PyPi-packagename 'Scaffold' (simple fork of pyscaffold?)
https://github.com/s3rius/FastAPI-template --> Complete Py-package based on cookiecutter. Feature-rich; choice of API-accessmethod, database etc.

## Generator Templates

### CookieCutter-based
The full list of *published* templates (on GitHub) for cookiecutter is at:
http://cookiecutter-templates.sebastianruml.name/

Simple:
cookiecutter https://github.com/luphord/cookiecutter-pyscript.git --> single-file Py-script
cookiecutter https://github.com/luphord/cookiecutter-pyscript --> same
cookiecutter https://github.com/dataloudlabs/cookiecutter-pyscript --> w. basic test-capability

Stand-alone apps:
cookiecutter https://github.com/benwebber/cookiecutter-standalone --> flexible, can generate Py-wheel, EXE or RPM (best for CLI-tools)
cookiecutter https://github.com/William-Lake/ScriptToExeCC.git --> generates Win-EXE using GitHub-action='pyinstaller-windows'

WebDev-focused:
https://github.com/tiangolo/full-stack --> choice of Flask or FastAPI as back-end server
https://github.com/BrentGruber/fastapi-mysql-cookiecutter
https://github.com/nhjeon/cookiecutter-fastapi-mysql
https://github.com/rwinte/cookiecutter-fastapi-sqlite
https://github.com/jonatasoli/fastapi-template-cookiecutter

Generic:
https://github.com/cjolowicz/cookiecutter-hypermodern-python --> with ALL bells & whistles ...


### Py-Scaffold based
https://github.com/SarthakJariwala/PyScaffold-Interactive


## NOTES

### Dockerfiles
Most of the template-based solutions (at least for 'cookiecutter') has a Dockerfile option for deployment. 
A basic TOML (or YAML) docker-compose specification file is typically given in combination with a Dockerfile, 
unless a Dockerfile-only basic setup is given.

Use 'docker ps' after startup of Dockerfile to see details like ID, hostname and assigned IP-address .

### TAR-archives

### PyInstaller-deployment


