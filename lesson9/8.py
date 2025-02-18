'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''
data_types = [True, "фильтр", False, "строки", 10, True, 3.14, "логический тип", 2]

str_types = list(filter(lambda x: isinstance(x, str), data_types))
print("Строки:", str_types)
# Вывод: Строки: ['фильтр', 'строки', 'логический тип']

bool_types = list(filter(lambda x: isinstance(x, bool), data_types))
print("Логические значения:", bool_types)
# Вывод: Логические значения: [True, False, True]