import Lab_2 as bmi

def test_CalcBMI_underweight():
    expected = -1
    result = bmi.calculate.bmi(1.73,37)
    assert(result == expected)

def test_CalcBMI_normalweight():
    expected = 0
    result = bmi.calculate.bmi(1.73,57)
    assert(result == expected)

def test_CalcBMI_overweight():
    expected = 1
    result = bmi.calculate.bmi(1.73,87)
    assert(result == expected)
