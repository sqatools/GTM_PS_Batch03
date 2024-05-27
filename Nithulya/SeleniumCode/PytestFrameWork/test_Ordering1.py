'''
install package : pytest_ordering
pytest.mark.first
pytest.ini file --> contains customized markers

'''
import pytest
@pytest.mark.third
def test_MethodC():
    print('Running test Method C')
@pytest.mark.fourth
def test_MethodD():
    print('Running test Method D')
@pytest.mark.fifth
def test_MethodE():
    print('Running test Method E')
@pytest.mark.first
def test_MethodA():
    print('Running test Method A')
@pytest.mark.second
def test_MethodB():
    print('Running test Method B')
