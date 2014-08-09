# -*- coding: utf-8 -*-
print 'Hellow world!'

##variables
simpleString = 'hello world'
simpleInteger = 1532

print('know type of variable')
print type(simpleString)

print 'Define a list'
myList = [0,3,6,9]
print myList

print 'You can mix the types'
myList = [2, 4, 'a', 4, 'b', 'c']
print myList

print 'Concatenate strings: ', simpleString

print 'Define dictionaries'
diccionario = {'a':1, 'e':4, 'c':50, 'd':'d', 'b':10}
print diccionario

print 'get dictionary value with the key dictionary["key"]'
print diccionario['c']

print 'You can unpackage lists on variables'
a, b, c, d, e, f = myList
print a, b, c, d, e, f

print 'Make loops on python is pretty easy'
for l in myList:
	print l

print 'And this works for dictionaries'
for d in diccionario:
	print d

print 'If you use dictionary.items() you can obtain key and value'
for l in diccionario.items():
	print l

for key, value in diccionario.items():
	print 'key: ', key, ' value: ', value

print 'You can sort with sorted()'
print sorted(myList)
print 'Or you can use reverse for descending sort'
print sorted(myList, reverse=True)

print 'Sort dictionaries'
print sorted(diccionario.items())
print 'But you can define the param to be sort'
print sorted(diccionario.items(), key=lambda x: x[1])

print 'You can filter what you use from dictionary'
ninjas = {'hugo':'front', 'iorch':'front', 'mario':'backend', 'luis':'ios'}
print ninjas
print 'Selecting just who are front'
print 'Our fronts are:'
for key, value in ninjas.items():
	if value == 'front':
		print key

	