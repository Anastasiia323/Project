from errors import IncorrectUserInputError
from errors import (SymbolInputError,
                    NameInputError,
                    PriceInputError,
                    SectorInputError)

from data_access import get_all_records


def validate_user_choice(user_choice):
    if not user_choice.isdigit():
        raise IncorrectUserInputError("Choice must be digit.")
    if user_choice not in map(str, range(1, 11)):
        raise IncorrectUserInputError("Choice must be from 1 to 10.")


def validate_symbol(symbol):
    if symbol in {row.get('Symbol') for row in get_all_records()}:
        raise SymbolInputError('Symbol already exists!')
    if len(symbol) < 3 or len(symbol) > 6:
        raise SymbolInputError('Symbol must be from 3 to 6')


def validate_name(name):
    if name in {row.get('Name') for row in get_all_records()}:
        raise NameInputError('Written name is already exists!')
    if len(name) > 50 or len(name) < 3:
        raise NameInputError('Name length must be from 3 to 50!')


def validate_price(price):
    if not float(price):
        raise PriceInputError('Price must be float!')
    if float(price) < 0 or float(price) > 1000:
        raise PriceInputError('Price must be a positive number!')


def validate_sector(sector):
    if sector not in {row.get('Sector') for row in get_all_records()}:
        raise SectorInputError("Written sector doesn't exist")
