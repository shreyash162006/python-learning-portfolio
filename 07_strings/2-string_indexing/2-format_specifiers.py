#format specifiers = {value : flags } formats a value based on what flags are inserted

# .(number)f = rounds to that many decimal places 
# : (number) = allocates that many spaces
#  :03 = allocate and zero pad that many spaces 
# :< = left justify
# :>  = right justify
# :^  = centre align
#  :+ = uses a plus sign to indicate a positive value
#  :  = inserts a space before positive numbers 
#  :,  = comma seperators
#  :=  = place sign to leftmost position

price1 = 3.14159
price2 =  -987.65
price3 = 12.34
price4 = 19000.3687
print(f"Prie 1 is : {price1 : .2f}")
print(f"Price 2 is :{price2 : 10}")
print(f"Price 3 left justify : {price3 :< }")
print(f"Price 3 Right justify : {price3 :>}")
print(f"Price 3 centre align : {price3 :^}")
print(f"Price4 thousand seperator : {price4 :, }")
print(f"Price4 thousand seperator : {price4 :, }")