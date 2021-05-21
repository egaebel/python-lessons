# Time to learn Python! But first, some tools and junk.

## Install Python3

Download and install Python from:

https://www.python.org/downloads/release/python-3810/

Click "Windows installer (64-bit)" to download and then follow the installation.

## Clone this repository

And then rename it to python-lesson-1.

```
git clone git@github.com:egaebel/python-lessons.git
mv python-lessons python-lesson-1
```

## Setup a VirtualEnv for today's lesson

Virtualenv (now called venv for Python3 apparently) is a handy way to separate
out Python projects, so that the packages you install for one project won't
interfere with another. It comes with Python.

Run the following in a directory you want to keep your code in:

```
cd python-lesson-1
py -m venv python-lesson-1
```

## Activate your Virtual Environment

Activating your virtual environment will change your default 'python' command
to be the one associated with your environment, the same with your 'pip'
command. To activate your virtual environment run:

```
cd python-lesson-1
.\Scripts\activate
```

## Install the following packages with the python package installer (pip).

We're going to need just two packages that aren't included with Python for today's lesson.

```
pip install numpy
pip install matplotlib
```
