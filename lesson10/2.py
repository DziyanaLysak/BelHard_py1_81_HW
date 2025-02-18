
"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""

def factorial():
    
    n = 1  
    value_factorial = 1  
    while True:
        yield value_factorial  
        n += 1      
        value_factorial = value_factorial * n   

factorial_gen = factorial()

print(next(factorial_gen))  # Вывод: 1
print(next(factorial_gen))  # Вывод: 2
print(next(factorial_gen))  # Вывод: 6
print(next(factorial_gen))  # Вывод: 24
print(next(factorial_gen))  # Вывод: 120

