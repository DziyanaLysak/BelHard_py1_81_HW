'''
Запросить фразу состоящую минимум из трех слов. 
Сформировать фразу из этих слов в которой каждая буква слова, 
продублирована то количество раз, которое соответствует номеру позиции 
данной буквы в слове этой буквы. 
Например: Привет как дела => Прриииввввееееетттттт кааккк деелллаааа

'''

phrase = input("Введите фразу из минимум трёх слов: ")

words = phrase.split()  
if len(words) < 3:
    print("Ошибка: Фраза должна содержать минимум три слова.")
else:
    
    result = []
    for word in words:
        new_word = ""  
        for i, letter in enumerate(word, start=1):  
            new_word += letter * i  
        result.append(new_word)  

   
    print("Результат:", " ".join(result))