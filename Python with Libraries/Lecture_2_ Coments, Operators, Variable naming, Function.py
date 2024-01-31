"""
Lecture 2: 6 Jan 2024

Python:

--> Coments:
    1. Single line ---> #
    2. Multi line ---> (""" """)
Advantage: code readibility, hide unimportant code, fast testing & debuging.

--> To take input from user -> input() -> by default string.

a = input("Enter your name:")
print(a)

Output:
Enter your name: Drish
Drish


--> int(input())
a = int(input("Enter value"))
b = int(input("Enter value"))
print(a+b)

str() --> for string


--> Operators:
    Operators are used to perform any operation with operands.
    Eg: 10 + 20
    In this (+) is operators and 10, 20 is operands.
"""
a = 10
b = 3
a = int(a)
b = int(b)
# Types of Operators:

# Arithmatic Operators: +, -, *, /, %, //, **.
#                       // --> flow division
#                       ** --> exponent

print("ans of a+b =",a+b)
print("ans of a-b =",a-b)
print("ans of a*b =",a*b)
print("ans of a/b =",a/b)
print("ans of a%b =",a%b)
print("ans of a//b =",a//b)
print("ans of a**b =",a**b)

"""-------------------------------------------------------------------------------------"""
# Relational/Comparison operator: == (Equal to), != (Not equal to), < (Less than), > (Greater than), <= (Less than or equal to), >= (Greater than or equal to).

print("ans of a==b =",a==b)
print("ans of a!=b =",a!=b)
print("ans of a<b =",a<b)
print("ans of a>b =",a>b)
print("ans of a<=b =",a<=b)
print("ans of a>=b =",a>=b)

"""-------------------------------------------------------------------------------------"""
# Logical operator: and, or, not.

print("ans of a and b =",a and b)
print("ans of a or b =",a or b)
print("ans of not(a==b) =",not(a==b))

"""-------------------------------------------------------------------------------------"""
# Assignment Operator: =, +=, -=, *=, /=, %=, **=, //=.

a+=2
print("a+=2 =",a)

a-=2
print("a-=2 =",a)

a*=2
print("a*=2 =",a)

a/=2
print("a/=2 =",a)

a%=2
print("a%=2 =",a)

a**=2
print("a**=2 =",a)

a//=2
print("a//=2 =",a)

"""-------------------------------------------------------------------------------------"""
# Bitwise Operator:
a = 5
b = 3
# & (Bitwise operator)
c = a & b
print("a & b =",c)

# | (Bitwise or)
c = a | b
print("a | b =",c)

# ^ (Bitwise XOR)
c = a ^ b
print("a ^ b =",c)

# ~ (Bitwise NOT)
c = ~b
print("~b =",c)

# << (Left Shift)
c = a << b
print("a << b =",c)

# >> (Right Shift)
c = a >> b
print("a >> b =",c)

"""-------------------------------------------------------------------------------------"""
# Membership Operator:

# 'in' (True if a value is found in sequence)
numbers = [1, 2, 3, 4, 5]
result = 3 in numbers
print("result of 3 in numbers =",result)

# 'not in' (True if a value is not found in sequence)
numbers = [1, 2, 3, 4, 5]
result = 7 not in numbers
print("result of 7 not in numbers =",result)

"""-------------------------------------------------------------------------------------"""
# Identity Operator:

# 'is' (True if the operands are identical)
x = [1, 2, 3]
y = [1, 2, 3]
result = x is y     # false as a and b are different objects in memory
print("result of x is y =",result)

# 'is not' (True if the operands are not identical)
c = [4, 5, 6]
d = c
result = c is not d
print("result of c is not d =",result)

"""-------------------------------------------------------------------------------------"""
# Unary operator: += (increment), -= (decrement)

counter = 0
counter += 1
print("counter += 1 =",counter)
counter -= 1
print("counter -= 1 =",counter)

"""-------------------------------------------------------------------------------------"""
# Ternary Operator:
x = 10
y = 5
result = x if x > y else y
print("result of x if x > y else y =",result)

"""-------------------------------------------------------------------------------------"""


"""
--> Variable naming  conversion:
1. Alphabatic, x = 10
2. Alpha-numeric, x1 = 10
3. Start from underscore (_), _x = 10
4. Can be in camal case, empName = 10
5. Any special keyword or numeric value can not be a variable name.
    eg: class = 20
        10 = 50
6. Class, the first character of class should be capital.
    class Ram {
        -----
    }

7. Can not use (-), emp-abc = 10                # This is wrong
8. We can not start name with numeric value:
eg: 10a = 5                                     # This is wrong


--> Function: Naming rules for functions are same as for variables.

--> range (start, end)
    range (1, 11)
    11 --> excluded 
    {1 to 10} it will execute

    range (start, end, step value)
    step value is interval or gap
    By default step value is 1
"""
