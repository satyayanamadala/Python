a = int(input("Enter the number:"))

if (a>=18):
    print("YOUR ELIGIBLE TO VOTE")
elif (a==17):
    print("YOUR ONE YEAR MORE TO VOTE \nYOUR NOT ELIGIBLE TO VOTE AT PRESENT")
else:
    print("YOUR NOT ELIGIBLE TO VOTE AT PRESENT")

b = int(input("enter  the number:"))
if (b>20):
    print("YOUR NOT A TEEN ")
elif (b<=20):
    if(b==20):
        print("YOUR STILL NOT TEEN \n THEN YOUR ADULT")
    elif(b==19):
        print("THEN YOUR AN TEEN")
    else:
        print("YOUR TEEN")
else:
    print("error")