# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

numbers=int(input("Введите целое положительное число: "))

i=0    # счетчик для прохождения по циклу

while numbers>i:
    numbers_max=0
    n=numbers%10
    if numbers_max<n:
        numbers_max = n
    i+=1
    numbers//10
print(f"Самая большая цифра в числе {numbers} -> {numbers_max}")

