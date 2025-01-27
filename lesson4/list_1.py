'''
Дан произвольный список. Вывести на экран в обратном порядке. 
Задачу решить 2мя способами. 
'''
#______________________________________________________
# 1- й способ
print("------------")

list_1 = [1, 2, [3], 4, 5, 6]
list_1.reverse()
print(list_1)
# >>>> [6, 5, 4, [3], 2, 1]

list_2 = ['a', 'b', ['c'], 'd', 'e']
list_2.reverse()
print(list_2)
# >>>> ['e', 'd', ['c'], 'b', 'a']

list_3 = [1, 2, [3], 4, 5, 6, 'a', 'b', ['c'], 'd', 'e']
list_3.reverse()
print(list_3)
# >>>> ['e', 'd', ['c'], 'b', 'a', 6, 5, 4, [3], 2, 1]

#______________________________________________________
# 2-й способ
print("-------------")

list_1 = [1, 2, 3, 4, 5, 6]
list_1.sort(reverse=True)
print(list_1)
# >>>> [6, 5, 4, 3, 2, 1]

list_2 = ['a', 'b', 'c', 'd', 'e']
list_2.sort(reverse=True)
print(list_2)
# >>>> ['e', 'd', 'c', 'b', 'a']

#_________________________________________________________
# Ошибки!!!
# Вопрос... Почему .sort(reverse=True) выдает ошибку в следующих случаях, и как ее исправить?

print("Ошибки!!!")

list_1 = [1, 2, [3], 4, 5, 6]
list_1.sort(reverse=True)
print(list_1)
# >>>> TypeError: '<' not supported between instances of 'list' and 'int'


list_2 = ['a', 'b', ['c'], 'd', 'e']
list_2.sort(reverse=True)
print(list_2)
# >>>> TypeError: '<' not supported between instances of 'list' and 'str'


list_3 = [1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'e']
list_3.sort(reverse=True)
print(list_3)
# >>>> TypeError: '<' not supported between instances of 'int' and 'str'



