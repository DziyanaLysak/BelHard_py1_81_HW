"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
и в зависимости от него возвращала ФИО в двух следующих форматах:
 -  Николаев И.С. 
 -  И.С.Николаев


"""

def short_format(full_name, surname_1=True):

  split_name = full_name.split()

  if len(split_name) < 3:
    return "Введите полное имя (Фамилия Имя Отчество)."

  surname = split_name[0]
  name = split_name[1]
  middle_name = split_name[2]

  initials = name[0] + "." + middle_name[0] + "."
  initials = f"{name[0]}.{middle_name[0]}."

  if surname_1:
    short_format = f"{surname} {initials}"
  else:
    short_format = f"{initials}{surname}"  

  return short_format

