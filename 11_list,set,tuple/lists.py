#collection = single "variable" used to store multiple values
# list[] = ordered and changeable ,allows duplicate items

fruits = [ "apple" , "banana" , "mango" , "coconut"]   #list 
print(fruits)
print(type(fruits))
print(fruits[3]) 
print(fruits[0 : 4 : 2])

#for fruit in fruits:             
#    print(fruit , end = " ")              (prints each item in fruits)

#list method
# 01 - lis.append()
fruits.append("kiwi")  # adds an element at the end 
# 02 - list.insert(index , element)  
fruits.insert(2 , "guava" )
print(fruits)
# 03 - list.sort() - arranges all the elements of a list in chronological order
nums = [ 3 , 4 , 6 , 2 , 1 ]
nums.sort()
print(nums)  

nums.reverse()  # reverses the list
print(nums)

nums.pop(3)  # removes the element at given index
print(nums)

nums.remove(4)  # removes a particular element
print(nums)