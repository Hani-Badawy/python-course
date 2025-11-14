# and or not

# and example : I went to the airport AND I drank coffee 
condition_1 = True
condition_2 = True
condition_3 = False

print(condition_1 and condition_2)
print(condition_1 and condition_3)
print(condition_1 and condition_2 and condition_3)

# or example : I will go to work or I will go to visit a friend
print(condition_1 or condition_3)
print(condition_1 or condition_2)
print(condition_3 or False)

age = 23 
gender = "male"


is_adult = age >=18 # True
is_female = gender =="female" #False

is_admitted = is_adult or is_female

print("Is the person admitted to the party?", is_admitted)

# not 
condition_4 = True
condition_5 = age <18 # False

print(not condition_4)
print(not condition_5)
