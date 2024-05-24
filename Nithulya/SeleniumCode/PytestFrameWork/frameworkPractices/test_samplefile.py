'''
  --junit-xml=path      Create junit-xml style report file at given path(if it is in same file, give file name).Also add extension .xml.
--html=file name and path.Also add extension .html
'''
import pytest
@pytest.mark.smoke
def test_sample1():
    a = 5
    b = 6
    assert a == b,"a is not equal to b"   # if test is passed, the message will not display
@pytest.mark.regression
def test_sample2():
    a = 7
    b = 14
    assert a<b
@pytest.mark.smoke
def test_sample3():
    a = 'Nivya'
    b = 'Bhavadas'
    assert a.__eq__(b),"Nivya is not equal to Bhavadas"