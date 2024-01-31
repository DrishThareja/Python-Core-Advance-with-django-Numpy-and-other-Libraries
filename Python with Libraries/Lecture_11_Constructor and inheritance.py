
'Constructor & Inheritance'

'Constructor' # :-A constructor is a special type of method (function) which is used to initialize the instance members of the class

# In C++ or Java, the constructor has the same name as its class, but it treats constructor differently in Python. It is used to create an object.


# Constructors can be of two types.

# 1. Parameterized Constructor
# 2. Non-parameterized Constructor


# Constructor definition is executed when we create the object of this class. Constructors also verify that there are enough resources for the object to perform any start-up task.


# In Python, the method the __init__() simulates the constructor of the class. This method is called when the class is instantiated. It accepts the self-keyword as a first argument which allows accessing the attributes or method of the class.


# We can pass any number of arguments at the time of creating the class object, depending upon the __init__() definition. It is mostly used to initialize the class attributes. Every class must have a constructor, even if it simply relies on the default constructor.





class Employee:
  
    def __init__(self, name, id):  
        self.id = id  
        self.name = name  
  
    def display(self):  
        print("ID: %d \nName: %s" % (self.id, self.name))  
  
emp1 = Employee("John", 101)  
emp2 = Employee("David", 102) 
emp3 = Employee("jaspreet", 103)  
  
# accessing display() method to print employee 1 information  
emp1.display()  
  
# accessing display() method to print employee 2 & 3 information  
emp2.display()  
emp3.display()  

'Output:'
# ID: 101
# Name: John
# ID: 102
# Name: David
# ID: 103
# Name: Jaspreet


'--------------------------------------------------------------------------------------------------------------------------------------'

# other method:

class Employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)

emp1 = Employee("John", 101)
emp2 = Employee("David", 102)
emp3 = Employee("Jaspreet", 103)

emp1.display()
emp2.display()
emp3.display()

'Output:'
# ID: 101
# Name: John
# ID: 102
# Name: David
# ID: 103
# Name: Jaspreet


'--------------------------------------------------------------------------------------------------------------------------------------'


class Student:    
    count = 0    
    def __init__(self):    
        Student.count = Student.count + 1    
s1=Student()    
s2=Student()    
s3=Student()    
print("The number of students:",Student.count)          # The number of students: 3

'--------------------------------------------------------------------------------------------------------------------------------------'



# Python Non-Parameterized Constructor
# The non-parameterized constructor uses when we do not want to manipulate the value or the constructor that has only self as an argument. Consider the following example.

# Example

class Student:  
    # Constructor - non parameterized  
    def __init__(self):  
        print("This is non parametrized constructor")  
    def show(self,name):  
        print("Hello",name)  
x = Student()  
x.show("John")      

'Output:'

# This is non parameterized constructor.
# Hello Drish

'--------------------------------------------------------------------------------------------------------------------------------------'


# Python Parameterized Constructor
# The parameterized constructor has multiple parameters along with the self. Consider the following example.

# Example

class Student:  
    # Constructor - parameterized  
    def __init__(self, name):  
        print("This is parametrized constructor")  
        self.name = name  
    def show(self):  
        print("Hello",self.name)

student = Student("John")  
student.show()

'Output:'
# This is non parameterized constructor
# Hello Drish

'--------------------------------------------------------------------------------------------------------------------------------------'



# Python Default Constructor:-
# When we do not include the constructor in the class or forget to declare it, then that becomes the default constructor. It does not perform any task but initializes the objects. Consider the following example.    




class Student:  
    roll_num = 101  
    name = "Joseph"  
  
    def display(self):  
        print(self.roll_num,self.name)  
  
st = Student()  
st.display()  






# More than One Constructor in Single class:-


class Student:  
    def __init__(self):  
        print("The First Constructor") 
         
    def __init__(self):  
        print("The second contructor")  
  
st = Student()  



'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'



'Inheritance' #:- it is a process in which child class object acquare all the properties and behaviour of  parent class object. it is a process in which child class inherit from the base or parent class. Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.


# //parent or base
class A {
	

}

# //child or drived class
class B ( 'parentclassname' ) {
	


}

# example:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class  Student(Person):
  def __init__(self, fname, lname):
     super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()



# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

# Now the Student class has the same properties and methods as the Person class.




class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()





# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()




# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.




class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):

    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)







class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()



