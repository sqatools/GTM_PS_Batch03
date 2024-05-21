"""
# install pytest library, then create test file with test_ as prefix and add test function
python -m pytest -v .\test_smoke_cases.py
"""



# def func(x):
#     return x + 1
#
#
# def test_answer():
#     assert func(3) == 4
#

import pytest


@pytest.fixture
def order():
    return []


@pytest.fixture
def outer(order, inner):
    order.append("outer")


class TestOne:
    @pytest.fixture
    def inner(self, order):
        order.append("one")

    def test_order(self, order, outer):
        assert order == ["one", "outer"]


class TestTwo:
    @pytest.fixture
    def inner(self, order):
        order.append("two")

    def test_order(self, order, outer):
        assert order == ["two", "outer"]









"""
def test_addition():
    var1 = 10
    var2 = 20
    assert var1 + var2 == 30


def test_multiplication():
    var1 = 10
    var2 = 20
    assert var1 * var2 == 200


def test_subtraction():
    var1 = 10
    var2 = 200
    assert var2 - var1 == 300


def division():
    var1 = 10
    var2 = 20
    assert var1 // var2 == 30
"""