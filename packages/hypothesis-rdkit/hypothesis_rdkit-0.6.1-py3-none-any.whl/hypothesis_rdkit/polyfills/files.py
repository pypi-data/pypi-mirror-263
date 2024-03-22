import sys

__all__ = ["files"]

# import importlib.resources or fall back to the backport
if sys.version_info < (3, 9):
    from importlib_resources import files
else:
    from importlib.resources import files
