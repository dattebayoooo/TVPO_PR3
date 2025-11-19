"""Модуль для расчета ипотеки"""


def calculate_mortgage(amount, rate, years):
    """Простой расчет ипотеки"""
    monthly_rate = rate / 100 / 12
    months = years * 12

    if monthly_rate == 0:
        return amount / months

    payment = amount * monthly_rate * (1 + monthly_rate)**months / ((1 + monthly_rate)**months - 1)
    return round(payment, 2)


def main():
    """Основная функция"""
    print("=== Ипотечный калькулятор ===")

    amount = float(input("Сумма кредита: "))
    rate = float(input("Процентная ставка: "))
    years = int(input("Срок (лет): "))

    monthly = calculate_mortgage(amount, rate, years)
    total = monthly * years * 12

    print("\nРезультат:")
    print(f"Ежемесячный платеж: {monthly} ₽")
    print(f"Общая сумма: {total} ₽")
    print(f"Переплата: {total - amount} ₽")


if __name__ == "__main__":
    main()
