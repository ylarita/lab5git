from calculator import TransportCalculator

def main():
    print("=== 货物运输成本计算器 v1.0 ===")
    calculator = TransportCalculator()

    weight = float(input("请输入货物重量^(kg^): "))
    floor = int(input("请输入目标楼层: "))
    has_elevator = input("是否有电梯？^(y/n^): ").lower() == 'y'

    result = calculator.calculate_total_cost(weight, floor, has_elevator)

    print(f"\n基础费用: {result['base_cost']}元")
    print(f"手动搬运费用: {result['manual_cost']}元")
    print(f"总费用: {result['total_cost']}元")

if __name__ == "__main__":
    main()
