"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""

a1 = 4.18         # дробное (float)
a2 = 56           # целое (int)
a3 = "hello"      # строка (str)
a4 = 6.11         # дробное (float)


fractional = all(isinstance(x, float) for x in [a1, a2, a3, a4])

string = any(isinstance(x, str) for x in [a1, a2, a3, a4])



integer_pair = (isinstance(a1, int) and isinstance(a3, int)) or \
                          (isinstance(a2, int) and isinstance(a4, int)) or \
                          (isinstance(a3, int) and isinstance(a4, int))

print(f"Все дробные: {fractional}")
print(f"Есть строка: {string}")
print(f"Есть целочисленная пара: {integer_pair}")