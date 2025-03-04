"""

Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты(свойства):
    - value - текущее значение счетчика
    ...

Определить методы:
    - инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
    - increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
    - decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
    - reset, сбрасывает значение счетчика на стартовое   
    - метод __iter__
    - метод __next__
    
    * - stat, возвращает среднее количество изменений счетчика в секунду

"""

class Counter:

    def __init__(self, start=0):
        self.value = start  
        self.start_value = start 

    def increase(self, num=1): #увеличивает счетчик
        self.value = self.value + num 

    def decrease(self, num=1):  # уменьшает счетчик
        self.value = self.value - num  

    def reset(self):    # сбрасывает значение счетчика на стартовое
        self.value = self.start_value 
            
    def __iter__(self):
        self.current = self.start_value # Начинаем с начального значения
        return self 

    def __next__(self):
        if self.current <= self.value: 
            result = self.current 
            self.current = self.current + 1 
            return result 
        else: 
            raise StopIteration 

    
counter1 = Counter(start=3)  
print(f"Начальное значение счетчика: {counter1.value}")  

counter1.increase(5)  
print(f"Счетчик увеличился: {counter1.value}")  

counter1.decrease(1)  
print(f"Счетчик уменьшился: {counter1.value}")  

print("Итерация по счетчику:")
for i in counter1:
    print(i)

counter1.reset() 
print(f"Сброс счетчика: {counter1.value}") 