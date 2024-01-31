'1. Distinct statement: '
# select distinct column_name_1, column_name_2, ... from table_name;

'2. Like operator: use to take output from the starting alphabet '
# select *from table_name where column_name like '(alphabet)%';
# Eg: select *from student where city like 'b%';

'3. And with like syntax: '
# select column_name_1, column_name_2,.. from table_name where column_name_1 like '(alphabet)%' and column_name_2 like '(alphabet)%';
# Eg: select name, city from student where city like 'm%' and name like 'm%';

'4. Or with like syntax: '
# select column_name_1, column_name_2,.. from table_name where column_name_1 like '(alphabet)%' or column_name_2 like '(alphabet)%';
# select name, city from student where city like 'm%' or name like 'm%';

'5. NOT syntax: '
# select column_name from table_name where not condition;
# select city from student where not city = 'bondi';

'6. Combining And Or: '
# select *from table_name where column_name_1 = (condition) and (column_name_2 = condition);
# select *from student where name = ('sdf'or'ert') and (city = 'sirsa' or 'mumbai');

'7. Order by ascending (ASC) and descending(DESC)'
# select *from table_name order by column ASC / DESC;

'8. Is Null Operator: '
# select column_name from table_name where column_name is null;
# select city from student where city is null;
# select *from student where city is null;

'9. Is Not Null Operator: '
# select column_name from table_name where column_name is not null;
# select city from student where city is not null;
# select *from student where city is not null;

'10. Update syntax: '
# update table_name set column_name_1 = value_1, column_name_2 = value_2,... where condition;
'If we have to put anything in NULL: '
# update student set city = 'bondi' where city is null;
'If we have to put null on the place of stored data: '
# update student set city = null where city = 'bondi';

# {In NULL we have to use is null and is not null}

'11. Deleting existing records in a statement: '
# delete from table_name where condition;

'12. Limit syntax: '
# select column_name from table_name where condition limit number;
# select *from table_name limit number;
# select *from table_name limit number offset number;

# select *from student limit 3;                 { from starting 3 will be showed }
# select *from student limit 3 offset 3;        { from 3 to next 3 will be shown excluding 3, means 4 - 5 - 6 will be shown }
'Limit 3 means 3 data will be shown and offset 3 means data after 3rd data will be shown}'

'13. Add a where clause: '
# select *from table_name where column_name = '---' limit number;
# select *from student where city = 'bondi' limit 3;    { the data in which city = bondi is there any 3 will be shown }

'14. MIN function: '
# select MIN(column_name) from table_name where condition;
# select min(id) as smallestid from student;                    { the column name will be shown as smallestid } 

'15. MAX function: '
# select MAX(column_name) from table_name where condition;
# select max(id) as largestid from student;                    { the column name will be shown as largestid }

'16. Count function: '
# select count(column_name) from table_name;
# select count(name) from student;
# select count(name) as Name from student;                    { the column name will be shown as Name }

'17. AVG function: '
# select avg(column_name) from table_name;
# select avg(id) from student;
# select avg(id) as AVERAGE from student;                    { the column name will be shown as AVERAGE }

'18. SUM function: '
# select sum(column_name) from table_name;
# select sum(id) from student;
# select sum(id) as SUM from student;                    { the column name will be shown as SUM }

'19. The MySQL LIKE Operator: '

'The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.'
'There are two wildcards often used in conjunction with the LIKE operator: '
'The percent sign (%) represents zero, one, or multiple characters'
'The underscore sign (_) represents one, single character'

#       Like Operator                  |         Description
#                                      |
'a.'  # Where CustomerName LIKE 'a%'   |  Finds any values that start with "a"
'b.'  # WHERE CustomerName LIKE '%a'   |  Finds any values that end with "a"
'c.'  # WHERE CustomerName LIKE '%or%' |  Finds any values that have "or" in any position
'd.'  # WHERE CustomerName LIKE '_r%'  |  Finds any values that have "r" in the second position
'e.'  # WHERE CustomerName LIKE 'a_%'  |  Finds any values that start with "a" and are at least 2 characters in length
'f.'  # WHERE CustomerName LIKE 'a__%' |  Finds any values that start with "a" and are at least 3 characters in length
'g.'  # WHERE ContactName LIKE 'a%o'   |  Finds any values that start with "a" and ends with "o"

'20. In operator: '
# select *from table_name where column_name in (condition);
# select *from student where city in ('mumbai')

'21. Not in operator: '
# select *from table_name where column_name not in (condition);
# select *from student where city not in ('mumbai')

'22. '