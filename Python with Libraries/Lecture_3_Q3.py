# Write a program to make simple calculator operation ='+', n1 = 30, n2 = 50

n1 = 30
n2 = 50
op = input("Enter any operator")

if (op == '+'):
    print(n1 + n2)

elif (op == '-'):
    print(n1-n2)

elif (op == '*'):
    print(n1*n2)

elif (op == '/'):
    print(n1/n2)

elif (op == '//'):
    print(n1//n2)

elif (op == '**'):
    print(n1**n2)

else:
    print("Invalid Operator")