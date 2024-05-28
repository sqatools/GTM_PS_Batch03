import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_add():
    var1 = 100
    var2 = 200
    assert var1 + var2 == 300
    print("addition is successful")

@pytest.mark.sanity
def test_sub():
    var1 = 1000
    var2 = 200
    assert var1 - var2 == 300
    print("subtraction is successful")

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.sanity
def test_mul():
    var1 = 10
    var2 = 20
    assert var1 * var2 == 200
    print("multiplication is successful")