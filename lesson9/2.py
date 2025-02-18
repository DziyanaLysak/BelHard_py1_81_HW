'''
Написать рекурсивную функцию, которая вычисляет  
факториал переданного в нее числа.

'''

def factorial(n):
    
    if n < 0:
        return "Ошибка. Отрицательное число"
    elif n == 0:
        return 1 
    else:
        return n * factorial(n - 1) 

print(factorial(4))  # Вывод: 24
print(factorial(0))  # Вывод: 1
print(factorial(-1)) # Вывод: Ошибка. Отрицательное число