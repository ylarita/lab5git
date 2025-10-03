from cargo import Cargo
from floor import Floor

class TransportCalculator:
    """运输成本计算器主类"""
    def __init__(self):
        pass

    def calculate_total_cost(self, weight, floor, has_elevator):
        """计算总费用"""
        cargo = Cargo(weight)
        floor_obj = Floor(floor, has_elevator)

        base_cost = cargo.get_base_price()
        manual_cost = floor_obj.calculate_manual_cost(weight)
        total = base_cost + manual_cost

        return {
            'base_cost': base_cost,
            'manual_cost': manual_cost,
            'total_cost': total
        }
