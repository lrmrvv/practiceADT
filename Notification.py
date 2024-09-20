class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Отправка email с сообщением: {message}")

class SmsNotification(Notification):
    def send(self, message):
        print(f"Отправка SMS с сообщением: {message}")
