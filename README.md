# Time to learn Python! But first, some tools and junk.

## Install Python3

## Setup a VirtualEnv for today's lesson

Virtualenv (now called venv for Python3 apparently) is a handy way to separate
out Python projects, so that the packages you install for one project won't 
interfere with another. It comes with Python.

Run the following in a directory you want to keep your code in:

mkdir python-lesson-1
py -m venv python-lesson-1

## Activate your Virtual Environment

Activating your virtual environment will change your default 'python' command
to be the one associated with your environment, the same with your 'pip'
command. To activate your virtual environment run:

cd python-lesson-1
.\Scripts\activate

## Install the following packages with the python package installer (pip).

We're going to need just two packages that aren't included with Python for today's lesson.

pip install numpy
pip install matplotlib