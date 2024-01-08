#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Function Documentation: This function returns True if the object is exactly an instance of the specified class; otherwise, False.

    Parameters:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is exactly an instance of the specified class; otherwise, False.

    Usage:
        is_same_class(obj, a_class)
    """
    return type(obj) == a_class
