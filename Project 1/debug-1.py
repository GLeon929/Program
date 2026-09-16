# Intro to Programming
# Debug Exercise 2

# This program should add three numbers together.
# Initialize "total" to 0
# before we can add 'total' needs to have value which is 0
total = 0
num1 = input("What's the first number? >")
total = total + int(num1) #need to change to int before adding to total because input will come back as a string 
num2 = input("What's the second number? >")#all good here just need to change to int before adding to total
total = total + int(num2) #need to change to int before adding to total
num3 = input("What's the third number? >")
total = total + int(num3) #need to change to int before adding to total otherwise will be put in as string 
print(f"Total is: {total}")#this line is good how it is 

