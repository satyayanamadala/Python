a1 = set() #empty set
print(a1,type(a1))

a ={2,21,93,50}   #set
print(a,type(a))


# Sets Method
set1 = {12,33,45,99}
set2 = {100,45,12,69}
set1.add(55)
set1.update([22,13])
set1.remove(33)
print(set1)
print(set1,type(set1))

set = set1.union(set2)
print(set)

set = set1.intersection(set2)
print(set)

print(set1.difference(set2)) 




