# -*- coding: utf-8 -*-
print '*** Hellow world! ***'

##variables
simpleString = 'hello world'
simpleInteger = 1532

print(' *** know type of variable *** ')
print type(simpleString)

print 'Define a list'
myList = [0,3,6,9]
print myList

print 'You can mix the types'
myList = [2, 4, 'a', 4, 'b', 'c']
print myList

print 'Concatenate strings: ', simpleString

print '*** Define dictionaries ***'
diccionario = {'a':1, 'e':4, 'c':50, 'd':'d', 'b':10}
print diccionario

print 'get dictionary value with the key dictionary["key"]'
print diccionario['c']

print 'You can unpackage lists on variables'
a, b, c, d, e, f = myList
print a, b, c, d, e, f

print ' *** Make loops on python is pretty easy *** '
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

print '*** You can sort with sorted() *** '
print sorted(myList)
print 'Or you can use reverse for descending sort'
print sorted(myList, reverse=True)

print 'Sort dictionaries'
print sorted(diccionario.items())
print 'But you can define the param to be sort'
print sorted(diccionario.items(), key=lambda x: x[1])

print ' *** You can filter what you use from dictionary *** '
ninjas = {'hugo':'front', 'iorch':'front', 'mario':'backend', 'luis':'ios'}
print ninjas
print 'Selecting just who are front'
print 'Our fronts are:'
for key, value in ninjas.items():
	if value == 'front':
		print key

print ' *** Merge lists *** '
owners = ['information', 'sells', 'contact']
emails = ['info@nyxtechnology.com', 'ventas@nyxtechnology.com', 'contact@nyxtechnology.com']
print owners
print emails
print 'Using zip() you can merge lists'
print zip(owners, emails)
print 'And you can merge and convert to dictionary'
print dict(zip(owners, emails))

print 'You can filter items on lists pretty easy'
myList = [2, 5, 9 ,-3 , 0, -4, 2, 0]
print myList
filteredList = [n for n in myList if n > 0]
print filteredList

print 'Now filter a dictionary'
diccionario = {'a':1, 'e':4, 'c':50, 'd':3, 'b':10, 'f':7}
print diccionario
filteredDictionary = [{k: v} for k, v in diccionario.items() if v%2 == 0]
print filteredDictionary

print ' *** Managing sets *** '
first = [1, 3, 5, 7]
second  = [5, 7, 9, 13]
print 'A: ', first
print 'B: ', second
print 'Union'
print set(first) | set(second)
print 'Intersection'
print set(first) & set(second)
print 'A - B'
print set(first) - set(second)
print 'B - A'
print set(second) - set(first)
print 'Clean sets'
third = [0, 0, 3, 4, 5, 7, 9, 2, 4, 7, 8, 3]
print third
print list(set(third))

print ' *** Working with slices *** '
text = '-This is the complete string'
print text
print 'Now just the first 10 characters'
print text[:10]
print third
print 'Slice of the first 5'
print third[:5]
print 'Slice of the last 5'
print third[-5:]
print 'Now try steps'
print third
print 'Jumping in the list in threes'
print third[::3]

print ' *** Delete elements *** '
print third
print 'Delete the first element'
del third[0]
print third
print 'Delete the last element'
third = third[:-1]
print third
print 'Delete from dictionary'
print diccionario
print 'Delete when key = c'
del diccionario['c']
print diccionario

print '*** Regular expressions ***'
print 'You need to import re'
import re
print 'Reordering date on a string with regular expressions'
text = 'today is 1/10/1987'
print text
print re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', text)
print 'String format'
text = '{} is a {}'
print text.format('leopard', 'feline')
text = '{animal} is a {family}'
print text.format(family = 'mammal', animal = 'human')
data = {'animal':'Elephant', 'family':'mammal'}
print text.format(**data)

print '*** Function ***'
def hello():
	print '- Hello this is a function'
hello()

print 'Now with params'
def hello(name):
	print '- Hello %s this is a function' % name
hello('phonnz')

def hello(*args, **kwargs):
	print 'args ', args
	print 'kwargs ', kwargs
print 'Function with args'
hello('python', 'learning')
print 'Function with kwargs'
hello(language='python', action='learning')

print '*** Classes ***'
print 'simple class'
class person():
	name = 'Static'

p = person()
print '- ', p.name

print 'Now overriding constructor'
class person():
	def __init__(self, name):
		self.name = name

p = person('phonnz')
print '- ', p.name

print 'Defining functions in objects'
class person():
	def __init__(self, name):
		self.name = name
	def initial(self):
		print '- The initial of {name} is {initial}'.format(name=self.name, initial=self.name[:1])

p = person('phonnz')
p.initial()
