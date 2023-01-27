from beartype import beartype

@beartype
def analyze_the_string(text: str) -> float | str:
    """Определяю, содержатся ли во входящей строке цифры
    и, в зависимости от результата, привожу к float"""
    d = text.isdigit()
    b = text.replace(',', '.')
    if d is True:
        return int(a)
    elif text[0] == '-':
        return float(b)
    elif '.' in text:
        return float(b)
    else:
        return 'Некорректная строка'

a = '-2,4'

print(analyze_the_string(a))