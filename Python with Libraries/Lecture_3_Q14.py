# Write a program to print sum of odd no. from 1 to 20

sum = 0
for number in range(1, 21):
    if ( number % 2 != 0):
        sum += number
print(sum)