'''
Написать функцию, которая вычисляет  факториал переданного в нее числа без рекурсии.

'''

"""
Функция calculate_factorial: Вычисляет факториал числа n (n!).

n: Целое число, факториал которого нужно вычислить.

"""
def calculate_factorial(n):
  
  if not isinstance(n, int):
    raise TypeError("Должно быть целое число")
  if n < 0:
    raise ValueError("Отрицательное число")

  factorial = 1
  for i in range(1, n + 1):
    factorial = factorial * i

  return factorial

print(calculate_factorial(4))   # Вывод: 24
print(calculate_factorial(0))   # Вывод: 1
# print(calculate_factorial(-1))  # Вывод: raise ValueError("Отрицательное число")
# print(calculate_factorial(3.5))  # Вывод: raise TypeError("Должно быть целое число")