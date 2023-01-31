from beartype import beartype

@beartype
def is_palindrome(some_list: tuple) -> list:
    """Определяю, есть ли в кортеже элементы-полиндромы. Если есть фильтрую их в отдельный список"""
    palindrome_list = filter((lambda i: i == i[::-1]), some_list)
    return list(palindrome_list)


print(is_palindrome(('шалаш', 'дом', 'мем', 'дед', 'привет')))