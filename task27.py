'''
Напишите функцию где исходный список содержит положительные и отрицательные
числа. Требуется положительные поместить в один список, а отрицательные - в другой.
'''
even_list = []
odd_list = []
def even_odd_in_list(some_list):
    global even_list
    global odd_list
    i=0
    while i < len(some_list):
        if some_list[i]%2 == 0:
            even_list.append(some_list[i])
            i+=1
        else:
            odd_list.append(some_list[i])
            i+=1
    
spisok = [1, 2, 3, 4, 5, 8, 9, 6, 11, 25, 15, 32]
even_odd_in_list(spisok)    
print (even_list)
print (odd_list)