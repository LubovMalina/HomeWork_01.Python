'''
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''

my_file = open("task-1.txt", "w", encoding='utf-8')
str = "start"
print("Текст в файл вводится построчно, чтобы закончить запись в файл, просто нажмите Enter.")
while str != "":
    str = input("Введите текст и нажмите Enter, для добавления текста в файл: ")
    my_file.write(str + '\n')
my_file.close()
print("Вы завершили работу с файлом.")