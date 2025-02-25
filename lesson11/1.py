"""
Написать декоратор который позволит не останавливать программу 
в случае если любая декорируемая функция выбрасывает ошибку, 
а выводить имя функции в которой произошла ошибка и информацию об ошибке в. 
Имя функции можно узнать использовав свойство __name__ ( print(func.__name__))

* сделать настраиваемы параметр который определяет печать в консоль или в файл
и если в файл передать название фала
"""

def decorator_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return print(f"Ошибка: {e} в функции {func.__name__}")
            
          
    return wrapper

@decorator_errors
def calculate1(x, y):
    return x / y
print(calculate1(364, 2))  # Вывод:  182.0
print(calculate1(364, 0))  # Вывод:  Ошибка: division by zero в функции calculate
                           #         None

@decorator_errors
def calculate2(x):
    return x * x
print(calculate2(5))       # Вывод: 25
print(calculate2("25"))    # Вывод: can't multiply sequence by non-int of type 'str' в функции calculate2
                           #        None


