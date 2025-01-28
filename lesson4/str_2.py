'''
Программа должна запросить несколько цифр через пробел 
    - выдать их общую сумму
    - выдать максимальную цифру
    - выдать среднее арифметическое

'''

user_str = (input('Введите несколько цифр через пробел:'))
print(user_str)

text_list = list(map(int, user_str.split()))

# сумма
print(sum(text_list))

# максимальная цифра
print(max(text_list))

# среднее арифметическое
average = sum(text_list)/len(text_list)
print(f'{average:.2f}')
