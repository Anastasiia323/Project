"""Task 1: encoding/decoding programme. Firstly, I have to decode from byte to string,
after that I have to encode from string to 'latin1'. Next I have to decode to string again."""

before_decoding = b'r\xc3\xa9sum\xc3\xa9'
after_decoding = before_decoding.decode('utf-8')
latin_1_encoding = after_decoding.encode('latin1')
finish_decoding = latin_1_encoding.decode('latin1')

print(after_decoding)
print(latin_1_encoding)
print(finish_decoding)

