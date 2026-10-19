from order import Order

# Змінна що зберігає назву
shop_name = "BEST DELIVERY AND SHOP PIZZA 228 BEST 1337"
# Виводить назву магазину в термінал
print(shop_name)

order_1 = Order()

order_1.pizza_size_choice()
order_1.print_topings_in_storage()
order_1.client_topings_choice()