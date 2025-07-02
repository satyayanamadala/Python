#TYPE CASTING

#EXPLICIT TYPECASTING
a = "satya"
b = 2
print(a+b)  #It will throw an error. TypeError: can only concatenate str (not "int") to str
print(a + str(b))
print(int(a)+b) #ValueError: invalid literal for int() with base 10: 'satya'

#Implicit TypeCasting
c = 3.6
d = 3
print(type(c+d)) #output will be 6.6 
print(c+d)  #a float value
