"""
Запросить любое число не менее 10. 
Вывести на экран сумму квадратов каждой цифры составляющей это число. 
Например: дано 236 => 2*2 + 3*3 + 6*6 = 49 

"""

number = input("Введите число не менее 10: ")

if number.isdigit() and int(number) >= 10:
    sum_of_squares = 0
    

    for digit in number:
        
        digit_int = int(digit)
        
        sum_of_squares += digit_int ** 2
    
    
    print("Сумма квадратов цифр числа:", sum_of_squares)
else:
    print("Введите корректное число не менее 10.")
