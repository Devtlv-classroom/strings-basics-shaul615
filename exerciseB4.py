# Exercise (medium)
# Ask the user for his full name (example: "John Doe"), and check the validity of his answer:

    # The name should contain only letters.
    # The name should contain only one space.
    # The first letter of each name should be upper cased.



print("- The name should contain only letters. ")
print("- The name should contain only one space. ")
print("- The first letter of each name should be upper cased. ")

user_name = input("Please enter your Full name (requirements Above) ")

count_spaces_in_name = user_name.count(" ")
no_spaces_user_name = user_name.replace(" ","")

if no_spaces_user_name.isalpha() == False:
     print("- The name should contain only letters")
if count_spaces_in_name>1:
     print("- The name should contain only one space. ")
if user_name.istitle() == False:
    print("- The first letter of each name should be upper cased.")

