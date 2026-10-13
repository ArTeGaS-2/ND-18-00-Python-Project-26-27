# Змінна що зберігає назву
shop_name = "BEST DELIVERY AND SHOP PIZZA 228 BEST 1337"





# Виводить назву магазину в термінал
print(shop_name)

# Отримуємо данні від користувача і зберігаємо в client_order

print()



print()

# Цикл, виконує вкладені рядки визначену кількість разів
for _ in range(max_topings_count):
    input_toping = input("Наповнювач: ")
    input_toping.title()

    for toping, num_in_storage in available_topings.items():
        toping.title()
        if input_toping == toping and num_in_storage[0] > 0:
            # Додає елемент до списку
            client_topings.append(toping)
            topings_list += toping + ", "
        elif num_in_storage <= 0:
            

print(topings_list)