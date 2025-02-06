'''
Запросить любое число. Заменить каждую цифру этого числа буквой, 
у которой номер в алфавите равен этой цифре. 
Например: 1352=aceb.
'''

num_user = input("Введите число: ")


abc = {
    '0': 'a',  
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f',
    '7': 'g',
    '8': 'h',
    '9': 'i'
}

result = ""
for digit in num_user:
    if digit in abc:  
        result += abc[digit]
    else:
        result += digit 

print("Результат:", result)
