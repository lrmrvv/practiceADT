class DiscountCalculator(ABC):
    @abstractmethod
    def apply_discount(self, total):
        pass

class NoDiscount(DiscountCalculator):
    def apply_discount(self, total):
        return total

class PercentageDiscount(DiscountCalculator):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, total):
        return total - (total * self.percentage / 100)

class FixedAmountDiscount(DiscountCalculator):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply_discount(self, total):
        return total - self.discount_amount
