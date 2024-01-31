# Details of all queries syntax:

'1. start'
# mysql -u root -p
# password: {enter}

'2. creating a database'
# create databases data_base_name;

'3. Using a database'
# use data_base_name;

'4. creating table and column of it'
# create table table_name (col1 type, col2 type, ...);

'5. inserting values in table'
# insert table_name (col1, col2....) values (val1, val2, ...);

'6. viewing full stored table data'
# select *from table_name;

'7. viewing table data with condition'
# select *from table_name where condition;

'8. selecting one or more specific columns'
# select col1_name, col2_name from table_name;

'9. to delete a table'
# drop table table_name;

'10. to delete a column'
# alter table table_name drop column column_name;

'11. to delete a database'
# drop database database_name;

'12. to see all databases'
# show databases;

'13. to add a column in the table after storing some data'
# alter table table_name add column_name type;

'14. to rename table name'
# alter table old_table_name rename to new_table_name;

'15. deleting some data with the condition'
# delete from table_name where condition;

'16. IN operator: use to show specific data using in and condition'
# select *from table_name where column_name in condition;
# Eg: select *from student where city in ('punjab', 'bondi');

'17. NOT IN operator:'
# select *from table_name where column_name not in condition;
# Eg: select *from student where city not in ('punjab', 'bondi');

'18. Between operator:'
# select *from table_name where column_name baetween 1st_value and 2nd_value;
# select *from student where id between 105 and 108;

'19. NOT Between operator:'
# select *from table_name where column_name not baetween 1st_value and 2nd_value;
# select *from student where id not between 105 and 108;

'20. Between with in operator:'
# select *from table_name where column_name_1 between 102 and 109 and column_name_2 in condition;
# select *from student where id between 102 and 109 and city in ('punjab');

'20. Between and order by: '
# select *from table_name where column_name between 1st_value  and 2nd_value order by column_name;
# select *from student where id between 105  and 109 order by id;

'21. NOT BETWEEN and order by: '
# select *from table_name where column_name not between 1st_value  and 2nd_value order by column_name;
# select *from student where id not between 105  and 109 order by id;

