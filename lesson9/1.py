"""
Написать функцию print_n() которая будет печатать переданный текст, 
но при этом перед этим текстом выводить строку с номером отражающим 
какой раз по счету выполняется эта функция. 

"""
text_number = 0  

def print_n(text):
    
    global text_number  
    text_number += 1  
    print(f"№{text_number}: {text}")  

print_n("Hello!")  # Вывод: №1: Hello!
print_n("Нow are you?")  # Вывод: №2: Нow are you?
print_n("Нow is your moodе?")  # Вывод: №3: Нow is your moodе?


# с использованием input()

text_number = 0  

def print_n():
    
    global text_number  
    text_number += 1
    text = input("Введите текст: ")  
    print(f"№{text_number}: {text}") 

print_n()   # Вывод: №1: Привет!
print_n()   # Вывод: №1: Как дела?
print_n()   # Вывод: №1: Как настроение?