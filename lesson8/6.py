"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""
def yes_or_no(numbers):
    """
    Принимает список целых чисел и возвращает список 'Yes' или 'No',
    указывающих, встречалось ли число ранее в списке.

    Args:
        numbers: Список чисел.

    Returns:
        Список строк ('Yes' или 'No') или False, если входной список
        содержит не целые числа.
    """


    for num in numbers:
        if isinstance(num, int) == False:  
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

