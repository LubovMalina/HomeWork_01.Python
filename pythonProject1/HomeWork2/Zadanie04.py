#Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

stroka=input("Введите предложение: ").split(" ")
for j in range(len(stroka)):
    if len(stroka[j])<=10:
        print(j,stroka[j])
    else:
        print(j, stroka[j][0:10])