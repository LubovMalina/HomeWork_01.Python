#Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

l=(123,'Первый, первый',[1,2,3,4,],('Прием','Прием',1,1),)
index=0
while len(l)>index:
    print(type(l[index]))
    index += 1