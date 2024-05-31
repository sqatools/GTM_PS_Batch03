import pytest


env = 'production'

@pytest.mark.smoke
@pytest.mark.regression
def addition_sk_marker():
    a = 20
    b = 30
    assert a + b == 50
    print("addition was successful")

@pytest.mark.sanity
@pytest.mark.skip
def multilplication_sk_marker():
    a = 20
    b = 30
    assert a * b == 600
    print("multilplication was successful")


@pytest.mark.sanity
@pytest.mark.smoke
def subtraction_sk_marker():
    a = 200
    b = 100
    assert a - b == 600
    print("subtraction was successful")

@pytest.mark.sanity
@pytest.mark.skipif(env == 'production', reason="cannot execute on production server")
def division_sk_marker():
    a = 200
    b = 100
    assert a - b == 600
    print("division was successful")