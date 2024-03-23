# apt/__init__.py
from . import apt
import importlib


def _import_aplustools():
    aplustools = importlib.import_module('aplustools')
    globals().update(aplustools.__dict__)


_import_aplustools()
del _import_aplustools
del importlib


__version__ = "2.2.4"
