count = 1
while count <=10:
    print(count)
    count += 1
    # first program that uses a while loop to print numbers 1-10
    
age = 0
while not age >= 18:
    age = int(input("Please enter your age: "))
    if age < 18:
        print("Sorry, you must be at least 18 years old to continue.")
    else:
        print("Thank you! You are old enough to continue.")
    # second program that uses a while loop to check if the user is old enough to continue
    
my_list = ["apple", "banana", "cherry"]
for item in my_list:
    print(item)
    # third program that uses a for loop to show each item in a list
    
for i in range(1, 11):
    print(i)
for i in range(1, 11):
    print(i ** 2)
    # fourth program that uses a for loop to print squares of numbers 1-10
    
my_name = "Gabe"
for char in my_name:
    print(char)
    # fifth program that shows each character in a string using a for loop
    
for i in range(1, 11):
    print(i)
    if i == 5:
        break
# sixth program shows controlling a loop with a break statement
    
for x in range(1, 4):
    for y in range(1, 4):
        print(f"({x}, {y})")
# seventh program shows loops within loops or a nested loop