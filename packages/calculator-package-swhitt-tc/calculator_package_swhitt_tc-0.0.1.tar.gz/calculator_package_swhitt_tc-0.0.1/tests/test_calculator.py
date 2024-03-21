from calculator import Calculator

c = Calculator()
c.default_num = 0

def test_add():
    assert c.add(5) == 5
    
def test_subtract():
    assert c.subtract(2) == 3
    
def test_multiply():
    assert c.multiply(4) == 12
    
def test_divide():
    assert c.divide(3) == 4
    
def test_nth_root():
    assert c.nth_root(2) == 2
    
def test_reset():
    assert c.reset() == 0
    assert c.reset(10) == 10
