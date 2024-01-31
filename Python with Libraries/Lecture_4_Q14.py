# wap to find factorial of a number using function

def factorial(num):
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial * i
    print(factorial)

num = int(input("Enter the number: "))
factorial(num)