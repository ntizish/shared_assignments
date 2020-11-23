"""."""

import pytest

from operators.div import Div
from operators.leaf import Leaf
from operators.add import Add
from operators.sub import Sub
from operators.mul import Mul
from operators.pow import Pow
from operators.or_ import Or
from operators.and_ import And
from operators.xor import Xor

@pytest.mark.timeout(1.0)
def test_leaf_to_class_string():
    """Done."""
    assert eval(Leaf(6).class_str()).apply() == 6


@pytest.mark.timeout(1.0)
def test_addition_with_leaves_to_class_string():
    """Done."""
    assert eval(Add(Leaf(5), Leaf(6)).class_str()).apply() == 11


@pytest.mark.timeout(1.0)
def test_subtraction_with_leaves_to_class_string():
    """Done."""
    assert eval(Sub(Leaf(5), Leaf(6)).class_str()).apply() == -1


@pytest.mark.timeout(1.0)
def test_leaf_to_string():
    """Done."""
    assert Leaf(7).__str__() == "7"


@pytest.mark.timeout(1.0)
def test_addition_with_leaves_to_string():
    """Done."""
    tree = Add(Leaf(5), Leaf(6))
    assert tree.apply() == 11
    assert tree.__str__() == "5 + 6"


@pytest.mark.timeout(1.0)
def test_subtraction_with_leaves_to_string():
    """Done."""
    tree = Sub(Leaf(6), Leaf(6))
    assert tree.apply() == 0
    assert tree.__str__() == "6 - 6"


@pytest.mark.timeout(1.0)
def test_division_given_addition_to_string():
    """."""
    tree = Add(Leaf(3), Div(Add(Leaf(12), Leaf(6)), Leaf(6)))
    """assert tree.apply() == 3"""
    assert tree.__str__() == '3 + (12 + 6) / 6'


@pytest.mark.timeout(1.0)
def test_division_given_addition_to_string():
    """."""
    tree = Add(Sub(Leaf(5), Leaf(6)),Sub(Leaf(5), Leaf(6)))
    """assert tree.apply() == 3"""
    assert tree.__str__() == "(5 - 6) + (5 - 6)"


@pytest.mark.timeout(1.0)
def test_bitwise_or_given_bitwise_and_given_div_given_mul_given_bitwise_pow_to_string():
    """."""
    tree = Or(And(Leaf(3), Div()),)
    assert tree.__str__() == "3 & 1 | 5 ** 2 * 1 / 5 & 2"
