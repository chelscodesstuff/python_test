import importlib
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


def test_import_snake():
    assert importlib.import_module('snake') is not None
