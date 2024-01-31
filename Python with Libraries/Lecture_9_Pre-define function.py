# Python Built-in Functions:

# Python built-in functions are defined as the functions whose functionality is pre-defined or use in Python. The python interpreter has several functions that are always present f


abs() #Function:  python abs() function is used to return the absolute value of a number. It takes only one argument, a number whose absolute value is to be returned. The argument can be an integer and floating-point number. If the argument is a complex number, then, abs() returns its magnitude.


#integer number     
a = -20  
print('Absolute value of -20 is:', abs(a))          #20
  
#  floating number  
b = -40.83  
print('Absolute value of -40.83 is:', abs(b))       #40.83



all() # Function:- all() function accepts an iterable object (such as list, dictionary, etc.). It returns true if all items in passed iterable are true. Otherwise, it returns False. If the iterable object is empty, the all() function returns True.


# all values true  
k = [1, 3, 4, 6]  
print(all(k))               # True
  
# all values false  
k = [0, False]  
print(all(k))               # False
  
# one false value  
k = [1, 3, 7, 0]  
print(all(k))               # False
  
# one true value  
k = [0, False, 5]  
print(all(k))               # False
  
# empty iterable  
k = []  
print(all(k))               # True



bin() # Function:- python bin() function is used to return the binary representation of a specified integer. A result always starts with the prefix 0b.

8421
1001


x =  10  
y =  bin(x)  
print (y)               # 0b1010


x =  9  
y =  bin(x)  
print (y)               #0b1001
8421

bool() # :the python bool() converts a value to boolean(True or False) using the standard truth testing procedure.

# True will come when the object is in square brackets [] or in quotes ''

test1 = []  
print(test1,'is',bool(test1))           # False         # Reason empty brackets

test1 = [0]  
print(test1,'is',bool(test1))           # True

test1 = 0.0  
print(test1,'is',bool(test1))           # False

test1 = None  
print(test1,'is',bool(test1))           # False

test1 = True  
print(test1,'is',bool(test1))           # False

test1 = 'Easy string'  
print(test1,'is',bool(test1))           # True




bytes() # :- python bytes() in Python is used for returning a bytes object. It is an immutable version of the bytearray() function.


string = "Hello World."  
array = bytes(string, 'utf-8')  
print(array)                            # b' Hello World.'





callable() # Function:A python callable() function in Python is something that can be called. This built-in function checks and returns true if the object passed appears to be callable, otherwise false.

# callable function like function

x = 8  
print(callable(x))                      #false  




exec() # Function: The python exec() function is used for the dynamic execution of Python program which can either be a string or object code and it accepts large blocks of code, unlike the eval() function which only accepts a single expression.


x = 8  
exec('print(x==8)')                     # true
exec('print(x+4)')                      # 12




sum() # Function: python sum() function is used to get the sum of numbers of an iterable, i.e., list.


s = sum([1,2,4 ])  
print(s)                                # 7 
  

s = sum([1, 2, 4], 10)  
print(s)                                # 17




eval() # Function:-The python eval() function parses the expression passed to it and runs python expression(code) within the program.

x = 8  
print(eval('x + 1'))                    # 9




float() # : The python float() function returns a floating-point number from a number or string.


# for integers  
print(float(9))                         # 9.0
  
# for floats  
print(float(8.19))                      # 8.19
  
# for string floats  
print(float("-24.27"))                  # -24.27
  
# for string floats with whitespaces  
print(float("     -17.19\n"))           # *17.19
  
# string float error  
print(float("xyz"))                     # value error: can not convert string to float







format() # Function : The python format() function returns a formatted representation of the given value.

# Python format() Function Example

# d, f and b are a type  , d =int, f = float, b = binary
  

# integer  
print(format(123, "d"))                 # 123
  
# float arguments  
print(format(123.4567898, "f"))         # 123.456790
  
# binary format  
print(format(12, "b"))                  # 1100




getattr() # Function:- python getattr() function returns the value of a named attribute of an object. If it is not found, it returns the default value.

class Details:  
    age = 22  
    name = "Phill"  
  
obj = Details()  
print('The age is:', getattr(obj, "age"))           # The age is: 22
print('The name is:', getattr(obj, "name"))         # The name is: Phill

print('The age is:', obj.age)                       # The age is: 22
print('The name is:', obj.name)                     # The name is: Phill


iter() # Function: The python iter() function is used to return an iterator object. It creates an object which can be iterated one element at a time.

list = [1,2,3,4,5]  
listIter = iter(list)  

print(next(listIter))  # 1 
print(next(listIter))  # 2
print(next(listIter))  # 3
print(next(listIter))  # 4



len() # Function: The python len() function is used to return the length (the number of items) of an object.

strA = 'Python'  
print(len(strA))      # 6





map() # Function: The python map() function is used to return a list of results after applying a given function to each item of an iterable(list, tuple etc.).


def calculateAddition(n):  
  return n+n  

numbers = (1, 2, 3, 4)  
result = map(calculateAddition, numbers)  
print(result)  


# converting map object to set  
numbersAddition = set(result)  
print(numbersAddition)  


# <map object at 0x7fb04a6bec18>
{8, 2, 4, 6}



