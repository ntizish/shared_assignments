"""."""

from abc import ABCMeta, abstractmethod


class TreeNode(metaclass=ABCMeta):
    """The main node class."""

    def __init__(self, *args):
        """:param make use of *args and store them in a way that it is easy to use them."""
        print(type(args), args)
        self.__value__ = args  # tuple of value

    @property
    @abstractmethod
    def default_operator(self):
        """abstract method which should be overridden to return the default_operator object."""
        pass

    @abstractmethod
    def apply(self):
        """abstract method which should be overridden to compute the value of the given abstract tree."""
        return self.__value__

    def class_str(self):
        """:return class string representation of the object."""
        return "Add(Leaf(5), Leaf(6))"

    def __eq__(self, other):
        """:return True when 2 object trees have the same shape and values."""
        return self is other

    def __ne__(self, other):
        """:return True when 2 object trees have a different shape and/or values."""
        return self is not other

    def __str__(self):
        """:return the mathematical string representation of the tree with least amount of parenthesis."""
        return "5 + 6"

    @property
    @abstractmethod
    def priority(self):
        """
        abstract method witch should be overridden to return priority of the node.

        Visit: https://en.wikipedia.org/wiki/Order_of_operations
        """
        pass

    @property
    @abstractmethod
    def associativity(self):
        """abstract method witch should be overridden to return a boolean whether the node is associative or not."""
        pass

    def is_bitwise(self):
        """It is bitwise operator."""
        return False
