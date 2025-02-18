
'''
Написать рекурсивную функцию, которая принимает 2 аргумента 
(целые числа - a и b) и высчитывает суммы всех чисел от a до b (включительно). 
Пример: a = 3, b = 5 -> 12 (3+4+5)
Пример: a = 5, b = 9 -> 35 (5+6+7+8+9)"

'''
def recursive_sum(a, b):
    
    if a > b:
        return 0  
    else:
        return a + recursive_sum(a + 1, b)  

print(recursive_sum(3, 5))  # Вывод: 12
print(recursive_sum(5, 9))  # Вывод: 35
print(recursive_sum(1, 1))  # Вывод: 1
print(recursive_sum(5, 3))  # Вывод: 0


# решение без рекурсии 

def sum_between(a, b):
    
    if a > b:
        return 0  
    else:
        sum_ab = 0
        for i in range(a, b+1):
            sum_ab = sum_ab + i
        return sum_ab 

print(sum_between(3, 5))  # Вывод: 12
print(sum_between(5, 9))  # Вывод: 35
print(sum_between(1, 1))  # Вывод: 1
print(sum_between(5, 3))  # Вывод: 0