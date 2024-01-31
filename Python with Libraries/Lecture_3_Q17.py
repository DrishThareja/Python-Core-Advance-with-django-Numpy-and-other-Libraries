# Print palidrome

# without using while loop
num = int(input("Enter number: "))

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

d4 = num % 10
num = num // 10

number = (str(d1) + str(d2) + str(d3) + str(d4) )

if(num == number):
    print("The number is a palidrome.")
else:
    print("The number is not a palidrome")


# using while loop
    
num = int(input("Enter number: "))
number = num
reserve = 0

while(num > 0):
    digit = num % 10
    reserve = ((reserve * 10) + digit)
    num = num // 10

if(number == reserve):
    print(number, " is a palidrome.")
else:
    print(number, " is not a palifrome")