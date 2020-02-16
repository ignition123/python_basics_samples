#!/usr/bin/python

# Number

counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print(counter)
print(miles)
print(name)

# String

str = 'Hello World!'

print(str)          # Prints complete string
print(str[0])      # Prints first character of the string
print(str[2:5])     # Prints characters starting from 3rd to 5th
print(str[2:])      # Prints string starting from 3rd character
print(str * 2)      # Prints string two times
print(str + "TEST") # Prints concatenated string

# List

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print(list)          # Prints complete list
print(list[0])       # Prints first element of the list
print(list[1:3])     # Prints elements starting from 2nd till 3rd 
print(list[2:])      # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(list + tinylist) # Prints concatenated lists

# Tuple

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print(tuple)           # Prints complete list
print(tuple[0])        # Prints first element of the list
print(tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print(tuple[2:])       # Prints elements starting from 3rd element
print(tinytuple * 2)   # Prints list two times
print(tuple + tinytuple) # Prints concatenated lists

# Dictionary / Associative array / Hashmap

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print(dict['one'])       # Prints value for 'one' key
print(dict[2])           # Prints value for 2 key
print(tinydict)          # Prints complete dictionary
print(tinydict.keys())   # Prints all the keys
print(tinydict.values()) # Prints all the values

# Fetching values directly
# Python3 code to iterate over a list 
list = [1, 3, 5, 7, 9] 
   
# Using for loop 
for i in list: 
    print(i) 

# Fetching using index
# Python3 code to iterate over a list 
list = [1, 3, 5, 7, 9] 
   
# getting length of list 
length = len(list) 
   
# Iterating the index 
# same as 'for i in range(len(list))' 
for i in range(length): 
    print(list[i]) 

# Using while loop

# Python3 code to iterate over a list 
list = [1, 3, 5, 7, 9] 
   
# Getting length of list 
length = len(list) 
i = 0
   
# Iterating using while loop 
while i < length: 
    print(list[i]) 
    i += 1

# Python3 code to iterate over a list 
list = [1, 3, 5, 7, 9] 
   
# Using list comprehension 
[print(i) for i in list] 

# Python3 code to iterate over a list 
list = [1, 3, 5, 7, 9] 
   
# Using enumerate()  
for i, val in enumerate(list): 
    print (i, ",",val) 

# Iterating in hashmap

for key in dict:
	print(key, '->', dict[key])

for item in dict.items():
	print(item)

# List of dictionaries

test_list = [{"id" : 1, "data" : "HappY"}, 
{"id" : 2, "data" : "BirthDaY"}, 
{"id" : 3, "data" : "Rash"}] 

# printing original list  
print (test_list) 

# using del + loop  
# to delete dictionary in list 
for i in range(len(test_list)): 
    if test_list[i]['id'] == 2: 
        del test_list[i] 
        break

# printing result 
print (test_list) 

# If statement

var1 = 100
if var1:
   print("1 - Got a true expression value")
   print(var1)

var2 = 0
if var2:
   print("2 - Got a true expression value")
   print(var2)
print("Good bye!")

# If statement and else

var1 = 100
if var1:
   print("1 - Got a true expression value")
   print(var1)
else:
   print("1 - Got a false expression value")
   print(var1)

# If statement else and elif

var = 100
if var == 200:
   print("1 - Got a true expression value")
   print(var)
elif var == 150:
   print("2 - Got a true expression value")
   print(var)
elif var == 100:
   print("3 - Got a true expression value")
   print(var)
else:
   print("4 - Got a false expression value")
   print(var)

print("Good bye!")

# Switch case

# def week(i):
# 	switcher={
#         0:'Sunday',
#         1:'Monday',
#         2:'Tuesday',
#         3:'Wednesday',
#         4:'Thursday',
#         5:'Friday',
#         6:'Saturday'
#  	}
#  	return switcher.get(i)

# print(week(0))

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except e:
   print("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")
   fh.close()