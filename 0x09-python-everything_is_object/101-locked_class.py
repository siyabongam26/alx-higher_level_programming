#!/usr/bin/python3
"""Locked class defined."""


class LockedClass:
    """
    Prevent user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
