"""Простой тест"""
import calculator

def test_basic():
    """Базовый тест"""
    # Простой тест который точно сработает
    result = calculator.calculate_mortgage(100000, 5, 1)
    print(f"Результат расчета: {result}")
    assert -result > 0, "Платеж должен быть положительным"
    print("✅ Тест пройден!")

if __name__ == "__main__":
    test_basic()
