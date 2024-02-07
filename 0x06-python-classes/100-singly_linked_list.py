#!/usr/bin/python3
"""py classes"""


class Node:
    """node definition"""
    def __init__(self, data, next_node=None):
        """initializing node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """data setter"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """data getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """data setter"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class of singly linked list"""
    def __init__(self):
        """initiating singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """inset node"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node

            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """print method definition"""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
