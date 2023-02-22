from data_access import (
    get_all_records,
    new_line,
    update_company_name,
    delete_company,
    clean_the_file,
    record_the_file
)

from functools import reduce
from caching import caching_decorator


find_by_name_cache = {}


# finding by name if user clicked 1
@caching_decorator(find_by_name_cache)
def find_by_name(company_name):
    companies_list = []
    for row in get_all_records():
        if company_name.lower() in row.get('Name').lower():
            companies_list.append(
                {
                    row.get('Name'),
                    row.get('Symbol'),
                    row.get('Sector'),
                    row.get('Price')
                    }
                )

    return companies_list


find_by_sector_cache = {}


# finding all companies by sector if user clicked 2
@caching_decorator(find_by_sector_cache)
def find_by_sector(sector_name):
    companies_names = []
    for row in get_all_records():
        if sector_name.lower() in row.get('Sector').lower():
            companies_names.append(row.get('Name'))
    return companies_names


# function to find average price if user clicked 3
def average_price():
    price = []
    for row in get_all_records():
        price.append(float(row['Price']))
    av_pr = (reduce(lambda x, y: x + y, price) / len(price))
    result = round(av_pr, 4)
    return result


# finding companies with the most expansive share
# if user clicked 3
def get_top_10():
    companies = []
    price = []
    for row in get_all_records():
        companies.append(row['Name'])
        price.append(row['Price'])
    fin_pr = list(zip(companies, price))
    fin = sorted(fin_pr, key=lambda x: (x[1]), reverse=True)
    result = fin[1:11]
    return result


# adding new line if user clicked 5 (searching file in dada module)
def make_new_line(symbol_name, company_name, sector_name, price):
    return new_line(symbol_name, company_name, sector_name, price)


# update a company name if user clicked 6
# (searching file in data module)
def update_the_line(symbol, company_name):
    result = update_company_name(symbol=symbol, company_name=company_name)
    if result:
        return "Successfully recorded"
    else:
        return "Written symbol doesn't exist"


# delete line if user clicked 7 (all actions with data in data file)
def delete_the_company(symbol):
    result = delete_company(symbol=symbol)
    if result:
        return "Successfully deleted"
    else:
        return "Written symbol doesn't exist"


# clean file if user clicked 8 (all actions in data module)
def clean_all_lines():
    result = clean_the_file()
    if result:
        return 'Successfully cleaned'

    else:
        return "File was not cleaned"


# new recording if user clicked 9
# all actions with data in data module
def record_new_file(count):
    result = record_the_file(count=count)
    return result
