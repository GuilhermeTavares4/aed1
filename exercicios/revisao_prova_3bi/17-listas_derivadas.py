lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print([num for num in lista if num >=1 and num <= 8]) #list comprehension

print(list(filter(lambda x: x >=8 and x <= 13, lista)))
print(list(filter(lambda x: x % 2 == 0, lista)))
print(list(filter(lambda x: x % 2 == 1, lista)))
print(lista[::-1])