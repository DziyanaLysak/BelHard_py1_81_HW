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
    "ФИО":"Иванов Иван Иванович", 
    "должность":"директор", 
    "год рождения":1981, 
    "навыки":"управление, менеджмент",
    "дети":{'Мария':2004, 'Ольга':2008}
    }
 
worker2 = {
    "ФИО":"Петров Петр Петрович", 
    "должность":"бухгалтер", 
    "год рождения":1983, 
    "навыки":"консалтинг, аудит",
    "дети":{'Игрь':2005, 'Анна':2006}
    } 

worker3 = {
    "ФИО":"Сидорова Анна Владимировна", 
    "должность":"менеджер", 
    "год рождения":1988, 
    "навыки":"ммаркетинг, продажи",
    "дети":{'Ирина':2010, 'Олег':2014}
    }
 
workers = {
    "Иванов Иван Иванович":worker1,
    "Петров Петр Петрович":worker2,
    "Сидорова Анна Владимировна":worker3
    }

user_input = input("Ведите ФИО: ")
keys = user_input

print("Информация о сотруднике:")
print(f"ФИО: {workers[keys]["ФИО"]}")
print(f"Должность: {workers[keys]["должность"]}")
print(f"Год рождения: {workers[keys]["год рождения"]}")
print(f"Навыки: {workers[keys]["навыки"]}")
print(f"Дети: {workers[keys]["дети"]}")

# print(f" Информация:{workers.get(input("Ведите ФИО: "))}")


       



