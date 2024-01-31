# TUPLE IN PYTHON:

# A collection of ordered and immutable objects is known as a tuple. Tuples and lists are similar as they both are sequences. Tuples and lists are different because we cannot modify tuples, although we can modify lists after creating them. As we use parentheses () to create tuples and square brackets [] to create lists this is also a reason.


tuple_1 = ("Python", "tuples", "immutable", "object")  
tuple_2 = (23, 42, 12, 53, 64) 
tuple_3 = "Python", "Tuples", "Ordered", "Collection"  
Empty_tuple = ()  #We represent an empty tuple by two parentheses enclosing nothing.
Tuple_1 = (50,)  # We need to add a comma after the element to create a tuple of a single element.

# Tuple indices begin at 0, and similar to strings, we can slice them, concatenate them, and perform other operations.

# Creating a Tuple

# All the objects (elements) must be enclosed in parenthesis (), each separated by a comma, to form a tuple. Although using parenthesis is not required, it is recommended to do so.


# Whatever the number of objects, even of various data types, can be included in a tuple (dictionary, string, float, list, etc.).



# Python program to show how to create a tuple  
  
# Creating an empty tuple  
empty_tuple = ()  
print("Empty tuple: ", empty_tuple)  # ()
  
# Creating tuple having integers  

int_tuple = (4, 6, 8, 10, 12, 14)  
print("Tuple with integers: ", int_tuple)  # (4, 6, 8, 10, 12, 14)
  
# Creating a tuple having objects of different data types  
mixed_tuple = (4, "Python", 9.3)  
print("Tuple with different data types: ", mixed_tuple)  # (4, 'Python', 9.3)
  
# Creating a nested tuple  
nested_tuple = ("Python", {4:5, 6: 2, 8:2},(5, 3, 5, 6))  
print("A nested tuple: ", nested_tuple)  # ('Python', {4: 5, 6: 2, 8: 2}, (5, 3, 5, 6))


# Parentheses is not mandatory to build tuples. Tuple packing is the term for this.

# Python program to create a tuple without using parentheses  
  
# Creating a tuple  
tuple_ = 4, 5.7, "Tuples", ["Python", "Tuples"]
print(tuple_)           # (4, 5.7, 'Tuples', ['Python', 'Tuples'])
print( type(tuple_) )   # <class 'tuple'>

# trying to modify tuple_  
  
tuple_[1] = 4.2 

# o/p:
# <class 'TypeError'>





# Python program to show how to create a tuple having a single element  
  
single_tuple = ("Tuple")  
print( type(single_tuple) ) #<class 'str'>   
  
# Creating a tuple that has only one element  
single_tuple = ("Tuple",)  
print( type(single_tuple) )   # <class 'tuple'>
  
# Creating tuple without parentheses  
single_tuple = "Tuple",  
print( type(single_tuple) )  #<class 'tuple'>



# Accessing Tuple Elements:-
# We can access the objects of a tuple in a variety of ways:-
# Indexing:-
# To access an object of a tuple, we can use the index operator [], where indexing in the tuple starts from 0.


# Python program to show how to access tuple elements  
  
tuple_ = ("Python", "Tuple", "Ordered", "Collection")    
print(tuple_[0])    # Python 
print(tuple_[1])    # Tuple
print(tuple_[5])    #tuple index out of range     
print(tuple_[1.0])  #tuple indices must be integers or slices, not float   


# Creating a nested tuple  
nested_tuple = ("Tuple", [4, 6, 2, 6], (6, 2, 6, 7))  
# Accessing the index of a nested tuple
print(nested_tuple[0][3])     # l   # 0 means the first element that is tuple and then its 3rd which is l   
print(nested_tuple[1][1])     # 6   # first [1] refers to the [4, 6, 2, 6] and then [1] refers to 6



# Negative Indexing
# Python's sequence objects support negative indexing.
# The last item of the collection is represented by -1, the second last item by -2, and so on.


# Python program to show how negative indexing works in Python tuples  

# Creating a tuple  
tuple_ = ("Python", "Tuple", "Ordered", "Collection")    
print("Element at -1 index: ", tuple_[-1])                  # Collection
print("Elements between -4 and -1 are: ", tuple_[-4:-1])    # ('Python', 'Tuple', 'Ordered')



# tuple Slicing:-
# We can use a slicing operator, a colon (:), to access a range of tuple elements


# Creating a tuple  
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects")    
print("Elements between indices 1 and 3: ", tuple_[1:3])    # ('Tuple', 'Ordered')
print("Elements between indices 0 and -4: ", tuple_[:-4])   # ('Python', 'Tuple')
print("Entire tuple: ", tuple_[:])                          # ('Python', 'Tuple', 'Ordered', 'Immutable', 'Collection', 'Objects')


# Deleting a Tuple
# The elements of a tuple cannot be changed, as was already said. Therefore, we are unable to eliminate or remove elements of a tuple.
# However, the keyword del makes it feasible to delete a tuple completely.

  
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects")  
# Deleting a particular element of the tuple  
del tuple_[3]  
print(tuple_)  # 'tuple' object doesn't support item deletion

