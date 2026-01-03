#indexing = indexing allows accessing of a sequence using []

#  S   T   R   I   N   G 
#  0   1   2   3   4   5    ( positive indexing )
# -6  -5  -4  -3  -2  -1    ( negative indexing )
# in a string the last index is skipped 
message = "hello_world" 
print(message)
print(message[3])
print(message[ 0:5 ])
print(message[ 0 : 10 : 2])  # string[start : end : step]
print(message[ 0:])  # same as message[ 0 : 11 ]
print(message[ 0 : 10] ) 

# negative indexing
print(message[-5 :])
print(message[-11 : ])