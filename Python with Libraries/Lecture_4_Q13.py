# wap to check number is prime or not using function

def Prime_or_Not(num):
    for i in range(2, num + 1):
        if (num % i == 0):
            break

    if( i == num):
        print(num, " is prime number.")

    else:
        print(num, " is not prime number.")

num = int(input("Enter a number: "))
Prime_or_Not(num)