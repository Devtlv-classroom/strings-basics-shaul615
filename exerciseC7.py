# Exercise 6 (medium)
# A group of teenagers is coming to your movie theater and want to see a movie
# that is restricted
# for people between 16 and 21 years old.
#
# Write a program that ask every user their age, and then tell them which can see the movie.
#
# Try to add the allowed ones to a list.


stop_process = True
teenallowed = []
age = 0

while stop_process == True :
    user_age_input = input(" Please enter your age (enter q to close processs)\n -" )
    if user_age_input == "q":
        break
    age = int(user_age_input)
    if age <= 21 and age >= 16:
        print("welcome to the movie, you can enter Enjoy !")
        teenallowed.append(user_age_input)
        stop_process == True
    else:
        print("you are not within the allowed age, sorry you can't enter. ):\n")
print("allowed age list \n",teenallowed)

