#!/usr/bin/python3

""" a class Node that defines a node of a singly linked """


class Node:
    """
    A class representing a node of a singly linked list

    Attributes:
    data (int): The data stored in the node
    next_node (Node): The next node in the linked list
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node instance.

        Args:
        data (int): The data stored in the node
        next_node (Node, optional): Next node in linked list.Defaults to None

        Raises:
        TypeError: If data is not an int or next_node is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ int: The data stored in the node """
        return self._data

    @data.setter
    def data(self, value):
        """
        Setter for the data attribute

        Args:
        value (int): The new value for the data attribute

        Raises:
        TypeError: If value is not an int
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Node: The next node in the linked list."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the next_node attribute

        Args:
        value (int): The new value for the data attribute

        Raises:
        TypeError: If value is not an int
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    A class representing a singly linked list

    Args:
    head: The head of the linked list
    """
    def __init__(self):
        """ Initialize an empty SinglyLinkedList """
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the linked list in sorted order.

        Args:
        value (int): The value to be inserted.
        """
        new_node = Node(value)
        if self.head is None or self.head.data > value:
        new_node.next_node = self.head
        self.head = new_node
    else:
        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Converts the linked list to a string representation.

        Returns:
        str: The string representation of the linked list
        """
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
