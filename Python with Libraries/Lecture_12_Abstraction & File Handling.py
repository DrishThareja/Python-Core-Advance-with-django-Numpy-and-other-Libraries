

'Abstraction & File Handling:'


# Abstraction: Abstraction is used to hide the internal functionality of the function from the users. The users only interact with the basic implementation of the function, but inner working is hidden. User is familiar with that "what function does" but they don't know "how it does."

# In simple words, we all use the smartphone and very much familiar with its functions such as camera, voice-recorder, call-dialing, etc., but we don't know how these operations are happening in the background. Let's take another example - When we use the TV remote to increase the volume. We don't know how pressing a key increases the volume of the TV. We only know to press the "+" button to increase the volume.

# That is exactly the abstraction that works in the object-oriented concept.

# Why Abstraction is Important?
# In Python, an abstraction is used to hide the irrelevant data/class in order to reduce the complexity. It also enhances the application efficiency.

# Abstraction classes in Python:-

# A class that consists of one or more abstract method is called the abstract class. Abstract methods do not contain their implementation. Abstract class can be inherited by the subclass and abstract method gets its definition in the subclass. Abstraction classes are meant to be the blueprint of the other class. An abstract class can be useful when we are designing large functions. An abstract class is also helpful to provide the standard interface for different implementations of components. Python provides the abc module to use the abstraction in the Python program. Let's see the following syntax.

# Syntax

'from abc import ABC'
'class ClassName(ABC):'




# Abstract Base Classes
# An abstract base class is the common application program of the interface for a set of subclasses. It can be used by the third-party, which will provide the implementations such as with plugins. It is also beneficial when we work with the large code-base hard to remember all the classes.



# Python program demonstrate  
# abstract base class work   

from abc import ABC     # abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")   
          
# Driver code   
t= Tesla ()   
t.mileage()             # The mileage is 30kmph 
r = Renault()   
r.mileage()             # The mileage is 27kmph
s = Suzuki()   
s.mileage()             # The mileage is 25kmph
d = Duster()   
d.mileage()             # The mileage is 24kmph



# In the above code, we have imported the abc module to create the abstract base class. We created the Car class that inherited the ABC class and defined an abstract method named mileage(). We have then inherited the base class from the three different subclasses and implemented the abstract method differently. We created the objects to call the abstract method.s  




# abstract class  
  
from abc import ABC  
  
class Polygon(ABC):   
  
   # abstract method   
   def sides(self):   
      pass  
  
class Triangle(Polygon):   
  
     
   def sides(self):   
      print("Triangle has 3 sides")   
  
class Pentagon(Polygon):   
  
     
   def sides(self):   
      print("Pentagon has 5 sides")   
  
class Hexagon(Polygon):   
  
   def sides(self):   
      print("Hexagon has 6 sides")   
  
class square(Polygon):   
  
   def sides(self):   
      print("Square have 4 sides")   
  
# Driver code   
t = Triangle()
t.sides()                   # Triangle has 3 sides
  
s = square()   
s.sides()                   # Square have 4 sides
  
p = Pentagon()   
p.sides()                   # Pentagon has 5 sides
  
k = Hexagon()   
k.sides()                   # Hexagon has 6 sides



'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'



#Python File Handling: The file handling plays an important role when the data needs to be stored permanently into the file. A file is a named location on disk to store related information. We can access the stored information (non-volatile) after the program termination.

# The file-handling implementation is slightly lengthy or complicated in the other programming language, but it is easier and shorter in Python.

# we can perform many operation in file like open ,close,read ,write ,search and more operation we can perform with file.


# In Python, files are treated in two modes as text or binary. The file may be in the text or binary format, and each line of a file is ended with the special character.

# Hence, a file operation can be done in the following order.

'Open a file'
'Read or write - Performing operation'
'Close the file'



# Opening a file: Python provides an open(filename,mode) function that accepts two arguments, file name and access mode in which the file is accessed. The function returns a file object which can be used to perform various operations like reading, writing, etc.

# Syntax:

# file object = open(<file-name>, <access-mode>, <buffering>)  




'r'	# It opens the file to read-only mode. The file pointer exists at the beginning. The file is by default open in this mode if no access mode is passed.

'rb' # It opens the file to read-only in binary format. The file pointer exists at the beginning of the file.

'r+' # It opens the file to read and write both. The file pointer exists at the beginning of the file.

'rb+' # It opens the file to read and write both in binary format. The file pointer exists at the beginning of the file.

