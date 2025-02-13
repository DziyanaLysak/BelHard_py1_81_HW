"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
и в зависимости от него возвращала ФИО в двух следующих форматах:
 -  Николаев И.С. 
 -  И.С.Николаев

"""

'''
Функция short_format: Принимает ФИО одной строкой и возвращает сокращенную версию.

full_name: ФИО (например, "Петров Владимир Сергеевич").
first_surname=True (по умолчанию): возвращает ФИО в формате "Фамилия И.О.".
first_surname=False: возвращает ФИО в формате "И.О. Фамилия".

'''
def short_format(full_name: str , first_surname=True):

  split_name = full_name.split()

  if len(split_name) < 3:
    return "Введите полное имя (Фамилия Имя Отчество):"

  surname = split_name[0]
  name = split_name[1]
  middle_name = split_name[2]

  initials = f"{name[0]}.{middle_name[0]}."

  if first_surname:
    short_format = f"{surname} {initials}"
  else:
    short_format = f"{initials} {surname}"  

  return short_format

print(short_format("Петров Владимир Сергеевич"))  # Вывод: Петров В.С.
print(short_format("Петров Владимир Сергеевич", first_surname=False ))  # Вывод: В.С. Петров
print(short_format("Петров Владимир"))  # Вывод: Введите полное имя (Фамилия Имя Отчество):
