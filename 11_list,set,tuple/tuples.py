# tuple() = cannot be modified
# to create a tuple with single element ( "hello" , ) or (1 , )
a = ( 1 , 45 , 30 , 12 , 10 , 45, 2)
print(a)
print(type(a))
# slicing a tuple 
tuple = ( "shivam" , 1 , 45 , 90 , "hello")
print(tuple[ 0 : 3])
print(tuple[ 0 : : 2])

 # len() - returns the length of the tuple
print(len(a))
i = a.index(45)  # returns the index of the element
print(i)

# .count() - returns the number of occurences of an element 
print( a.count(45) )

# multiplication of a tuple with a scalar
multiplication = a * 3
print(multiplication)   # prints the tuple 3 times

# in statement is used to check wheather an item is present in a tuple or not 
print( 45 in a )
print( 33 in a)

#unpacking a tuple 
my_tuple = ( 1 , 3 , 5)
a, b , c = my_tuple
print( a , b , c)
