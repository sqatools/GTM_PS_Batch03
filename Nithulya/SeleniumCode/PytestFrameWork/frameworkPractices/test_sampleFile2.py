'''
pytest -rA -m smoke
pytest -rA -m regression
pytest -rA -k (specific method name)  - to run specific testcase.
'''
import pytest
@pytest.mark.smoke
def test_sample4():
    a = 5
    b = 6
    c = a+b
    assert c == 11
@pytest.mark.regression
def test_sample5():
    a = 8
    b = 12
    assert a-b==4
@pytest.mark.smoke
def test_sample6():
    a=12
    b=4
    assert a//b==4
