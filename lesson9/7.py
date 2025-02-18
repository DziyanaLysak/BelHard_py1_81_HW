"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""

users = [
    {"name": "David", "login": "David111", "password": "dvd_1987"},
    {"name": "Carl", "login": "Carl85!", "password": "cl1409"},
    {"name": "Kelly", "login": "Kelly-55", "password": "kll1"},
    {"name": "Bob", "login": "Bob123", "password": "bb_25"}
]

passwords = list(filter(lambda user: len(user["password"]) < 5, users))
print("Пользователи с короткими паролями:", passwords)
# Вывод: Пользователи с короткими паролями: [{'name': 'Kelly', 'login': 'Kelly-55', 'password': 'kll1'}]

def login_verification(login):
    for symbol in login:
        if not ('a' <= symbol <= 'z' or
                'A' <= symbol <= 'Z' or
                '0' <= symbol <= '9' or
                symbol == '_'):
            return False  
    return True 

login_invalid = list(filter(lambda user: not login_verification(user["login"]), users))

for user in login_invalid:
    print(f"Ваш логин {user['login']} не является корректным.")

# Вывод: Ваш логин Carl85! не является корректным. 
#        Ваш логин Kelly-55 не является корректным.