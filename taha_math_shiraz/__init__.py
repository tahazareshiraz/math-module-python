from importlib import import_module

_module = import_module("src.taha_math_shiraz")

__version__ = getattr(_module, "__version__", None)
__all__ = getattr(
    _module, "__all__", [name for name in dir(_module) if not name.startswith("_")]
)

for name in __all__:
    globals()[name] = getattr(_module, name)

