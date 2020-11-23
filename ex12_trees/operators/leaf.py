"""."""

from default_operator import DefaultOperator
from tree_node import TreeNode


class Leaf(TreeNode):
    """Leaf node."""

    def __init__(self, value):
        """default constructor."""
        super().__init__(value)
        self.__value = value

    def __str__(self):
        """String repr."""
        return str(self.__value)

    @property
    def priority(self):
        """:return the value of the operation."""
        return 10

    @property
    def associativity(self):
        """Nothing fancy here."""
        return True

    def class_str(self):
        """Class string."""
        return f'Leaf({self.__value})'

    @property
    def default_operator(self):
        """Nothing fancy here."""
        return DefaultOperator(lambda x: x, "")

    def apply(self):
        """:return the value."""
        return self.__value

    def __eq__(self, other):
        """It is equal."""
        return self.__value == other.apply() and self.class_str() == other.class_str()
