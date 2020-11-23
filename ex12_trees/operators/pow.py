"""."""

from default_operator import DefaultOperator
from operators.operator import Operator
from tree_node import TreeNode


class Pow(Operator):
    """Custom operation."""

    def __init__(self, left: TreeNode, right: TreeNode):
        """default constructor."""
        super().__init__((left, right))

    @property
    def priority(self):
        """priority of the operation."""
        return 10

    @property
    def default_operator(self):
        """Make use of the 'operator' library or use a lambda function."""
        return DefaultOperator(lambda x, y: x ** y, "**")

    @property
    def actions(self):
        """No additional actions needs to be defined here."""
        return {
        }

    @property
    def associativity(self):
        """
        Boolean whether the operation is associative or not.

        For example addition is associative but subtraction is not.
        Override this property for operations where the given operation is not associative.
        """
        return False

    @property
    def is_bitwise(self):
        """It is operator."""
        return True
