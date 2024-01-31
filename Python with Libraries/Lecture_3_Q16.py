# Print armstrong no.

num = int(input("Enter number: "))
number = num
cube = 0

while(num > 0):
    digit = num % 10
    cube = (cube + (digit ** 3))
    num = num // 10

if(cube == number):
    print(num, " is a armstrong.")
else:
    print(num, " is not an armstrong.")
