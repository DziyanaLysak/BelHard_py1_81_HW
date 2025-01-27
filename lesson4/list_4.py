'''
Дан список:
['hello', 'python', 'интерпретатор', 'pep8', "123"]
Вернуть список где вместо элементов данного списка прописаны количество символов каждого элемента.

'''

list_1 = ['hello', 'python', 'интерпретатор', 'pep8', "123"]


el_0, el_1, el_2, el_3, el_4 = list_1[0], list_1[1], list_1[2], list_1[3], list_1[4]
# print(list_1[0], list_1[1], list_1[2], list_1[3], list_1[4])
# >>>> hello python интерпретатор pep8 123

el_0, el_1, el_2, el_3, el_4 = len(el_0), len(el_1), len(el_2), len(el_3), len(el_4)
list_3 = el_0, el_1, el_2, el_3, el_4 
# print(list_3)
# >>>> (5, 6, 13, 4, 3)

print(list(list_3))
# >>>> [5, 6, 13, 4, 3]