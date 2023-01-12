a = 'Привет, Мир!'.encode('utf-8') # передала в байтах фразу

print(a)

phone_number = 14

print(bytes(phone_number)) # вывела в байтах число

print(bytes([50, 100, 76, 72, 41])) # вывела в байтах список

a = chr(47)  # тоже байты, но с функцией chr
print(a)


new_phrase = 'Python is interesting'
code = bytearray(new_phrase, 'utf-8')

print(code)  # вывела массив данных из строки, почему не зашифровывается?

size = 7
code1 = bytearray(size)
print(code1)  # вывела число

byte_list = [1, 2, 3, 4]
code3 = bytearray(byte_list) # вывод листа

print(code3)



