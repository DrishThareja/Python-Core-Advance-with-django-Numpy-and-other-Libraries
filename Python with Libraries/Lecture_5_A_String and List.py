
# String: group of char is known as string.we can perform many operations with string.like compare,concat,reverse,lower-case,upper-case,copy,length,split...etc
# 'ram',"mohan"....,"""i am seldom """ ....etc.

# -> we can write string inside single,double and truple quotes 
# ''," ","""......"""

# ->string index start from zero.(0)
# a='ram'
#    012

# b="ram is a good boy"

# c="""asif is also a good boy and sin.'''


# #Using single quotes  
# str1 = 'Hello Python'  
# print(str1)  

# #Using double quotes  
# str2 = "Hello Python"  
# print(str2)  
  
# #Using triple quotes  
# str3 = '''''Triple quotes are generally used for  
#     represent the multiline or 
#     docstring'''   
# print(str3)  


#  splitting: 

#  [start:end]
 
# ram is a good boy
#  [1:5]


# str = "HELLO"  
# print(str[0])   
# print(str[1])  
# print(str[2])  
# print(str[3])  
# print(str[4])  

# # It returns the IndexError because 6th index doesn't exist  
# print(str[6])  


# str = "HELLO"  
# print(str[:]) #HELLO  
# print(str[0:]) #HELLO 
# print(str[:3]) #HEL  
# print(str[:5])  #HELLO
# print(str[2:5]) #LLO  


# -> RANGE CAN BE NEGATIVE
# str = "HELLO"

# print(str[-1]) #O  
# print(str[-3]) #L 
# print(str[-2:]) #LO 
# print(str[-4:-1])  #ELL


# UPDATE(Reassigning Strings):-Updating the content of the strings is as easy as assigning it to a new string. The string object doesn't support item assignment i.e., A string can only be replaced with new string since its content cannot be partially replaced. Strings are immutable in Python.


# str = "HELLO"

# str[0] = "h"    
# print(str)    

# O/P:TypeError: 'str' object does not support item assignment

# -> the string str can be assigned completely to a new content

# str = "HELLO"    
# print(str)   

# str = "hello"    
# print(str)    


# Output:

# HELLO
# hello  



# Deleting the String:-

# As we know that strings are immutable. We cannot delete or remove the characters from the string.  But we can delete the entire string using the del keyword.

# str = "hello" 
# del str[0]
# o/p:TypeError: 'str' object doesn't support item deletion 


# -> we can delete the entire string using the del keyword
# str = "hello" 
# del str
# print(str)
# o/pNameError: name 'str' is not defined




# str = "Hello"     
# str1 = " world"    
# print(str*3) # prints HelloHelloHello    
# print(str+str1)# prints Hello world     
# print(str[4]) # prints o                
# print(str[2:4]); # prints ll                    
# print('w' in str) # prints false as w is not present in str    
# print('wo' not in str1) # prints false as wo is present in str1.     
# prints              

# (r'C://python37') # prints C://python37 as it is written    

# print("The string str : %s"%(str)) # prints The string str : Hello     


# String Formatting:-
# suppose we need to write the text as - They said, "Hello what's going on?"- the given statement can be written in single quotes or double quotes but it will raise the SyntaxError as it contains both single and double-quotes.


# str = "They said, "Hello what's going on?" 
# print(str)  
# o/p
# SyntaxError: invalid syntax

# # using triple quotes  
# print('''''They said, "What's there?"''')  
  
# # escaping single quotes  
# print('They said, "What\'s going on?"')  
  
# # escaping double quotes  
# print("They said, \"What's going on?\"")  


# o/p:They said, "What's there?"
#     They said, "What\'s going on?"
#     They said, "What's going on?"

# capitalize():It capitalizes the first character of the String. This function is deprecated  
#             in python3   

#             a="ram is a good boy"
#             b=a.capitalize()
#             print("old string is "+a)
#             print("new string is "+b)

# o/p:

# old string is ram is a good boy
# new string is Ram is a good boy     # only 1st alphabet of 1st word becomes capital.

# upper():	It converts all the characters of a string to Upper Case.  


# str = "Hello lavya"  
# str2 = str.upper()  
# print(str2) 

# o/p:
# HELLO LAVYA



# list = ["irfan","sohan","mohan"]  

# for  i in list:  
#     print(i.upper())

# O/P:
#     IRFAN SOHAN MOHAN

# # Python upper() method   

# # Declaring variables  
# names = ["irfan","sohan","aman","mohan"]  
# vowels = ['a','e','i','o','u'] 

# for  i in names:  
#     for v in vowels:  
#         if(i.startswith(v)):  
#             print(i.upper())


#             O/P IRFAN AMAN


# startswith(str,beg=0,end=len(str))	It returns a Boolean value if the string starts with given str between begin and end.




# str = "Hello lavya"  
# str2 = str.startswith("Hello")  
# print (str2) 



# lower():	It converts all the characters of a string to Lower case.


# str = "Lavya Computer"  

# str = str.lower()  

# print(str)  

# o/p:lavya computer

# str = "LAVYA COMPUTER"  

# if str.lower() == "lavyacomputer":  
#     print("lowercase")  
# else:  
#     print("not lowercase")  



# isupper()	It returns true if all the characters of the string(if exists) is true otherwise it returns false.

# str = "WELCOME TO LAVYA"  

# str2 = str.isupper()  

# print(str2) 


# islower()	It returns true if the characters of a string are in lower case, otherwise false.

# str = "lavyacomputer"  

# str2 = str.islower()  

# print(str2) 


# str = "Welcome To Lavya "  

# str2 = str.islower()  

# print(str2)  



# isnumeric()	It returns true if the string contains only numeric characters.


# str = "12345"

