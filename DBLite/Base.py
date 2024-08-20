
"""
DBLite - A Simple Database Library

DBLite is a lightweight and easy-to-use database library implemented in Python.
It provides basic functionality for creating, managing, and querying simple databases.

Features:
- Create and connect to database files
- Add, retrieve, and remove data fields
- Support for optional PIN protection
- Simple object storage and retrieval
- Database copying and serialization

This library is suitable for small-scale projects and educational purposes.
It is not intended for use in production environments or with large datasets.

Author: Pavlov Ivan
Version: 1.5
License: MIT
"""

from copy import deepcopy
from DBLite import BaseErrors
from typing import Optional
from random import randint
import pickle




class DataField:
    """
    Represents a data field in the database.

    Attributes:
        __filed (dict): A dictionary to store field data.
        __filed_name (str): The name of the field.
        __id (int): A unique identifier for the field.

    Example:
        >>> field = DataField("users")
        >>> field.add(1, {"name": "John", "age": 30})
        >>> field.get(1)
        {'name': 'John', 'age': 30}
    """

    def __init__(self, filed_name_: str, id_: Optional[int] = None) -> None:
        """
        Initialize a new DataField instance.

        Args:
            filed_name_ (str): The name of the field.
            id_ (Optional[int]): An optional unique identifier. If not provided, a random ID will be generated.

        Example:
            >>> field = DataField("products")
        """
        self.__filed = {}
        self.__filed_name = filed_name_
        self.__id = randint(0, 999999999999999) if id_ is None else id_

    def check_field_name(self, field_name_: str) -> bool:
        """
        Check if the given field name matches the current field name.

        Args:
            field_name_ (str): The field name to check.

        Returns:
            bool: True if the names match, False otherwise.

        Example:
            >>> field = DataField("users")
            >>> field.check_field_name("users")
            True
            >>> field.check_field_name("products")
            False
        """
        if self.__filed_name == field_name_: return True
        return False
    
    def get(self, identifier_: int | str) -> object:
        """
        Retrieve an object from the field using its identifier.

        Args:
            identifier_ (int | str): The identifier of the object to retrieve.


        Returns:
            object: The retrieved object.

        Raises:
            BaseErrors.ErrorIdentifierNotFound: If the identifier is not found.

        Example:
            >>> field = DataField("users")
            >>> field.add(1, {"name": "Alice"})
            >>> field.get(1)
            {'name': 'Alice'}
            >>> field.get(2)
            Raises BaseErrors.ErrorIdentifierNotFound
        """
        try:
            return self.__filed[identifier_]
        except:
            raise BaseErrors.ErrorIdentifierNotFound(identifier_)
    
    def get_id(self) -> int:
        """
        Get the unique identifier of the field.

        Returns:
            int: The field's unique identifier.

        Example:
            >>> field = DataField("users")
            >>> field.get_id()
            123456789  # (example ID)
        """
        return self.__id
    
    def new_id(self):
        """
        Generate a new random ID for the field.

        Example:
            >>> field = DataField("users")
            >>> old_id = field.get_id()
            >>> field.new_id()
            >>> new_id = field.get_id()
            >>> old_id != new_id
            True
        """
        self.__id = randint(0, 999999999999999)
    
    def get_idetifiers(self) -> list[int | str]:
        """
        Get a list of all identifiers in the field.

        Returns:
            list[int | str]: A list of all identifiers.

        Example:
            >>> field = DataField("users")
            >>> field.add(1, {"name": "Alice"})
            >>> field.add(2, {"name": "Bob"})
            >>> field.get_idetifiers()
            [1, 2]
        """
        return list(self.__filed.keys())
    
    def get_objects(self) -> list[object]:
        """
        Get a list of all objects in the field.

        Returns:
            list[object]: A list of all objects.

        Example:
            >>> field = DataField("users")
            >>> field.add(1, {"name": "Alice"})
            >>> field.add(2, {"name": "Bob"})
            >>> field.get_objects()
            [{'name': 'Alice'}, {'name': 'Bob'}]
        """
        return list(self.__filed.values())
    
    def get_name(self) -> str:
        """
        Get the name of the field.

        Returns:
            str: The field's name.

        Example:
            >>> field = DataField("users")
            >>> field.get_name()
            'users'
        """
        return self.__filed_name
    
    def add(self, identifier_: int | str, obj_: object):
        """
        Add an object to the field with the given identifier.

        Args:
            identifier_ (int | str): The unique identifier for the object.
            obj_ (object): The object to be added to the field.

        Raises:
            BaseErrors.ErrorObjectIsDataBase: If the object is an instance of DataBase.

        Example:
            >>> field = DataField("users")
            >>> field.add(1, {"name": "Alice", "age": 30})
            >>> field.add("user2", {"name": "Bob", "age": 25})
            >>> field.get_objects()
            [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        """
        if isinstance(obj_, DataBase): raise BaseErrors.ErrorObjectIsDataBase(obj_)
        self.__filed[identifier_] = obj_

    def remove(self, identifier_: int | str):
        """
        Remove an object from the field using its identifier.

        Args:
            identifier_ (int | str): The identifier of the object to remove.

        Raises:
            BaseErrors.ErrorIdentifierNotFound: If the identifier is not found.

        Example:
            >>> field = DataField("users")
            >>> field.add(1, {"name": "David"})
            >>> field.remove(1)
            >>> field.get(1)
            Raises BaseErrors.ErrorIdentifierNotFound
        """
        try:    del self.__filed[identifier_]
        except: raise BaseErrors.ErrorIdentifierNotFound(identifier_)

    def lenght(self) -> int:
        """
        Get the number of objects in the field.

        Returns:
            int: The number of objects.

        Example:
            >>> field = DataField("users")
            >>> field.add(1, {"name": "Eve"})
            >>> field.add(2, {"name": "Frank"})
            >>> field.lenght()
            2
        """
        return len(self.__filed)
    
    def __len__(self) -> int:
        """
        Get the number of objects in the field (magic method).

        Returns:
            int: The number of objects.

        Example:
            >>> field = DataField("users")
            >>> field.add(1, {"name": "Grace"})
            >>> len(field)
            1
        """
        return len(self.__filed)
    
