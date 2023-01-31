import time


def to_dec(func):
    """Decorating function creating"""
    def wrapper(owner, **pets):
        """Wrapper creating"""
        start = time.time()
        ret = func(owner, **pets)
        end = time.time()
        print(f'Working time: {end-start}')
        return ret
    return wrapper

@to_dec
def main_func(owner, **pets) -> str:
    time.sleep(0.5)
    print(f'Owner name: {owner}')
    for pet, name in pets.items():
        print(f'{pet}:{name}')


main_func('Anastasiia', cat='Lisa', dog='Tom', fish=['Dori', 'Nemo', 'Goldie'], pig='Piggy', horse='Pifagor')
