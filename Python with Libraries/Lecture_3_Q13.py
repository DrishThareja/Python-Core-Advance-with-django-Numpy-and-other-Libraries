# Write a program to check a no. is prime or not prime.

num = int(input("Enter a number: "))

for i in range(2, num + 1):
    if (num % i == 0):
        break

if( i == num):
    print(num, " is prime number.")

else:
    print(num, " is not prime number.")