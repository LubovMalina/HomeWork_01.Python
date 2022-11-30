# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month=int(input("Введите месяц от 1 до 12: "))

month_list=['Зима','Весна','Лето','Осень']
month_dict={1:'Зима',2:'Весна',3:'Лето',4:'Осень'}


if 1<=month<=2 or month==12:
    print(month_list[0])
    print(month_dict.get(1))
elif 3<=month<=5:
    print(month_list[1])
    print(month_dict.get(2))
elif 6<=month<=8:
    print(month_list[2])
    print(month_dict.get(3))
elif 9<=month<=11:
    print(month_list[3])
    print(month_dict.get(4))
else:
    print("Такого месяца не существует")


