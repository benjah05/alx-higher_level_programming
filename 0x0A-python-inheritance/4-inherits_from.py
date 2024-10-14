#!/usr/bin/python3
def inherits_from(obj, a_class):
    """check if an object is an instance of a class that
    inherited directly or indirectly from the specified class
    """
    def inherits_from(obj, a_class):
        return (issubclass(obj, a_class))
