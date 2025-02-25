"""
Создать класс Student.


Определить атрибуты:
    - surname - фамилия
    - name - имя
    - group - номер группы
    - grads - список оценок

Определить методы:
    - инициализатор __init__
    - Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
    студентов по среднему баллу
    - метод add_grade - добавляет в список оценок одну или несколько оценок от 1 до 10
    - метод average_grade -считает и возвращает среднюю оценку ученика

Создать список из 5 студентов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 8
"""

class Student:
    
    def __init__(self, surname, name, group):
        self.surname = surname
        self.name = name
        self.group = group
        self.grades = []

    def __eq__(self, other):   # равенство 
        return self.average_grade() == other.average_grade()
    
    def __ne__(self, other):   # неравенство 
        return self.average_grade() != other.average_grade()
    
    def __lt__(self, other):   # меньше 
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):   # больше
        return self.average_grade() > other.average_grade()

    def __le__(self, other):   # меньше или равно
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):   # больше или равно
        return self.average_grade() >= other.average_grade()
    
    def add_grade(self, grades): 
        for grade in grades:
            if 1 <= grade <= 10:
                self.grades.append(grade)
            else:
                print(f"Оценка должна быть от 1 до 10.")
    
    def average_grade(self):
        if self.grades == []:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.surname} {self.name}, группа {self.group}, средний балл: {self.average_grade():.2f}"


students = [
    Student("Зайцев", "Максим", "ML01"),
    Student("Гусев", "Андрей", "ML02"),
    Student("Голубев", "Антон", "ML03"),
    Student("Комаров", "Дмитрий", "ML04"),
    Student("Орлов", "Сергей", "ML05"),
]

students[0].add_grade([9, 10, 7])
students[1].add_grade([7, 8, 9])
students[2].add_grade([10, 8, 10])
students[3].add_grade([7, 7, 8])
students[4].add_grade([6, 9, 10])


students_rise = sorted(students)
print("Студенты по возрастанию среднего балла:")
print(*students_rise, sep="\n")

print()

students_wane = sorted(students, reverse=True)
print("Студенты по убыванию среднего балла:")
print(*students_wane, sep="\n")

print()

print("Студенты со средним баллом больше 8:")
for student in students:
    if student.average_grade() > 8:
        print(student)