'''
Запросить у пользователя число
    - если число менее 20 -  вывести на экран сколько чисел 
        в диапазоне от 0 до этого числа делится без остатка на 7. 
    - если более 20 - вывести на экран сколько чисел 
        в диапазоне от 0 до этого числа делится без остатка на 11.
'''

num = int(input("Введите число: "))


if num < 20:
    a = 0
    for i in range(0, num + 1):
        if i % 7 == 0:  
            a += 1  
    print(f"Количество чисел, делящихся на 7: {a}")
else:
    a = 0
    for i in range(0, num + 1):
        if i % 11 == 0: 
            a += 1 
    print(f"Количество чисел, делящихся на 11: {a}")


