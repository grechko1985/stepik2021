# На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление
# исходной строки обратно. Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с
# помощью кодирования повторов, и производит обратную операцию, получая исходный текст. Запишите полученный текст в
# файл и прикрепите его, как ответ на это задание. В исходном тексте не встречаются цифры, так что код однозначно
# интерпретируем. Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у
# вас появляется ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными
# данными к себе на компьютер. Запустите вашу программу, используя этот файл в качестве входных данных.
# Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.
with open('File1_for_3_9.txt') as dataset:      # открываем файл на чтение
    inf = dataset.readline()                    # считываем строку из файла
numbers = "0123456789"                          # создаем строку от 0 до 9
count = ''                                      # задаем счетчик равным пустой строке
bukva = inf[0]                                  # считываем первую букву строки по нолевому индексу
result = ''                                     # результат пустая строка

for i in inf:                                   # производим цикл по считыванию элементов строки
    if i in numbers:                            # если i присутсвует в строке numbers
        count += i                              # добавляем в строку count это число
    elif i != bukva:                            # если i не не равен bukva
        result = result + bukva * int(count)    # результат записываем в строку
        bukva = i                               # букве присваиваем новое значение
        count = ''                              # строку обнуляем

with open('File2_for_3_9.txt', 'w') as res:     # открываем файл на запись
    res.write(result)                           # записываем в него результат