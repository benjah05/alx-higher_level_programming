#!/usr/bin/python3
"""Define class Node"""


class Node:
    """Present class Node
    Attributes:
        __data (int): value of a node in a list
        __next_node (Node): next node in a list
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
    """Use getter method"""
    @property
    def data(self):
        """Get data value
        Returns:
            Retrieve data
        """
        return (self.__data)
    """Use setter method"""
    @data.setter
    def data(self, value):
        """Set value for data
        Args:
            value (int): value to set to data
        Raises:
            TypeError: if value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    """Use getter method"""
    @property
    def next_node(self):
        """Get next_node
        Returns:
            Retrieve next_node
        """
        return (self.__next_node)
    """Use setter method"""
    @data.setter
    def data(self, value):
        """Set next_node
        Args:
            value (int): value to set to node
        Raises:
            TypeError: if node is not None or a node object
        """
        if isinstance(value, Node) or value == None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


"""Define a class SinglyLinkedList"""


class SinglyLinkedList:
    """Represent class SinglyLinkedList
    Attributes:
        __head (Node): pointer to the head of the list
    """
    def __init__(self):
        pass
    """print sorted list"""
    def sorted_insert(self, value):
        """Assign value based on index
        Args:
            value (int): data to assign in next_node
        """
        for i in range(value):
            self.__head[i] = value
