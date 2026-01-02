#Excercise 2 - Shopping Cart Program

item = input("What item would you like to buy :")
price = float(input("What is the price of each : "))
quantity = int(input("How many would you like to buy : "))
# total bill
total = price*quantity

# BILL 
print(f"You need to pay {total} ,for {quantity} {item}")