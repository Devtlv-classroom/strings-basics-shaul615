# Exercise (medium)
# This time you have a list of users, and you want to remove every user
# that is below 16 years old.
#
# Write a program that ask every user their age, and if they are
# less than 16 years old, remove them from the list.
#
# At the end, print the final list.

user_list = ["boris", "james", "shaul", "peter", "einav", "orit"]

stop_process = True
list_counter = 0

while stop_process == True:
    if list_counter < len(user_list):
        user_input = input("Hello {} how old are you? \n-".format(user_list[list_counter]))
        if int(user_input) < 16:
            user_list.pop(list_counter)
        else:
            list_counter += 1
    else:
        stop_process = False

print("User who are older than 16:\n", user_list)