'''
Дан список:
['samsung', 'lg', 'xerox', 'bosch']
Удалить элемент с именем 'xerox'
Добавить элемент на 2 место 'indesit'

'''
#1________________________________________
list_1 = ['samsung', 'lg', 'xerox', 'bosch']

list_1.remove('xerox')
#print(list_1)
# >>>> ['samsung', 'lg', 'bosch']

list_1.insert(1, 'indesit')
print(list_1)
# >>>> ['samsung', 'indesit', 'lg', 'bosch']


#2_________________________________________
print('--------------')

list_1 = ['samsung', 'lg', 'xerox', 'bosch']

list_1.pop(2)
#print(list_1)
# >>>> ['samsung', 'lg', 'bosch'] 

list_1.insert(1, 'indesit')
print(list_1)
# >>>> ['samsung', 'indesit', 'lg', 'bosch']