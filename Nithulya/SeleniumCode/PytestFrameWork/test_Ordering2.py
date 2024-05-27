'''
install package : pytest_ordering
pytest.mark.first
pytest.ini file --> contains customized markers
(OR)
pytest.mark.run(order=?)

'''
import pytest
@pytest.mark.run(order=3)
def test_MethodC():
    print('Running test Method C')
@pytest.mark.run(order=4)
def test_MethodD():
    print('Running test Method D')
@pytest.mark.run(order=5)
def test_MethodE():
    print('Running test Method E')
@pytest.mark.run(order=1)
def test_MethodA():
    print('Running test Method A')
@pytest.mark.run(order=2)
def test_MethodB():
    print('Running test Method B')