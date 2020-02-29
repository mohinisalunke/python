#list of list:

>>> lists = [1,2,['m','o','h','i','n','i',[11,12,13,14]],4]
>>> lists[2][6][0]
11
>>> lists[1]=3
>>> lists
[1, 3, ['m', 'o', 'h', 'i', 'n', 'i', [11, 12, 13, 14]], 4]
>>> lists[0:2]
[1, 3]
>>> lists[:-1]
[1, 3, ['m', 'o', 'h', 'i', 'n', 'i', [11, 12, 13, 14]]]
>>> lists[:5:-2]
[]
>>> lists[:2:-1]
[4]
>>> lists[:2:2]
[1]


#lists of tuple :

lists = [1,2,('m','o','h','i','n','i',(11,12,13,14)),4]
>>> lists[2][0]
'm'
>>> lists[2][0] = "r" (because tuples are immutable)
"""Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    lists[2][0] = "r"
TypeError: 'tuple' object does not support item assignment"""
>>> lists[2:]
[('m', 'o', 'h', 'i', 'n', 'i', (11, 12, 13, 14)), 4]


#list of dictionary :

lists = [10,12,{'name':'mohini', 'age':23},{'subject':'math','marks':91}]
>>> lists[2]['age']
23
>>> lists[3]['subject'] = 'marathi'
>>> lists
[10, 12, {'name': 'mohini', 'age': 23}, {'subject': 'marathi', 'marks': 91}]
>>> lists[1:]
[12, {'name': 'mohini', 'age': 23}, {'subject': 'marathi', 'marks': 91}]
>>> lists[1:3:1]
[12, {'name': 'mohini', 'age': 23}]


#tuple of tuple :

>>>tuples = ('d','h','i',(11,12,13,14),'a','j')
>>>tuples[0]
'd'
>>> tuples[3][1]
12

# tuple of list :

 tuples = ([10,11,12,13],22,24,[31,32,[41,42,43]],51)
>>> len(tuples)
5
>>> tuples[3][2][0]
41

>>> tuples[3][2][0] = 40
>>> tuples
([10, 11, 12, 13], 22, 24, [31, 32, [40, 42, 43]], 51)


#tuple of dictionary :

tuples = ({'name':'mohini','age':22,'location':'pune'},1,11,21,{'subject':'maths','marks':'92'})
>>> tuples[4]['marks']
'92'
>>> tuples[4]['class'] = 'firstclass'
>>> tuples
({'name': 'mohini', 'age': 22, 'location': 'pune'}, 1, 11, 21, {'subject': 'maths', 'marks': '92', 'class': 'firstclass'})
>>> tuples[1:3]
(1, 11)
>>> tuples[:]
({'name': 'mohini', 'age': 22, 'location': 'pune'}, 1, 11, 21, {'subject': 'maths', 'marks': '92', 'class': 'firstclass'})

# dictionary of dictionary :

 dictionary = {'name':'mohini','age':22,'details':{'location':'pune','pin':431001}}
>>> len(dictionary)
3
>>> dictionary['details']['pin']
431001

# dictionary of list :

>>> dictionary = {'subjects':['maths','marathi','hindi','history'],'standerd':['tenth','eightth','nineth',['A','B','C']]}
>>> dictionary['subjects'][1]
'marathi'
>>> dictionary['standerd'][0] = 'seventh'
>>> dictionary
{'subjects': ['maths', 'marathi', 'hindi', 'history'], 'standerd': ['seventh', 'eightth', 'nineth', ['A', 'B', 'C']]}


# dictionary of tuple :

>>> dictionary = {'numbers':(1,2,3),'name':('mohini','meghna','mayuri')}
>>> dictionary['name'][1]
'meghna'
>>> dictionary['name'][:]
('mohini', 'meghna', 'mayuri')
>>> dictionary['name'][1:2:1]
('meghna',) 


