"""
Написать функцию (без регулярных выражений), которая принимает текстовую строку 
и возвращает словарь, который содержит информацию о количестве 
символов, слов, строк и предложений в тексте. 
Затем создайте вторую функцию, которая принимает этот словарь, 
и выводит его содержимое в удобном и красивом формате. 

"""

def text_analysis(text):

    count_symbols = len(text)

    count_strings = text.count('\n') + 1

    count_words = len(text.split())

    count_sentences = text.count('.') + text.count('!') + text.count('?')

    result = {
        "symbols": count_symbols,
        "words": count_words,
        "strings": count_strings,
        "sentence": count_sentences,
    }

    return result

text = """London is the capital of Great Britain, its political, economic and cultural centre! 
          It’s one of the largest cities in the world. Its population is more than 9 million people. 
          London is situated on the river Thames. 
          It was founded more than two thousand years ago."""

print(text_analysis(text))
# Вывод: {'symbols': 297, 'words': 46, 'strings': 4, 'sentence': 5}

"""
Функция get_results : Выводит содержимое словаря в удобном и красивом формате.

dictionary: Словарь с результатами анализа функции text_analysis.

"""
def get_results(dictionary):

    print("Результаты анализа текста:")
    print(f"Символов: {dictionary['symbols']}")
    print(f"Слов: {dictionary['words']}")
    print(f"Строк: {dictionary['strings']}")
    print(f"Предложений: {dictionary['sentence']}")

dictionary = text_analysis(text)
get_results(dictionary)

# Вывод:  Результаты анализа текста:
#         Символов: 297
#         Слов: 46
#         Строк: 4
#         Предложений: 5


