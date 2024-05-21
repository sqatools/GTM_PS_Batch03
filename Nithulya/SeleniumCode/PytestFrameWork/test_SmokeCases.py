"""
# install pytest library, then create test file with test_ as prefix and add test function
python -m pytest -v .\test_smoke_cases.py
"""

def testAddition():
    var1 = 10
    var2 = 20
    assert var1 + var2 == 30
def testMultiplication():
    var1 = 10
    var2 = 20
    assert var1 * var2 == 200
def testSubtraction():
    var1 = 10
    var2 = 210
    assert var2 - var1 == 300
def division():   # without adding test in function name.
    var1 = 10
    var2 = 20
    assert var1 // var2 == 30