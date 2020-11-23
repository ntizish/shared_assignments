"""."""

from abc import abstractmethod
from tree_node import TreeNode


class Operator(TreeNode):
    """Custom operation wrapper."""

    def __init__(self, *args):
        """Store the given arguments somehow."""
        super().__init__(*args[0])
        self.__value__ = args[0]  # usually tuple of 2 elements

    def apply(self):
        """Make use of the *args to compute the value of the given subtree. Recursion is your friend."""
        params = [x.apply() for x in self.__value__]
        types = tuple(type(x) for x in params)
        if self.actions.get(types):
            return self.actions[types](*params)
        else:
            return self.default_operator(*params)

    @property
    def associativity(self):
        """
        Boolean whether the operation is associative or not.

        For example addition is associative but subtraction is not.
        Override this property for operations where the given operation is not associative.
        """
        return False

    @property
    @abstractmethod
    def actions(self):
        """
        All custom implemented actions on different data structures.

        For example set - int does not exist, but we can implement it.
        :return a dictionary of functions where key is accepted parameters and value is a function which takes the
        aforementioned parameters as inputs and computes a value with them.
        """
        pass

    def __str__(self):
        """String."""
        operator_as_string = f" {self.default_operator.__str__()} "
        values = [x for x in self.__value__]
        string_values = [x.__str__() for x in self.__value__]

        ass0 = values[0].associativity
        pr0 = values[0].priority

        ass1 = values[1].associativity
        pr1 = values[1].priority

        own_ass = self.associativity

        if pr0 == pr1 == 5:
            string_values[0] = f'({string_values[0]})'
            string_values[1] = f'({string_values[1]})'

        elif pr0 > pr1:
            if ass1 is True and pr1 != 5 or own_ass is False:
                string_values[1] = f'({string_values[1]})'
        elif pr1 > pr0:
            if ass0 is True or own_ass is False:
                string_values[0] = f'({string_values[0]})'

        elif pr0 == pr1 != 10 and own_ass is False or pr0 == pr1 == 7:
            string_values[0] = f'({string_values[0]})'
            string_values[1] = f'({string_values[1]})'

        elif pr0 == pr1 == 8 and ass0 is False and own_ass is True:
            string_values[0] = f'({string_values[0]})'
            string_values[1] = f'({string_values[1]})'

        return operator_as_string.join(string_values)

    def __eq__(self, other):
        """It is equal."""
        return self.__value__ == other.__value__ and self.class_str() == other.class_str()
