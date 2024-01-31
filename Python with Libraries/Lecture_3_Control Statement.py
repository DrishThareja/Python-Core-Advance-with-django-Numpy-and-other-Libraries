"""
--> Control Statement:
1. if
2. if-else
3. if-elif
4. Switch
5. Loop

1. if statement: It executes when condition is true.
    syntax:
    if(condition):
        # code
    
    Eg:
    age = 23
    if (age>=18):
        print("can vote")

    Eg:
    num = 35
    if (num % 2 == 0):
        print("even")

    Eg:
    n1 = 20
    n2 = 20
    if (n1 == n2)
        print("equal")


2. if-else: When the condition is false then else statement will execute.
    syntax: 
    if(condition):
        # code
    else:
        # code

    Eg:
    age = 23
    if (age>=18):
        print("can vote")
    else:
        print("can not vote")

    Eg:
    num = 35
    if (num % 2 == 0):
        print("even")
    else:
        print("odd")

    Eg:
    n1 = 20
    n2 = 20
    if (n1 == n2)
        print("equal")
    else:
        print("not equal")


3. if-elif: When we have more than one condition then we have to use if-elif statement.
    syntax:
    if(condition):
        #code
    elif(condition):
        #code
    elif(condition):
        #code
    else:
        #code


4. Loop: Iteration of a task more than one time after a fixed interval known as loop.
    Eg: 1, 2, 3, .... n

--> Types of loops:
1. For loop: If we know the starting or end of loop then we have to use it.
    syntax:
    for varname in range (start, end):
        statement
    
    Eg: wap to 1 to 10
    for i in range (1, 11):
        print(i)

2. While loop: When condition is unknown then we have to use it.
    syntax:
    while (condition):
        statement
        increement / decreement


5. Switch: In this there are cases.
    syntax:
    switch(expression):

    case value:
        statement
        break
        
    case value:
        statement
        break
        
    case value:
        statement
        break
        
    default:
        statement
"""