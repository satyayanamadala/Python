#lists are mutable
list = ["satya","yanamadala",19,493,"CSE"]
print(list)
print(list[2]) 
print(list[1:5])
list[2] = 20      
print(list)

# lists methods 
list1 = ["jai","yanamadala",21,420,"ELC"]
list2 = [2,34,0,10,5,1,99]
list1.append("AIML") 
print(list1)
list1.insert(2,"siva")
print(list1)
list2.sort()
print(list2)
list1.reverse()
print(list1)
list1.pop(4)
print(list1)
list1.remove("jai")
print(list1)