# Deleting the variable from the global space of the program  
del tuple_  
print(tuple_)  # NameError: name 'tuple_' is not defined. Did you mean: 'tuple'?



# Repetition Tuples in Python:-

# Python program to show repetition in tuples  
    
tuple_ = ('Python',"Tuples")  
print("Original tuple is: ", tuple_)    # ('Python', 'Tuples')
  
# Repeting the tuple elements  
tuple_ = tuple_ * 3  
print("New tuple is: ", tuple_)         # ('Python', 'Tuples', 'Python', 'Tuples', 'Python', 'Tuples')




# Tuple Methods:
# Tuple does not provide methods to add or delete elements, and there are only the following two choices.

# Python program to show how to tuple methods (.index() and .count()) work  

tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Ordered")  
  
print(tuple_.count('Ordered')) # 2 
print(tuple_.index('Ordered')) # 2



# Tuple Membership Test:-
# Python program to show how to perform membership test for tuples  
# Creating a tuple
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Ordered")  

# In operator  
print('Ordered' in tuple_)          # True
print('Items' in tuple_)            # False
  
# Not in operator  
print('Immutable' not in tuple_)    # False
print('Items' not in tuple_)        # True



# Iterating Through a Tuple:-

# We can use a for loop to iterate through each element of a tuple

# Python program to show how to iterate over tuple elements  
  
# Creating a tuple  
tuple_ = ("Python", "Tuple", "Ordered", "Immutable")  
  
# Iterating over tuple elements using a for loop  
for item in tuple_:  
    print(item)  

# Output:

# Python
# Tuple
# Ordered
# Immutable


# Changing a Tuple:- Tuples, as opposed to lists, are immutable objects.

# This implies that after a tuple's elements have been specified, we cannot modify them. However, we can modify the nested elements of an element if the element itself is a mutable data type like a list.


# Python program to show that Python tuples are immutable objects  
  
# Creating a tuple  
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", [1,2,3,4])  
  
# Trying to change the element at index 2  
  
tuple_[2] = "Items"  
print(tuple_)                       # Error
  
# But inside a tuple, we can change elements of a mutable object  
tuple_[-1][2] = 10   
print(tuple_)                       # ('Python', 'Tuple', 'Ordered', 'Immutable', [1, 2, 10, 4])    # -1 position ka 2nd part changed
  
# Changing the whole tuple  
tuple_ = ("Python", "Items")    
print(tuple_)                       # ('Python', 'Items')


# To merge multiple tuples, we can use the + operator. Concatenation is the term for this.

# Using the * operator, we may also repeat a tuple's elements for a specified number of times. This is already shown above.


# Python program to show how to concatenate tuples  

# Creating a tuple  
tuple_ = ("Python", "Tuple", "Ordered", "Immutable")  
  
# Adding a tuple to the tuple_  
print(tuple_ + (4, 5, 6))  # ('Python', 'Tuple', 'Ordered', 'Immutable', 4, 5, 6)




"""----------------------------------------------------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------------------------------------------------"""

# Sets in python:-

# A Python set is the collection of the unordered items. Each element in the set must be unique, immutable, and the sets remove the duplicate elements. Sets are mutable which means we can modify it after its creation.

# Unlike other collections in Python, there is no index attached to the elements of the set, i.e., we cannot directly access any element of the set by the index. However, we can print them all together, or we can get the list of elements by looping through the set.


# Creating a set:

# The set can be created by enclosing the comma-separated immutable items with the curly braces {}. Python also provides the set() method, which can be used to create the set by the passed sequence.

Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}   
print(Days)             # {'Friday', 'Tuesday', 'Monday', 'Saturday', 'Thursday', 'Sunday', 'Wednesday'}   
print(type(Days))       # <class 'set'>  

print("looping through the set elements ... ")    
for i in Days:    
    print(i)    

# o/p: 

# Monday
# Wednesday
# Friday
# Tuesday
# Thursday
# Sunday
# Saturday

# Creating a set which have immutable elements  

set1 = {1,2,3, "JavaTpoint", 20.5, 14}  
print(type(set1))       # <class 'set'>

#Creating a set which have mutable element  
set2 = {1,2,3,["Javatpoint",4]}  
print(type(set2))       # TypeError: unhashable



# Adding items to the set:-
# Python provides the add() method and update() method which can be used to add some particular item to the set.
# The add() method is used to add a single element whereas the update() method is used to add multiple elements to the set



Months = set(["January","February", "March", "April", "May", "June"])    
  

print("\nAdding other months to the set...");    
Months.add("July");    
Months.add ("August");  

print("\nPrinting the modified set...");    
print(Months)                               # {'June', 'April', 'March', 'August', 'January', 'May', 'February', 'July'}

print("\nlooping through the set elements ... ")    
for i in Months:    
    print(i) 

# o/p of loop:
# June
# April
# March
# August
# January
# May
# February
# July



Months = set(["January","February", "March", "April", "May", "June"])    

