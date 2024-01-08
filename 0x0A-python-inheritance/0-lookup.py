#!/usr/bin/python3
"""This function returns the list of available attributes and methods of an object."""

def lookup (obj):
   """Returns a list containing the names of attributes and methods of the object."""
    return (dir(obj))
