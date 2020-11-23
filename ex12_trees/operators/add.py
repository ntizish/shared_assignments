"""."""

from default_operator import DefaultOperator
from operators.operator import Operator
from tree_node import TreeNode


class Add(Operator):
    """Custom operation."""

    def __init__(self, left: TreeNode, right: TreeNode):
        """default constructor."""
        super().__init__((left, right))
        self.left = left
        self.right = right

    @property
    def priority(self):
        """:return the value of the operation."""
        return 8

    def class_str(self):
        """Class string."""
        return f'Add(Leaf({self.__value__[0]}), Leaf({self.__value__[1]}))'

    @property
    def default_operator(self):
        """:return the default operator of the operation."""
        return DefaultOperator(lambda x, y: x + y, "+")

    @property
    def actions(self):
        """:return a dictionary of custom operations."""
        return {
            (set, set): lambda x, y: x | y,  # set union
            (set, int): lambda x, y: x | {y}  # add to set
        }

    def __eq__(self, other):
        """It is equal."""
        return self.left == other.left and self.right == other.right and self.class_str() == other.class_str()

    @property
    def associativity(self):
        """
        Boolean whether the operation is associative or not.

        For example addition is associative but subtraction is not.
        Override this property for operations where the given operation is not associative.
        """
        return True
