"""
Fixture scope:

function scope = function level fixture will execute for each of the test function in the file.
module scope = module level fixture will execute once for each module file
package scope = package level fixture will execute for each of the folder which contains module files.
session scope = session level fixture has wider scope which will initiate with session of automation execution
class scope = class level fixture will execute for specific class only.

"""

import pytest

@pytest.fixture(autouse=True,scope="session")
def setup_and_teardown():
    print('Launch Browser')
    print('Open Application URL in browser')

    yield
    print('Logout from application')
    print('Close Browser')