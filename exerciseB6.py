# Exercise (medium)
# Write a python program to get a string made of the first 2 and
# the last 2 chars from a given string, if the string length is less than 2,
# return instead the empty string.

# For example: "Helloworld" output "Held", while "Sik" returns ""

user_string = input("please enter a string of words: ")
if len(user_string) > 3 :
    print(user_string[:2]+user_string[-2:])
else:
    print(" ")

