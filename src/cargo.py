class Cargo:
    """货物类 - 管理货物信息和折扣"""
    def __init__(self, weight, discount=0):
        self.weight = weight
        self.discount = discount

    def get_base_price(self):
        """根据重量计算基础价格"""
        if self.weight <= 50:
            base = 300
        elif self.weight <= 100:
            base = 1000
        elif self.weight <= 300:
            base = 2000
        else:
            base = 2000 + (self.weight - 300) * 10
        return base * (1 - self.discount)

    def __str__(self):
        return f"货物重量: {self.weight}kg, 折扣: {self.discount*100}%"
