

import pytest
import pytest
@pytest.mark.smoke
def test_addition_file1():
    var1 = 10
    var2 = 20
    assert var1 + var2 == 30
    print("test addition successful")

@pytest.mark.sanity
def test_multiplication_file1():
    var1 = 10
    var2 = 20
    assert var1 * var2 == 200
    print("test multiplication successful")

@pytest.mark.regression
def test_subtraction_file1():
    var1 = 10
    var2 = 200
    assert var2 - var1 == 300
    print("test subtraction successful")