Months.update(["July","August","September","October"]);    
print(Months);              # {'May', 'January', 'September', 'July', 'October', 'June', 'February', 'March', 'April', 'August'}





# Removing items from the set:-

# Python provides the discard() method and remove() method which can be used to remove the items from the set. The difference between these function, using discard() function if the item does not exist in the set then the set remain unchanged whereas remove() method will through an error

# DISCARD:-
months = set(["January","February", "March", "April", "May", "June"])    


print("\nRemoving some months from the set...");    
months.discard("January");    
months.discard("May");    

print("\nPrinting the modified set...");    
print(months)                       # {'March', 'April', 'June', 'February'}

print("\nlooping through the set elements ... ")    
for i in months:    
    print(i)    #  |
                #  |
# o/p:          # <-
# March
# April
# June
# February


# REMOVE :
months = set(["January","February", "March", "April", "May", "June"])    

print("\nprinting the original set ... ")    
print(months)    

print("\nRemoving some months from the set...");    
months.remove("January");    
months.remove("May"); 

print("\nPrinting the modified set...")
print(months)               # {'March', 'April', 'June', 'February'}



# Union of two Sets:

# The union of two sets is calculated by using the pipe (|) operator. The union of the two sets contains all the items that are present in both the sets.

Days1 = {"Monday","Tuesday","Wednesday","Thursday", "Sunday"}    
Days2 = {"Friday","Saturday","Sunday"}    
print(Days1|Days2) #printing the union of the sets  
# {'Friday', 'Sunday', 'Saturday', 'Tuesday', 'Wednesday', 'Monday', 'Thursday'}


# Python also provides the union() method which can also be used to calculate the union of two sets
Days1 = {"Monday","Tuesday","Wednesday","Thursday"}
Days2 = {"Friday","Saturday","Sunday"}    
print(Days1.union(Days2)) #printing the union of the sets    
# {'Friday', 'Sunday', 'Saturday', 'Tuesday', 'Wednesday', 'Monday', 'Thursday'}

"""----------- Both union keyword and | can be use for same output. -----------"""


# Intersection of two sets:-

# The intersection of two sets can be performed by the and & operator or the intersection() function. The intersection of the two sets is given as the set of the elements that common in both sets.


# Example 1: Using & operator

Days1 = {"Monday","Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday","Tuesday","Sunday", "Friday"}    
print(Days1&Days2) #prints the intersection of the two sets  


# Output:

{'Monday', 'Tuesday'}


# Example 2: Using intersection() method

set1 = {"Devansh","John", "David", "Martin"}    
set2 = {"Steve", "Milan", "David", "Martin"}    
print(set1.intersection(set2)) #prints the intersection of the two sets    

# Output:

{'Martin', 'David'}


# The intersection_update() method

# The intersection_update() method removes the items from the original set that are not present in both the sets (all the sets if more than one are specified).


# The intersection_update() method is different from the intersection() method since it modifies the original set by removing the unwanted items, on the other hand, the intersection() method returns a new set.

a = {"Devansh", "bob", "castle"}    
b = {"castle", "dude", "emyway"}    
c = {"fuson", "gaurav", "castle"}    
    
a.intersection_update(b, c)      
print(a) 

# o/p:-
{'castle'}


# Difference between the two sets:-

# The difference of two sets can be calculated by using the subtraction (-) operator or intersection() method. Suppose there are two sets A and B, and the difference is A-B that denotes the resulting set will be obtained that element of A, which is not present in the set B.



Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday", "Sunday"}    
print(Days1-Days2) # {"Wednesday", "Thursday" will be printed}  

# o/p:
{'Thursday', 'Wednesday'}  



# Example 2 : Using difference() method

Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday", "Sunday"}    
print(Days1.difference(Days2)) # prints the difference of the two sets Days1 and Days2    


# Output:

{'Thursday', 'Wednesday'}


# Set comparisons

# Python allows us to use the comparison operators i.e., <, >, <=, >= , == with the sets by using which we can check whether a set is a subset, superset, or equivalent to other set. The boolean true or false is returned depending upon the items present inside the sets.



Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday"}    
Days3 = {"Monday", "Tuesday", "Friday"}    
    
#Days1 is the superset of Days2 hence it will print true.     
print (Days1>Days2)     
    
#prints false since Days1 is not the subset of Days2     
print (Days1<Days2)    
    
#prints false since Days2 and Days3 are not equivalent     
print (Days2 == Days3)    

# Example - 1: Write a program to remove the given number from the set.

my_set = {1,2,3,4,5,6,12,24}  
n = int(input("Enter the number you want to remove"))   # 12  
my_set.discard(n)  
print("After Removing:",my_set)  

# o/p:-  1,2,3,4,5,6,24


# Example - 2: Write a program to add multiple elements to the set.

set1 = set([1,2,4,"John","CS"])  
set1.update(["Apple","Mango","Grapes"])  
print(set1)  

# {'CS', 1, 2, 'Grapes', 4, 'Mango', 'Apple', 'John'}