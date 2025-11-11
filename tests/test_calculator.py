import pytest
from calculator import FinanceCalculator


@pytest.fixture
def calculator():
    """Фикстура для создания экземпляра калькулятора перед каждым тестом"""
    return FinanceCalculator()

def test_initial_balance(calculator):
    """Тест начального баланса"""
    assert calculator.get_balance() == 0

def test_add_income(calculator):
    """Тест добавления дохода"""
    calculator.add_income(1000, "Зарплата")
    assert calculator.get_balance() == 1000
    assert calculator.get_transactions() == [("Зарплата", 1000)]

def test_add_income_with_default_description(calculator):
    """Тест добавления дохода с описанием по умолчанию"""
    calculator.add_income(500)
    assert calculator.get_balance() == 500
    assert calculator.get_transactions() == [("Доход", 500)]

def test_add_expense(calculator):
    """Тест добавления расхода"""
    calculator.add_income(1000)
    calculator.add_expense(500, "Продукты")
    assert calculator.get_balance() == 500
    assert calculator.get_transactions() == [("Доход", 1000), ("Продукты", -500)]

def test_add_expense_with_default_description(calculator):
    """Тест добавления расхода с описанием по умолчанию"""
    calculator.add_income(1000)
    calculator.add_expense(300)
    assert calculator.get_balance() == 700
    assert calculator.get_transactions() == [("Доход", 1000), ("Расход", -300)]

def test_invalid_income_amount(calculator):
    """Тест невалидной суммы дохода"""
    with pytest.raises(ValueError, match="Доход должен быть больше 0."):
        calculator.add_income(-100)

def test_invalid_income_amount_zero(calculator):
    """Тест нулевой суммы дохода"""
    with pytest.raises(ValueError, match="Доход должен быть больше 0."):
        calculator.add_income(0)

def test_invalid_expense_amount(calculator):
    """Тест невалидной суммы расхода"""
    with pytest.raises(ValueError, match="Расход должен быть больше 0."):
        calculator.add_expense(-50)

def test_invalid_expense_amount_zero(calculator):
    """Тест нулевой суммы расхода"""
    with pytest.raises(ValueError, match="Расход должен быть больше 0."):
        calculator.add_expense(0)

def test_multiple_transactions(calculator):
    """Тест нескольких транзакций"""
    calculator.add_income(2000, "Зарплата")
    calculator.add_income(500, "Премия")
    calculator.add_expense(300, "Еда")
    calculator.add_expense(700, "Аренда")
    
    assert calculator.get_balance() == 15000  # 2000 + 500 - 300 - 700 = 1500
    assert len(calculator.get_transactions()) == 4

# Дополнительные тесты для проверки точности вычислений с плавающей точкой
def test_float_operations(calculator):
    """Тест операций с дробными числами"""
    calculator.add_income(1000.50)
    calculator.add_expense(250.75)
    
    # Используем приблизительное сравнение для float
    assert abs(calculator.get_balance() - 749.75) < 0.01

print("Тесты все!")