# Пишем в файл
f = open('test_file.txt', 'w')
f.write('Hello\n')
f.write('world\n')
f.close()

import os
print(os.getcwd())

# Читаем из файла (r - по умолчанию)
f = open(r'./test_file.txt')
text = f.read()
print(text)

# Файл - строка
text.split() 

# Выводим построчно через цикл
for line in open('test_file.txt'): print(line)

# Справка
#print(dir(f))
#print(help(f.seek))

# Двоичный файл: порядок байт big-endian + int + char + short (>i4sh)
import struct
packed = struct.pack('>i4sh', 7,  b'spam', 8)

# 10 байтов (не объекты, и не текст)
print(packed)

# Пишем
file = open('data.bin', 'wb')
file.write(packed)
file.close()

# Читаем
data = open('data.bin', 'rb').read()

# Нарежем байты в середине
print(data[4:8])

# Последовательность 8-битных байтов
print(list(data))

# Распакуем в объекты
print(struct.unpack('>i4sh', data))


# Кодировки
# Текст Unicode отличающийся от ascii
s  = 'sp\xc4m'
print(s)
print(s[2])

