import pytest


class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_LoginByEmail(self):
        print("This is login by email..")
        assert True == True

    @pytest.mark.regression
    def test_LoginByFacebook(self):
        print("This is login by facebook..")
        assert True == True

    @pytest.mark.regression
    def test_LoginByTwitter(self):
        print("This is login by twitter..")
        assert True == True
