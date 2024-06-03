# when we have to execute single case with different type of values
import pytest
from test_data1 import *
@pytest.mark.parametrize("username, password", [
    ('abc', 'a@123'), ('xyz', 'xyz@123'), ('pqr', 'pqr@123')
])

def test_login(username, password):
    db_username = 'xyz'
    db_password = 'xyz@123'
    assert username == db_username and password == db_password, "Invalid credentials"
    print("login successful")

@pytest.mark.parametrize("greeting", greetings_list)
 def test_greeting(greeting):
     assert greeting