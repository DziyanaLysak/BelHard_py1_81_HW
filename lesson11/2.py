"""
Написать функцию hello, которая принимает 2 аргумента name и surname и
выводит принтом "Привет, {name} {surname}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
Выполняеся функция <имя> с аргусентами <аргументы> 
После выполнения функции напечатать строку "<имя функции> - завершена"
"""

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняется функция {func.__name__} с аргументами: {args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} - завершена")
        return result
    return wrapper

@log_decorator
def hello(name, surname):
    print(f"Привет, {name} {surname}")

hello("Игорь", "Владимирович")

# Вывод: Выполняется функция hello с аргументами: ('Игорь', 'Владимирович'), {}
#        Привет, Игорь Владимирович
#        hello - завершена