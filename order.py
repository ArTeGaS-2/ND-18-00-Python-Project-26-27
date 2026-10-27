class Order:
    def __init__(self):
        self.available_topings = {
            "кетчуп": [0, 10],  # "Ключ":[Кількість в нявності, ціна]
            "курка": [132, 15],
            "сир": [87, 12],
            "Ковбаса": [144, 12],
            "Майонез": [121, 10],
            "Ананас": [111, 14],
            "Маринована Цибуля": [156, 8],
            "Гриби": [138, 13]
            }

        # Пустий список
        self.client_topings = []
        self.choosed_topings = ""
        self.list_of_topings = []
        # Максимум наповнювачів у замовленні
        self.max_topings_count = 5
        self.pizza_size = None

    def pizza_size_choice(self):
        self.pizza_size = input("Доброго дня! Який розмір піцци ви хочете замовити? \n")
        print(f"Ви обрали {self.pizza_size} піццу.")

    def print_topings_in_storage(self):
        print("Наповнювювачі в наявності:")
        for key, value in self.available_topings.items():
            print(f"{key.title()} в наявності.")
            print(f"Ціна: {value[1]} грн")
            print("-----")

    def client_topings_choice(self):
        def client_input():
            is_continue = True
            # Користувач вводить назву наповнювача
            toping = input("Наповнювач: ")
            toping = toping.title()
            # Перебираємо назви і кількість та ціну
            for key, value in self.available_topings.items():
                is_continue = is_continue
                key = key.title()
                # Порівнюємо назву користувача і назву на складі
                if (toping.lower() == key.lower()) and (value[0] > 0):
                    # Додаємо до рядка з переліком обраних наповнювачів нову назву
                    self.choosed_topings += f"{key}, "
                    # Додає обраний наповнювач до списку обраних наповнювачів
                    self.client_topings.append(key)
                elif toping == "-":
                    is_continue = False
                    break
            if is_continue != True:
                return False
            else:
                return True

        topings_count_flag = True

        print(f'Оберіть {self.max_topings_count} наповнювачів. Коли завершите, поставте "-" ')
        self.choosed_topings = "Ви вибрали наступні наповнювачі: \n"

        while topings_count_flag and (len(self.client_topings) <= self.max_topings_count):
            topings_count_flag = client_input()

        print(self.choosed_topings)
