"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""

def yes_or_no(numbers):
    
    for num in numbers:
        if isinstance(num, int) != True:  
            return False

    seen = set()
    result = []  

    for num in numbers:
        if num in seen:
            result.append("Yes")  
        else:
            result.append("No") 
            seen.add(num)  

    return result

print(yes_or_no([1, 1, 2, 3, 4]))  # Вывод: ['No', 'Yes', 'No', 'No', 'No']
print(yes_or_no([1, 2, 3, 1, "l"])) # Вывод: False
