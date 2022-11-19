def func1(number):
    if number % 1 == 0:
     return True
    else:
     return False


def func2(number):
    if number % number == 0:
     return True
    else:
     return False


def func3(number) :
    for n in range(2, number):

     if number % n ==0:
          return True
    return False




if __name__ == '__main__':

    number = int(input())

    d1 = func1(number)
    di = func2(number)
    nd = func3(number)

    
    if d1 and di and not nd:
        print(f"The number {number} is a prime number")
    else:
        print(f'The number {number} is not a prime number')
    