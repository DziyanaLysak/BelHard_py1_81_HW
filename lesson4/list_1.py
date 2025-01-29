'''
Дан произвольный список. Вывести на экран в обратном порядке. 
Задачу решить 2мя способами. 
'''

# 1- й способ

list_1 = [1, 2, [3], 4, 5, 6]
list_1.reverse()
print(list_1)

list_2 = ['a', 'b', ['c'], 'd', 'e']
list_2.reverse()
print(list_2)

list_3 = [1, 2, [3], 4, 5, 6, 'a', 'b', ['c'], 'd', 'e']
list_3.reverse()
print(list_3)

# 2-й способ
list_1 = [1, 2, 3, 4, 5, 6]
list_1.sort(reverse=True)
print(list_1)

list_2 = ['a', 'b', 'c', 'd', 'e']
list_2.sort(reverse=True)
print(list_2)





