#The goal of this lab will be like the ones we've done in previous classes. We will be experimenting with If-Else statements and the goal will be to showcase different ways to use them. This can be done with user input, static values, or even random values. There are many ways to break these statements though. You will be making a few if-else statements based on some prompts. Afterwards, I want you to draw a diagram (like the picture on Canvas) based on one of the branches you created below. Tasks Pick 3 of these branch statements to create. 1) Pick one of the following options: a. Create a grading system. Have it reflect A/B/C/D/F grades. i. Make this based off user input so that the user can enter the grade they have. b. Create an age classifier. Categorize them as child, teenager, adult, or seniors. i. Make this based off user input. Examples would be a child being 12 or younger, teenager would be 13-19, adult would be 20-64, and senior would be 65+ 2) Create a BMI checker. a. Make this based off of user input and have it calculate the user’s BMI from their weight and height. Then classify their BMI as either Underweight, normal weight, overweight, or Obesity. 3) Create a discount calculator. a. The specifications would be as follows: b. 0% discount under $30 c. 5% discount under $50 d. 10% discount under $100 e. 15% discount under $250 4) Create a temperature converter, but with a choice between Celsius and Fahrenheit. a. This is like what you’ve created in previous labs, but now with branching. 5) Create a simple password checker. a. The password should be at least 8 characters long and if it isn’t then tell the user what they must do to create a password.

#Making a grading system using if-else statments and using comparison operators 
Grades=input("enter your grade: ").upper()
if Grades=="A":
    print("Your awesome!")
elif Grades=="B":
    print("Your doing great!")
elif Grades=="C":
    print("Your doing okay!")
elif Grades=="D":
    print("Your barely here!")
else:
    print("You suck!")

#making a BMI checker
weight=float(input("Enter your weight in pounds: "))
height=float(input("Enter your height in inches: "))
if weight<=100 and height<=60:
    print("you are underweight")
elif weight>=140 and height>=70:
    print("you are overweight")
elif weight>=115 and height>=65:
    print("You are normal weight")

#making a discount calculator 
total=float(input("Enter your total order: "))
if total<30:
    print("You get 0% discount")
elif total<50:
    print("You get 5% discount")
elif total<100:
    print("You get 10% discount")
elif total<250:
    print("You get 15% discount")