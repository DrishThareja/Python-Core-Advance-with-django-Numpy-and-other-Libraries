
'MySQL'

# MySQl ( databases )
# It is used to store data in large amount permanently. It can easily connect with any language. And we can handle large project data with it. In databases data stored in table in the form of row and column. SQL is used to communicate with mySQL databases.

# SQL is Structured Query Language

'1.' # Install Xampp
'2.' # Go to start menu and search xampp in control panel and open it.

'----------------------------------------------------------------------------'

'1.' # mysql -u root -p
     # password:

'2.' # show databases;

'3.' # create database database_Name;

'4.' # use database_Name;

'5.' # create table table_Name (column_Name1 type(size), column_Name2 type(size), ... , n);

# Eg: create table student (Name varchar(50), Roll_no int(10));

'6.' # for single data
    # insert into table_Name (column_Name1, column_Name2) values (value1, value2);

    # for multiple data
    # insert into table_Name (column_Name1, column_Name2) values (value1, value2), (value1, value2), ... , n;

# Eg: # insert into student (Name, Roll_no) values ('Drish', 001);
      # insert into student (Name, Roll_no) values ('Drish', 001), ('Chirag', 002), ('Ishan', 003);

'7.' # select *from table_Name;
'By using this we can see all the data that we have stored.'
# Eg: select *from student;

'8.' # select column_Name1, column_Name2, .... , n from table_Name;
# Eg: select Name from student;
'It will show all the names'

'9.' # select *from student where condition;
# Eg: select *from student where Name = 'Drish Thareja';
'It will show the Sr. No., Name, Father Name, Roll_no of that condition.'

