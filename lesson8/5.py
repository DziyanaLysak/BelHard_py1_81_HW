'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''

def count_char(text):

  symbolS = {}  

  for symbol in text:  
    if symbol in symbolS:  
      symbolS[symbol] = symbolS[symbol] + 1  
    else:  
      symbolS[symbol] = 1  

  return symbolS  


