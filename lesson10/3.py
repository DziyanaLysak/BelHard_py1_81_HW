"""
Написать функцию которая принимает строку в которой есть 
круглые скобки и возвращает True или False анализируя все ли скобки 
являются закрытыми и расставлены в правильном порядке.
Примеры:
    (()()) -> True
    (()()() -> False
    (hello(2)ver()(33)python) -> True
    (hello(2()ver(33)python)) -> True
    (hello(2()ver(33)python) -> False

"""

def func_bracket(string):
   
    opening_bracket = 0  

    for symbol in string:
        if symbol == '(':
            opening_bracket = opening_bracket + 1  
        elif symbol == ')':
            opening_bracket = opening_bracket - 1  
        if opening_bracket < 0:
            return False  

    return opening_bracket == 0  


print(func_bracket("(()())"))  # Вывод: True
print(func_bracket("(()()()"))  # Вывод: False
print(func_bracket("(hello(2)ver()(33)python)"))  # Вывод: True
print(func_bracket("(hello(2()ver(33)python))"))  # Вывод: True
print(func_bracket("(hello(2()ver(33)python)"))  # Вывод: False