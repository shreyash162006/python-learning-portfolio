# String methods in python
name = input("Enter your name : ")

#len()- returns the length of the string 
length = len(name)
print(f"The name {name} has {length} characters ")

# .find() - returns the first occurence of a character
a = name.find("a") 
print(f"In the name {name}'a' appears at {a} ")   # numebering of a string starts with 0

# .capital() - capitalizes the first character
capital = name.capitalize() 
print(f"name with first letter capitalized : {capital}")

#.lower() - makes all the character of the string into lower case
lower = name.lower()  # converts the string into lower case
print(f"{name} in lower case : {lower}")

#.upper() - makes all the characters of the string into upper case 
upper = name.upper() 
print(f"Name in upper case : {upper}")

# to check if a string contains only digits use the .isdigit() method [ returns true or false]
digit = name.isdigit()
print(f"Does the string contains only digits : {digit}")

# .isaplha() -  to check if a string contains only alphabets 
alpha = name.isalpha()
print(f"Does the string contains only aplabets : {alpha}")

#.count()- returns the number of occurences 
h = name.count("h")
print(f"In the name {name} 'h' appears {h} times")

