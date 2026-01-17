# Membership operators = used to test wheather a value or variable is found in a sequence
#                        ( set , list , string , tuple or dictionary)
#                         1.In                     
#                         2.Not In
'''word = "apple"

letter = input("Enter a letter in the secret word : ")
index = word.find(letter)
if letter in word:
    print(f"The letter : {letter} is present in the word : {word} at the {index +1 } position")
else:
    print("Letter not found in the word")'''
students = { "Shreyash" , "Vedant" , "Om" , "Raj" , "Jay"}

student = input("Enter the name of a student : ").capitalize()
if student in students :
    print(f"{student} is a student ")
else:
    print(f"{student} is not a student ")