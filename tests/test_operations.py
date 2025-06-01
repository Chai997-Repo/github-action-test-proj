from src.math_operations import add, sub

def test_add():
    assert add(2,3) == 5 # assert func gives the output as true if 2,3 output is equal 5 else it gives false
    assert add(-1,1) == 0
    assert add(100, 500) == 300

def test_sub():
    assert sub(12,10) == 2
    assert sub(20,30) == -10
    assert sub(50,70) == 20