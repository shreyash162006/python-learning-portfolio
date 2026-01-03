# elif allows mutltiple conditions to be checked simultanaeously

age = int(input("Enter your age : "))

if(age >= 100 ):
    print("You are very older to vote ")
elif(age <= 0):
    print("You entered invalid age")
elif(age >= 18 ):
    print("You are eligible to vote ")
else:
    print("You are not eligible to vote")