class DataBase:
    """
    Represents a database containing multiple DataFields.

    Attributes:
        __name (str): The name of the database file.
        __pin (Optional[int]): An optional PIN for database access.
        __fields (list[DataField]): A list of DataField objects in the database.

    Example:
        >>> db = DataBase.create("mydb.dbl", 1234)
        >>> db.add_field("users")
        >>> db.add("users", {"name": "Alice"}, 1)
        >>> db.get("users", 1)
        {'name': 'Alice'}
    """

    def __init__(self) -> None:
        """
        Initialize a new DataBase instance.

        Note: This method should not be called directly. Use DataBase.create() or DataBase.connect() instead.
        """
        self.__name = None
        self.__pin = None
        self.__fields: list[DataField] = None

    def __check_pin(self, pin_: Optional[int]) -> bool:
        """
        Check if the given PIN matches the database PIN.

        Args:
            pin_ (Optional[int]): The PIN to check.

        Returns:
            bool: True if the PINs match or if no PIN is set, False otherwise.

        Example:
            >>> db = DataBase.create("mydb.dbl", 1234)
            >>> db._DataBase__check_pin(1234)
            True
            >>> db._DataBase__check_pin(5678)
            False
        """
        if self.__pin == pin_: return True
        return False

    def __set_name(self, name_: str):
        """
        Set the name of the database.

        Args:
            name_ (str): The name to set.

        Returns:
            DataBase: The current instance for method chaining.

        Example:
            >>> db = DataBase()
            >>> db._DataBase__set_name("mydb.dbl")
            <DataBase object>
        """
        self.__name = name_
        return self
    
    def __set_pin(self, pin_: int):
        """
        Set the PIN for the database.

        Args:
            pin_ (int): The PIN to set.

        Returns:
            DataBase: The current instance for method chaining.

        Example:
            >>> db = DataBase()
            >>> db._DataBase__set_pin(1234)
            <DataBase object>
        """
        self.__pin = pin_
        return self

    def __set_data_fileds(self, fields_: list[DataField]):
        """
        Set the list of DataFields for the database.

        Args:
            fields_ (list[DataField]): The list of DataFields to set.

        Example:
            >>> db = DataBase()
            >>> fields = [DataField("users"), DataField("products")]
            >>> db._DataBase__set_data_fileds(fields)
        """
        self.__fields = fields_

    @classmethod
    def create(self, name_: str = 'database.dbl', pin_: Optional[int] = None, data_fileds_: list[DataField] = []):
        """
        Create a new database file.

        Args:
            name_ (str): The name of the database file. Defaults to 'database.dbl'.
            pin_ (Optional[int]): An optional PIN for database access.
            data_fileds_ (list[DataField]): A list of initial DataFields. Defaults to an empty list.

        Returns:
            DataBase: A new DataBase instance.

        Example:
            >>> db = DataBase.create("mydb.dbl", 1234)
            >>> db.get_fields_names()
            []
        """
        file = open(name_, 'wb')

        db = DataBase()
        db.__set_name(name_)
        db.__set_pin(pin_)
        db.__set_data_fileds(data_fileds_)

        pickle.dump(db, file)
        return db

    @classmethod
    def connect(self, name_: str, pin_: Optional[int] = None):
        """
        Connect to an existing database file.

        Args:
            name_ (str): The name of the database file to connect to.
            pin_ (Optional[int]): The PIN for database access, if required.

        Returns:
            DataBase: The connected DataBase instance.

        Raises:
            BaseErrors.ErrorDataBaseNotFound: If the database file is not found.
            BaseErrors.ErrorPin: If the provided PIN is incorrect.

        Example:
            >>> db = DataBase.create("mydb.dbl", 1234)
            >>> db2 = DataBase.connect("mydb.dbl", 1234)
            >>> db2.get_fields_names()
            []
        """
        try:    file = open(name_, 'rb')
        except: raise BaseErrors.ErrorDataBaseNotFound(name_)
        db: DataBase = pickle.load(file)

        if  db.__check_pin(pin_):   return db
        else:   raise BaseErrors.ErrorPin(pin_)
            
    def get_field(self, field_name_: str) -> DataField:
        """
        Get a DataField by its name.

        Args:
            field_name_ (str): The name of the field to retrieve.

        Returns:
            DataField: The requested DataField.

        Raises:
            BaseErrors.ErrorFieldNotFound: If the field is not found in the database.

        Example:
            >>> db = DataBase.create("mydb.dbl")
            >>> db.add_field("users")
            >>> users_field = db.get_field("users")
            >>> users_field.get_name()
            'users'
        """
        for filed in self.__fields:
            if filed.check_field_name(field_name_): return filed
        raise BaseErrors.ErrorFieldNotFound(field_name_, self.__name)
    
    def get_fileds(self) -> list[DataField]:
        """
        Get all DataFields in the database.

        Returns:
            list[DataField]: A list of all DataFields.

        Example:
            >>> db = DataBase.create("mydb.dbl")
            >>> db.add_field("users")
            >>> db.add_field("products")
            >>> fields = db.get_fileds()
            >>> len(fields)
            2
        """
        return self.__fields
    
    def get(self, field_name_: str, identifier_: int | str) -> object:
        """
        Get an object from a specific field using its identifier.

        Args:
            field_name_ (str): The name of the field.
            identifier_ (int | str): The identifier of the object.

        Returns:
            object: The requested object.

        Raises:
            BaseErrors.ErrorFieldNotFound: If the field is not found.
            BaseErrors.ErrorIdentifierNotFound: If the identifier is not found in the field.

        Example:
            >>> db = DataBase.create("mydb.dbl")
            >>> db.add_field("users")
            >>> db.add("users", {"name": "Alice"}, 1)
            >>> db.get("users", 1)
            {'name': 'Alice'}
        """
        field = self.get_field(field_name_)
        return field.get(identifier_)
    
    def get_fields_names(self) -> list[str]:
        """
        Get a list of all field names in the database.

        Returns:
            list[str]: A list of field names.

        Example:
            >>> db = DataBase.create("mydb.dbl")
            >>> db.add_field("users")
            >>> db.add_field("products")
            >>> db.get_fields_names()
            ['users', 'products']
        """
        return [filed.get_name() for filed in self.__fields]

    def add(self, field_name_: str, obj_: object, identifier_: int | str | None = None):
        """
        Add a new object to a specific field.

        Args:
            field_name_ (str): The name of the field to add the object to.
            obj_ (object): The object to add.
            identifier_ (int | str | None): The identifier for the object. If None, a random identifier will be used.

        Raises:
            BaseErrors.ErrorFieldNotFound: If the field is not found.

        Example:
            >>> db = DataBase.create("mydb.dbl")
            >>> db.add_field("users")
            >>> db.add("users", {"name": "Bob"}, 1)
            >>> db.get("users", 1)
            {'name': 'Bob'}
        """
        filed = self.get_field(field_name_)
        filed.add(identifier_, obj_)

    def add_field(self, field_name_: str):
        """
        Add a new field to the database.

        Args:
            field_name_ (str): The name of the new field.

        Example:
            >>> db = DataBase.create("mydb.dbl")
            >>> db.add_field("categories")
            >>> db.get_fields_names()
            ['categories']
        """
        filed = DataField(field_name_)
        self.__fields.append(filed)

    def pool(self):
        """
        Save the current state of the database to a file.

        This method serializes the database object using pickle and saves it to the file
        specified by self.__name.

        Example:
            >>> db = DataBase.create("mydb.dbl")
            >>> db.add_field("users")
            >>> db.add("users", {"name": "Alice"}, 1)
            >>> db.pool()
            # The database is now saved to "mydb.dbl"
        """
        file = open(self.__name, 'wb')
        db: DataBase = pickle.dump(self, file)
        self = db

    def remove_field(self, field_name_: str):
        """
        Remove a field from the database.

        Args:
            field_name_ (str): The name of the field to remove.

        Raises:
            BaseErrors.ErrorFieldNotFound: If the field is not found in the database.

        Example:
            >>> db = DataBase.create("mydb.dbl")
            >>> db.add_field("users")
            >>> db.add_field("products")
            >>> db.remove_field("users")
            >>> db.get_fields_names()
            ['products']
            >>> db.remove_field("nonexistent")
            Traceback (most recent call last):
                ...
            BaseErrors.ErrorFieldNotFound: Field 'nonexistent' not found in database 'mydb.dbl'
        """
        for filed in self.__fields:
            if filed.check_field_name(field_name_):
                self.__fields.remove(filed)
                return
        raise BaseErrors.ErrorFieldNotFound(field_name_, self.__name)

    def copy(self, new_name_: str = 'copebase.dbl', new_pin_: Optional[int] = None):
        """
        Create a copy of the current database with a new name and optional new PIN.

        This method creates a deep copy of the database, including all fields and their contents.
        Each field in the new database gets a new unique identifier.

        Args:
            new_name_ (str): The name for the new database file. Defaults to 'copebase.dbl'.
            new_pin_ (Optional[int]): The PIN for the new database. If None, no PIN is set.

        Returns:
            DataBase: A new DataBase object representing the copied database.

        Example:
            >>> original_db = DataBase.create("original.dbl")
            >>> original_db.add_field("users")
            >>> original_db.add("users", {"name": "Bob"}, 1)
            >>> copied_db = original_db.copy("copied.dbl", 1234)
            >>> copied_db.get_fields_names()
            ['users']
            >>> copied_db.get("users", 1)
            {'name': 'Bob'}
        """
        self.pool()

        coped_fields = deepcopy(self).get_fileds()
        for field in coped_fields:
            field.new_id()

        new_db = DataBase.create(new_name_, new_pin_, coped_fields)
        return new_db
