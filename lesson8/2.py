'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.


'''

def calculate(side1: int, side2: int, square=True):
  
  if square:
    return side1 * side2
  else:
    return 2 * (side1 + side2)

print(f'Площадь: {calculate(3,4)}')  # Вывод: Площадь: 12
print(f'Периметр: {calculate(3, 4, square=False) }') # Вывод: Периметр: 14 