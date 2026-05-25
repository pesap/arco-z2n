from importlib.metadata import PackageNotFoundError, version

from arco_z2n.core import hello

try:
    __version__ = version("arco-z2n")
except PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = ["__version__", "hello"]
