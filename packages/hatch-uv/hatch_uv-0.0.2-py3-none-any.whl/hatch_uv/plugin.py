from __future__ import annotations

import os
import re
import shutil
import signal
import sys
from contextlib import contextmanager
from pathlib import Path
from types import FrameType
from typing import Callable

import pexpect
from hatch.env.virtual import VirtualEnvironment
from hatch.env.utils import add_verbosity_flag



class UVEnvironment(VirtualEnvironment):
    PLUGIN_NAME = "uv"

    def construct_pip_install_command(self, args: list[str]):
        """
        A convenience method for constructing a [`pip install`](https://pip.pypa.io/en/stable/cli/pip_install/)
        command with the given verbosity. The default verbosity is set to one less than Hatch's verbosity.
        """
        command = ['python', '-u', '-m', 'uv', 'pip', 'install', '--disable-pip-version-check', '--no-python-version-warning']

        # Default to -1 verbosity
        add_verbosity_flag(command, self.verbosity, adjustment=-1)

        command.extend(args)
        return command