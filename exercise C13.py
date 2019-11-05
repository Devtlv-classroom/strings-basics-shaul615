# Exercise (hard)
# Convert a string into password format Example: input : "mypassword" output: "***********"

user_input =input("Please enter a password:\n-")
hidden_password = ""
counter = 0

while counter < len(user_input):
    hidden_password += "*"
    counter += 1

print( "Your password was {} when in a hidden format it is {} ".format(user_input,hidden_password) )