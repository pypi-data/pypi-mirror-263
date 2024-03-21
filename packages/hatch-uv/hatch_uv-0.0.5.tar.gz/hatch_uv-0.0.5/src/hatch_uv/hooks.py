from hatchling.plugin import hookimpl

from .plugin import UVEnvironment


@hookimpl
def hatch_register_environment():
    return UVEnvironment
