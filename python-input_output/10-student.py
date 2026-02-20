#!/usr/bin/python3
"""class Student that defines a student by
Public instance attributes: first_name, last_name, age"""


class Student:
    """Class Student defined by first_name, last_name, age"""
    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first_name, last_name, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the JSON representation of the Student instance"""
        if attrs is None:
            return self.__dict__
        return {key: self.__dict__[key]
                for key in attrs if key in self.__dict__}
