import csv
from functools import reduce


def choose_the_point():
    with open('sp500.csv') as my_file:
        reader = csv.DictReader(my_file)
        while True:
            # creating a menu
            point_of_menu = input('1. Find info by name\n'
                                  '2. Get all companies by sector\n'
                                  '3. Calculate average price\n'
                                  '4. Get top 10 companies\n'
                                  '5. Exit\nYour choice: ')
            # checking every point of menu to return relevant result
            if point_of_menu == '1':
                name_of_company = input('Write the company name: ')
                companies = []
                for row in reader:
                    if name_of_company in row['Name']:
                        companies.append(row)
                return companies

            elif point_of_menu == '2':
                sector = input('Write the sector: ')
                list_of_companies = []
                for row in reader:
                    if sector in row['Sector']:
                        list_of_companies.append(row['Name'])
                return list_of_companies

            elif point_of_menu == '3':
                price = []
                for row in reader:
                    price.append(float(row['Price']))
                av_pr = (reduce(lambda x, y: x + y, price) / len(price))
                return round(av_pr, 4)

            elif point_of_menu == '4':
                companies = []
                price = []
                for row in reader:
                    companies.append(row['Name'])
                    price.append(row['Price'])
                fin_pr = list(zip(companies, price))
                fin = sorted(fin_pr, key=lambda x: (x[1]), reverse=True)
                return fin[1:11]
            else:
                return "Good bye!"


print(choose_the_point())
