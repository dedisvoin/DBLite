"""
This module contains custom exception classes for handling errors in the DBLite database system.

These exceptions are used to provide detailed error messages with color-coded output
using the colorama library.

Classes:
    ErrorIdentifierNotFound: Raised when an identifier is not found in the database field.
    ErrorFieldNotFound: Raised when a field is not found in the specified database.
    ErrorDataBaseNotFound: Raised when the specified database is not found.
    ErrorPin: Raised when the provided password does not match the database.

Constants:
    BASE_ERROR: A formatted string used as a prefix for all error messages.
"""

from colorama import Fore

BASE_ERROR = f'[{Fore.RED} error {Fore.RESET}]'

class ErrorObjectIsDataBase(BaseException):
    """
    Exception raised when an object is not a database.
    Attributes:
        __arg (object): The object that is not a database.
    """
    def __init__(self, arg) -> None:
        """
        Initialize the ErrorObjectIsDataBase exception.
        Args:
            arg (object): The object that is not a database.
        """
        self.__arg = arg
    
    def __str__(self) -> str:
        """
        Return a formatted error message.
        Returns:
            str: The formatted error message.
        """
        return f'\n{BASE_ERROR} The object ( {Fore.LIGHTMAGENTA_EX}{self.__arg}{Fore.RESET} ) is not a database.'


class ErrorIdentifierNotFound(BaseException):
    """
    Exception raised when an identifier is not found in the database field.

    Attributes:
        __arg (str): The identifier that was not found.
    """

    def __init__(self, arg) -> None:
        """
        Initialize the ErrorIdentifierNotFound exception.

        Args:
            arg (str): The identifier that was not found.
        """
        self.__arg = arg

    def __str__(self) -> str:
        """
        Return a formatted error message.

        Returns:
            str: The formatted error message.
        """
        return f'\n{BASE_ERROR} This <{Fore.YELLOW}{self.__arg}{Fore.RESET}> identifier not founded to this data base field.'
    
class ErrorFieldNotFound(BaseException):
    """
    Exception raised when a field is not found in the specified database.

    Attributes:
        __arg1 (str): The field that was not found.
        __arg2 (str): The name of the database.
    """

    def __init__(self, arg1, arg2) -> None:
        """
        Initialize the ErrorFieldNotFound exception.

        Args:
            arg1 (str): The field that was not found.
            arg2 (str): The name of the database.
        """
        self.__arg1 = arg1
        self.__arg2 = arg2

    def __str__(self) -> str:
        """
        Return a formatted error message.

        Returns:
            str: The formatted error message.
        """
        return f'\n{BASE_ERROR} Field <{Fore.YELLOW}{self.__arg1}{Fore.RESET}> not founded to this data base {Fore.GREEN}"{self.__arg2}"{Fore.RESET}.'
    
class ErrorDataBaseNotFound(BaseException):
    """
    Exception raised when the specified database is not found.

    Attributes:
        __arg (str): The name of the database that was not found.
    """

    def __init__(self, arg) -> None:
        """
        Initialize the ErrorDataBaseNotFound exception.

        Args:
            arg (str): The name of the database that was not found.
        """
        self.__arg = arg

    def __str__(self) -> str:
        """
        Return a formatted error message.

        Returns:
            str: The formatted error message.
        """
        return f'\n{BASE_ERROR} Data base {Fore.GREEN}"{self.__arg}"{Fore.RESET} not found.'
    
class ErrorPin(BaseException):
    """
    Exception raised when the provided password does not match the database.

    Attributes:
        __arg (str): The incorrect password that was provided.
    """

    def __init__(self, arg) -> None:
        """
        Initialize the ErrorPin exception.

        Args:
            arg (str): The incorrect password that was provided.
        """
        self.__arg = arg

    def __str__(self) -> str:
        """
        Return a formatted error message.

        Returns:
            str: The formatted error message.
        """
        return f'\n{BASE_ERROR} The password ( {Fore.LIGHTMAGENTA_EX}{self.__arg}{Fore.RESET} ) does not match the database.'
    
class ErrorFieldNotFound(BaseException):
    """
    Exception raised when a field is not found in the specified database.
    Attributes:
        __arg1 (str): The field that was not found.
        __arg2 (str): The name of the database.
    """
    def __init__(self, arg1, arg2) -> None:
        """
        Initialize the ErrorFieldNotFound exception.
        Args:
            arg1 (str): The field that was not found.
            arg2 (str): The name of the database.
        """
        self.__arg1 = arg1
        self.__arg2 = arg2
    
    def __str__(self) -> str:
        """
        Return a formatted error message.
        Returns:
            str: The formatted error message.
        """
        return f'\n{BASE_ERROR} Field <{Fore.YELLOW}{self.__arg1}{Fore.RESET}> not founded to this data base {Fore.GREEN}"{self.__arg2}"{Fore.RESET}.'
    
class ErrorIdentifierNotFound(BaseException):
    """
    Exception raised when an identifier is not found in the database field.
    Attributes:
        __arg (str): The identifier that was not found.
    """
    def __init__(self, arg) -> None:
        """
        Initialize the ErrorIdentifierNotFound exception.
        Args:
            arg (str): The identifier that was not found.
        """
        self.__arg = arg

    def __str__(self) -> str:
        """
        Return a formatted error message.
        Returns:
            str: The formatted error message.
        """
        return f'\n{BASE_ERROR} This <{Fore.YELLOW}{self.__arg}{Fore.RESET}> identifier not founded to this data base field.'