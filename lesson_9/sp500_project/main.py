from business_logic import (
    find_by_name,
    find_by_sector,
    average_price,
    get_top_10,
    make_new_line,
    update_the_line,
    delete_the_company,
    clean_the_file,
)

from validator import validate_user_choice
from errors import IncorrectUserInputError
from validator import (validate_name,
                       validate_price,
                       validate_sector,
                       validate_symbol)

from errors import (SymbolInputError,
                    NameInputError,
                    PriceInputError,
                    SectorInputError)


while True:
    point_of_menu = input('1. Find info by name\n'
                          '2. Get all companies by sector\n'
                          '3. Calculate average price\n'
                          '4. Get top 10 companies\n'
                          '5. Add new company\n'
                          '6. Update company name\n'
                          '7. Delete company\n'
                          '8. Truncate all\n'
                          '9. Populate file with random data\n'
                          '10. Exit\nYour choice: ')
    try:
        validate_user_choice(user_choice=point_of_menu)
    except IncorrectUserInputError as err:
        print(err)
        continue

    if point_of_menu == '10':
        print('Good bye!')
        break

    # finding company by name
    elif point_of_menu == '1':
        name = input('Write the name: ')
        result = find_by_name(company_name=name)
        print(result)

    # print all companies by sector
    elif point_of_menu == '2':
        sector = input('Write the sector: ')
        result = find_by_sector(sector_name=sector)
        print(result)

    # printing average price of all companies
    elif point_of_menu == '3':
        result = average_price()
        print(result)

    # printing companies with the most expensive share
    elif point_of_menu == '4':
        result = get_top_10()
        print(result)

    # adding new line in csv file
    elif point_of_menu == '5':
        symbol = input('Write the symbol: ')

        try:
            validate_symbol(symbol=symbol)
        except SymbolInputError as err:
            print(err)
            continue

        name = input('Write the name: ')

        try:
            validate_name(name=name)
        except NameInputError as err:
            print(err)
            continue

        sector = input('Write the sector: ')

        try:
            validate_sector(sector=sector)
        except SectorInputError as err:
            print(err)
            continue

        price = input('How much it cost: ')

        try:
            validate_price(price=price)
        except PriceInputError as err:
            print(err)
            continue

        result = make_new_line(symbol_name=symbol,
                               company_name=name,
                               sector_name=sector,
                               price=price)

    # updating company name, using symbol checking
    elif point_of_menu == '6':
        symbol = input('Write the symbol: ')
        company_name = input('Write the new name: ')
        result = update_the_line(symbol=symbol, company_name=company_name)
        print(result)

    # delete line after symbol checking
    elif point_of_menu == '7':
        symbol = input('Write the symbol: ')
        result = delete_the_company(symbol=symbol)
        print(result)

    # cleaning csv file
    elif point_of_menu == '8':
        result = clean_the_file()
        print(result)
