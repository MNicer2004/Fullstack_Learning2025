# List and Tuples

'''
# +Index       0       1      2
# -Index      -3      -2     -1
courses = ["BSIT", "BSCS", "BSBA"]
print(courses[-3])
'''

# Reading List RANGE
'''
courses = ["BSIT", "BSCS", "BSBA", "BST", "BSHM"]
print(courses[:3])
#3: , 1:3
'''

# List LENGTH
# len
'''
courses = ["BSIT", "BSCS", "BSBA", "BST", "BSHM"]
print(len(courses))
'''

# List COUNT
# variablename.count("What are u looking")
'''
name = ["Mark", "Mark", "Mork", "Mwark", "Mark"]
print(name.count("Mark"))
'''

# List ADD items by APPEND()
# syntax list.append(value) or ("string")
'''
catname = ["SUNNY", "SYOGI", "SIOPAO", "MEOWMEOW"]
catname.append("soony")
print(catname)
'''
# DELETE List Itemb by REMOVE()
# syntax list.remove(value or "string")
'''
catname = ["SUNNY", "SYOGI", "SIOPAO", "MEOWMEOW"]
catname.remove("SIOPAO")
print(catname)
'''
# List DELETE ITEMS by DEL
# syntax del list[index] or del list to delete all in the list
'''
catname = ["SUNNY", "SYOGI", "SIOPAO", "MEOWMEOW"]
del catname[1]  # the syogi is deleted
# del catname  # catname index is deleted
print(catname)
'''
# Clearing a LIST
# clear()
# syntax list.clear()
'''
catname = ["SUNNY", "SYOGI", "SIOPAO", "MEOWMEOW"]
catname.clear()  # just cleared the value in a list but still can access
print(catname)
'''
# Combining a LIST by ADDING
# use + operator to combine a lists
'''
catname = ["SUNNY", "SYOGI", "SIOPAO", "MEOWMEOW"]
dogname = ["ARF", "DOGIE", "DOGS", "DAWG"]
combinedlist = catname + dogname
print(combinedlist) or print (catname + dogname)
'''
# SORT item LISTS
# SORT list by alphabet or value
# syntax list.sort() like a-z
# syntax list.sort(reverse=True) like z-a
'''
names = ["Nyah", "Nicole", "Nami", "Chopper", "Luffy"]
names.sort() #reverse=True for z-a
print(names)
'''
#NESTED Lists
# index      0         1         2                          3
'''
anime = ["OnePiece","Naruto","Re:Zero",["SoloLevelin","DanDaDan",["Frieren","Demon Slayer","AttackOnTitan"]]]
print(anime[3][2][2]) #3 is inner, 2 is inner of 3, and  2 is the index of inner 2
'''
#TUPLES
#Tuples is just like a list but tuples is just read only it means you can't edit what's inside the lists. much better for fixed list to use this i guess
#same syntax for lists but it's () not []
'''
anime = ("OnePiece","Naruto","Re:Zero")
print(anime)
print(anime[1])
'''
# S E T S
'''
Unordered and Unindex - it means it doesn't have index like 0 1 2 3 and so on..
Partially writable - it means u can add but you can't edit 
Curly braces {} to make it SETS

evenNumbers = {2,4,6,8,10}
print (evenNumbers)
'''
#Set ADD ITEMS by add() #set.add()
'''
evenNumbers = {2,4,6,8,10}
evenNumbers.add(12) 
print (evenNumbers)
'''
#Set ADD ITEMS by update #set.update(list)
#if you want to add a lot in 1 line
'''
evenNumbers = {2,4,6,8,10}
evenNumbers.update([12,14,16,18,20]) 
print (evenNumbers) #output {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
'''
#Set DELETING ITEMS by REMOVE()
#set.remove(value) || number.remove(1)
'''
evenNumbers = {2,4,6,8,10}
evenNumbers.remove(2) #remove the 2 
print (evenNumbers) #output {4, 6, 8, 10}
'''
#Set DELETING ITEMS by DISCARD()
#set.discard || numbers.discard(1)
#same as remove but the DIFFERENCE is if the value DOESN'T EXIST in the set it will NOT be counted as an ERROR 
''''
evenNumbers = {2,4,6,8,10}
evenNumbers.discard(12)  #even it doesn't have 12 in the set it still run 
print (evenNumbers)
'''
#Clearing a SET
#set.clear || number.clear()
#it wont delete, it will just clear the value of the set
'''
number ={1,2,3,4,5}
number.clear()
print(number) #output set()
'''
#UNION SET
#Relationship of 2 set like venn diagram
#No duplicate in the set for ex. num1 has a value of 2 and num2 has a value of 2 too, so what happen is it will just print 2 not 22.
'''
evenNum = {2,4,6,8,10}
oddNum = {1,3,5,7,9}
number = evenNum.union(oddNum) 
print(number) # outut {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
'''
#DIFFERENCE Set
#basically it will just remove the values that only exist on the left set
'''
setOne ={1,2,3,4,5}
setTwo ={1,5} #removed 1 and 5
setThree = setOne.difference(setTwo)
print(setThree) #output {2, 3, 4}
'''
