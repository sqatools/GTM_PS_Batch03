"""
# install pytest library, then create test file with test_ as prefix and add test function
python -m pytest -v .\test_smoke_cases.py
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
