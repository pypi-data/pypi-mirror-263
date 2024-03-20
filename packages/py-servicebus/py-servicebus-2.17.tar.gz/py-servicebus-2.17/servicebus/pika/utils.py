"""
Non-module specific functions shared by modules in the pika package

"""
import collections


def is_callable(handle):
    """Returns a bool value if the handle passed in is a callable
    method/function

    :param any handle: The object to check
    :rtype: bool

    """
    try:
        # Python2 and older Python3 works
        return isinstance(handle, collections.Callable)
    except Exception:
        # Newer Python3 works
        return isinstance(handle, collections.abc.Callable)
