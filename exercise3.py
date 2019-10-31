# Ask a user for his name, and if it starts with a vowel, greet him
# 
vowels = "AEIOU"

user_name = input("Please enter your name: ")


if  str.upper(user_name[0]) in vowels:
    print("hello", user_name," you name starts with vowel")
else:
    print(user_name, ", I can't greet you because your name does not start with a vowel SORRY!")
