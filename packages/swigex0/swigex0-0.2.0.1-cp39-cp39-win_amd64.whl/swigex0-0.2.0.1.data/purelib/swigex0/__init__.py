# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _swigex0
else:
    import _swigex0

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _swigex0.delete_SwigPyIterator

    def value(self):
        return _swigex0.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _swigex0.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _swigex0.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _swigex0.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _swigex0.SwigPyIterator_equal(self, x)

    def copy(self):
        return _swigex0.SwigPyIterator_copy(self)

    def next(self):
        return _swigex0.SwigPyIterator_next(self)

    def __next__(self):
        return _swigex0.SwigPyIterator___next__(self)

    def previous(self):
        return _swigex0.SwigPyIterator_previous(self)

    def advance(self, n):
        return _swigex0.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _swigex0.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _swigex0.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _swigex0.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _swigex0.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _swigex0.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _swigex0.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _swigex0:
_swigex0.SwigPyIterator_swigregister(SwigPyIterator)
class VectorInt(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _swigex0.VectorInt_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _swigex0.VectorInt___nonzero__(self)

    def __bool__(self):
        return _swigex0.VectorInt___bool__(self)

    def __len__(self):
        return _swigex0.VectorInt___len__(self)

    def __getslice__(self, i, j):
        return _swigex0.VectorInt___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _swigex0.VectorInt___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _swigex0.VectorInt___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _swigex0.VectorInt___delitem__(self, *args)

    def __getitem__(self, *args):
        return _swigex0.VectorInt___getitem__(self, *args)

    def __setitem__(self, *args):
        return _swigex0.VectorInt___setitem__(self, *args)

    def pop(self):
        return _swigex0.VectorInt_pop(self)

    def append(self, x):
        return _swigex0.VectorInt_append(self, x)

    def empty(self):
        return _swigex0.VectorInt_empty(self)

    def size(self):
        return _swigex0.VectorInt_size(self)

    def swap(self, v):
        return _swigex0.VectorInt_swap(self, v)

    def begin(self):
        return _swigex0.VectorInt_begin(self)

    def end(self):
        return _swigex0.VectorInt_end(self)

    def rbegin(self):
        return _swigex0.VectorInt_rbegin(self)

    def rend(self):
        return _swigex0.VectorInt_rend(self)

    def clear(self):
        return _swigex0.VectorInt_clear(self)

    def get_allocator(self):
        return _swigex0.VectorInt_get_allocator(self)

    def pop_back(self):
        return _swigex0.VectorInt_pop_back(self)

    def erase(self, *args):
        return _swigex0.VectorInt_erase(self, *args)

    def __init__(self, *args):
        _swigex0.VectorInt_swiginit(self, _swigex0.new_VectorInt(*args))

    def push_back(self, x):
        return _swigex0.VectorInt_push_back(self, x)

    def front(self):
        return _swigex0.VectorInt_front(self)

    def back(self):
        return _swigex0.VectorInt_back(self)

    def assign(self, n, x):
        return _swigex0.VectorInt_assign(self, n, x)

    def resize(self, *args):
        return _swigex0.VectorInt_resize(self, *args)

    def insert(self, *args):
        return _swigex0.VectorInt_insert(self, *args)

    def reserve(self, n):
        return _swigex0.VectorInt_reserve(self, n)

    def capacity(self):
        return _swigex0.VectorInt_capacity(self)
    __swig_destroy__ = _swigex0.delete_VectorInt

# Register VectorInt in _swigex0:
_swigex0.VectorInt_swigregister(VectorInt)

def fibn(n):
    return _swigex0.fibn(n)

def fib(n):
    return _swigex0.fib(n)
class Fibo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        _swigex0.Fibo_swiginit(self, _swigex0.new_Fibo(*args, **kwargs))
    __swig_destroy__ = _swigex0.delete_Fibo

    def resetFromFiboVal(self, fib):
        return _swigex0.Fibo_resetFromFiboVal(self, fib)

    def resetFromFiboRef(self, fib):
        return _swigex0.Fibo_resetFromFiboRef(self, fib)

    def display(self, showTitle=True):
        return _swigex0.Fibo_display(self, showTitle)

    def getVector(self):
        return _swigex0.Fibo_getVector(self)

    def getTitle(self):
        return _swigex0.Fibo_getTitle(self)

# Register Fibo in _swigex0:
_swigex0.Fibo_swigregister(Fibo)
class StdoutRedirect(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        _swigex0.StdoutRedirect_swiginit(self, _swigex0.new_StdoutRedirect(*args, **kwargs))
    __swig_destroy__ = _swigex0.delete_StdoutRedirect

    def start(self, file):
        return _swigex0.StdoutRedirect_start(self, file)

    def stop(self):
        return _swigex0.StdoutRedirect_stop(self)

# Register StdoutRedirect in _swigex0:
_swigex0.StdoutRedirect_swigregister(StdoutRedirect)




