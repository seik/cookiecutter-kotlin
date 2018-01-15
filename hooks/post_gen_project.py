#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from subprocess import Popen

PROJECT_ROOT = os.path.realpath(os.path.curdir)

def remove_file(filename):
    """
    Removes file from project root
    """
    fullpath = os.path.join(PROJECT_ROOT, filename)
    if os.path.exists(fullpath):
        os.remove(fullpath)

def init_git():
    """
    Init git folder
    """

    GIT_COMMANDS = [['git', 'init'], ['git', 'add', '.'], ['git',
                    'commit', '-a', '-m', 'Initial Commit.']]

    for command in GIT_COMMANDS:
        git = Popen(command, cwd=PROJECT_ROOT)
        git.wait()


if '{{ cookiecutter.use_git }}'.lower() == 'y':
    init_git()
else:
    remove_file('.gitignore')

remove_file('README.md')
