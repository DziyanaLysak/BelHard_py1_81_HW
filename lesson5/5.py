"""
Запросить фразу 
    - вывести на экран количество уникальных символов
    - вывести на экран количество уникальных слов
    -* вывести символ который встречался чаще всего

"""

phrase = input("Введите фразу: ")

a = set(phrase)
 
print("Количество уникальных символов:", len(a))

words = phrase.split()
  
b = set(words)
print("Количество уникальных слов:", len(b))

from collections import Counter 

collect = Counter(phrase)
most, count = collect.most_common(1)[0]
print(f"Самый частый символ: '{most}' (встречается {count} раз)")
