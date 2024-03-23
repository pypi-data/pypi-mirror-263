import importlib
import sys


def fix():
    try:
        import ufl_legacy
    except ImportError:
        return  # no need, we don't have to do the rename thing

    for old in """
ufl.algebra
ufl.algorithms.transformer
ufl.classes
ufl.constantvalue
ufl.core.expr
ufl.core.ufl_type
ufl.equation
ufl.mathfunctions
    """.split():
        before, sep, after = old.partition(".")
        new = "".join(("ufl_legacy", sep, after))
        sys.modules[old] = importlib.import_module(new)
