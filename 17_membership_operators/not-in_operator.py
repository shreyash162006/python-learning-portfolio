# Membership operators = used to test wheather a value or variable is found in a sequence
#                        ( set , list , string , tuple or dictionary)
#                         1.In                     
#                         2.Not In

#name = "shreyash"
#letter = input("Enter any letter of the secret name : ") 
#if letter not in name : 
#    print(f"{letter} is not present")
#else:
#    print(f"{letter} is present") 

student_data = { "om" : 1,"Tejas" : 2 ,"sagar"  : 3 ,"sahil" : 4  ,"shreyash" : 5}
name = input("Enter the student name to get the roll no :")
roll_no = student_data[name]
if name not in student_data:
    print(f"The {name} is not a student")
else:
    print(f"The {name} has roll no {roll_no}")