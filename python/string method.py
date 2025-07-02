str1 = "AbcDEfghIJ"   #The upper() method converts a string to upper case.
print(str1.upper())

str = "AbcDEfghIJ"   #The lower() method converts a string to lower case.
print(str.lower())

str2 = " Silver Spoon "     #The strip() method removes any white spaces before and after the string.
print(str2.strip())

str3 = "Hello !!!"          #The rstrip() removes any trailing characters.
print(str3.rstrip("!"))

str4 = "Silver Spoon"       #The replace() method replaces a string with another string.
print(str4.replace("Sp", "M"))

str5 = "Silver Spoon"  #The split() method splits the given string at the specified instance and returns the separated strings as list items.
print(str5.split(" "))  # Splits the string at the whitespace " ".

str1 = "hello"
capStr1 = str1.capitalize()     #The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase.The string has no effect if the first character is already uppercase.
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)

str1 = "Welcome to the Console!!!"
print(len(str1))
print(str1.center(50))      #The center() method aligns the string to the center as per the parameters given by the user.
str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))     #We can also provide a padding character. It will fill the rest of the fill characters provided by the user.

str2 = "Abracadabra"
print(str2.count("a"))      #The count() method returns the number of times the given value has occurred within the given string.

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))     #The endswith() method checks if the string ends with a given value. If yes, then return True, else return False.
str1 = "Welcome to the Console !!!" 
print(str1.endswith("to", 4, 10))  #We can even also check for a value in-between the string by providing start and end index positions.

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))  #The find() method searches for the first occurrence of the given value and returns the index where it is present. If the given value is absent from the string, then return -1.

str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))  #The index() method searches for the first occurrence of the given value and returns the index where it is present. If the given value is absent from the string, then raise an exception.

#As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if the value is absent whereas find() does not.

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())   #The title() method capitalizes each letter of the word within the string.