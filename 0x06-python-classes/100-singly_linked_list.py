#!/usr/bin/python3
"""Define class Node"""


class Node:
    """Initialize class Node
    Args:
        data (int): value of a node in a list
        next_node (Node): next node in a list
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
    @next_node.setter
    def next_node(self, value):
        """Set next_node
        Args:
            value (int): value to set to node
        Raises:
            TypeError: if node is not None or a node object
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
        
"""Define a class SinglyLinkedList"""


class SinglyLinkedList:
    """Initialize a new SinglyLinkedList"""
    def __init__(self):
        """Initialize the head to None"""
        self.__head = None
    """print sorted list"""
    def sorted_insert(self, value):
        """Insert a new node and maintain a sorted order
        Args:
            value (Node): The new Node to insert
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head == new_node
        else:
            tmp_node = self.__head
            while (tmp_node.next_node is not None and
                    tmp_node.next_node.data < value):
                tmp_node = tmp_node.next_node
            new_node.next_node = tmp_node.next_node
            tmp_node.next_node = new_node
"""String representation"""
def __str__(self):
    """String representation of the list"""
    result = []
    current = self.__head
    while current is not None:
        result.append(str(current.data))
        current = current.next_node
    return ('\n'.join(result))
