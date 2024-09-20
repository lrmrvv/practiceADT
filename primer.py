order = Order()

order.mprod("Ноутбук", 1, 1000)
order.mprod("Мышь", 2, 50)

order.mpayType(CreditCardPayment())
order.mdelivery_method(CourierDelivery())

order.mdiscount_calculator(PercentageDiscount(10))

print(f"Общая стоимость заказа: {order.calculate_total()}")

order.checkout()

notification = EmailNotification()
notification.send("Ваш заказ успешно оформлен.")
