import sys

__all__ = ["version"]

# version is valid only since Python 3.10
if sys.version_info < (3, 10):
    from importlib_metadata import version
else:
    from importlib.metadata import version
