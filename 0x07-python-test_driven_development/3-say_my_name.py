#!/usr/bin/python3
"""3-say_my_name module prints first name and last name"""


def say_my_name(first_name, last_name=""):
    """say_my_name method prints my name is (firstname) and
    (last name)
       Args:
           first_name(string): takes first name
           last_name(string): takes last name by default
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
