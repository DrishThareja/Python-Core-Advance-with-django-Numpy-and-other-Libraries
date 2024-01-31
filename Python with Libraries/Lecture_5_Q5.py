# Write the program to find the lists consist of at least one common element.

list1 = [1,2,3,4,5,6]  
list2 = [7,8,9,2,10] 

for x in list1:  
    for y in list2:  
        if x == y:  
            print("common element:",x) 