# str2 = str.isnumeric()  
# print(str2)  




# isspace()	It returns true if the characters of a string are white-space, otherwise false.


# str = " " # empty string  
# # Calling function  
# str2 = str.isspace()  
# # Displaying result  
# print(str2)






# join(seq)	It merges the strings representation of the given sequence.

# str = ":"   # string  
# list = ['1','2','3']    # iterable  
# # Calling function  
# str2 = str.join(list)  
# # Displaying result  
# print(str2)  

# o/p: 1:2:3






# len(string)	It returns the length of a string.

# a="welcome to lavya"
# b=len(a)
# print("length is =",b)






# count(string,begin,end):It counts the number of occurrences of a substring in a String between begin and end index
# str = "Hello lavya computer"  
# str2 = str.count('e')  
# # Displaying result  
# print("occurences:", str2)  







# str = "ab bc ca de ed ad da ab bc ca"  
# oc = str.count('a')  
# # Displaying result  
# print("occurences:", oc)  











# find(substring ,beginIndex, endIndex):-It returns the index value of the string where substring is found between begin index and end index.

# Python find() method finds substring in the whole string and returns index of the first match. It returns -1 if substring does not match.


# str = "Welcome to the Javatpoint."  
# # Calling function  
# str2 = str.find("the")  
# # Displaying result  
# print(str2)  


# str = "Welcome to the to lavya computer."  
# # Calling function  
# str2 = str.find("to")  
# # Displaying result  
# print(str2)  




"""----------------------------------------------------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------------------------------------------------"""



# Python List:-A list in Python is used to store the sequence of various types of data. Python lists are mutable type its mean we can modify its element after it created. However, Python consists of six data-types that are capable to store the sequences, but the most common and reliable type is the list.

# A list can be defined as a collection of values or items of different types. The items in the list are separated with the comma (,) and enclosed with the square brackets [].

# l1=["ram","shyam","ashif","jasi",101]

# type():-use to check the type
# print(type(l1))


# o/p: <class - list>


# Characteristics of Lists
# The list has the following characteristics:

# The lists are ordered.
# The element of the list can access by index.
# The lists are the mutable type.
# A list can store the number of various elements.


# a = [1,2,"Peter",4.50,"Ricky",5,6]  
# b = [1,2,5,"Peter",4.50,"Ricky",6]  
# print(a == b) 

# False	


# List indexing and splitting:-
# The indexing is processed in the same way as it happens with the strings. The elements of the list can be accessed by using the slice operator [].

# The index starts from 0 and goes to length - 1. The first element of the list is stored at the 0th index, the second element of the list is stored at the 1st index, and so on.


# list = [1,2,3,4,5,6,7]
# print(list[0])  
# print(list[1])  
# print(list[2])  
# print(list[3])  

# # Slicing the elements  

# print(list[0:6])  #123456
# print(list[:])#1234567
# print(list[2:5]) #345
# print(list[1:6:2]) #246


# list = [1,2,3,4,5]  
# print(list[-1])  #5

# print(list[-3:])  #345
# print(list[:-1])  #1234
# print(list[-3:-1])  #3 4


# a=[10,20,30,40,50,90]
#            -3  -2 -1
# print(a[2:5]) #30 40 50
# print(a[-2:])
# print(a[-5:-1]) 


# Updating List values:-Lists are the most versatile data structures in Python since they are mutable, and their values can be updated by using the slice and assignment operator.

# Python also provides append() and insert() methods, which can be used to add values to the list.

# list = [1, 2, 3, 4, 5, 6]     
# print(list) #123456

# # It will assign value to the value to the second index   
# list[2] = 10   
# print(list) #1 2 10 4 5 6   

# # Adding multiple-element   
# list[1:3] = [89, 78]     
# print(list)  # 1 89 78 4 5 6  

# # It will add value at the end of the list  
# list[-1] = 25  
# print(list)#[1, 89, 78, 4, 5, 25]  

# Iterating a Lists:-

# list = ["John", "David", "James", "Jonathan"]  

# for i in list:   
#     # The i variable will iterate over the elements of the List and contains each element in each iteration. 

#     print(i)  


# Adding elements to the list:-
# Python provides append() function which is used to add an element to the list. However, the append() function can only add value to the end of the list.



# l =[]  
# n = int(input("Enter the number of elements in the list:"))5  
# for i in range(0,n):     
#     l.append(input("Enter the item:"))     

# print("printing the list items..")   
# for i in l:   
#     print(i, end = "  ")     





# Enter the number of elements in the list:5
# Enter the item:25
# Enter the item:46
# Enter the item:12
# Enter the item:75
# Enter the item:42
# printing the list items
# 25  46  12  75  42  


# Removing elements from the list
# Python provides the remove() function which is used to remove the element from the list.


# list = [0,1,2,3,4]     
# print("printing original list: ")    
# for i in list:    
#     print(i,end=" ") 

# list.remove(2)    
# print("\nprinting the list after the removal of first element...")    
# for i in list:    
#     print(i,end=" ")  



# Example: 1- Write the program to remove the duplicate element of the list.

# list1 = [1,2,2,3,55,98,65,65,13,29]  

# # Declare an empty list that will store unique values  
# list2 = []  

# for i in list1: 
#     if i not in list2:  
#         list2.append(i)  
# print(list2) 


# Example:2- Write a program to find the sum of the element in the list.

# list1 = [3,4,5,9,10,12,24]  
# sum = 0  
# for i in list1:  
#     sum += i      
# print("The sum is:",sum)  


# Example: 3- Write the program to find the lists consist of at least one common element.

# list1 = [1,2,3,4,5,6]  
# list2 = [7,8,9,2,10] 

# for x in list1:  
#     for y in list2:  
#         if x == y:  
#             print("The common element is:",x) 
