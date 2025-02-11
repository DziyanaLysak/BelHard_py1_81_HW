'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''

def calculate(side1, side2, square=True):
  
  if square:
    return side1 * side2
  else:
    return 2 * (side1 + side2)
