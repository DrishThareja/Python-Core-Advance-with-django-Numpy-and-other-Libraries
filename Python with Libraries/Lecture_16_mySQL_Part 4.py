import mysql.connector  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "pyt")  
 
cur = myconn.cursor()



cur.execute("delete from employee where id = 0")
myconn.commit()    
  

cur.execute("select *from employee")      
result = cur.fetchall()
for x in result:
    print(x)  


print("Data is deleted.")  
myconn.close()  


