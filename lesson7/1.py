"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
Выдать средний бал ученика.
"""

total = 0  
count = 0 

while True:
    grade = int(input("Введите оценку (или 0 для завершения): "))
    
    if grade == 0:
        break  
    
    total += grade
    count += 1

if count > 0:  
    average = total / count
    print(f"Средний балл ученика: {average:.2f}")
else:
    print("Оценки не были введены.")