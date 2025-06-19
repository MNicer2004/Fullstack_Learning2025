# DICTIONARY
# - Unordered, Changeable, and Indexed
# - key is always string and value is any data type
'''
studentOne ={
    "name":"Mark",
    "course":"BSIT",
    "age":21
}

studentTwo ={
    "name":"Christian",
    "course":"BSCS",
    "age":20
}
print(studentOne) #print the dictionary
print(studentOne["name"]) #print the "name" value
print(studentTwo["age"])
'''

# Assigning DICTIONARY ITEMS
# change the value od a certain item in a dictionary
'''
studentOne ={
    "name":"Mark",
    "course":"BSIT",
    "age":21
}

studentTwo ={
    "name":"Christian",
    "course":"BSCS",
    "age":20
}
studentOne["course"] = "BSN"           #changed the "course" "value" from "BSIT" to "BSN"
print(studentOne)                      #OUTPUT {'name': 'Mark', 'course': 'BSN', 'age': 21}
'''
#DICTIONARY ADD ITEMS
# - add items on a dictionary by assigning non existent key value
'''
studentOne ={
    "name":"Mark",
    "course":"BSIT",
    "age":21
}

studentOne["gender"] = "male"          #added "gender" and "male" at studentOne
print(studentOne)     
'''
#Clearing a Dictionary
#syntax dictionary.clear() || studenOne.clear()
''''
studentOne ={
    "name":"Mark",
    "course":"BSIT",
    "age":21
}         
studentOne.clear()                     #cleared the value of studentOne 
print(studentOne)   
'''
#Copying a Dictionary
#syntax dictionary.copy() || copyStudentOne.copy()
'''
studentOne ={
    "name":"Mark",
    "course":"BSIT",
    "age":21
}  

copyStudentOne = studentOne.copy()     #copied studentOne Dictionary
print(copyStudentOne)
'''
#Getting All KEYS in DICTIONARY
#syntax dictionary.keys()
studentOne ={
    "name":"Mark",
    "course":"BSIT",
    "age":21
}  
print(studentOne.keys())              #printed the theys only
#OUTPUT dict_keys(['name', 'course', 'age'])

#GETTING ALL VALUES IN DICTIONARY
# dictionary.values() ||studentOne.values()
'''
studentOne ={
    "name":"Mark",
    "course":"BSIT",
    "age":21
}  
print(studentOne.values())           #printed the values only
#OUTPUT dict_values(['Mark', 'BSIT', 21])
'''

#LIST OF DICTIONARIES
#LIST
studOne={
    "name":"mark",        #index 0
    "age":19
}
studTwo={
    "name":"christian",   #index 1
    "age":20
}
studThree={
    "name":"nicer",       #index 2
    "age":21
}

students = [studOne,studTwo,studThree]   #make your dictionary into a list
print(students)                          # print the dictionary lists
print(students[0])                       #prints the library on the index 0
print(students[1].get("age"))           #gets that value of the "age" on index 1

