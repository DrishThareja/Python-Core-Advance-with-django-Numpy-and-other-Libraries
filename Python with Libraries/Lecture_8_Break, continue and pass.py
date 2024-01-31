
# Break, Continue and Pass statement:



'Python break statement:-'
#The break is a keyword in python which is used to bring the program control out of the loop. The break statement breaks the loops one by one, i.e., in the case of nested loops, it breaks the inner loop first and then proceeds to outer loops. In other words, we can say that break is used to abort the current execution of the program and the control goes to the next line after the loop.

# The break is commonly used in the cases where we need to break the loop for a given condition.
# The syntax of the break is given below.


#loop statements  
# break;   


list = [1,2,3,4]  
count = 1;  
for i in list:  
    if i == 4:  
        print("item matched")  
        count = count + 1;  
        break  
print("found at", count, "location");  



str = "python"  
for i in str:  
    if i == 'o':  
        break  
    print(i);  





n=2  
while 1:  
    i=1;  
    while i<=10:  
        print("%d X %d = %d\n"%(n,i,n*i));  
        i = i+1;  
    choice = int(input("Do you want to continue printing the table, press 0 for no?"))  
    if choice == 0:  
        break;      
    n=n+1  



'Python continue Statement' # it make the flow of loop continues. Continue keyword to skip the remaining statements of the current loop and go to the next iteration. 


for iterator in range(10, 21):  
   
    # If iterator is equals to 15, loop will continue to the next iteration  
    if iterator == 15:  
        continue  
    # otherwise printing the value of iterator  
    print( iterator ) 




'Pass Statement' # The null statement is another name for the pass statement. A Comment is not ignored by the Python interpreter, whereas a pass statement is not


# We can use the pass statement as a placeholder when unsure what code to provide. So, we only have to place the pass on that line. Pass may be used when we don't wish any code to be executed. We can simply insert a pass in places where empty code is prohibited, such as loops, functions, class definitions, or if-else statements



sequence = {"Python", "Pass", "Statement", "Placeholder"}  
for value in sequence:  
    if value == "Pass":  
        pass # leaving an empty if block using the pass keyword  
    else:  
        print("Not reached pass keyword: ", value)  

