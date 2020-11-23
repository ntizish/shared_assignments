"""Custom wrapper for function with a string representation."""


class DefaultOperator:
    """Default operator is a wrapper to a mathematical function with a string form."""

    def __init__(self, function_to_apply, string_repr_of_function):
        """Constructor."""
        self.function_to_apply = function_to_apply
        self.string_repr_of_function = string_repr_of_function

    def __call__(self, *args):
        """Caller."""
        return self.function_to_apply(*args)

    def __str__(self):
        """Stringer."""
        return self.string_repr_of_function


if __name__ == '__main__':
    operator = DefaultOperator(lambda x, y: x + y, "+")
    assert operator.__call__(1, 2) == 3
    assert operator(1, 2) == 3
    assert operator.__str__() == "+"
    assert str(operator) == "+"
