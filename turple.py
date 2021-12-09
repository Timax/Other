# turple - Кортежи

T  = (1, 2, 3, 4, 3)
print(T)

T = T + (5, 6)
print(T, len(T))

print(T.index(3))
print(T.count(3))

T = (10, ) + T[3:]
print(T)

T = 'spam', 15, ['car', 43, 'moto']
print(T)
print(T[2][1])