"""Initialization Module"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "0.0.0"

__version_info__ = tuple(__version__.split("."))