'w' # It opens the file to write only. It overwrites the file if previously exists or creates a new one if no file exists with the same name. The file pointer exists at the beginning of the file.

'wb' # It opens the file to write only in binary format. It overwrites the file if it exists previously or creates a new one if no file exists. The file pointer exists at the beginning of the file.

'w+' # It opens the file to write and read both. It is different from r+ in the sense that it overwrites the previous file if one exists whereas r+ doesn't overwrite the previously written file. It creates a new file if no file exists. The file pointer exists at the beginning of the file.

'wb+' # It opens the file to write and read both in binary format. The file pointer exists at the beginning of the file.

'a' # It opens the file in the append mode. The file pointer exists at the end of the previously written file if exists any. It creates a new file if no file exists with the same name.

'ab' # It opens the file in the append mode in binary format. The pointer exists at the end of the previously written file. It creates a new file in binary format if no file exists with the same name.

'a+' # It opens a file to append and read both. The file pointer remains at the end of the file if a file exists. It creates a new file if no file exists with the same name.

'ab+' # It opens a file to append and read both in binary format. The file pointer remains at the end of the file.



fileptr = open("file.txt","r")    
    
if fileptr:    
    print("file is opened successfully")  


# we have passed filename as a first argument and opened file in read mode as we mentioned r as the second argument. The fileptr holds the file object and if the file is opened successfully, it will execute the print statement



# The close() method: Once all the operations are done on the file, we must close it through our Python script using the close() method. Any unwritten information gets destroyed once the close() method is called on a file object.

# We can perform any operation on the file externally using the file system which is the currently opened in Python; hence it is good practice to close the file once all the operations are done.

# The syntax to use the close() method is given below.

# Syntax

# fileobject.close()   



fileptr = open("file.txt","r")    
    
if fileptr:    
    print("file is opened successfully")  

    fileptr.close()


# After closing the file, we cannot perform any operation in the file. The file needs to be properly closed. If any exception occurs while performing some operations in the file then the program terminates without closing the file.



# open the file.txt in append mode. Create a new file if no such file exists.  
fileptr = open("file2.txt", "w")  
  
# appending the content to the file  
fileptr.write('''''Python is the modern day language. It makes things so simple. 
It is the fastest-growing programing language ''')  
  
# closing the opened the file  
fileptr.close()  








#open the file.txt in write mode.    
fileptr = open("file2.txt","a")  
    
#overwriting the content of the file    
fileptr.write(" Python has an easy syntax and user-friendly interaction.")    
      
#closing the opened file     
fileptr.close()



#open the file.txt in read mode. causes error if no such file exists.    
fileptr = open("file.txt","r")  
#stores all the data of the file into the variable content    
content = fileptr.read(10) 

# prints the type of the data stored in the file    
print(type(content))      
#prints the content of the file    
print(content)       
#closes the opened file    
fileptr.close()   









#open the file.txt in read mode. causes an error if no such file exists.    
fileptr = open("file2.txt","r");     
#running a for loop     
for i in fileptr:    
    print(i) # i contains each line of the file     






#open the file.txt in read mode. causes error if no such file exists.    
fileptr = open("file2.txt","r");     
#stores all the data of the file into the variable content    
content = fileptr.readline()     
content1 = fileptr.readline()  
#prints the content of the file    
print(content)     
print(content1)  
#closes the opened file    
fileptr.close()    

# Python provides also the readlines() method which is used for the reading lines. It returns the list of the lines till the end of file(EOF) is reached.



fileptr = open("file2.txt","r");     
  
content = fileptr.readlines()     
    
print(content)     
  
fileptr.close()  



# Creating a new file:-

'x:' # it creates a new file with the specified name. It causes an error a file exists with the same name.

'a:' # It creates a new file with the specified name if no such file exists. It appends the content to the file if the file already exists with the specified name.

'w:' # It creates a new file with the specified name if no such file exists. It overwrites the existing file


# open the file.txt in read mode. causes error if no such file exists.    
fileptr = open("file2.txt","x")   
print(fileptr)    
if fileptr:    
    print("File created successfully")  




# File Pointer positions

'tell()' # method which is used to print the byte number at which the file pointer currently exists. Consider the following example.


fileptr = open("file2.txt","r")     
print("The filepointer is at byte :",fileptr.tell())    
content = fileptr.read();        
print("After reading, the filepointer is at:",fileptr.tell())        


# delete file:
# To delete a file, you must import the OS module, and run its os.remove() function

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")




# Delete Folder
# To delete an entire folder, use the os.rmdir() method:

import os
os.rmdir("myfolder")




