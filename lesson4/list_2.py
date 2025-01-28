'''
Запросить по очереди у пользователя 5 имен. Добавить все в список. 
Отсортировать. 
Вывести на экран.
Вывести True при наличии в списке имени 'Вася'
'''

# если ввести к примеру имена Коля, Маша, Вася, Боря, Аня по очереди
name_1 = input('Введите 1-е имя:')
name_2 = input('Введите 2-е имя:')
name_3 = input('Введите 3-е имя:')
name_4 = input('Введите 4-е имя:')
name_5 = input('Введите 5-е имя:')

names = list([name_1, name_2, name_3, name_4, name_5])
print(names)
# >>>>  ['Коля', 'Маша', 'Вася', 'Боря', 'Аня']

names.sort()
print(names)
# >>>> ['Анна', 'Боря', 'Вася', 'Коля', 'Маша']

el = 'Вася'
if el in names:
    print(True)
else:
    print(False)
# >>>> True