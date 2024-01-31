str1 = 'Hi'
str2 = "Hello"
str3 = """Boy"""

print(str3) # String 3 will be print

# Splitting:
# [ start : end ]

str4 = "ram is a good boy."
print(str4[1:5])


print(str2[0])
print(str2[1])
print(str2[2])
print(str2[3])
print(str2[4])
print(str2[6])  # it returns the IndexError because 6th index doesn't exist

# splitting:
print(str[:])   # Hello
print(str[0:])  # Hello     # It starts from 0 to end
print(str[:3])  # Hel       # It starts from 0 to 3 excluding 3
print(str[:5])  #Hello
print(str[2:5]) #llo        # It starts from 2 to 4


# Range can be Negative:
str4 = "HELLO"

print(str[-1]) #O  
print(str[-3]) #L 
print(str[-2:]) #LO 
print(str[-4:-1])  #ELL


# Updating:

str = "HELLO"
str[0] = "h"
print(str)  #o/p : TypeError: 'str' object does not support item assignment

# the string can be assigned completely to a new content

str = "HELLO"
print(str)

str = "hello"
print(str)

# Output;
# HELLO
# hello


# Deleting the string:

str = "hello"
del str[0]
# o/p: TypeError: 'str' object doesn't support item deletion


# we can delete the entire string using the del keyword

str = "hello"
del str
print(str)
# O/P: NameError: name 'str' is not defined



str = " Hello "
str1 = " world"
print(str*3)    # Hello  Hello  Hello
print(str + str1)   # Hello  world
print(str[4])   # l
print(str[2:4]) # el

print('w' in str)   # print: false as w is not present in str
print('wo' not in str1) # print: false as wo is present in str1

print("The string str: %s"%(str))   # prints The string str : Hello



# String Formating:

str = "They said, Hello what's going on?"
print(str)
# o/p:
# SyntaxError: invalid syntax

# using triple quotes:
print("""They said, \"What's there?\"""")

# escaping single quotes  
print('They said, "What\'s going on?"')  
  
# escaping double quotes  
print("They said, \"What's going on?\"")

# o/p:
# They said, "What's there?"
# They said, "What\'s going on?"
# They said, "What's going on?"


# capitalize():

a = "ram is a good boy"
b = a.capitalize()  # only 1st alphabet of 1st word will become capital
print("old string is "+a)
print("new string is "+b)

#o/p:
# old string is ram is a good boy.
# new string is Ram is a good boy.



# upper():
str = "Hello lavya"  
str2 = str.upper()  
print(str2) 

# o/p:
# HELLO LAVYA

str = "Hello lavya"  
str2 = str.startswith("Hello")  
print (str2)    # true


# lower():

str = "Lavya Computer"  
str = str.lower()  
print(str)  

# o/p:lavya computer

str = "LAVYA COMPUTER"  
if str.lower() == "lavyacomputer":  
    print("lowercase")  
else:  
    print("not lowercase")


# isupper():
str = "Welcome to lavya"
str2 = str.isupper()
print(str2) # false


# islower():
str2 = str.islower()
print(str2) # false


# isnumeric()
str = "12345"
str2 = str.isnumeric()
print(str2) # true


# isspace():
str = " "
str2 = str.isspace()
print(str2) # True

# join(seq):
str = ":"
list = ['1','2','3']
str2 = str.join(list)
print(str2) # o/p:- 1:2:3


# len(string):
a="welcome to lavya"
b=len(a)
print("length is =",b)


# count(string,begin,end):
str = "Hello lavya computer"
str2 = str.count('e')
print("occurences: ",str2)  # 2


str = "ab bc ca de ed ad da ab bc ca"
oc = str.count('a')
print("occurences: ",oc)    # 6


# find(substring ,beginIndex, endIndex)
str = "Welcome to the Javatpoint."   
str2 = str.find("the")  
print(str2)  # 11


str = "Welcome to the to lavya computer."   
str2 = str.find("to")  
print(str2) # 8

