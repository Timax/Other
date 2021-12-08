# string format

s1 = '%s, test1 ,, %s' % ('cat', 'dog')
print(s1)
s2 = 'test {} + tes2{}'.format('rat', 'snake')
print(s2)
s3 = 'test {0}    {2} {1}'.format('a', 'l', 'm')
print(s3)

s4  = 'a\nb\tcc'
print(s4)
print(len(s4), ord('\n'))

s5 = 'a\0ggjf\0fgd'
print(s5)

s6 = '''' hhjrfjvdv
jgvbhhk
kjh

ggjgdjffuhvdubv\tjfhn

5\ngv'''
print('Многострочная строка : ' ,s6)

s7 = r'C:\text\new.txt'
print(s7)

s8 = 'spam'.encode('utf-16')
print(s8)

s9 = 'sp\xc4\u00c4\U000000c4'
print(s9)

print(list(range(4)))
print(list(range(4,24,2)))


print('list comprehension')
print('список')
print([[x, x ** 2, x**3] for x in range(12)])



M = [[1, 7, 7], [2, 0, 4], [-1, 3, -3]]
k = list(map(sum, M))
print(k)

s = {i : sum(M[i]) for i in range(3)}
print('словарь')
print(s)

print('Генератор')

r = (sum(i) for i in M)
print(next(r))

print('map и множество')

print(list(map(sum, M)))

print({sum(row) for row in M})