# wap to check a number even or odd using function

def Even_or_Odd(num):
    if(num % 2 == 0):
        print("even")
    else:
        print("odd")


num = int(input("Enter number: "))

Even_or_Odd(num)