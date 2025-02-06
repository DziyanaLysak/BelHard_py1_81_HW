"""
1. Запросить у пользователей имя и отзыв о магазине. 
Программа должна запрашивать данные пока не введено слово "stop". 
Все данные сложить в словарь.
    -распечатать количество отзывов
    -распечатать отдельно имена пользователей
    -распечатать отдельно отзывы

"""

reviews = {}

while True:
    name_user = input("Введите ваше имя (или 'stop' для завершения): ")
    
    if name_user.lower() == "stop":
        break  
    
    feedback = input("Введите ваш отзыв: ")
    
    reviews[name_user] = feedback


print(f"Количество отзывов: {len(reviews)}")

print("Имена пользователей:")
for name_user in reviews.keys():
    print(name_user)
    

print("Отзывы:")
for feedback in reviews.values():
    print(feedback)
