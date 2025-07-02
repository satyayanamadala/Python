name = "satya" #this is global variable
age = 19
passed = True
print(name,age,passed) 

def details ():
    branch = "CSE" #this is local variable
    section = "AI1"
    print(branch + " this my branch")
    print(section+"this my section")
    print(name)

details()