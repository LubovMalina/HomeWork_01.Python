#Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чи сел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

list_reiting = [5, 4, 3, 2, 1]
print(f"Рейтинг - {list_reiting}")
number_reiting = int(input("Введите число (00 - выход) "))
while number_reiting != 00:
    for el in range(len(list_reiting)):
        if list_reiting[el] == number_reiting:
            list_reiting.insert(el + 1, number_reiting)
            break
        elif list_reiting[0] < number_reiting:
            list_reiting.insert(0, number_reiting)
        elif list_reiting[-1] > number_reiting:
            list_reiting.append(number_reiting)
        elif list_reiting[el] > number_reiting and list_reiting[el + 1] < number_reiting:
            list_reiting.insert(el + 1, number_reiting)
    print(f"текущий список - {list_reiting}")
    number_reiting = int(input("Введите число (00 - выход) "))