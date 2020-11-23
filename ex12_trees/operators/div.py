"""."""

from default_operator import DefaultOperator
from operators.operator import Operator
from tree_node import TreeNode


class Div(Operator):
    """Custom operation."""

    def __init__(self, left: TreeNode, right: TreeNode):
        """default constructor."""
        super().__init__((left, right))
        self.left = left
        self.right = right

    @property
    def priority(self):
        """priority of the operation."""
        return 9

    @property
    def associativity(self):
        """
        Boolean whether the operation is associative or not.

        For example addition is associative but subtraction is not.
        Override this property for operations where the given operation is not associative.
        """
        return False

    @property
    def default_operator(self):
        """Make use of the 'operator' library or use a lambda function."""
        return DefaultOperator(lambda x, y: x / y, "/")

    def class_str(self):
        """Class string."""
        return f'Div(Leaf({self.__value__[0]}), Leaf({self.__value__[1]}))'

    def __eq__(self, other):
        """It is equal."""
        return self.left == other.left and self.right == other.right and self.class_str() == other.class_str()

    @property
    def actions(self):
        """:return a dictionary of custom operations."""
        return {
            (set, set): lambda x, y: x - y,  # set exclusion
            (set, int): lambda x, y: x - {y},  # remove from set
            (int, int): lambda x, y: x / y,
            (set, float): lambda x, y: x - {y}  # integer division
        }
