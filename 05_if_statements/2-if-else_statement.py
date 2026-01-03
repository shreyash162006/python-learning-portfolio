# IF statement - do some code only if the statement is true .
# The Else statement is executed when if statement is false 

print("CHECK ELIGIBILITY TO VOTE")

age = int(input("Enter your age: "))

if(age >= 18 ):
    print("You are eligible to vote")
else:                                      #executed when age is less than 18
    print("You are not eligible to vote")