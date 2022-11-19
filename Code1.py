def func1(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


def func2(year): 
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0: 
        return True
    else:
        return False



def func3(statement1, statement2, year):
    print(f"statement1 = {statement1} and statement2 = {statement2}")
    if statement1 or statement2:
        print(f"The year {year} is a leap-year")
    else:
        print(f"The year {year} is not a leap year") 





if __name__ == '__main__':
    year = int(input())

    statement1 = func1(year)
    statement2 = func2(year)
    func3(statement1, statement2, year)