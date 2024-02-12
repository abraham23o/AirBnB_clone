#!/usr/bin/python3
"""class BaseModel that defines all common attributes
/methods for other
classes
"""
import uuid
from datetime import datetime
# from . import storage


class BaseModel:
    """class BaseModel that defines all common attributes
    /methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization
        :param args: arguments input as a list
        :param kwargs: arguments input as a dictionary
        id - assign with an uuid when an instance is created
        created_at: assign with current datetime when an instance is created
        updated_at: assign with the current datetime when an instance is
        created and will be updated everytime you change your object
        """
        if len(kwargs) > 0:
            date_time_keys = ['created_at', 'updated_at']
            for k, v in kwargs.items():
                if k in date_time_keys:
                    self.__dict__[k] = datetime\
                        .strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                elif k == 'id':
                    self.id = v

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of an instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
         of the instance
         """
        _dict = self.__dict__.copy()
        _dict['created_at'] = self.created_at.isoformat()
        _dict['updated_at'] = self.updated_at.isoformat()
        _dict['__class__'] = self.__class__.__name__
        return _dict
