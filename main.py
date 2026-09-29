shop_name = "Best pizza ever 2026 1337 best love pizza"

available_topings = {
    "Сир":[25, 141],  # Ціна, кількість наявності
    "Ковбаса":[34, 122]
}
list_of_toppings = []

print(shop_name)

client_order = input("Доброго дня! Який розмір піцци ви бажаєте замовити? \n")
print(f"Розмір обраної піци: {client_order}")

print("Оберіть до 5 наповнювачів: ")
for _ in range(5):
    toping = input("Введіть назву наповнювача: ")
    list_of_toppings.append(toping)

print("Обрані наповнювачі: ")
for toping in list_of_toppings:
    print(toping)

