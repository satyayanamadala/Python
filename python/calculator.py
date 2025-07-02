a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("ENTER THE 1 FOR ADDITION \nENTER THE 2 FOR SUBTRACTION \nENTER THE 3 FOR MULTIPLICATION\nENTER THE 4 FOR DIVISION\nENTER THE 5 FOR MODULUS\nENTER THE 6 FOR FLOOR DIVISION\nENTER THE 7 FOR EXPONENTIAL\n")

c = int(input("ENTER NUMBER FOR WHICH OPERATION TO PERFORM: "))

if c == 1:
    print("THIS FOR THE ADDITION:", a, "+", b, "=", a + b)
elif c == 2:
    print("THIS FOR THE SUBTRACTION:", a, "-", b, "=", a - b)
elif c == 3:
    print("THIS FOR THE MULTIPLICATION:", a, "*", b, "=", a * b)
elif c == 4:
    print("THIS FOR THE DIVISION:", a, "/", b, "=", a / b)
elif c == 5:
    print("THIS FOR THE MODULUS:", a, "%", b, "=", a % b)
elif c == 6:
    print("THIS FOR THE FLOOR DIVISION:", a, "//", b, "=", a // b)
elif c == 7:
    print("THIS FOR THE EXPONENTIAL:", a, "**", b, "=", a ** b)
else:
    print("ERROR: INVALID CHOICE. TRY AGAIN.")
