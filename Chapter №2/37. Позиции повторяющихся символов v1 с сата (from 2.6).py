# Напишите программу, которая считывает список чисел lst из первой строки и число xx из второй строки, которая выводит
# все позиции, на которых встречается число xx в переданном списке lst. Позиции нумеруются с нуля, если число xx не
# встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).
l = [int(i) for i in input().split()]       # вводим последовательность символов
x = int(input())                            # вводим число для проверки
if x not in l:                              # если число не всписке
    print('Отсутствует')                    # печатаем, что оно отсуствует
for i in range(len(l)):                     # для i из диапазона от 0 до длины писка
    if l[i] == x:                           # если элемент из списка равен x
        print(i, end=' ')                   # печатаем в строку