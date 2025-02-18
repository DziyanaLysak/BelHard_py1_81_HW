"""
Написать генератор triangular_numbers, который возвращает подряд 
треугольные числа

Формула:
Tn = 1 / 2 * n * (n + 1)

Например:
tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 3
next(tn_gen) -> 6
next(tn_gen) -> 10
next(tn_gen) -> 15
next(tn_gen) -> 21
"""

def triangular_numbers():
    
    n = 1  
    while True:
        Tn = (1 / 2) * n * (n + 1)  
        yield int(Tn)  
        n += 1  

tn_gen = triangular_numbers()

print(next(tn_gen))  # Вывод: 1
print(next(tn_gen))  # Вывод: 3
print(next(tn_gen))  # Вывод: 6
print(next(tn_gen))  # Вывод: 10
print(next(tn_gen))  # Вывод: 15
print(next(tn_gen))  # Вывод: 21