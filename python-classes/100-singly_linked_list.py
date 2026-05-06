#!/usr/bin/python3
"""Module for singly linked list with sorted insertion."""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Instantiate a Node with data and next_node.

        Args:
            data (int): The integer data stored in the node.
            next_node (Node, optional): The next node in the list.
            Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next_node of the node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node of the node.

        Args:
            value (Node or None): The new next node.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list with sorted insertion."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Provide a string representation of the list,
           one node number per line.

        Returns:
            str: All node data joined by newline characters.
        """
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Insert a new Node with the given value into the correct position.

        The list remains in increasing order after insertion.

        Args:
            value (int): The integer value to insert.
        """
        new_node = Node(value)

        # If list is empty or new node belongs at the beginning
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Traverse the list to find the insertion point
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        # Insert after current
        new_node.next_node = current.next_node
        current.next_node = new_node
