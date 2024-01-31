'Steps for mysql: '
# Import mysql.connector module
# Create the connection object
# Create the cursor object
# Execute the query



'1.'
# importing mysql
import mysql.connector

# Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "pyt")  

# printing the connection object
print(myconn)

'-----------------------------------------------------------'

'2.'
# importing mysql
import mysql.connector

# Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "pyt")

# printing the connection object
print(myconn)

# Creating the cursor object
cur = myconn.cursor()

# priniting the cursor object
print(cur)

'-----------------------------------------------------------'

'3. Seeing databases: '
import mysql.connector  
  
# Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "")  
  
# creating the cursor object  
cur = myconn.cursor()  
  
try:  
    dbs = cur.execute("show databases")  
except:  
    myconn.rollback()  
for x in cur:  
    print(x)  
myconn.close()

'-----------------------------------------------------------'

'4.'
import mysql.connector

# create the connection object
myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "")

# creating the cursor object
cur = myconn.cursor()

# creating a new database
cur.execute("create database Py123")

# getting the list of all the databases which will now include the new database
dbs = cur.execute("show databases")

for x in cur:
    print(x)
myconn.close()

'-----------------------------------------------------------'

'5.'
import mysql.connector  
  
# Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "PythonDB")  
  
# creating the cursor object  
cur = myconn.cursor()  
  

#Creating a table with name Employee having four columns i.e., name, id, salary, and department id  
dbs = cur.execute("create table employee(name varchar(20) not null, id int(20) not null primary key, salary float not null, Dept_id int not null)")    
  
myconn.close()  

'-----------------------------------------------------------'

'6.'
import mysql.connector  
  
# Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "PythonDB")  
  
# creating the cursor object  
cur = myconn.cursor()  
  
# adding a column branch name to the table Employee  
cur.execute("alter table Employee add branch_name varchar(20) not null")  

myconn.close()  

'-----------------------------------------------------------'

'7.'
import mysql.connector  

#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "PythonDB")  

#creating the cursor object  
cur = myconn.cursor()  
sql = "insert into Employee(name, id, salary, dept_id) values (%s, %s, %s, %s, %s)"  
  
#The row values are provided in the form of tuple   
val = ("John", 110, 25000.00, 201)  
  
# inserting the values into the table  
cur.execute(sql,val)  

# commit the transaction   
myconn.commit()  
      
print(cur.rowcount,"record inserted!")  
myconn.close()  

'-----------------------------------------------------------'

'8.'
import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "google",database = "PythonDB")  
  
#creating the cursor object  
cur = myconn.cursor()  
  
  
# Reading the Employee data      
cur.execute("select * from Employee")  
  
# fetching the rows from the cursor object  
result = cur.fetchall()  

# printing the result  
      
for x in result:  
    print(x);  
  
myconn.close()  

'-----------------------------------------------------------'

'9.'

#Update Operation
#The UPDATE-SET statement is used to update any column inside the table. The following SQL query is used to update a column.
# update Employee set name = 'alex' where id = 110  

myconn.commit()  # { it is necessary }

'-----------------------------------------------------------'

'10.'
# Delete Operation
# The DELETE FROM statement is used to delete a specific record from the table. Here, we must impose a condition using WHERE clause otherwise all the records from the table will be removed.

# The following SQL query is used to delete the employee detail whose id is 110 from the table.


# delete from Employee where id = 110  

import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "google",database = "PythonDB")  
  
#creating the cursor object  
cur = myconn.cursor()  
  
# Deleting the employee details whose id is 110  
cur.execute("delete from Employee where id = 110")  

myconn.commit()  
  
myconn.close()  
