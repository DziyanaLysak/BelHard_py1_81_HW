"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").

Если все именованные аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""
def dict_from_args(*args, **kwargs):
      
    args_sum = 0
    for arg in args:
        if not isinstance(arg, int):
            raise TypeError("Все позиционные аргументы должны быть целыми")
        args_sum = args_sum + arg


    kwargs_max_len = 0
    for key, value in kwargs.items():
        if not isinstance(value, str):
            raise TypeError("Все аргументы - ключевые слова должны быть строками")
        kwargs_max_len = max(kwargs_max_len, len(value))

    return {
        "args_sum": args_sum,
        "kwargs_max_len": kwargs_max_len
    }


try:
    print(dict_from_args(14, 8, 2, name="Bob", post="manager", skills="marketing")) 
except TypeError as e:
    print(e) 
# Вывод: {'args_sum': 24, 'kwargs_max_len': 9}

try:
    print(dict_from_args(14, 8, "a", name="Bob"))  
except TypeError as e:
    print(e)
# Вывод: Все позиционные аргументы должны быть целыми

try:
   print(dict_from_args(1, 2, name="Bob", post=385))  
except TypeError as e:
    print(e)
# Вывод: Все аргументы - ключевые слова должны быть строками