#!/usr/bin/python3

def lookup(obj):
    """
    Function Documentation: This function returns the list of available attributes and methods of an object.

    Parameters:
        obj: The object for which to look up attributes and methods.

    Returns:
        list: A list containing the names of attributes and methods of the object.

    Usage:
        lookup(obj)
    """
    return dir(obj)
