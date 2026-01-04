#continue statement - used to skip a value 
#break - terminates the loop at a particular value

# using continue statement 
for x in range (1 , 25 ):
    if x == 16:
        continue   # the loop skips 16 and continues to print till 24
    else:
        print(x)

# break statement
for x in range(1 , 25):
    if x== 16:
        break   # the loop breaks at x = 16 and only 1-15 numbers are printed
    else:
        print(x)
        