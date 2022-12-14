'''
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо
предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении
числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
'''

from itertools import count, cycle

j=0
while j <=0:
    try:
        j = int(input('Введите целое число больше 0 с которого начнется генерация целых чисел: '))
    except:
        j = 0
count_number = 0
while count_number <=0:
    try:
        count_number = int(input('Введите количество чисел, которые нужно сгенерировать: '))
    except:
        count_number=0

for i in count(j):
    if i >= j + count_number:
        break
    else:
        print(i, end=' ')
print()

# итератор повторяет элементы столько же раз сколько чисел в  первом итераторе генерит.
# список формируется динамически от 0 до числа с которого начинается генерация целых чисел в первом итераторе.
value = 0
for element in cycle([element for element in range(j)]):
    if value >= count_number:
        break
    print(element, end=' ')
    value += 1