'''
Skipping : @pytest.mark.skip
'''


import pytest

def test_loginByEmail():
    print('This is login by Email')
    assert 1==1
def test_loginByFacebook():
    print('This is login by Facebook')
    assert 1==1
def test_loginByTwitter():
    print('This is login by Twitter')
    assert 1==1
@pytest.mark.skip
def test_SignupByEmail():
    print('This is signup by Email')
    assert 1==1
@pytest.mark.skip
def test_SignupByFacebook():
    print('This is signup by Facebook')
    assert 1==1
@pytest.mark.skip
def test_SignupByTwitter():
    print('This is signup by Twitter')
    assert 1==1