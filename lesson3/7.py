'''
Запросить логин и пароль.
Вывести - True/False  соответственно
если ввели логин - 'admin', пароль - '12345'.
Формат вывода: "Логин:True / Пароль:True"

'''
 
ok = True
ok = False

login = input("Введите логин: ")
password = input("Введите пароль: ")

ok = login == 'admin'
ok = password == '12345'

print("Логин:", ok)
print("Пароль:", ok)

#>>>  Введите логин: admin
#>>>  Введите пароль: 12345
#>>>  Логин: True
#>>>  Пароль: True

#>>>  Введите логин: adm
#>>>  Введите пароль: 1234
#>>>  Логин: False
#>>>  Пароль: False