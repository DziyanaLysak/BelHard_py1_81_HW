'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))


if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c


print(f"Наибольшее число: {max_num}")