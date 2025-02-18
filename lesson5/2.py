"""
2. Создать структуру данных сотрудников фирмы с 
    тремя сотрудниками. каждый сотрудник должен иметь:
        ФИО, 
        должность, 
        год рождения, 
        список навыков, 
        список детей с их именем и годом рождения. 
    
    Запросить ФИО сотрудника и вывести по нему информацию.
"""

worker1 = {
    "Full Name":"Иванов Иван Иванович", 
    "post":"директор", 
    "birth year":1981, 
    "skills":"управление, менеджмент",
    "children":{'Мария':2004, 'Ольга':2008}
    }
 
worker2 = {
    "Full Name":"Петров Петр Петрович", 
    "post":"бухгалтер", 
    "birth year":1983, 
    "skills":"консалтинг, аудит",
    "children":{'Игрь':2005, 'Анна':2006}
    } 

worker3 = {
    "Full Name":"Сидорова Анна Владимировна", 
    "post":"менеджер", 
    "birth year":1988, 
    "skills":"маркетинг, продажи",
    "children":{'Ирина':2010, 'Олег':2014}
    }
 
workers = {
    "Иванов Иван Иванович":worker1,
    "Петров Петр Петрович":worker2,
    "Сидорова Анна Владимировна":worker3
    }

user_input = input("Ведите Full Name: ")
keys = user_input

print("Информация о сотруднике:")
print(f"Full Name: {workers[keys]["Full Name"]}")
print(f"post: {workers[keys]["post"]}")
print(f"birth year: {workers[keys]["birth year"]}")
print(f"skills: {workers[keys]["skills"]}")
print(f"children: {workers[keys]["children"]}")

# print(f" Информация:{workers.get(input("Ведите Full Name: "))}")


       



