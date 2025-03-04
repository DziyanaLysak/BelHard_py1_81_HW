"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""


from datetime import date

CURRENT_YEAR = date.today().year

class BookCard:

    def __init__(self, author, title, year):
        
        self.author = author
        self.title = title
        self.year = year

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year

    def __lt__(self, other):
        return self.year < other.year

    def __gt__(self, other):
        return self.year > other.year

    def __le__(self, other):
        return self.year <= other.year

    def __ge__(self, other):
        return self.year >= other.year

    # Author 
    def get_author(self):
        return self._author

    def set_author(self, author):
        if not isinstance(author, str):
            raise ValueError("Автор должен быть строкой")
        self._author = author

    author = property(get_author, set_author)

    # Title
    def get_title(self):
        return self._title

    def set_title(self, title):
        if not isinstance(title, str):
            raise ValueError("Название должно быть строкой")
        self._title = title

    title = property(get_title, set_title)

    # Year
    def get_year(self):
        return self._year

    def set_year(self, year):
        if not isinstance(year, int):
            raise ValueError("Год должен быть целым числом")
        if year <= 0 or year > CURRENT_YEAR:
            raise ValueError("Год должен быть больше 0 и не больше текущего года")
        self._year = year

    year = property(get_year, set_year)

    def __str__(self):
        return f"\"{self.title}\" - {self.author} ({self.year})"


try:
    book1 = BookCard("Сент-Экзюпери", "Маленький принц", 2019)
    book2 = BookCard("Джеймс Барри", "Питер Пэн", 2020)
    book3 = BookCard("Джанни Родари", "Приключения Чиполлино", 2022)

    print(book1)
    print(book2)
    print(book3)

    print(f"book1 == book2: {book1 == book2}")
    print(f"book1 > book2: {book1 > book2}")

    book1.year = 2026  
except ValueError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Непредвиденная ошибка: {e}")