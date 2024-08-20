"""
DBLite initialization module.

This module initializes the DBLite package and prints the version information.

Attributes:
    __version__ (float): The version number of the DBLite package.

Functions:
    None

Dependencies:
    colorama: Used for colored console output.

Usage:
    This module is automatically executed when the DBLite package is imported.
    It will print the version information to the console.

Example:
    >>> import DBLite
    DBLite init < v1.5 >
"""

from colorama import Fore

__version__ = 1.5

def print_version():
    """
    Print the DBLite version information to the console.

    This function uses colorama to print the version number in cyan color.

    Returns:
        None
    """
    print(f'DBLite init < {Fore.CYAN}v{__version__}{Fore.RESET} >')

print_version()