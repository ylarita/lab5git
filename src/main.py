from calculator import TransportCalculator

def main():
    print("== Калькулятор стоимости доставки груза v1.0 ===")
    calculator = TransportCalculator()

    weight = float(input("Введите вес товара^(kg^): "))
    floor = int(input("Войдите в целевое здание: "))
    has_elevator = input("Есть ли лифт？^(y/n^): ").lower() == 'y'

    result = calculator.calculate_total_cost(weight, floor, has_elevator)

    print(f"\nБазовая плата: {result['base_cost']}Руб")
    print(f"Стоимость ручной обработки: {result['manual_cost']}Руб")
    print(f"Расходы: {result['total_cost']}Руб")

if __name__ == "__main__":
    main()
