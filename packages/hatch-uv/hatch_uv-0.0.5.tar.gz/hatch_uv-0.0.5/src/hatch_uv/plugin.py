from typing import List
from hatch.env.virtual import VirtualEnvironment
from hatch.env.utils import add_verbosity_flag

class UVEnvironment(VirtualEnvironment):
    PLUGIN_NAME = "uv"

    def construct_pip_install_command(self, args: List[str]):
        """
        A convenience method for constructing a [`pip install`](https://pip.pypa.io/en/stable/cli/pip_install/)
        command with the given verbosity. The default verbosity is set to one less than Hatch's verbosity.
        """
        command = ['python', '-u', '-m', 'uv', 'pip', 'install']

        # Default to -1 verbosity
        add_verbosity_flag(command, self.verbosity, adjustment=-1)

        command.extend(args)
        return command