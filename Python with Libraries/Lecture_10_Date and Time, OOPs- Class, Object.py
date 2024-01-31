

'Python Date and time:-'


#Python provides the datetime module work with real dates and times. In real-world applications, we need to work with the date and time. Python enables us to schedule our Python script to run at a particular timing.

# In Python, the date is not a data type, but we can work with the date objects by importing the module named with datetime, time, and calendar.

# The datetime classes are classified in the six main classes.

'date' # - It is a naive ideal date. It consists of the year, month, and day as attributes.

'time' # - It is a perfect time, assuming every day has precisely 24*60*60 seconds. It has hour, minute, second, microsecond, and       tzinfo as attributes.

'datetime' # - It is a grouping of date and time, along with the attributes year, month, day, hour, minute, second, microsecond, and tzinfo.

'timedelta' # - It represents the difference between two dates, time or datetime instances to microsecond resolution.

'tzinfo' # - It provides time zone information objects.

'timezone' # - It is included in the new version of Python. It is the class that implements the tzinfo abstract base class.



# Tick
# In Python, the time instants are counted since 12 AM, 1st January 1970. The function time() of the module time returns the total number of ticks spent since 12 AM, 1st January 1970. A tick can be seen as the smallest unit to measure the time.



import time;  
#prints the number of ticks spent since 12 AM, 1st January 1970  

print(time.time())                                  # 1705489503.7420108

# How to get the current time?
# The localtime() functions of the time module are used to get the current time tuple.



import time;        
#returns a time tuple     
    
print(time.localtime(time.time()))
# time.struct_time(tm_year=2024, tm_mon=1, tm_mday=17, tm_hour=11, tm_min=5, tm_sec=3, tm_wday=2, tm_yday=17, tm_isdst=0)


'--------------------------------------------------------------------------------------------------------------------------------------'


# Python Arrays:- array is defined as a collection of items that are stored at contiguous memory locations. It is a container which can hold a fixed number of items, and these items should be of the same type. An array is popular in most programming languages like C/C++, JavaScript, etc.


# Array is an idea of storing multiple items of the same type together and it makes easier to calculate the position of each element by simply adding an offset to the base value. A combination of the arrays could save a lot of time by reducing the overall size of the code. It is used to store multiple values in single variable. If you have a list of items that are stored in their corresponding variables like this:



value =10, 20, 30, 40, 50
index = 0, 1,  2,  3,  4


car1 = "Lamborghini"
car2 = "Bugatti"
car3 = "swift"




# Element - Each item stored in an array is called an element.

# Index - The location of an element in an array has a numerical index, which is used to identify the position of the element.




a =       10,20,30,40,50,60
index =    0, 1, 2 ,3, 4, 5

#    index = size - 1
#        5 = 6 - 1

# -> Index starts with 0.
# -> We can access each element via its index.
# -> The length of the array defines the capacity to store the elements.


# Why to use arrays in Python?
# A combination of arrays saves a lot of time. The array can reduce the overall size of the code.

# Array operations
# Some of the basic operations supported by an array are as follows:

'Traverse'      # - It prints all the elements one by one.
'Insertion'     # - It adds an element at the given index.
'Deletion'      # - It deletes an element at the given index.
'Search'        # - It searches an element using the given index or by the value.
'Update'        # - It updates an element at the given index.



# The Array can be created in Python by importing the array module to the python program.


from array import *  
arrayName = array('typecode', ['initializers']) 



import array as arr 

a = arr.array('i', [2, 4, 6, 8])  
print("First element:", a[0])       # 2
print("Second element:", a[1])      # 4

print("last element:", a[-1])       # 8

# we have imported an array, defined a variable named as "a" that holds the elements of an array and print the elements by accessing elements through indices of an array.


# How to change or add elements: Arrays are mutable, and their elements can be changed in a similar way like lists.


import array as arr  
numbers = arr.array('i', [1, 2, 3, 5, 7, 10])  
   
# changing first element  
numbers[0] = 17     
print(numbers)  

# Output: array('i', [17, 2, 3, 5, 7, 10])  
   
