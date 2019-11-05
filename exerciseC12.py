# Exercise (medium)
# Write a program that calculate the number of upper case letters
# and lower case letters in a string.

user_string = "The rain in Spain is always good in London but only in Nottingham town."

counter = 0
count_upper = 0
count_lower = 0


while counter < len(user_string):
    if user_string[counter] != " ":
        if user_string[counter].islower()== True:
            count_lower += 1
        if user_string[counter].isupper()== True:
            count_upper += 1
    counter += 1

print("In the String:  \n {} \n there are \n upper case letter: {}\n lower case letter: {}".format(user_string,count_upper,count_lower))
