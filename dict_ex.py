D = { 'age': 28, 'name' : 'Kolya', 'job' : 'cpl'}
print(D , '\n')

print('Элементы по ключу')
print(D['job'], '\n')

D['age'] += 1
print(D)

D2 = {}
D2[5] = 15
D2['len'] = 'long'
print(D2, '\n')

print('Через dict', '\n')

D3 = dict(game = 'chess', type = 'classic')
print(D3)
D3 = dict(zip(['cat' , 'dog'], [0, 1]))
print(D3)

#Усложненная структура
D4 = {'name' : {'first' : 'Kolya', 'last' : 'Kulemzin'}, 'role' :['analyst', 'dev'], 'age' : 28}

print(D4)
print(D4['name']['last'], D4['role'][1])

#Проверка на пустоту

D5 = {'a' : 1,  'b' : 3, 'c' :17}
print(D5)

if not 'f' in D5:
	print('missing')
else:
	print(D5['f'])
	
value1 = D5.get('a', 0)
value2 = D5.get('e', 0)
print(value1, value2)

value3 = D5['x'] if 'x' in D5 else 0
print(value3)

#Сортировка ключей


