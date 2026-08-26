# CISW 125
# Intro to programming

# Follow the Documentation Policy as it's good practice and will get you used to what you should do for
# your projects and other labs.

# If you're stuck, ask questions. There are no dumb questions.
# ------------------------------------------------------------------------------------------------------
# We're going to play around with variables and expressions today
# The goal is to just test out things and put them to use and possibly
# save the ideas/work for projects down the line.

# Again, the goal is to "play" around and explore. There's no right or wrong to this.
# Just think about input vs output and what we can do with them.
# ------------------------------------------------------------------------------------------------------


# Create some variables, give them a theme. Example: items on a grocery list, games/books/movies you enjoy, etc.
FavMovie="Transformers"
UnfavMovie="Kpop demon hunters"
FavFruit="Mango"



# Then print your variables.
print(FavMovie)
print(UnfavMovie)
print(FavFruit)
# Now try to reassign a value. This is essentially "overwriting" your variables data with new data. Python works from top to bottom.
FavMovie="Transformers 2"
UnfavMovie="Mario bros movie"
FavFruit="Strawberry"

# After you've done this, try to print your variables in string using f-strings.
print(f"My favorite movie is {FavMovie}, my least favorite movie is {UnfavMovie}, and my favorite fruit is {FavFruit}.")


# Next, try to create some expressions that involve addition, subtraction, multiplication, and division
# Store the results of your expressions in a variable and then print the outcome
x=10
y=5
addition=x+y
print(addition)
x=28
y=7
subtraction=x-y
print(subtraction)
x=11
y=3
multiplication=x*y
print(multiplication)
x=20
y=4
division=x/y
print(division)

# See if you can find other ways to "do maths" (hint: operators are useful and efficient.)
# https://www.w3schools.com/python/python_operators.asp


# Now, I'd like you to make two variables that contain your first and last name
# After you've made the variables, find a way to join the two strings to print your full name. This is string concatenation.
# Think of it as "adding" your variables together.
Fname="Gabriel"
Lname="Leon"
fullname=Fname + " " + Lname
print(fullname)

# While we did some math earlier, I'd like you to try doing math with variables this time. (If you already did this, you can skip this. Good job.)


# Lastly, do something of your own choice. Anything that involves variables and expressions is allowed here.
# If you're stumped on ideas, just try and make an expression that converts Celsius to Fahrenheit or vice versa.
celsius=20
fahrenheit=(celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
# Upload this to Canvas under the Variable and Expressions Lab assignment.
