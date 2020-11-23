"""."""

from default_operator import DefaultOperator
from operators.operator import Operator
from tree_node import TreeNode


class Or(Operator):
    """Custom operation."""

    def __init__(self, left: TreeNode, right: TreeNode):
        """default constructor."""
        super().__init__((left, right))

    @property
    def priority(self):
        """priority of the operation."""
        return 5

    @property
    def associativity(self):
        """
        Boolean whether the operation is associative or not.

        For example addition is associative but subtraction is not.
        Override this property for operations where the given operation is not associative.
        """
        return True

    @property
    def default_operator(self):
        """Make use of the 'operator' library or use a lambda function."""
        return DefaultOperator(lambda x, y: x | int(y) if isinstance(y, float) else x | y, "|")

    @property
    def actions(self):
        """No additional actions needs to be defined here."""
        return {
        }

    def class_str(self):
        """Class string."""
        return f'Or(Leaf({self.__value__[0]}), Leaf({self.__value__[1]}))'

    @property
    def is_bitwise(self):
        """It is bitwise operator."""
        return True
