# importing the random library 

import random

number = random.randint(1,6)  # prints a random number from 1 to 6
print(number)
# the range of random.randint() can also be variables
# low = 1
# high = 100
#  num2 = random.randint( low , high )
# print(num2)   { prints a random number from 1 - 100 } 

# choice method
options = ( "rock" , "paper" , "scissor")
choice = random.choice(options)
print(choice)

# shuffle method
cards = [ "A" , "Q" , "K" , "J" , "2", "3", "4", "5","6","7","8","9","10"]
random.shuffle(cards)
print(cards)