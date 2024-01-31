# List:

list = ["irfan","sohan","mohan"]  

for  i in list:  
    print(i.upper())

#O/P:
#    IRFAN SOHAN MOHAN


# Python upper() method   
  
names = ["irfan","sohan","aman","mohan"]  
vowels = ['a','e','i','o','u'] 

for  i in names:  
    for v in vowels:  
        if(i.startswith(v)):  
            print(i.upper())

#            O/P IRFAN AMAN


l1=["ram","shyam","ashif","jasi",101]
# type():-use to check the type
print(type(l1))

# o/p: <class - list>


a = [1,2,"Peter",4.50,"Ricky",5,6]  
b = [1,2,5,"Peter",4.50,"Ricky",6]  
print(a == b)   # false


list = [1,2,3,4,5,6,7]
print(list[0])  # 1
print(list[1])  # 2
print(list[2])  # 3
print(list[3])  # 4


# Slicing the elements  

print(list[0:6])    #123456
print(list[:])      #1234567
print(list[2:5])    #345
print(list[1:6:2])  #246    # 1 from start, 6 end, 2 is gap


list = [1,2,3,4,5]  
print(list[-1])     #5

print(list[-3:])    #345
print(list[:-1])    #1234
print(list[-3:-1])  #3 4


a=[10,20,30,40,50,90]
#           -3  -2 -1
print(a[2:5])   # 30 40 50
print(a[-2:])   # 50, 90
print(a[-5:-1]) # 20, 30, 40, 50


# updating list:
list = [1, 2, 3, 4, 5, 6]     
print(list) #123456
list[2] = 10   
print(list) #1 2 10 4 5 6 

# Adding multiple-element   
list[1:3] = [89, 78]     
print(list)  # 1 89 78 4 5 6 

# It will add value at the end of the list  
list[-1] = 25  
print(list)#[1, 89, 78, 4, 5, 25] 


# Iterating a Lists:-

list = ["John", "David", "James", "Jonathan"]
for i in list:
    print(i)


# Adding elements to the list:-
# Python provides append()
    
# append():
    
l =[]  
n = int(input("Enter the number of elements in the list:"))
for i in range(0,n):     
    l.append(input("Enter the item:"))     

print("printing the list items..")   
for i in l:   
    print(i, end = "  ")     


# Enter the number of elements in the list:5
# Enter the item:25
# Enter the item:46
# Enter the item:12
# Enter the item:75
# Enter the item:42
# printing the list items
# 25  46  12  75  42  
    

"""-----------------------------------------------------------------"""

# remove():

list = [0,1,2,3,4]     
print("printing original list: ")    
for i in list:    
    print(i,end=" ") 

list.remove(2)    
print("\nprinting the list after the removal of first element...")    
for i in list:    
    print(i,end=" ")  


# printing original list: 
# 0 1 2 3 4 
# printing the list after the removal of first element...
# 0 1 3 4
    

