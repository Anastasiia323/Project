from beartype import beartype

@beartype
def make_a_string() -> list:
    """Создаю новый список, где каждый элемент является строкой с помощью map и lambda"""
    b = list(map(lambda nums: str(nums), a))
    return b

a = [1, 2, 3, 23, 34, 54, 89, 51, 90, 76, 21]

print(make_a_string())