# changing 3rd to 5th element  
numbers[2:5] = arr.array('i', [4, 6, 8])    
print(numbers)    # Output: array('i', [17, 2, 4, 6, 8, 10])  


# How to delete elements from an array?: elements can be deleted from an array using Python's del statement. If we want to delete any value from the array, we can do that by using the indices of a particular element.


import array as arr  
number = arr.array('i', [1, 2, 3, 3, 4])  
del number[2]                           # removing third element  
print(number)                           # Output: array('i', [1, 2, 3, 4])  


# Finding the length of an array:-

# The length of an array is defined as the number of elements present in an array. It returns an integer value that is equal to the total number of the elements present in that array.

# Syntax

len('array_name')  


# Array Concatenation:-
# we can easily concatenate any two arrays using the + symbol.

a=arr.array('d',[1.1 , 2.1 ,3.1,2.6,7.8])  
b=arr.array('d',[3.7,8.6])  
c=arr.array('d')  
c=a+b  
print("Array c = ",c)  # Array c= array('d', [1.1, 2.1, 3.1, 2.6, 7.8, 3.7, 8.6])





cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)




# Adding Array Elements
# You can use the append() method to add an new element to an array.

cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda")

print(cars)



# Removing Array Elements:-
# You can use the pop() method to remove an element from the array.

cars = ["Ford", "Volvo", "BMW"]

cars.pop(1)

print(cars)

# You can also use the remove() method to remove an element from the array.

cars = ["Ford", "Volvo", "BMW"]

cars.remove("Volvo")


print(cars)





'copy()' # Method:-The copy() method returns a copy of the specified list.

# Syntax
# list.copy()


fruits = ["apple", "banana", "cherry"]

x = fruits.copy()

print(x)            # ['apple', 'banana', 'cherry']



'reverse()' # Method:-The reverse() method reverses the sorting order of the elements.

# Syntax
# list.reverse()

fruits = ["apple", "banana", "cherry"]

fruits.reverse()

print(fruits)       # ['cherry', 'banana', 'apple']




'sort()' # Method:-Sort the list alphabetically:

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()
print(cars)         # ['BMW', 'Ford', 'Volvo']



'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'



'Python OOPs:-' 

# class
# object
# constructor
# inheritance 
# abstraction


# class:- group of object is known as class that have variable,function,constructor and another more objects class can contains

'class' # keyword use to delcare the class

# -> it is also known as logical entity because it dont exist physically.
# -> and also known as template or blueprint

# syntax:

class classname:
	# var,
	# fun
	# constr





# class Lavya:
    id = 10   
    name = "Devansh"   

    def display (self):    
        print(self.id,self.name)  


# the self is used as a reference variable, which refers to the current class object. It is always the first argument in the function definition. However, using self is optional in the function call.


# The self-parameter
# The self-parameter refers to the current instance of the class and accesses the class variables. We can use anything instead of self, but it must be the first parameter of any function which belongs to the class.


class Employee:    
    id = 10   
    name = "John"  
      
    def display (self):    
        print("ID: %d \nName: %s"%(self.id,self.name))  

# Creating a emp instance of Employee class  
emp = Employee() 
emp1 = Employee()
emp2 = Employee()     
emp.display() 




'Object' # :- it is instance of the class that have more then one property.
# -> it is used to access memeber of the class.
# -> we can create more then one object of a class.but object name always be different.

# syntax:

# object - name = class - name ( arguments1 , args2 )
  
class Demo:
# pass

# d = Demo()

# d.membername



# class Demo:
    def ram():
       print("hello ram")

d=Demo()
d1=Demo()
d.ram() 
d1.ram()      





# Delete the Object:- we can delete the object
# We can delete the properties of the object or object itself by using the del keyword.

class Employee:  
    id = 10  
    name = "John" 

    def display(self):  
        print("ID: %d \nName: %s" % (self.id, self.name)) 

    # Creating a emp instance of Employee class  
  
emp = Employee()  
  
# Deleting the property of object  
del emp.id 


# Deleting the object itself  
del emp  
emp.display()  


