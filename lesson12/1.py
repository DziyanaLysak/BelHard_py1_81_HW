"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: 
        <Бренд-Модель> - Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""
class Phone:
    
    def __init__(self, brand, model, issue_year):
        print("__init__")
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, name):
        print(f"<{self.brand}-{self.model}> - Звонит {name}")

    def get_info(self):
        return (self.brand, self.model, self.issue_year)
    
    def __str__(self):
        print("__str__")
        return f"""Бренд: {self.brand}
Модель: {self.model}
Год выпуска: {self.issue_year}"""
    
ph1 = Phone("Samsung", "Galaxy S25", 2022)

ph1.receive_call("Валентина")  

ph1_inf = ph1.get_info()
print(ph1) 
