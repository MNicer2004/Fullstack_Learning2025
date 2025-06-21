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
'''
studentOne ={
    "name":"Mark",
    "course":"BSIT",
    "age":21
}  
print(studentOne.keys())              #printed the theys only
#OUTPUT dict_keys(['name', 'course', 'age'])

#GETTING ALL VALUES IN DICTIONARY
# dictionary.values() ||studentOne.values()

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
'''
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
'''
'''
students = [studOne,studTwo,studThree]   #make your dictionary into a list
print(students)                          # print the dictionary lists
print(students[0])                       #prints the library on the index 0
print(students[1].get("age"))           #gets that value of the "age" on index 1
'''

'''
#CONDITIONAL STATEMENT
# IF STATEMENT - 1 CONDITION
# IF-ELSE STATEMENT - 2 CONDITION
# IF-ELIF-ELSE STATEMNT - 3 OR MORE CONDITION
# NESTED CONDITION STATEMENT - CONDITION AFTER A CONDITION

# O P E R A T O R S

== EQUAL
!- NOT EQUAL
> GREATER THAN
< LESS THAN
>= GREATER THAN OR EQUAL
<= LESS THAN OR EQUAL
!= NOT EQUAL
'''
#SKIPPED IF STATEMENT TO IF ELIF ELSE 
#NESTED CONDITIONAL STATEMENT
#it simply just 2nd condition
'''
age = (int(input("How old are you? ")))

if age >= 18:                           #if age is >=18 is goes to nested if
    height = (int(input("Height: ")))   
    if height >=175:
        print("Nice!")
    elif height >=150:
        print("Not Bad!")
    elif height <150:
        print("Bad")
elif age < 18:                          #if not it will only read this and print
    print ("18+ only")   
 '''

#LOGICAL OPERATORS
# AND - BOTH CONDITION IS TRUE
# OR - EITHER CONDITION MUST BE TRUE
'''
username = (input("Username: "))
password = (input("Password: "))

if username  == "Admin":            #I used nested if else here
    if password == "admin123":
        print("Welcome Admin!")
    else:
        print("Wrong password!")
elif username and  password == 'abcdefghijklmnopqrstuvwxyz' or 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': #for this is used (and,or)
    print("Welcome User!");
else:
    print("Account not found!")
'''
#COLLECTION CONDITIONAL STATEMETS
# - USED TO CHECK AN ITEM IF IT'S IN A COLLECTION (LIST AND TUPLES)
'''
animeList = ["One Piece","Naruto","Dragon Ball"]
animeList.append("One punch")   #if i removed this is will print Nope but since i append it it will print YES

if "One punch" in animeList:     # if value is in list
   print("YES")                  # then print "YES"
else:
   print("Nope")                 # if not in the list "Nope"
'''

# WHILE LOOP
# - A STATEMENT that will repeat a block of code as long as it's condition is fulfilled
# Syntax while valueOne > valueTwo:
        # Do something

# age = 12
# while age < 18:
#     print(f"Still young: {age}")
#     age = age + 1

#ELSE in WHILE LOOP
'''
applicant = 1
while applicant <= 10:
    print(f"Applicant number: {applicant}")
    applicant = applicant + 1
else:                                                          #else after the while loop is ended
    print("Only 10 applicant can only apply for this job!")
'''

#WHILE LOOP IN COLLECTION
#               0        1       2       3
# studentID = [2025123,2025124,2025125,2025126]
# index = 0

# while index < (len(studentID)):
#     print(studentID[index])
#     index = index + 1
    
#break - does brake the loop 

#CONDITION IN WHILE LOOP

# student = input("What does IT stands for? ")

# while True: # it will loop until the if is true
#     if student == "Information Technology" or student == "information technology":
#         print("That's Correct!")
#         break  #the loop will stop when the condition is true
#     else:
#         print("That's Incorrect! Try again.")
#         student = input("What does IT stands for? ")
    