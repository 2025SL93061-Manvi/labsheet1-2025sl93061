import calculator
 
def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    print("add() passed")
 
def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 5) == -5
    print("subtract() passed")
 
def test_multiply():
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-2, 3) == -6
    print("multiply() passed")
 
def test_divide():
    assert calculator.divide(10, 2) == 5.0
    assert calculator.divide(7, 2) == 3.5
    print("divide() passed")
 
if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("\nAll tests passed!")
