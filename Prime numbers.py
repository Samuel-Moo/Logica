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

    divisible_by_1 = func1(number)
    divisible_by_itself = func2(number)
    not_divisible_by_other = func3(number)

    if divisible_by_1 and divisible_by_itself and not not_divisible_by_other:
        print(f"The number {number} is a prime number")
    else:
        print(f'The number {number} is not a prime number')
    if number % 1 == 0 and number % number == 0 and not not_divisible_by_other:
        print(f'The number {number} is a prime number')
    else:
        print(f'The number {number} is not a prime number')
