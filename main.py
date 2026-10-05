shop_name = "Best pizza ever 2026 1337 best love pizza"

available_topings = {
    "кетчуп": [10, 132],  # "Ключ":[Ціна ,Кількість в нявності]
    "курка": [15, 132],
    "сир": [12, 87],
    "Ковбаса": [12, 144],
    "Майонез": [10, 121],
    "Ананас": [14, 111],
    "Маринована Цибуля": [8, 156],
    "Гриби": [13, 138]
}
list_of_toppings = []

number_of_toppings_in_pizza = 5


print(shop_name)

client_order = input("Доброго дня! Який розмір піцци ви бажаєте замовити? \n")
print(f"Розмір обраної піци: {client_order}")

print()
print("Наповнювачі в наявності:")
for toping, price in available_topings.items():
    print(f"{toping}: {price[0]} грн")

print()

for _ in range(number_of_toppings_in_pizza):
    toping_name = input("Введіть назву: ")

    if toping_name in available_topings:
        list_of_toppings.append(toping_name)
    else:
        print("Невірна назва")
        number_of_toppings_in_pizza += 1




