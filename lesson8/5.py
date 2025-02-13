'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''

"""
Функция count_char:
Подсчитывает количество вхождений каждой буквы в строку и возвращает словарь.
 
text: Строка, в которой нужно подсчитать буквы.
  
"""
def count_char(text: str):

  symbolS = {}  

  for symbol in text:  
    if symbol in symbolS:  
      symbolS[symbol] = symbolS[symbol] + 1  
    else:  
      symbolS[symbol] = 1  

  return symbolS  

print(count_char("aaaabbbccd"))
 # Вывод: {'a': 4, 'b': 3, 'c': 2, 'd': 1}



