class Cargo:
    """货物类 - 管理货物信息"""
    def __init__(self, weight):
        self.weight = weight

    def get_base_price(self):
        """根据重量计算基础价格 - 调整后的价格"""
        if self.weight <= 50:
            return 350
        elif self.weight <= 100:
            return 1100
        elif self.weight <= 300:
            return 2200
        else:
            return 2200 + (self.weight - 300) * 10

    def __str__(self):
        return f"货物重量: {self.weight}kg"
