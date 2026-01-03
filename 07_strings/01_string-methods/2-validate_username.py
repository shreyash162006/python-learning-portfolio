# validate user input excercise
# 1. Username should have 12 or less characters
# 2. username must not contain
# 3. username must not contain digit 

user_name = input("Enter your username : ")
#1. length of username
length = len(user_name)
# check for spaces 
space = user_name.isspace()
#check digits
alpha = user_name.isalpha()

if(length <= 12 and space == False and alpha == True ):
    print(f"The username {user_name} is valid ")
else:
    print(f"The username {user_name} is invalid")