# Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
# которые встречаются в нём более одного раза. Для решения задачи может пригодиться метод sort списка.
# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
# numbers = [int(i) for i in input('Строка из целых чисел через пробел: ').split()]
current_list, new_list = [int(i) for i in input().split()], []      # создаем два списка - один вводим, а другой пустой
current_list.sort()
for i in current_list:                                              # считываем элементы списка
    if current_list.count(i) > 1 and new_list.count(i) == 0:        # если счетчик встречающего числа > 1 и число не в
        new_list.append(i)                                          # списке 2, то добавить это число в него
for i in new_list:                                                  # считываем поэлементно новый список (список 2)
    print(i, end=" ")                                               # выводим поэлементно в строку все значения списка 2

