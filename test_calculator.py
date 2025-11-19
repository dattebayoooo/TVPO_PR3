"""Тесты для калькулятора"""
import calculator

def test_mortgage_calculation():
    """Тест расчета ипотеки"""
    result = calculator.calculate_mortgage(1000000, 7.5, 10)
    expected = 11865.84
    assert abs(result - expected) < 0.1, f"Ожидалось {expected}, получено {result}"

def test_zero_interest():
    """Тест с нулевой ставкой"""
    result = calculator.calculate_mortgage(120000, 0, 1)
    assert result == 10000.0

def test_another_case():
    """Тест другого случая"""
    result = calculator.calculate_mortgage(500000, 5, 5)
    assert result > 0

if __name__ == "__main__":
    test_mortgage_calculation()
    test_zero_interest()
    test_another_case()
    print("Все тесты прошли!")