# Python Dictionary:

# Python Dictionary is used to store the data in a key-value pair format. The dictionary is the data type in Python, which can simulate the real-life data arrangement where some specific value exists for some particular key. It is the mutable data-structure. The dictionary is defined into element Keys and values.



# Keys must be a single element
# Value can be any type such as list, tuple, integer, etc.


# In other words, we can say that a dictionary is the collection of key-value pairs where the value can be any Python object. In contrast, the keys are the immutable Python object, i.e., Numbers, string, or tuple.


# Creating the dictionary
# The dictionary can be created by using multiple key-value pairs enclosed with the curly brackets {}, and each key is separated from its value by the colon (:).



Dict = {"Name": "Tom", "Age": 22} 
print(Dict)             # {"Name": "Tom", "Age": 22}
print(type(Dict))       # <class 'dict'>


Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
print(type(Employee))        # <class 'dict'>
print(Employee)              # {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}




# dict() method which is also used to create dictionary. The empty curly braces {} is used to create empty dictionary.

Dict={}
print(Dict)     # {}


Dict= dict({1:'lavya',2:'mohan',3:'ashif'})
print(Dict)     # {1:'lavya',2:'mohan',3:'ashif'}


# with each item as a Pair   
Dict = dict([(1, 'Devansh'), (2, 'Sharma')])      
print(Dict)     # {1: 'Devansh', 2: 'Sharma'}




# Accessing the dictionary values:
# We have discussed how the data can be accessed in the list and tuple by using the indexing.
# However, the values can be accessed in the dictionary by using the keys as keys are unique in the dictionary.
# The dictionary values can be accessed in the following way.



Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}  
print(type(Employee))                               # <class 'dict'>


print("Name : %s" %Employee["Name"])                #   Name : John
print("Age : %d" %Employee["Age"])                  #   Age : 29
print("Salary : %d" %Employee["salary"])            #   Salary : 25000
print("Company : %s" %Employee["Company"])          #   Company : GOOGLE

# another way

print("Name :", Employee["Name"])                   #   Name : John
print("Age :", Employee["Age"])                     #   Age : 29
print("Salary:", Employee["salary"])                #   Salary : 25000
print("Company:", Employee["Company"])              #   Company : GOOGLE





# Adding dictionary values:-

# The dictionary is a mutable data type, and its values can be updated by using the specific keys. The value can be updated along with key 
# Dict[key] = value. The update() method is also used to update an existing value.


# Creating an empty Dictionary   
Dict = {}   
print("Empty Dictionary: ")   
print(Dict)                                         # {}
    

# Adding elements to dictionary one at a time   
Dict[0] = 'Peter'  
Dict[2] = 'Joseph'  
Dict[3] = 'Ricky'  
print("\nDictionary after adding 3 elements: ")   
print(Dict)                                         # {0: 'Peter', 2: 'Joseph', 3: 'Ricky'}
    

# Adding set of values with a single Key   
# The Emp_ages doesn't exist to dictionary  
Dict['Emp_ages'] = 20, 33, 24  
print("\nDictionary after adding 3 elements: ")   
print(Dict)                                         # {0: 'Peter', 2: 'Joseph', 3: 'Ricky', 'Emp_ages': (20, 33, 24)}

# Updating existing Key's Value   
Dict[3] = 'rohit'  
print("\nUpdated key value: ")   
print(Dict)                                         # {0: 'Peter', 2: 'Joseph', 3: 'rohit', 'Emp_ages': (20, 33, 24)}






# Deleting elements using del keyword:-
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
print(type(Employee))                                           # <class 'dict'>

print("printing Employee data .... ")    
print(Employee)                                                 # {'Name': 'John', 'Age': 29, 'salary': 25000, 'Company': 'GOOGLE'}

print("Deleting some of the employee data") 

del Employee["Name"]    
del Employee["Company"]    
print("printing the modified information ")    
print(Employee)                                                 # {'Age': 29, 'salary': 25000}

print("Deleting the dictionary: Employee");  

del Employee  

print("Lets try to print it again ")

print(Employee)                                                 # ERROR!


# Using pop() method:-
# The pop() method accepts the key as an argument and remove the associated value

# Creating a Dictionary   

Dict = {1: 'lavya', 2: 'Peter', 3: 'Thomas'}   

# Deleting a key    
# using pop() method  

pop_ele = Dict.pop(3)   
print(Dict)                         # {1: 'lavya', 2: 'Peter'}
"""-----------------------"""

pop_ele = Dict.pop(3)
pop_ele = Dict.pop(1)
print(Dict)                         # {2: 'Peter'}
print(pop_ele)                      # lavya             # because it is the done after 3rd one




# loop in dictionary:

Employee = {"Name": "John", "Age": 29, "Salary":25000,"Company":"GOOGLE"}    
for x in Employee:    
    print(x)  

    # Name 
    # Age
    # Salary
    # Company



Employee = {"Name": "John", "Age": 29, "Salary":25000,"Company":"GOOGLE"}    
for x in Employee:
     print(x, " = ", Employee[x])
         
# Name  =  John
# Age  =  29
# Salary  =  25000
# Company  =  GOOGLE




Employee = {"Name": "John", "Age": 29, "Salary":25000,"Company":"GOOGLE"}    
for x in Employee.values():    
    print(x)  

# John
# 29
# 25000
# GOOGLE




Employee = {"Name": "John", "Age": 29, "Salary":25000,"Company":"GOOGLE"}    
for x in Employee.items():    
    print(x)  


('Name', 'John')
('Age', 29)
('Salary', 25000)
('Company', 'GOOGLE')

# to clear content of dict complete
Employee.clear()                            # .clear() --> to clear the data of dictionary

data=Employee.copy()                        # .copy() --> to copy the data of dictionary
print(data)                                 # {}    --> empty dict as data is clear


