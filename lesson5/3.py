"""
дан словарь
d = {'one':11, 'two':22, 'hello':'python', True:False}
запросить номер элемента и удалить его из словаря с помощью del.

"""

d = {'one': 11, 'two': 22, 'hello': 'python', True: False}

keys_list = list(d.keys())
print(keys_list)     # ['one', 'two', 'hello', True]

user_el = int(input("Введите номер элемента для удаления (начиная с 0): "))

deleted = keys_list[user_el]
print(deleted)   

del d[deleted]

print("Обновлённый словарь:", d)



