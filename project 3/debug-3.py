# Intro to Programming
# Debug Exercise 3
#
# There are two problems here. One is quite obvious;
# the other is less so. If you need a hint
# send me a message on Canvas or email me ~Tom
count = 1 #adding this line to fix the error in the for loop below
while True:
    # This loop should output numbers from 1 through 10.
    print("Counting up: ", end=" ")#this is right 
    for count in range(1, 11):# added the range to fix the error in the for loop
        print(count, end=" ")#this is right
    print(count, end="") # this is just an easy way to make a new-line and makes it much more readable
    choice = input("Should I print them again? (y/n)")
    if choice.lower() == 'n':
        # do something to stop the loop 
       break# added this line to break the loop when the user inputs 'n'
    
    