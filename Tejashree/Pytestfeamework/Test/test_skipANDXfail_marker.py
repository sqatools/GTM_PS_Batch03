import pytest
env = "Prod"
@pytest.mark.skip
@pytest.mark.smoke
def test_addition_file3():
    var1 = 10
    var2 = 20
    assert var1 + var2 == 30
    print("test addition successful")

@pytest.mark.skipif(env =="Prod", reason="cannot execute on production server")
@pytest.mark.sanity
def test_multiplication_file3():
    var1 = 10
    var2 = 20
    assert var1 * var2 == 200
    print("test multiplication successful")

# Xfail marker - used when test cases are flacky(it may fail or pass)
@pytest.mark.regression
@pytest.mark.xfail
def test_add_first_10():
     sum = 0
     for i in range(1, 11):
         sum += 1
     assert sum > 20
     print("addition of first 10 numbers")
@pytest.mark.regression
@pytest.mark.xfail
def test_product_values():
    sum = 0
    for i in range(1, 11):
     sum = sum * i
    assert sum == 50

@pytest.mark.regression
def test_subtraction_file3():
    var1 = 100
    var2 = 200
    assert var2 - var1 == 100
    print("test subtraction successful")