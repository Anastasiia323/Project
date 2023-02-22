import csv


def get_all_records():
    with open('sp500.csv') as my_file:
        return list(csv.DictReader(my_file))


# recording a new line in csv if user clicked 5
def new_line(symbol_name, company_name, sector_name, price):
    with open('sp500.csv', 'a', newline='') as my_file:
        return csv.DictWriter(
            my_file,
            fieldnames=csv.DictReader(open('sp500.csv')).fieldnames
        ).writerow({
            'Symbol': symbol_name,
            'Name': company_name,
            'Sector': sector_name,
            'Price': price}
        )


def all_records():
    with open('sp500.csv', 'r', newline='') as file:
        return list(csv.reader(file))


# updating company name if user clicked 6
def update_company_name(symbol, company_name):
    result = False
    records = all_records()
    with open('sp500.csv', 'w', newline='') as newfile:
        new_csv = csv.writer(newfile)
        for row in records:
            if row[0].lower() == symbol.lower():
                row[1] = company_name
                result = True
            new_csv.writerow(row)
        return result


# deleting line if user clicked 7
def delete_company(symbol):
    records = all_records()
    with open('sp500.csv', 'w', newline='') as newfile:
        new_csv = csv.writer(newfile)
        for row in records:
            if row[0].lower() != symbol.lower():
                new_csv.writerow(row)
        else:
            result = True
    return result


def clean_the_file():
    result = False
    lines = all_records()
    new_file = open('sp500.csv', 'w', newline='')
    for line in lines:
        if line:
            result = True
            new_file.writelines(line[:-1])
    return result
