class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self):
        pass

class CourierDelivery(DeliveryMethod):
    def deliver(self):
        print("Доставка курьером.")

class PostDelivery(DeliveryMethod):
    def deliver(self):
        print("Доставка почтой.")

class PickUpPointDelivery(DeliveryMethod):
    def deliver(self):
        print("Доставка в пункт выдачи.")
