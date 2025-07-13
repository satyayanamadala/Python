#Tuples are Immutable
tuple = ("satya",19,493,"cseaiml")
print(tuple)
a,b,c,d = tuple
print(a,b,c,d)

#Tuples Method
tuple1 = ("jai","yanamadala","jai",21,420,"ELC")
a=tuple1.count("jai")
print(a)
b=tuple1.index("ELC")
print(b)

#Built-in Functions That Work with Tuples

t = (1, 2, 3, 4)
# Built-in functions
print(len(t))       # 4
print(max(t))       # 4
print(sum(t))       # 10
# Operations
t2 = (5, 6)
print(t + t2)       # (1, 2, 3, 4, 5, 6)
print(t * 2)        # (1, 2, 3, 4, 1, 2, 3, 4)
print(3 in t)       # True
# Tuple unpacking
a, b, c, d = t
print(a, b, c, d)   # 1 2 3 4




