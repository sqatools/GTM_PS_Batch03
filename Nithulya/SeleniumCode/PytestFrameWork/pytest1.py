'''
Pytest :
 pytest is a framework by which we can use certain features in automation.

 1) Fixtures
 2) Reports
 3) Parallel Testing
 4) Skip the test
 5) Group tests
 6) Parameterization
  etc...
'''
import pytest
@pytest.fixture()
def setup():
    print('Launching browser')
    yield
    print('Closing browser')
def test_Login(setup):
    print('This is login test')
def test_Search(setup):
    print('This is search test')
def test_AdvancedSearch(setup):
    print('This is advanced search test')
