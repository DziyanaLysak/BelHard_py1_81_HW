'''
Запросить высоту елочки - число от 3 до 20. 
Напечатать на экране елочку где ее высота равна числу строк. 
Пример елочки из 4 строк:
   *
  ***
 *****
*******

'''

height = int(input("Введите высоту ёлочки (от 3 до 20): "))

if 3 <= height <= 20:
    for i in range(1, height + 1):  
        
        void = " " * (height - i)  
        stars = "*" * (2 * i - 1)   
        print(void + stars)       
else:
    print("Ошибка: Высота должна быть от 3 до 20.")