# Write the program to remove the duplicate element of the list.

list1 = [1,2,2,3,55,98,65,65,13,29]  
list2 = [] 
for i in list1: 
    if i not in list2:  
        list2.append(i)  
print(list2) 