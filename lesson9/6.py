"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""
temperature = {"day1": 18, "day2": 22, "day3": 7, "day4": 11, "day5": 14}


increasing = dict(sorted(temperature.items(), key=lambda item: item[1]))
print("Сортировка по возрастанию:", increasing)
# Вывод: Сортировка по возрастанию: {'day3': 7, 'day4': 11, 'day5': 14, 'day1': 18, 'day2': 22}


decreasing = dict(sorted(temperature.items(), key=lambda item: item[1], reverse=True))
print("Сортировка по убыванию:", decreasing)
# Вывод: Сортировка по убыванию: {'day2': 22, 'day1': 18, 'day5': 14, 'day4': 11, 'day3': 7}