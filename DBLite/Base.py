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
    """

    def __init__(self, filed_name_: str, id_: Optional[int] = None) -> None:
        """
        Initialize a new DataField instance.

        Args:
            filed_name_ (str): The name of the field.
            id_ (Optional[int], optional): The unique identifier for the field. Defaults to None.
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
            bool: True if the field names match, False otherwise.
        """
        if self.__filed_name == field_name_: return True
        return False
    
    def get(self, identifier_: int | str) -> object:
        """
        Retrieve an object from the field using the given identifier.

        Args:
            identifier_ (int | str): The identifier of the object to retrieve.

        Returns:
            object: The retrieved object.

        Raises:
            BaseErrors.ErrorIdentifierNotFound: If the identifier is not found in the field.
        """
        try:
            return self.__filed[identifier_]
        except:
            raise BaseErrors.ErrorIdentifierNotFound(identifier_)
    
    def add(self, identifier_: int | str, obj_: object):
        """
        Add an object to the field with the given identifier.

        Args:
            identifier_ (int | str): The identifier for the object.
            obj_ (object): The object to add to the field.
        """
        self.__filed[identifier_] = obj_
    

class DataBase:
    """
    Represents a database.

    Attributes:
        __name (str): The name of the database.
        __pin (int): The PIN for database access.
        __fields (list[DataField]): A list of DataField objects in the database.
    """

    def __init__(self) -> None:
        """
        Initialize a new DataBase instance.
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
            bool: True if the PINs match, False otherwise.
        """
        if self.__pin == pin_: return True
        return False

    def __set_name(self, name_: str):
        """
        Set the name of the database.

        Args:
            name_ (str): The name to set.

        Returns:
            DataBase: The current DataBase instance.
        """
        self.__name = name_
        return self
    
    def __set_pin(self, pin_: int):
        """
        Set the PIN of the database.

        Args:
            pin_ (int): The PIN to set.

        Returns:
            DataBase: The current DataBase instance.
        """
        self.__pin = pin_
        return self

    def __set_data_fileds(self, fields_: list[DataField]):
        """
        Set the data fields of the database.

        Args:
            fields_ (list[DataField]): The list of DataField objects to set.
        """
        self.__fields = fields_

    @classmethod
    def create(self, name_: str = 'database.dbl', pin_: Optional[int] = None, data_fileds: list[DataField] = []):
        """
        Create a new database.

        Args:
            name_ (str, optional): The name of the database file. Defaults to 'database.dbl'.
            pin_ (Optional[int], optional): The PIN for database access. Defaults to None.
            data_fileds (list[DataField], optional): The list of DataField objects. Defaults to [].

        Returns:
            DataBase: The newly created DataBase instance.
        """
        file = open(name_, 'wb')

        db = DataBase()
        db.__set_name(name_)
        db.__set_pin(pin_)
        db.__set_data_fileds(data_fileds)

        pickle.dump(db, file)
        return db

    @classmethod
    def connect(self, name_: str, pin_: Optional[int] = None):
        """
        Connect to an existing database.

        Args:
            name_ (str): The name of the database file to connect to.
            pin_ (Optional[int], optional): The PIN for database access. Defaults to None.

        Returns:
            DataBase: The connected DataBase instance.

        Raises:
            BaseErrors.ErrorDataBaseNotFound: If the database file is not found.
            BaseErrors.ErrorPin: If the provided PIN is incorrect.
        """
        try:    file = open(name_, 'rb')
        except: raise BaseErrors.ErrorDataBaseNotFound(name_)
        db: DataBase = pickle.load(file)

        if  db.__check_pin(pin_):   return db
        else:   raise BaseErrors.ErrorPin(pin_)
            

    def get_field(self, field_name_: str) -> DataField:
        """
        Get a DataField object by its name.

        Args:
            field_name_ (str): The name of the field to retrieve.

        Returns:
            DataField: The DataField object with the matching name.

        Raises:
            BaseErrors.ErrorFieldNotFound: If the field is not found in the database.
        """
        for filed in self.__fields:
            if filed.check_field_name(field_name_): return filed
        raise BaseErrors.ErrorFieldNotFound(field_name_, self.__name)

    def add(self, field_name_: str, identifier_: int | str, obj_: object):
        """
        Add an object to a specific field in the database.

        Args:
            field_name_ (str): The name of the field to add the object to.
            identifier_ (int | str): The identifier for the object.
            obj_ (object): The object to add to the field.
        """
        filed = self.get_field(field_name_)
        filed.add(identifier_, obj_)

    def pool(self):
        """
        Save the current state of the database to the file.
        """
        file = open(self.__name, 'wb')
        db: DataBase = pickle.dump(self, file)
        self = db

    def get(self, field_name_: str, identifier_: int | str) -> object:
        """
        Retrieve an object from a specific field in the database.

        Args:
            field_name_ (str): The name of the field to retrieve the object from.
            identifier_ (int | str): The identifier of the object to retrieve.

        Returns:
            object: The retrieved object.
        """
        field = self.get_field(field_name_)
        return field.get(identifier_)
