[//]: # (copyright 2010-2012,2017,2020,2022 by flonatel GmbH & Co. KG / Andreas Florath)
[//]: # ( )
[//]: # (SPDX-License-Identifier: GPL-3.0-or-later)
[//]: # ( )
[//]: # (This file is part of rmtoo.)
[//]: # ( )  
[//]: # (rmtoo is free software: you can redistribute it and/or modify)
[//]: # (it under the terms of the GNU General Public License as published by)
[//]: # (the Free Software Foundation, either version 3 of the License, or)
[//]: # (at your option any later version.)
[//]: # ( )
[//]: # (rmtoo is distributed in the hope that it will be useful,)
[//]: # (but WITHOUT ANY WARRANTY; without even the implied warranty of)
[//]: # (MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the)
[//]: # (GNU General Public License for more details.)
[//]: # ( )  
[//]: # (You should have received a copy of the GNU General Public License)
[//]: # (along with rmtoo.  If not, see <https://www.gnu.org/licenses/>.)

# rmToo

Open Source Requirements Management Tool

[![image](https://img.shields.io/github/release/florath/rmtoo.svg)](https://github.com/florath/rmtoo/releases)
[![image](https://travis-ci.org/florath/rmtoo.svg?branch=master)](https://travis-ci.org/florath/rmtoo)
[![image](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)
[![image](https://img.shields.io/codecov/c/github/codecov/example-python.svg)](https://codecov.io/gh/florath/rmtoo)
[![image](https://img.shields.io/github/downloads/florath/rmtoo/total.svg)](http://rmtoo.florath.net)
[![image](https://img.shields.io/pypi/v/rmtoo.svg)](https://pypi.python.org/pypi/rmtoo)
[![image](https://img.shields.io/coverity/scan/12488.svg)](https://scan.coverity.com/projects/rmtoo)
[![Code Climate](https://codeclimate.com/github/florath/rmtoo/badges/gpa.svg)](https://codeclimate.com/github/florath/rmtoo)
[![Issue Count](https://codeclimate.com/github/florath/rmtoo/badges/issue_count.svg)](https://codeclimate.com/github/florath/rmtoo)

## Introduction

This Readme gives a short overview over the available online
documentation for rmtoo.

## Content

This file contains the following chapters:

[Conventions](#Conventions)  
[Operating System Support](#Operating-System-Support)  
[Preinstalled VMs](#Preinstalled-VMs)  
[Installation](#Installation)  
[Installation using virtualenv](#Installation-using-virtualenv)  
[First Project](#First-Project)  
[Man Pages](#Man-Pages)  
[Other Documentation](#Other-Documentation)  
[Emacs Mode for Editing Requirements](#Emacs-Mode-for-Editing-Requirements)  
[Footer](#Footer)

## Conventions

`YY`: names the version of rmtoo. You have to replace this with the real
    version number.

`$ cmd`: This is a command you have to type in. The `$` is a replacement for
    the shell prompt - do not enter it as a part of the command.

## Operating System Support

rmtoo is fully supported under Linux. Nevertheless, because it is
written in computer independent programming languages (such as python),
is also works on other operating systems.

Mac OS X users might want to read `Readme-OS-X.txt`.

Windows users might want to read the `Readme-Windows.txt`.

## Preinstalled VMs

For evaluation proposes and running small projects there is the
possibility to use Amazon AWS EC2 preinstalled VMs.

More details are available in a dedicated
[Readme](contrib/vmsetup/Readme.rst).

## Installation

The following sections assume, that you are using Linux. Please refer to
the appropriate Readme file for your operating system for more
information if you do not use Linux.

### Dependencies

To use rmtoo, other software packages must be installed.

rmtoo is written in python. At least version 3.5 of python is needed.
python 3.8 may work, but there is a problem (bug (fix)?) is python 3.8
which create different XML elements as the previous versions.

When you want to create LaTeX or PDF documentation, LaTeX is needed.

For the requirements dependency graph, graphviz is used.

For statistics plot gnuplot is used. For the estimation module the
python-scipy package is needed.

Typically the packages from your distribution will work.

### First Project

The recommended way of starting is to copy the provided template
project.

The basic steps are:

1)  Copy over the template project to some other directory.
2)  Set up the environment
3)  Run `make`
4)  Check, if everything worked
5)  Start changing / adapting things to your needs

Note that during this document the project will be called
\'MyNewProject\'. Please adapt the name for your needs.

## Installation using virtualenv

This is the preferred installation method - it takes care that at least
the python dependencies are correctly installed.

### Installation

To install `rmtoo` in a virtualenv, execute the following steps:

``` {.bash}
$ mkdir RMTOO
$ cd RMTOO
$ virtualenv venv
$ source venv/bin/activate
$ pip install --upgrade pip setuptools wheel
$ pip install --only-binary=numpy,scipy numpy scipy
$ pip install rmtoo
```

This has only to be done once.

## First Project

### Installation

Change to a directory where you want to create the new project. This is
needed only once.

``` {.bash}
# cd to virtualenv directory - if not already there
$ cd RMTOO
$ cp -r venv/rmtoo/contrib/template_project MyNewProject
```

### Usage

To create all the artifacts for the template project, execute

``` {.bash}
$ cd MyNewProject
$ source ./setenv.sh VENV
$ make
$ ls artifacts
```

In the artifacts directory there are all the generated files. A typical
workflow is, to change or add requirements, topics or the configuration
in the `MyNewProject` directory, run `make` again and check the
artifacts.

## Man Pages

When using the virtualenv, use

``` {.bash}
$ man -l venv/rmtoo/share/man/man7/rmtoo.7
```

to get an overview over all available man pages. Those other man pages
you can read also with man. Replace the file name with the appropriate
manual page, like:

``` {.bash}
$ man -l venv/rmtoo/share/man/man7/rmtoo-analytics.7
```

### Additional Documentation

Additional documentation can be found in the directories
`RMTOO/venv/rmtoo/doc` (especially the Readme files).

## Other Documentation

### FAQ

Frequently asked questions A collection of questions which were ask in
the past - including the answers.

### Presentations

There are also two presentations about the design and features of rmtoo.
Theese presentations can be found in the download section of the
sourceforge project page. Please visit the projects home page
<http://rmtoo.florath.net>

### Readme-Overview.txt

Description of the features of rmtoo.

### Readme-Hacking.txt

Small (and yet unfinished) document how to develop functionality and
modules for rmtoo.

### Readme-OS-X.txt

Hints for Mac Users.

### Readme-Windows.txt

Hints for Windows users.

### Readme-RmtooOnRmtoo.txt

Run rmtoo to get the documentation for rmtoo itself.

### Readme-GitPython.txt

Some note about the (internal) use of GitPython.

## Emacs Mode for Editing Requirements

When using the tar package, emacs mode can be loaded in emacs by:
`M-x load-file` point to `RMTOO/venv/rmtoo/contrib/req-mode.el` All
files with suffix `.req` will now use the requirements editing mode.

## Footer

If you have some problems, remarks or feature request, you\'re welcome
to visit the project home page

<http://rmtoo.florath.net>

| flonatel GmbH & Co. KG  
| Andreas Florath  
| <rmtoo@florath.net>

\(c\) 2010-2012,2017,2020,2022 by flonatel GmbH & Co. KG  
For licensing details see COPYING
