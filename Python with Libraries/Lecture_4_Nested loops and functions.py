"""
nested for loop :-for loop inside the for loop known as nested for loop.

 # row
for varname in range():
# col
  for varname in range():

      statement 



example:
for i in range(1 ,6):
    for j in range(1,6):
        print("*",end="")
    print("")

Output:
o/p:
*****
*****
*****
*****
*****


function :-block of code is known as function that is used to perform a specific task.
            def keyword is used to declare the function.
            
           -> it provide code reusablity and optimization.
            
           -> 'def' keyword is used to define function 

syntax:

 def function_name():
     code to exicute.


why: no need to write code again and again to perform similar task
     thats why we make function.



     type of function:

     1.predefined function(library fun)
     2.user defined function

predefined function(library fun):- library function are known as predefined function.its name and working is all ready fixed.

print(),input(),range()


2.user defined funtion: function that is created by user according to need.known as user defined function, we can provide any name to the function and can perform any task.
	 


def demo():
    print("hello")

how to call  a function: 
function is called by function name and followed by the (),we can call a function more then one time.

demo() #hello'
demo() #hello 
demo() #hello 



basis of argument type of function:-

1. non parametrized functon
2. parametrized function

a). non parametrized functon:-
 if we not pass any arguments in () at the time of function declaration known as non parametrized function.

def demo():
    print("hello")

demo()


b)parametrized function:- if we pass arguments in () at the time of function declaration.known as parametrized function,we can pass more then one arguments in ()and of any type.

def sum(a,b):
    print(a+b) #30



def sum(a,b):
    c=a+b
    print(c)



sum(10,20)  #30
sum(70,60)  #130


def cube(x):
   r=x**3
   return r

b=cube(2)
print(b)


def add(a, b):
 
    # returning sum of a and b
    return a + b
 
 
def is_true(a):
 
    # returning boolean of a
    return bool(a)
 
# calling function
res = add(2, 3)
print("Result of add function is {}".format(res))
 
res = is_true(2<5)
print("Result of is_true function is {}".format(res))


# This function returns a tuple
def fun():
    str = "geeks"
    x = 20
    return str, x;  # Return tuple, we could also
                    # write (str, x)
   
# Driver code to test above method
str, x = fun() # Assign returned tuple
print(str)
print(x)
"""

