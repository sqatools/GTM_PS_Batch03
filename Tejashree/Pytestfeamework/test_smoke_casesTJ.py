"""
# install pytest library, then create test file with test_ as prefix and add test function
python -m pytest -v .\test_smoke_cases.py
"""
import pytest

@pytest.fixture(scope='function')
def setup():
    print("execution started")
    yield
    print("\n execution completed")

def test_addition(setup):
    var1 = 20
    var2 = 30
    assert var1 + var2 == 50
    print("addition is successful")

def test_subtraction(setup):
    var1 = 50
    var2 = 20
    assert var1 - var2 == 30
    print("subtraction is successful")

def test_multilply(setup):
    var1 = 20
    var2 = 30
    assert var1 * var2 == 50

def division():
    var1 = 100
    var2 = 20
    assert var1//var2 == 5