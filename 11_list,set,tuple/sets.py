# set{} = unordered and immutable . no duplicates , elements can be added or removed.

names = {"shreyash" , "siddhant" , "krrish" , "chitransh" }
print(names)
print(type(names))
#.add() - adds an element at the end of the set
names.add("anuj")
print(names)
#.remove() - removes an element from the set
names.remove("siddhant")
print(names)
# .clear() - empties the set
empty = names.clear()
print(empty)

# another set methods
s1 = { 1 , 4 , 6 , 7 , 3 , 2}
s2 = { 1, 4 , 9 , 5 , 2  , 10}
s3 = {1 , 4 , 2 , 3 }
# .intersection - gives the common elements between two sets
print(s1.intersection(s2) )
# .union() - gives a new set which combines the elements of 2 sets
print(s1.union(s2) )
# .difference() - gives the difference between two sets
print(s1.difference(s2) )
# .issubset = checks if one set is the subset of another one and returs boolean value
print (s3.issubset(s1) )
print(s2.issubset(s1))
# .issuperset() - checks if one set is the superset of another and retuns boolean value
print( s1.issuperset(s3) )