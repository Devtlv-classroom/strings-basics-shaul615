# Exercise (medium)
# Count the number of words in a string.

user_string = "The rain in spain is always good in main but only in spring."

counter = 0
space_counter = 0

while counter < len(user_string):
    if user_string[counter] == " ":
        space_counter += 1
    counter += 1

print("The amount of words in the string:  \n {} \n is: {}".format(user_string,space_counter+1))
