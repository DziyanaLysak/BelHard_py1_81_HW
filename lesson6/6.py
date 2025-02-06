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



if type(a1) == float and type(a2) == float and type(a3) == float and type(a4) == float:
    print("1) Все переменные дробные:", True)
else:
    print("1) Все переменные дробные:", False)



if type(a1) == str or type(a2) == str or type(a3) == str or type(a4) == str:
    print("2) Хотя бы одна переменная строка:", True)
else:
    print("2) Хотя бы одна переменная строка:", False)


if (
    (type(a1) == int and type(a3) == int) or 
    (type(a2) == int and type(a4) == int) or 
    (type(a3) == int and type(a4) == int)
    ):
    print("3) Есть одна пара целочисленных переменных:", True)
else:
    print("3) Есть одна пара целочисленных переменных:", False)