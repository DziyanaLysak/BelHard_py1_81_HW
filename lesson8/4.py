'''

Написать функцию, которая возвращает любое число в виде денежной величины 
с разделителями групп разрядов в качестве пробела и валютой в конце. 
Денежная величина всегда должна содержать количество копеек в виде дух 
знаков после точки, даже если исходное число целое. 
*Нельзя использовать форматную строку.
Например: 1234567 -> "1 234 567.00 руб."

с помощью try перехватить возможные ошибки.
'''

"""
Функция monetary: Преобразует число в денежный формат: разделители пробелами, копейки, "руб.".
    
number: Число (int или float).

"""
def monetary(number):
    
    try:
    
        if not isinstance(number, (int, float)):
            return "Ошибка: Введите число!"

        integer_part = int(number) 
        pennies = int(round((number - integer_part) * 100))  

        pennies_str = str(pennies).zfill(2)  

        integer_part_formatted = ""
        categories = str(integer_part)[::-1]  
        for i, digit in enumerate(categories):
            integer_part_formatted += digit
            if (i + 1) % 3 == 0 and i != len(categories) - 1:  
                integer_part_formatted += " "

        integer_part_formatted = integer_part_formatted[::-1] 

        result = integer_part_formatted + "." + pennies_str + " руб."

        return result

    except Exception as exception:
        return f"Произошла ошибка: {exception}"

print(monetary(1234567)) # Вывод: 1 234 567.00 руб.
print(monetary("a")) # Вывод: Ошибка: Введите число!


